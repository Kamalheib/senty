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


class Service(object):
    def __init__(self, name, logger, host):
        self._name = name
        self._logger = logger
        self._host = host

    def get_name(self):
        return self._name

    def get_logger(self):
        return self._logger

    def get_host(self):
        return self._host

    def start(self):
        rc, out = self.Host.run_command("systemctl start %s" % self.Name)
        if rc:
            self.Logger.pr_err('%s - Failed to start %s service' % self.Name)
            self.Logger.pr_err('%s - %s' % (self.Host.IP, out))
        return rc

    def stop(self):
        rc, out = self.Host.run_command("systemctl stop %s" % self.Name)
        if rc:
            self.Logger.pr_err('%s - Failed to stop %s service' % self.Name)
            self.Logger.pr_err('%s - %s' % (self.Host.IP, out))
        return rc

    Name = property(get_name)
    Host = property(get_host)
    Logger = property(get_logger)
