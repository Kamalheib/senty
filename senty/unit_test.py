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
import subprocess
from distutils.cmd import Command

tools = [
    'senty.tools.Senty',
    'senty.tools.run_multi',
    'senty.tests.ip.ping.ping_test',
    'senty.tests.ip.iperf.iperf_test',
    'senty.tests.ip.netperf.netperf_test',
    'senty.tests.rdma.ibv_rc_pingpong.ibv_rc_pingpong',
    'senty.tests.rdma.ibv_uc_pingpong.ibv_uc_pingpong',
    'senty.tests.rdma.ibv_ud_pingpong.ibv_ud_pingpong',
    'senty.tests.rdma.ibv_srq_pingpong.ibv_srq_pingpong',
    'senty.tests.rdmacm.mckey.mckey_test',
    'senty.tests.rdmacm.rping.rping_test',
    'senty.tests.rdmacm.ucmatose.ucmatose_test',
    'senty.tests.rdmacm.udaddy.udaddy_test'
]


class UnitTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    @staticmethod
    def __run():
        rcs = 0
        for tool in tools:
            cmd = [sys.executable, '-m', tool, '-h']
            rcs += subprocess.call(cmd)
        return rcs

    def run(self):
        raise SystemExit(self.__run())
