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

from senty.tests.blocks.traffic import Traffic


class Ping(Traffic):
    def __init__(self, logger, server, ip, is_ipv6=False, args='-c 1'):
        super(Ping, self).__init__(logger=logger, server=server)
        self._ip = ip
        self._is_ipv6 = is_ipv6
        self._args = args

    def get_server_command(self):
        return "%s %s %s" % (("ping", "ping6")[self._is_ipv6], self._args, self._ip)

    def get_client_command(self):
        return None

    def init(self):
        self.Logger.pr_dbg('--------=== Initialization stage - [ %s ] ===--------' % self.__class__.__name__)

    def wait(self):
        self.Logger.pr_dbg('--------=== Wait stage - [ %s ] ===--------' % self.__class__.__name__)
        (rc, out) = self.Server.wait_process(self._host_to_pid[self.Server])
        if rc:
            self.Logger.pr_err('%s - %s' % (self.Server.IP, out))
        return rc
