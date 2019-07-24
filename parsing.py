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
        self.read = {
                "nodes":False,
                "multi_rules":False,
                "queries":False,
                "entries":False,
                }

    def take_entries(self, line):
        if not is_upper(line):
            errors.parse(self.line, "Entry not well formated, only upper-case alphabetical characters allowed")
        if self.read["entries"]:
            errors.parse(self.line, "Only one line for initial facts allowed")
        for c in line:
            self.entries.append(c)

    def take_queries(self, line):
        if not is_maj(line):
            print("Query not well formated")
            exit()
        for c in line:
            self.queries.append(c)
    
    def take_rules(self, line):
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
