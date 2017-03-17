#!python
# -*-coding:utf-8-*-

# Author: Guo Zhang
# Reference: http://shelly-kuang.iteye.com/blog/797713

from __future__ import print_function

import os
import sys
from optparse import OptionParser


def texcleaning(path):
    for fname in os.listdir(path):
        name, ext = os.path.splitext(fname)
        latex_exts = [".aux",
                      ".fdb_latexmk",
                      ".fls",
                      ".gz",
                      ".log",
                      ".out",
                      ".nav",
                      ".snm",
                      ".toc",
                      ]
        if (ext in latex_exts) and \
                (name.replace(".synctex", "") + ".tex" in os.listdir(path)):
            os.remove(os.path.join(path, fname))
            print("Deleted: %s" % (fname))

    print("All tex temporary files in %s cleaned." % (path))


def main():

    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage=usage, version="%prog 0.0.1.dev2")
    parser.add_option('-p', '--path', default=os.getcwd())
    (options, args) = parser.parse_args()

    texcleaning(options.path)


if __name__ == "__main__":
    sys.exit(main())
