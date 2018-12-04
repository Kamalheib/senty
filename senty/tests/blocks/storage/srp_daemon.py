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

from senty.tests.blocks.common.service import Service


class SRPDaemon(Service):
    def __init__(self, logger, host):
        super(SRPDaemon, self).__init__("srp_daemon", logger, host)

    def init(self):
        cmds = [
            'echo "a 0x001175000078b784 pkey=ffff" > /etc/srp_daemon.conf',
            'echo "a 0xe41d2d03001d6470 pkey=ffff" >> /etc/srp_daemon.conf',
            'echo "d" >> /etc/srp_daemon.conf'
        ]

        rcs = [0]
        for cmd in cmds:
            rcs += [self.Host.run_command(cmd)[0]]

        return sum(rcs)
