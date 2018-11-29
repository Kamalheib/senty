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

import sys

from senty.tests.common.basic_test import BasicTest
from senty.tests.blocks.ibutils.ibstat import IBStat
from senty.tests.blocks.ibutils.ibdiagnet import IBDiagnet


class IBUtilsTest(BasicTest):
    def __init__(self, setup_file=None, test_file=None):
        super(IBUtilsTest, self).__init__(self.__class__.__name__, setup_file, test_file)
        self.caseToTests = {}

    def init_tests(self):
        for case in self.Cases:
            tests = []
            for host in self.Hosts:
                if "ibdiagnet" in case.Summary:
                    tests.append(IBDiagnet(self.Logger, host))
                elif "ibstat" in case.Summary:
                    tests.append(IBStat(self.Logger, host))
            self.caseToTests[case] = tests

    def setup(self):
        super(IBUtilsTest, self).setup()
        self.init_tests()
        for case, tests in self.caseToTests.iteritems():
            [test.init() for test in tests]
        return 0

    def run(self):
        super(IBUtilsTest, self).run()
        rcs = [0]
        for case in self.Cases:
            self.Logger.pr_info("%s" % case.Summary)
            tests = self.caseToTests[case]
            for test in tests:
                rcs += [test.run()]
        return sum(rcs)

if __name__ == '__main__':
    ibutils_test = IBUtilsTest()
    rc = ibutils_test.execute(sys.argv[1:])
    sys.exit(rc)
