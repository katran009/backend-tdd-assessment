#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "katran009, demo with Piero"


import argparse
import sys


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(description="Perform transformation on input text.")
    parser.add_argument("-u", "--upper", action="store_true", help="convert text to uppercase")
    parser.add_argument("-l", "--lower", help="convert text to lowercase")
    parser.add_argument("-t", "--title", help="convert text to titlecase")
    parser.add_argument("text", help="text to be manipulated")
    return parser

def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)

    # The BIDNESS LOGIC
    result = ns.text
    if ns.upper:
        result = result.upper()
    if ns.lower:
        result = result.lower()
    if ns.title:
        result = result.title()

    return result


if __name__ == '__main__':
    main(sys.argv[1:])