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

import sys
from senty.tests.common.traffic_test import TrafficTest
from senty.tests.blocks.rdma.ibv_xx_pingpong import IBvXXPingPong


class IBvSRQPingPong(TrafficTest):
    def __init__(self, logger=None, setup_file=None, test_file=None):
        super(IBvSRQPingPong, self).__init__(logger, setup_file, test_file)
        self.caseToTests = {}

    def init_tests(self):
        for case in self.Cases:
            tests = []
            for s_dev, c_dev in self.RDMAPairs.iteritems():
                for s_port in s_dev.Ports:
                    c_port = self.get_pair(s_port, c_dev.Ports)
                    for s_gid in s_port.V1GIDs:
                        c_gid = c_port.V1GIDs[s_port.V1GIDs.index(s_gid)]
                        tests.append(IBvXXPingPong(self.Logger, self.Server, self.Client, "srq", s_dev.Name, c_dev.Name,
                                                   s_gid, c_gid, case.ServerArgs, case.ClientArgs))
                    for s_gid in s_port.V2GIDs:
                        c_gid = c_port.V2GIDs[s_port.V2GIDs.index(s_gid)]
                        tests.append(IBvXXPingPong(self.Logger, self.Server, self.Client, "srq", s_dev.Name, c_dev.Name,
                                                   s_gid, c_gid, case.ServerArgs, case.ClientArgs))
            self.caseToTests[case] = tests

    def setup(self):
        super(IBvSRQPingPong, self).setup()
        for case, tests in self.caseToTests.iteritems():
            [test.init() for test in tests]
        return 0

    def run(self):
        super(IBvSRQPingPong, self).run()
        rcs = [0]
        for case in self.Cases:
            self.Logger.pr_info("%s" % case.Summary)
            tests = self.caseToTests[case]
            for test in tests:
                rcs += [test.run()]
        return sum(rcs)

if __name__ == "__main__":
    test = IBvSRQPingPong()
    rc = test.execute(sys.argv[1:])
    sys.exit(rc)
