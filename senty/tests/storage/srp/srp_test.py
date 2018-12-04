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
from senty.tests.blocks.storage.srp_daemon import SRPDaemon


class SRPTest(BasicTest):
    def __init__(self, logger=None, setup_file=None, test_file=None):
        super(SRPTest, self).__init__(self.__class__.__name__, logger, setup_file, test_file)
        self.hostToSRPDaemon = {}

    def setup(self):
        super(SRPTest, self).setup()
        rcs = [0]
        for host in self.Hosts:
            self.hostToSRPDaemon[host] = SRPDaemon(self.Logger, host)
            rcs += [self.hostToSRPDaemon[host].init()]

        if sum(rcs) == 0:
            for host in self.Hosts:
                rcs += [self.hostToSRPDaemon[host].start()]

        return sum(rcs)

    def run(self):
        super(SRPTest, self).run()
        rcs = [0]
        for host in self.Hosts:
            rcs += [host.run_command("/usr/sbin/ibsrpdm -vc")[0]]
        return sum(rcs)

    def teardown(self):
        super(SRPTest, self).teardown()
        rcs = [0]
        for host in self.Hosts:
            rcs += [self.hostToSRPDaemon[host].stop()]
        return sum(rcs)


if __name__ == '__main__':
    srp_test = SRPTest()
    rc = srp_test.execute(sys.argv[1:])
    sys.exit(rc)
