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


class TestCase(object):
    def __init__(self, summary="", server_args="", client_args=""):
        self._summary = summary
        self._server_args = server_args
        self._client_args = client_args

    def get_summary(self):
        return self._summary

    def get_server_args(self):
        return self._server_args

    def get_client_args(self):
        return self._client_args

    Summary = property(get_summary)
    ServerArgs = property(get_server_args)
    ClientArgs = property(get_client_args)
