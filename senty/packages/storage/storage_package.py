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

from senty.packages.package import Package
from senty.tests.storage.srp.srp_test import SRPTest


class StoragePackage(Package):
    def __init__(self, logger, setup_file, tests):
        super(StoragePackage, self).__init__("storage", logger, setup_file, tests)

    def create_tests(self):
        for name, path in self.TestDict.items():
            if name == "srp":
                self.Tests.append(SRPTest(self.Logger, self.SetupFile, path))
            else:
                raise ValueError("Invalid test name %s" % name)
