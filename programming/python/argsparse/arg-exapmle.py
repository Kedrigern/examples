#!/usr/bin/env python3

__version__ = "v1.1.0"

import sys
import argparse
import configargparse

def parse_args_base(parser: argparse.ArgumentParser):
    """ Common definition of arguments """
    subparsers = parser.add_subparsers()
    parser_cmd1 = subparsers.add_parser("cmd1", description="Command 1 description")
    parser_cmd2 = subparsers.add_parser("cmd2", description="Command 2 description")
    parser_cmd1.add_argument('-f', '--force', action='store_true', help="Use force!")
    parser_cmd1.add_argument('-t', '--text', help="Text variable.")
    parser_cmd2.add_argument('--42', action='store_const', const=42, help="Use 42")
    parser_cmd2.add_argument('inputs', metavar='input files', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='Input files')

    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__ )

def parse_args_1(arguments):
    """ Usualy argparse """
    parser = argparse.ArgumentParser(description="Example script with arguments")
    parse_args_base(parser)
    return parser.parse_args(arguments)


def parse_args_2(arguments):
    """ ConfigArgParse """
    parser = configargparse.ArgParser(description="Example script with arguments", default_config_files=['./config.ini'])
    parse_args_base(parser)
    return parser.parse_args(arguments)

if __name__ == '__main__':
    argv = sys.argv[1:]
    settings = parse_args_1(argv)
    #settings = parse_args_2(argv)
    print(settings)
