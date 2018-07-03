#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import codecs
import os, sys
import pprint
import re

#-------------------------------------------------------------------------#
#
#                         ▗▀▖▗       ▐                
#                   ▌ ▌▞▀▖▐  ▄ ▞▀▖▝▀▖▜▀ ▞▀▖▙▀▖  ▛▀▖▌ ▌
#                   ▚▄▌▌ ▌▜▀ ▐ ▌ ▖▞▀▌▐ ▖▌ ▌▌  ▗▖▙▄▘▚▄▌
#                   ▗▄▘▝▀ ▐  ▀▘▝▀ ▝▀▘ ▀ ▝▀ ▘  ▝▘▌  ▗▄▘
#
# Description:
#    This is a Russian text yoficator (ёфикатор).
#
#    It conservatively replaces every "е" to "ё" when it's unambiguously 
#    a case of the latter. No context is used; it relies entirely on a lack
#    of dictionary entries for a correspondent "truly е" homograph. 
#
#    Yoficating Russian texts remove some unnecessary ambiguity.
#    https://en.wikipedia.org/wiki/Yoficator
#    https://ru.wikipedia.org/wiki/Ёфикатор
#
#    Syntax: yoficator.py [text-file-in-Russian | string-in-Russian]
# 
#    Depends on yoficator.dic, which is used for the lookup.
#
#    Limitations: 
#    * The code being conservative and not looking for context, it won't correct 
#      when a "truly е" homograph exists. Thus a "все" will never be corrected, 
#      because both все and всё exist as different words.
#    * Prone to wrongly yoficate other Cyrillic-based languages, such as 
#      Bulgarian, Ukrainian, Belarussian.
#    * It's not the fastest thing in the world, mind you. But does the job.
#
#-------------------------------------------------------------------------
#
# Found this useful? Appalling? Appealing? Please let me know.
# The Unabashed welcomes your impressions. 
#
# You will find the
#   unabashed
# at the location opposite to
#   moc • thgimliam
#
#-------------------------------------------------------------------------
#
# License:
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
#--------------------------------------------------------------------------#

# TODO Better handle lowercase, uppercase

pp = pprint.PrettyPrinter(4) 

# Variables initialization; tests a file if no argument is supplied.
# Save the yoficator as a subfolder of your Desktop
# TODO: Make it compatible with other OSs.
workingDir = "./"
textFile = workingDir + "tests/yoficator.txt"
dictionaryFile = workingDir + "yo.dat"

if len(sys.argv) > 1:
    # Is the input a filename?
    if os.path.isfile(sys.argv[1]):
        text = codecs.open(sys.argv[1].decode("utf-8"), "r", "utf-8").read()
    # Else we will assume it's a string
    else:
        text = sys.argv[1].decode("utf-8")
else:
    # We will assume using textFile as input filename above
    text = codecs.open(textFile, "r", "utf-8").read()

dictionary = {}


# Splitter / tokenizer
splitter = re.compile(r'(\s+|\w+|\W+|\S+)', re.UNICODE)
tokens = splitter.findall(text)

# Make key:value, ignore *
with codecs.open(dictionaryFile, "r", "utf-8") as f:
    for line in f:
        if not "*" in line:
            value = line.rstrip('\n')
            key = re.sub(r'ё', 'е', value)
            dictionary[key] = value

for token in tokens:
    if token in dictionary:
        print(dictionary[token].encode('utf8'), end='')
    else:
        print(token.encode('utf8'), end='')


sys.exit(0)

# -------------------- END -----------------------

