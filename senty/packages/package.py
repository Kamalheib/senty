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


class Package(object):

    def __init__(self, name, logger, setup_file, tests):
        self._name = name
        self._logger = logger
        self._setup_file = setup_file
        self._tests_dict = tests
        self._tests = []

    def get_name(self):
        return self._name

    def get_setup_file(self):
        return self._setup_file

    def get_test_dict(self):
        return self._tests_dict

    def get_logger(self):
        return self._logger

    def get_tests(self):
        return self._tests

    def create_tests(self):
        raise NotImplementedError

    def execute_tests(self):
        rcs = 0
        for test in self.Tests:
            rcs += test.execute(None)
        return rcs

    Name = property(get_name)
    Tests = property(get_tests)
    Logger = property(get_logger)
    TestDict = property(get_test_dict)
    SetupFile = property(get_setup_file)
