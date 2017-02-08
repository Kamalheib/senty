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


class Address(object):
    def __init__(self, id, ip, is_ipv6=False):
        self._id = id
        self._ip = ip
        self._is_ipv6 = is_ipv6

    def get_id(self):
        return self._id

    def get_ip(self):
        return self._ip

    def is_ipv6(self):
        return self._is_ipv6

    ID = property(get_id)
    IP = property(get_ip)
    IsIPv6 = property(is_ipv6)
