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

from distutils.core import setup

setup(
    name='senty',
    version='0.1',
    description='Senty Project',
    long_description='Senty is a python based project for testing network.',
    license='GPL v2',
    author='Kamal Heib, Slava Shwartsman, Erez Alfasi',
    author_email='kamalheib1@gmail.com, valyushash@gmail.com, Erez8272@gmail.com',
    url='https://github.com/Kamalheib/senty',
    packages=[
        'senty',
        'senty.rpc',
        'senty.utils',
        'senty.tests',
        'senty.tests.ip',
        'senty.tests.ip.ping',
        'senty.tests.ip.iperf',
        'senty.tests.ip.netperf',
        'senty.tests.blocks',
        'senty.tests.blocks.ip',
        'senty.tests.blocks.rdma',
        'senty.tests.blocks.rdmacm',
        'senty.tests.blocks.common',
        'senty.tests.common',
        'senty.tools',
        'senty.modules',
        'senty.packages',
        'senty.packages.ip'
    ],
    data_files=[('/lib/systemd/system/', ['senty/senty.service'])],
    scripts=['senty/rpc/senty_rpc_server.py']
)
