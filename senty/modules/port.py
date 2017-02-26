#!/usr/bin/env python

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


class Port(object):
    def __init__(self, name, id, type, v1_gids=[], v2_gids=[]):
        self._id = id
        self._name = name
        self._type = type
        self._v1_gids = v1_gids
        self._v2_gids = v2_gids

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_v1_gids(self):
        return self._v1_gids

    def get_v2_gids(self):
        return self._v2_gids

    ID = property(get_id)
    Name = property(get_name)
    Type = property(get_type)
    V1GIDs = property(get_v1_gids)
    v2GIDs = property(get_v2_gids)
