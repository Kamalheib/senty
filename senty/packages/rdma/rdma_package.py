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

from senty.packages.package import Package
from senty.tests.rdma.ibv_uc_pingpong.ibv_uc_pingpong import IBvUCPingPong
from senty.tests.rdma.ibv_ud_pingpong.ibv_ud_pingpong import IBvUDPingPong
from senty.tests.rdma.ibv_rc_pingpong.ibv_rc_pingpong import IBvRCPingPong
from senty.tests.rdma.ibv_srq_pingpong.ibv_srq_pingpong import IBvSRQPingPong


class RDMAPackage(Package):

    def __init__(self, logger, setup_file, tests):
        super(RDMAPackage, self).__init__("rdma", logger, setup_file, tests)

    def create_tests(self):
        for name, path in self.TestDict.items():
            if name == "uc_pingpong":
                self.Tests.append(IBvUCPingPong(self.Logger, self.SetupFile, path))
            elif name == "ud_pingpong":
                self.Tests.append(IBvUDPingPong(self.Logger, self.SetupFile, path))
            elif name == "srq_pingpong":
                self.Tests.append(IBvSRQPingPong(self.Logger, self.SetupFile, path))
            elif name == "rc_pingpong":
                self.Tests.append(IBvRCPingPong(self.Logger, self.SetupFile, path))
            else:
                raise ValueError("Invalid test name %s" % name)
