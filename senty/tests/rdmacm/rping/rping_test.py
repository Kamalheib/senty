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
from senty.tests.blocks.rdmacm.rping import RPing
from senty.tests.common.traffic_test import TrafficTest


class RPingTest(TrafficTest):
    def __init__(self, logger=None, setup_file=None, test_file=None):
        super(RPingTest, self).__init__(logger, setup_file, test_file)
        self.caseToTests = {}

    def init_tests(self):
        for case in self.Cases:
            tests = []
            for s_interface, c_interface in self.Pairs.items():
                for address in s_interface.Addresses:
                    addr = self.get_pair(address, s_interface.Addresses)
                    tests.append(RPing(self.Logger, self.Server, self.Client, addr.IP, addr.IsIPv6,
                                       case.ServerArgs, case.ClientArgs))
            self.caseToTests[case] = tests

    def setup(self):
        super(RPingTest, self).setup()
        for case, tests in self.caseToTests.items():
            [test.init() for test in tests]
        return 0

    def run(self):
        rcs = [0]
        for case in self.Cases:
            tests = self.caseToTests[case]
            self.Logger.pr_info("%s" % case.Summary)
            for test in tests:
                rcs += [test.run()]
        return sum(rcs)

    def teardown(self):
        rcs = [0]
        super(RPingTest, self).teardown()
        for case, tests in self.caseToTests.items():
            for test in tests:
                rcs += [test.restore()]
        return sum(rcs)

if __name__ == '__main__':
    rping_test = RPingTest()
    rc = rping_test.execute(sys.argv[1:])
    sys.exit(rc)
