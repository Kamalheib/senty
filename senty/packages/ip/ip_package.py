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
from senty.tests.ip.ping.ping_test import PingTest
from senty.tests.ip.iperf.iperf_test import IperfTest
from senty.tests.ip.netperf.netperf_test import NetperfTest


class IPPackage(Package):
    def __init__(self, logger, setup_file, tests):
        super(IPPackage, self).__init__("ip", logger, setup_file, tests)

    def create_tests(self):
        for name, path in self.TestDict.iteritems():
            if name == "ping":
                self.Tests.append(PingTest(self.Logger, self.SetupFile, path))
            elif name == "iperf":
                self.Tests.append(IperfTest(self.Logger, self.SetupFile, path))
            elif name == "netperf":
                self.Tests.append(NetperfTest(self.Logger, self.SetupFile, path))
            else:
                raise ValueError("Invalid test name %s" % name)
