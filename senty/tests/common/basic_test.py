#!/usr/bin/evn python

"""
Senty Project
Copyright(c) 2017 Senty.

This program is free software; you can redistribute it and/or modify it
under the terms and conditions of the GNU General Public License,
version 2, as published by the Free Software Foundation.

This program is distributed in the hope it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
more details.

You should have received a copy of the GNU General Public License along
with this program.  If not, see <http://www.gnu.org/licenses/>.

The full GNU General Public License is included in this distribution in
the file called "COPYING".

Contact Information:
Kamal Heib <kamalheib1@gmail.com>
"""

import signal
import traceback
import xml.etree.ElementTree
from abc import ABCMeta, abstractmethod
from argparse import ArgumentParser

from senty.modules.host import Host
from senty.modules.port import Port
from senty.utils.logger import Logger
from senty.modules.address import Address
from senty.modules.rdma_dev import RDMADev
from senty.modules.interface import Interface
from senty.tests.common.test_case import TestCase


class BasicTest(object):
    __metaclass__ = ABCMeta

    def __init__(self, name, logger=None, setup_file=None, test_file=None):
        self._name = name
        self.logger = logger
        self.setup_file = setup_file
        self.test_file = test_file

    def get_name(self):
        return self._name

    def get_parser(self):
        if not hasattr(self, '_parser'):
            self._parser = ArgumentParser(self.Name)
        return self._parser

    def get_logger(self):
        if not hasattr(self, '_logger') and not self.logger:
            self._logger = Logger(self.Name, self.verbose)
        else:
            self._logger = self.logger
        return self._logger

    def __get_addresses(self, interface_xml):
        addresses = []
        if interface_xml.find('addresses') is not None:
            for address in interface_xml.find('addresses').findall('address'):
                ip = address.text
                is_ipv6 = (False, True)[address.get('ipv6') == "yes"]
                id = address.get('id')
                addresses.append(Address(id, ip, is_ipv6))
        return addresses

    def __get_interfaces(self, host_xml):
        interfaces = []
        if host_xml.find('interfaces') is not None:
            for interface in host_xml.find('interfaces').findall('interface'):
                name = interface.get('name')
                id = interface.get('id')
                addresses = self.__get_addresses(interface)
                interfaces.append(Interface(name, id, addresses))
        return interfaces

    def __get_ports(self, device_xml):
        ports = []
        if device_xml.find('ports') is not None:
            for port in device_xml.find('ports').findall('port'):
                v1_gids = []
                v2_gids = []
                name = port.get('name')
                id = port.get('id')
                type = port.get('type')
                if port.find('v1_gids') is not None:
                    v1_gids = port.find('v1_gids').text.split(' ')
                if port.find('v2_gids') is not None:
                    v2_gids = port.find('v2_gids').text.split(' ')
                ports.append(Port(name, id, type, v1_gids, v2_gids))
        return ports

    def __get_rdma_devs(self, host_xml):
        rdma_devs = []
        if host_xml.find('ib_devices') is not None:
            for device in host_xml.find('ib_devices').findall('ib_device'):
                name = device.get('name')
                id = device.get('id')
                ports = self.__get_ports(device)
                rdma_devs.append(RDMADev(name, id, ports))
        return rdma_devs

    def get_hosts(self):
        if not hasattr(self, '_hosts'):
            self._hosts = []
            for host in self._setup_xml.findall('host'):
                host_ip = host.find('ip').text
                host_id = host.get('id')
                interfaces = self.__get_interfaces(host)
                rdma_dev = self.__get_rdma_devs(host)
                self._hosts.append(Host(host_ip, self.Logger, host_id, interfaces=interfaces, rdma_devs=rdma_dev))
        return self._hosts

    def get_cases(self):
        if not hasattr(self, '_cases'):
            self._cases = []
            for case in self._test_xml.findall('case'):
                summary = case.find('summary').text
                server_args = ""
                client_args = ""
                if case.find('server_args') is not None:
                    server_args = case.find('server_args').text
                if case.find('client_args') is not None:
                    client_args = case.find('client_args').text
                self._cases.append(TestCase(summary, server_args, client_args))
        return self._cases

    def parse_setup_xml(self):
        self._setup_xml = xml.etree.ElementTree.parse(self.setup_file).getroot()

    def parse_test_xml(self):
        self._test_xml = xml.etree.ElementTree.parse(self.test_file).getroot()

    def __kill_handler(self, signum, frame):
        signal.signal(signal.SIGTERM, signal.SIG_DFL)
        self.teardown()

    def configure_parser(self):
        self.Parser.add_argument('-v', '--verbose', help='log message level',
                                 default='info', choices=['info', 'debug'])
        self.Parser.add_argument('-t', '--test_file', help="test.xml file that describe the test",
                                 required=True)
        self.Parser.add_argument('-s', '--setup_file', help='setup.xml file that describe the setup',
                                 required=True)

    def parse_args(self, args):
        self.Parser.parse_args(args=args, namespace=self)

    def setup(self):
        self.Logger.pr_info('--------=== Setup stage - [ %s ] ===--------' % self.Name)
        signal.signal(signal.SIGTERM, self.__kill_handler)
        return 0

    @abstractmethod
    def run(self):
        self.Logger.pr_info('--------=== Run stage - [ %s ] ===--------' % self.Name)
        return 0

    def teardown(self):
        self.Logger.pr_info('--------=== Teardown stage - [ %s ] ===--------' % self.Name)
        return 0

    def execute(self, args):
        rc = 0
        try:
            if args:
                self.configure_parser()
                self.parse_args(args)
            self.parse_setup_xml()
            self.parse_test_xml()
            self.Logger.pr_info('--------=== Start Test - [ %s ] ===--------' % self.Name)
            rc = rc or self.setup()
            rc = rc or self.run()
            rc = rc or self.teardown()
        except Exception, e:
            rc = 1
            self.Logger.pr_err(e)
            traceback.print_exc()
        finally:
            signal.signal(signal.SIGTERM, signal.SIG_DFL)
        return rc

    Parser = property(get_parser)
    Logger = property(get_logger)
    Hosts = property(get_hosts)
    Cases = property(get_cases)
    Name = property(get_name)
