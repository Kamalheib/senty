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

import sys
import xml.sax
from argparse import ArgumentParser
from senty.utils.logger import Logger
from senty.packages.ip.ip_package import IPPackage
from senty.packages.packages_parser import PackagesParser
from senty.packages.rdma.rdma_package import RDMAPackage
from senty.packages.rdmacm.rdmacm_package import RDMACMPackage


class Senty(object):

    def __init__(self):
        self.packages_file_parser = xml.sax.make_parser()
        self.packages_file_handler = PackagesParser()
        self.ip_tests_dict = {}
        self.rdma_tests_dict = {}
        self.rdmacm_tests_dict = {}
        self.packages_list = []

    def get_logger(self):
        if not hasattr(self, "_logger"):
            self._logger = Logger(self.__class__.__name__, self.verbose)
        return self._logger

    def get_parser(self):
        if not hasattr(self, "_parser"):
            self._parser = ArgumentParser(self.__class__.__name__)
        return self._parser

    def parse_args(self, args):
        self.Parser.add_argument('-v', '--verbose', help='log message level',
                                 default='info', choices=['info', 'debug'])
        self.Parser.add_argument('-p', '--package_file', help='a Packages xml file')
        self.Parser.add_argument('-s', '--setup_file', help='a setup.xml file to config senty')
        self.Parser.add_argument('-id', default=None, help='component id to run the package on it')
        self.Parser.parse_args(namespace=self, args=args)

    def create_packages_list(self):
        self.packages_list.append(IPPackage(self.Logger, self.setup_file, self.ip_tests_dict))
        self.packages_list.append(RDMAPackage(self.Logger, self.setup_file, self.rdma_tests_dict))
        self.packages_list.append(RDMACMPackage(self.Logger, self.setup_file, self.rdmacm_tests_dict))
        for pkg in self.packages_list:
            pkg.create_tests()

    def execute_packages(self):
        rcs = 0
        for pkg in self.packages_list:
            rcs += pkg.execute_tests()
        return rcs

    def parse_packages_file(self):
        self.packages_file_parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        self.packages_file_parser.setContentHandler(self.packages_file_handler)
        self.packages_file_parser.parse(self.package_file)
        (self.ip_tests_dict, self.rdma_tests_dict, self.rdmacm_tests_dict) = \
            self.packages_file_handler.get_test_dictionaries()

    def execute(self, args):
        self.parse_args(args)
        self.parse_packages_file()
        self.create_packages_list()
        return self.execute_packages()

    Logger = property(get_logger)
    Parser = property(get_parser)

if __name__ == '__main__':
    sys.exit(Senty().execute(sys.argv[1:]))
