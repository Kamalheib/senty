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

from senty.tests.blocks.common.block import Block


class Traffic(Block):
    def __init__(self, logger, server=None, client=None):
        super(Traffic, self).__init__(logger=logger)
        self._server = server
        self._client = client
        self._host_to_pid = {}

    def get_server(self):
        return self._server

    def get_client(self):
        return self._client

    def get_server_command(self):
        raise NotImplementedError()

    def get_client_command(self):
        raise NotImplementedError()

    def init(self):
        raise NotImplementedError()

    def run_bg(self):
        self.Logger.pr_dbg('--------=== Run background stage - [ %s ] ===--------' % self.__class__.__name__)
        if self.Server and self.get_server_command():
            self._host_to_pid[self.Server] = self.Server.run_process(self.get_server_command())

        if self.Client and self.get_client_command():
            self._host_to_pid[self.Client] = self.Client.run_process(self.get_client_command())

    def wait(self):
        raise NotImplementedError()

    def kill(self):
        self.Logger.pr_dbg('--------=== Kill stage - [ %s ] ===--------' % self.__class__.__name__)
        if self._host_to_pid[self.Client]:
            self.Client.kill_process(self._host_to_pid[self.Client])
            self._host_to_pid[self.Client] = None

        if self._host_to_pid[self.Server]:
            self.Server.kill_process(self._host_to_pid[self.Server])
            self._host_to_pid[self.Server] = None

    def restore(self):
        self.Logger.pr_dbg('--------=== Restore stage - [ %s ] ===--------' % self.__class__.__name__)
        return 0

    Server = property(get_server)
    Client = property(get_client)
