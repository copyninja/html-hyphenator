#!/usr/bin/python

############################################################################################################################
#                                                                                                                          #
#   lhtml-hyphenator.py                                                                                                     #
#                                                                                                                          #
#   Copyright 2011 Vasudev Kamath <kamathvasudev@gmail.com>                                                                #
#                                                                                                                          #
#   This program is free software; you can redistribute it and/or modify                                                   #
#   it under the terms of the GNU  General Public License as published by                                                  #
#   the Free Software Foundation; either version 3 of the License, or                                                      #
#   (at your option) any later version.                                                                                    #
#                                                                                                                          #
#   This program is distributed in the hope that it will be useful,                                                        #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of                                                         #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                                                          #
#   GNU General Public License for more details.                                                                           #
#                                                                                                                          #
#   You should have received a copy of the GNU General Public License                                                      #
#   along with this program; if not, write to the Free Software                                                            #
#   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,                                                             #
#   MA 02110-1301, USA.                                                                                                    #
############################################################################################################################




from BeautifulSoup import BeautifulSoup,SoupStrainer,Comment
from hypy import Hyphenator
from optparse import OptionParser
import sys

hyphen = Hyphenator()

usage = """%prog [optional] lang_code input_file

           lang_code: ISO language code. Specifies the language of input file
           input_file: HTML file which should be used as input
"""

parser = OptionParser(usage=usage)
parser.add_option("-s","--symbol",dest="hyphen_symbol",action="store",
                  help="Hyphenation Symbol to use by default soft hyphen(\u00AD) is used",metavar="SYMBOL")
parser.add_option("-o","--output",dest="out_file",action="store",
                  help="Output file by default this command over writes input file",metavar="FILE")

def parse_and_hyphenate(data,lang_code="ml_IN",hyphen_symbol="\u00AD"):
    soup1 = BeautifulSoup(data)
    soup2 = BeautifulSoup(data,parseOnlyThese=SoupStrainer('body'))

    for t in soup2.findAll(text= lambda text:not isinstance(text,Comment)):
        text = unicode(t)
        text = hyphen.hyphenate(text,lang_code)
        t.replaceWith(text)

    soup1.body.replaceWith(soup2.body)
    return soup1.prettify()

def main():
    (options,args) = parser.parse_args()
    if len(args) != 2:
        print "Insufficient arguments. Use " + sys.argv[0] + " -h or --help to get more information on command usage."
        sys.exit(1)

    hyphenated_data = ""
    
    lang_code = args[0]
    input_file = args[1]

    fp = open(input_file,"r")
    data = fp.read()
    fp.close()

    if options.hyphen_symbol:
        hyphenated_data = parse_and_hyphenate(data,lang_code,options.hyphen_symbol)
    else :
        hyphenated_data = parse_and_hyphenate(data,lang_code)

    if options.out_file:
        fp = open(options.out_file,"wb")
        fp.write(hyphenated_data)
        fp.close()
    else :
        fp = open(input_file,"w")
        fp.write(hyphenated_data)
        fp.close()
