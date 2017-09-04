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

import xml.sax


class PackagesParser(xml.sax.ContentHandler):

    def __init__(self):
        self.CurrentData = ""
        self.package = ""
        self.test_path = ""
        self.test_title = ""
        self.name = ""
        self.ip_test_dict = {}
        self.rdma_test_dict = {}
        self.rdmacm_test_dict = {}

    def get_test_dictionaries(self):
        return self.ip_test_dict, self.rdma_test_dict, self.rdmacm_test_dict

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "package":
            self.name = attributes["name"]
        if tag == "test":
            self.test_title = attributes["name"]

    def endElement(self, tag):
        if self.CurrentData == "test":
            self.add_to_dict()
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "test":
            self.test_path = content
        else:
            self.CurrentData = ""

    def add_to_dict(self):
        if self.name == 'ip':
            self.ip_test_dict.__setitem__(self.test_title, self.test_path)
        elif self.name == 'rdma':
            self.rdma_test_dict.__setitem__(self.test_title, self.test_path)
        elif self.name == 'rdmacm':
            self.rdmacm_test_dict.__setitem__(self.test_title, self.test_path)
