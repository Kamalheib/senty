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
from argparse import ArgumentParser

from senty.modules.host import Host
from senty.utils.logger import Logger


class RunMulti(object):

    def get_logger(self):
        if not hasattr(self, "_logger"):
            self._logger = Logger(self.__class__.__name__, self.verbose)
        return self._logger

    def get_parser(self):
        if not hasattr(self, "_parser"):
            self._parser = ArgumentParser(self.__class__.__name__)
        return self._parser

    def get_hosts(self):
        if not hasattr(self, '_hosts'):
            self._hosts = set()
            for ip in self.ips:
                self._hosts.add(Host(ip, self.Logger))
        return self._hosts

    def run_commands(self):
        self._hostToPid = {}
        for host in self.Hosts:
            self._hostToPid[host] = host.run_process(self.command)

    def validate_commands(self):
        for host in self.Hosts:
            (rc, out) = host.wait_process(self._hostToPid[host])
            if rc:
                self.Logger.pr_err("-E- Failed to run %s on %s" % (self.command, host.IP))
            self.Logger.pr_info("-" * 60)
            self.Logger.pr_info("--==%s==--" % host.IP)
            self.Logger.pr_info("-" * 60)
            self.Logger.pr_info("%s" % out)
            self.Logger.pr_info("-" * 60)

    def parse_args(self, args):
        self.Parser.add_argument('-v', '--verbose', help='log message level',
                                 default='info', choices=['info', 'debug'])
        self.Parser.add_argument('-c', '--command',
                                 help='command to run on multi hosts')
        self.Parser.add_argument('-i', '--ips',
                                 help='list of ip addresses or hosts',
                                 nargs='+')
        self.Parser.parse_args(namespace=self, args=args)

    def execute(self, args):
        self.parse_args(args)
        self.run_commands()
        self.validate_commands()

    Logger = property(get_logger)
    Parser = property(get_parser)
    Hosts = property(get_hosts)

if __name__ == '__main__':
    run_multi = RunMulti()
    run_multi.execute(sys.argv[1:])
