#!/usr/bin/Python3.4

import errors

def file_opener(name):
    if name is None:
        return None
    try:
        f = open(name, "r")
    except:
        errors.file_fail(name, "failed to open")
        return None
    if f.mode == "r":
        content = f.read()
        return content
    else:
        errors.file_fail(name, "couldn't read")

#
#   Check if a string / character is caps
#

def is_upper(c):
    if type(c) is chr:
        ascii_val = ord(c)
        if ascii_val < 65 or ascii_val > 90:
            return False
        return True
    else:
        for e in c:
            ascii_val = ord(e)
            if ascii_val < 65 or ascii_val > 90:
                return False
        return True

class Inputs:
    def __init__(self):
        self.line = 0
        self.nodes = dict()
        self.multi_rules = dict()
        self.queries = []
        self.entries = []
        self.current = "rules"

    def take_entries(self, line):
        if self.current != "rules":
            if self.current == "entries":
                msg = "Only one line for initial facts allowed"
            else:
                msg = "You cannot insert initial facts here, respect the order : " \
                        + "Rules => Initial facts => Queries"
            errors.parse(self.line, msg)
        if not is_upper(line):
            errors.parse(self.line, "Initial facts not well formated, only upper-case " \
                    + "alphabetical characters allowed")
        for c in line:
            self.entries.append(c)
        self.current = "entries"

    def take_queries(self, line):
        if self.current != "entries":
            if self.current == "queries":
                msg = "Only one line for querys allowed"
            else:
                msg = "You cannot insert queries here, respect the order : " \
                        + "Rules => Initial facts => Queries"
            errors.parse(self.line, msg)
        if not is_maj(line):
            errors.parse(self.line, "Query not well formated, only upper-case alphabetical characters allowed")
        for c in line:
            self.queries.append(c)
        self.current = "queries"
    
    def take_rules(self, line):
        if self.current != "rules":
            errors.parse(self.line, "You cannot insert a rule here, respect the order : " \
                    + "Rules => Initial facts => Queries")
        return None

    def parsing(self, content):
        content = content.replace(" ", "")
        content = content.replace("\t", "")
        lines = content.split("\n")
        for line in lines:
            self.line += 1
            if '#' in line:
                line = line[:line.index('#')]
            if len(line) > 0 and line[0] == '=':
                self.take_entries(line[1:])
            if len(line) > 0 and line[0] == '?':
                self.take_queries(line[1:])
            else:
                self.take_rules(line)
