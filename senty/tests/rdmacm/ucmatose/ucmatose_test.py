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
from senty.tests.blocks.rdmacm.ucmatose import UCMatose


class UCMatoseTest(TrafficTest):
    def __init__(self):
        super(UCMatoseTest, self).__init__()
        self.caseToTests = {}

    def init_tests(self):
        for case in self.Cases:
            tests = []
            for s_interface, c_interface in self.Pairs.iteritems():
                for s_addr in s_interface.Addresses:
                    c_addr = self.get_pair(s_addr, c_interface.Addresses)
                    tests.append(UCMatose(self.Logger, self.Server, self.Client, s_addr.IP, c_addr.IP, s_addr.IsIPv6, case.ServerArgs, case.ClientArgs))
            self.caseToTests[case] = tests

    def setup(self):
        super(UCMatoseTest, self).setup()
        for case, tests in self.caseToTests.iteritems():
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
        super(UCMatoseTest, self).teardown()
        for case, tests in self.caseToTests.iteritems():
            for test in tests:
                rcs += [test.restore()]
        return sum(rcs)

if __name__ == '__main__':
    ucmatose_test = UCMatoseTest()
    rc = ucmatose_test.execute(sys.argv[1:])
    sys.exit(rc)