#!/usr/bin/evn python

"""
Senty Project
Copyright(c) 2018 Senty.

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


class Operation(Block):
    def __init__(self, logger, host=None):
        super(Operation, self).__init__(logger=logger)
        self._host = host
        self._host_to_pid = {}

    def get_host(self):
        return self._host

    def get_host_command(self):
        raise NotImplementedError()

    def init(self):
        raise NotImplementedError()

    def run_bg(self):
        self.Logger.pr_dbg('--------=== Run background stage - [ %s ] ===--------' % self.__class__.__name__)
        if self.Host and self.get_host_command():
            self._host_to_pid[self.Host] = self.Host.run_process(self.get_host_command())

    def wait(self):
        raise NotImplementedError()

    def kill(self):
        self.Logger.pr_dbg('--------=== Kill stage - [ %s ] ===--------' % self.__class__.__name__)
        if self._host_to_pid[self.Host]:
            self.Host.kill_process(self._host_to_pid[self.Host])

    def restore(self):
        self.Logger.pr_dbg('--------=== Restore stage - [ %s ] ===--------' % self.__class__.__name__)
        return 0

    Host = property(get_host)
