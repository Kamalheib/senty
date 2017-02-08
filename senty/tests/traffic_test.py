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

from abc import ABCMeta, abstractmethod
from senty.tests.basic_test import BasicTest


class TrafficTest(BasicTest):
    __metaclass__ = ABCMeta

    def __init__(self):
        super(TrafficTest, self).__init__(self.__class__.__name__)

    def get_server(self):
        return filter(lambda h: h.ID == 'h1', self.Hosts)[0]

    def get_client(self):
        return filter(lambda h: h.ID == 'h2', self.Hosts)[0]

    @staticmethod
    def get_pair_addr(id, addresses):
        return filter(lambda i: i.ID == id, addresses)[0]

    @staticmethod
    def get_pair(interface, interfaces):
        return filter(lambda i: interface.ID == i.ID, interfaces)[0]

    def get_pairs(self):
        if not hasattr(self, '_pairs'):
            self._pairs = {}
            for interface in self.Server.Interfaces:
                client_if = self.get_pair(interface, self.Client.Interfaces)
                self._pairs[interface] = client_if
        return self._pairs

    @abstractmethod
    def init_tests(self):
        return 0

    def setup(self):
        super(TrafficTest, self).setup()
        self.init_tests()

    Pairs = property(get_pairs)
    Client = property(get_client)
    Server = property(get_server)
