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

from senty.tests.blocks.common.traffic import Traffic


class RPing(Traffic):
    def __init__(self, logger, server, client, ip, is_ipv6=False, server_args='', client_args=''):
        super(RPing, self).__init__(logger=logger, server=server, client=client)
        self._ip = ip
        self._is_ipv6 = is_ipv6
        self._server_args = server_args
        self._client_args = client_args

    def get_server_command(self):
        if self._is_ipv6:
            return "rping -a ::0 -s %s" % (self._server_args)
        else:
            return "rping -s %s" % (self._server_args)

    def get_client_command(self):
        return "rping -c -a %s %s" % (self._ip, self._client_args)

    def init(self):
        self.Logger.pr_dbg('--------=== Initialization stage - [ %s ] ===--------' % self.__class__.__name__)

    def wait(self):
        self.Logger.pr_dbg('--------=== Wait stage - [ %s ] ===--------' % self.__class__.__name__)
        (rc, out) = self.Client.wait_process(self._host_to_pid[self.Client])
        if rc:
            self.Logger.pr_err('%s - Command: %s' % (self.Client.IP, self.get_client_command()))
            self.Logger.pr_err('%s - %s' % (self.Client.IP, out))

        super(RPing, self).kill()
        return rc