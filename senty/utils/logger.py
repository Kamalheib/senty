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

import logging

LOG_FILE = '/var/log/%s.log'
FORMAT = '%(asctime)s - %(name)s: %(levelname)s: %(message)s'


class Logger(object):
    def __init__(self, name, level='info', create_log=False):
        numeric_level = getattr(logging, level.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s' % level)

        logging.basicConfig(filename=('', LOG_FILE % name)[create_log],
                            level=numeric_level, format=FORMAT)
        self._logger = logging.getLogger(name)

    def pr_info(self, msg):
        self._logger.info(msg)

    def pr_err(self, msg):
        self._logger.error(msg)

    def pr_dbg(self, msg):
        self._logger.debug(msg)
