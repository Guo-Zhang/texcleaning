#!/usr/local/opt/python/bin/python2.7
# -*-coding:utf-8-*-

# Author: Guo Zhang
# Reference: http://shelly-kuang.iteye.com/blog/797713

from __future__ import print_function

import os
from optparse import OptionParser


def texcleaning(path):
    """
    Clean temporary files created by tex engines

    Parameters
    ----------
     path: the path of input dictionary

    """
    _delete = False

    for fname in os.listdir(path):
        if os.path.isdir(os.path.join(path, fname)):
            texcleaning(os.path.join(path, fname))

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
            _delete = True
            print("Deleted: %s" % (os.path.join(path, fname)))

    if _delete:
        print("All tex temporary files in %s cleaned." % (path))


def main():

    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage=usage, version="%prog 0.0.1.dev3")
    parser.add_option('-p', '--path', default=os.getcwd())
    (options, args) = parser.parse_args()

    texcleaning(options.path)


if __name__ == "__main__":
    texcleaning("/Users/zhangguo/CPP")
