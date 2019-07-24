#!/usr/bin/Python3.4

from sys import argv as av
import errors
import parsing

if len(av) != 2:
    errors.usage()
content = parsing.file_opener(av[1])
if content is "":
    errors.empty(av[1])
print(content)
inputs = parsing.Inputs()
inputs.parsing(content)
print(inputs.entries)
