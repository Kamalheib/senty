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

import subprocess


class Execute(object):
    def __init__(self, logger):
        self._logger = logger
        self.process_list = dict()

    def run_command(self, command):
        self._logger.pr_dbg("run_command: command=%s" % command)
        return subprocess.getstatusoutput(command)

    def run_process(self, command):
        self._logger.pr_dbg("run_process: command=%s" % command)
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        self.process_list[process.pid] = process
        return process.pid

    def wait_process(self, pid):
        self._logger.pr_dbg("wait_process: pid=%d" % pid)
        rc = self.process_list[pid].wait()
        return rc, self.process_list[pid].communicate()[0].strip()

    def kill_process(self, pid):
        self._logger.pr_dbg("kill_process: pid=%d" % pid)
        try:
            self.process_list[pid].kill()
        except:
            pass
