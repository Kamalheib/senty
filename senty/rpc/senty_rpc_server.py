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
import socket
from argparse import ArgumentParser
from xmlrpc.server import SimpleXMLRPCServer

from senty.utils.logger import Logger
from senty.utils.execute import Execute


class RPCServer(object):

    def get_ip(self):
        if not hasattr(self, '_ip'):
            if not self.server:
                try:
                    self._ip = socket.gethostbyname(socket.gethostname())
                except Exception as e:
                    self.Logger.pr_err("Couldn't get server IP address")
                    self.Logger.pr_err(e)
            else:
                self._ip = self.server
        return self._ip

    def get_port(self):
        if not hasattr(self, '_port'):
            self._port = self.port
        return self._port

    def get_parser(self):
        if not hasattr(self, '_parser'):
            self._parser = ArgumentParser(self.__class__.__name__)
        return self._parser

    def get_logger(self):
        if not hasattr(self, '_logger'):
            self._logger = Logger(self.__class__.__name__, self.verbose)
        return self._logger

    def __register_modules(self, rpc_server):
        modules = [Execute(self.get_logger())]
        for module in modules:
            rpc_server.register_instance(module)

    def get_server(self):
        if not hasattr(self, 'rpc_server'):
            self.Logger.pr_info("Starting server at %s port %d" % (self.IP, self.Port))
            self._rpc_server = SimpleXMLRPCServer((self.IP, self.Port),
                                                  logRequests=True,
                                                  allow_none=True)
            self._rpc_server.quit = False
            self.__register_modules(self._rpc_server)
        return self._rpc_server

    def parse_args(self, args):
        self.Parser.add_argument('-v', '--verbose',
                                 help='log message level',
                                 default='debug',
                                 choices=['info', 'debug'])
        self.Parser.add_argument('-p', '--port',
                                 help='Server port number',
                                 default=8000, type=int)
        self.Parser.add_argument('-s', '--server',
                                 help='Server name/IP address')

        self.Parser.parse_args(namespace=self, args=args)

    def execute(self, args):
        self.parse_args(args)
        self.Logger.pr_info("Starting %s" % self.__class__.__name__)
        self.Server.serve_forever()

    IP = property(get_ip)
    Port = property(get_port)
    Server = property(get_server)
    Logger = property(get_logger)
    Parser = property(get_parser)

if __name__ == '__main__':
    rpc_server = RPCServer()
    rpc_server.execute(sys.argv[1:])
