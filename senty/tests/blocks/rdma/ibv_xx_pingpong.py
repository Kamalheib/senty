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


class IBvXXPingPong(Traffic):
    def __init__(self, logger, server, client, con_type, s_dev, c_dev, s_gid, c_gid, s_args='', c_args=''):
        super(IBvXXPingPong, self).__init__(logger=logger, server=server, client=client)
        self._con_type = con_type
        self._s_dev = s_dev
        self._c_dev = c_dev
        self._s_gid = s_gid
        self._c_gid = c_gid
        self._s_args = ("", s_args)[s_args is not None]
        self._c_args = ("", c_args)[c_args is not None]

    def get_server_command(self):
        return "ibv_%s_pingpong -d %s -g %s %s" % (self._con_type, self._s_dev, self._s_gid, self._s_args)

    def get_client_command(self):
        return "ibv_%s_pingpong -d %s -g %s %s %s" % (self._con_type, self._c_dev, self._c_gid, self._c_args, self.Server.IP)

    def init(self):
        self.Logger.pr_dbg('--------=== Initialization stage - [ %s ] ===--------' % self.__class__.__name__)

    def wait(self):
        self.Logger.pr_dbg('--------=== Wait stage - [ %s ] ===--------' % self.__class__.__name__)
        (rc, out) = self.Client.wait_process(self._host_to_pid[self.Client])
        if rc:
            self.Logger.pr_err('%s - Command: %s' % (self.Client.IP, self.get_client_command()))
            self.Logger.pr_err('%s - %s' % (self.Client.IP, out))

        super(IBvXXPingPong, self).kill()
        return rc
