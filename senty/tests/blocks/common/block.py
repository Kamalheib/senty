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


class Block(object):
    def __init__(self, logger):
        self._logger = logger

    def get_logger(self):
        return self._logger

    def run(self):
        self.Logger.pr_dbg('--------=== Run stage - [ %s ] ===--------' % self.__class__.__name__)
        self.run_bg()
        return self.wait()

    def init(self):
        raise NotImplementedError()

    def run_bg(self):
        raise NotImplementedError()

    def wait(self):
        raise NotImplementedError()

    def kill(self):
        raise NotImplementedError()

    def restore(self):
        raise NotImplementedError()

    Logger = property(get_logger)
