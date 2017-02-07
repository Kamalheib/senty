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


class Interface(object):
    def __init__(self, name, id, addresses=[]):
        self._name = name
        self._id = id
        self._addresses = addresses

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def get_addresses(self):
        return self._addresses

    ID = property(get_id)
    Name = property(get_name)
    Addresses = property(get_addresses)
