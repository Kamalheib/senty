#!/usr/bin/env python

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

import re
import xmlrpclib


class Host(object):
    ERROR_KEYWORDS = r'(error|fail|synd|assert)'

    def __init__(self, ip, logger, id, port=8000, interfaces=[]):
        self._ip = ip
        self._logger = logger
        self._id = id
        self._port = port
        self._interfaces = interfaces

    def get_ip(self):
        return self._ip

    def get_logger(self):
        return self._logger

    def get_id(self):
        return self._id

    def get_port(self):
        return self._port

    def get_interfaces(self):
        return self._interfaces

    def get_proxy_server(self):
        if not hasattr(self, "_proxy_server"):
            self._proxy_server = xmlrpclib.ServerProxy("http://%s:%d" % (self.IP, self.Port), allow_none=True)
        return self._proxy_server

    def run_command(self, command):
        self.Logger.pr_info("%s - Running command: %s" % (self.IP, command))
        (rc, output) = self.ProxyServer.run_command(command)
        if rc:
            self.Logger.pr_err("%s - %s" % (self.IP, output))
        return rc, output

    def run_process(self, command):
        self.Logger.pr_info("%s - Running process: %s" % (self.IP, command))
        pid = self.ProxyServer.run_process(command)
        return pid

    def wait_process(self, pid):
        (rc, output) = self.ProxyServer.wait_process(pid)
        if rc:
            self.Logger.pr_err("%s - %s" % (self.IP, output))
        return rc, output

    def kill_process(self, pid):
        try:
            self.ProxyServer.kill_process(pid)
        except OSError:
            self.ProxyServer.kill_process(pid, 1)

    def get_logs(self):
        DMESG_CMD = 'dmesg'
        return self.run_command(DMESG_CMD)[1]

    def validate_logs(self):
        """
        Return Value:
            False - No errors were found in the log
            True - Error was found in the log
        """
        out = self.get_logs()
        match_obj = re.search(self.ERROR_KEYWORDS, out, flags=re.IGNORECASE)

        if match_obj:
            self.Logger.pr_err("%s - --==FOUND ERROR IN LOGS==--" % self.IP)
            self.Logger.pr_err("%s - %s" % (self.IP, "-" * 80))
            self.Logger.pr_err("%s - \n%s" % (self.IP, out))
            self.Logger.pr_err("%s - %s" % (self.IP, "-" * 80))
            return True
        return False

    def clear_logs(self):
        DMESG_CLEAR_CMD = 'dmesg -c'
        return self.run_command(DMESG_CLEAR_CMD)[0]

    ID = property(get_id)
    IP = property(get_ip)
    Port = property(get_port)
    Logger = property(get_logger)
    Interfaces = property(get_interfaces)
    ProxyServer = property(get_proxy_server)
