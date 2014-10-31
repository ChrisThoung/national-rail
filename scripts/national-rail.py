#!/usr/bin/python3


import argparse

from nationalrail import __version__ as version


# Create top-level parser
parser = argparse.ArgumentParser(
    description='Command-line tools for UK national rail queries')
parser.add_argument(
    '-V', '--version',
    action='version',
    version=version)

# Add sub-parsers
subparsers = parser.add_subparsers(
    title='commands',
    dest='command')

# 'plan' sub-parser
parser_plan = subparsers.add_parser(
    'plan',
    help='run a journey query')
# Required arguments: from, to
parser_plan.add_argument(
    'from',
    nargs=1,
    metavar='FROM',
    default=None,
    type=str,
    help='set station to travel from')
parser_plan.add_argument(
    'to',
    nargs=1,
    metavar='TO',
    default=None,
    type=str,
    help='set station to travel to')
# Optional arguments (with defaults)
parser_plan.add_argument(
    '--date',
    nargs=1,
    metavar='DATE',
    default=['today'],
    type=str,
    required=False,
    help='set date for travel')
parser_plan.add_argument(
    '--time',
    nargs=1,
    metavar='TIME',
    default=['now'],
    type=str,
    required=False,
    help='set time for travel')
parser_plan.add_argument(
    '--when',
    nargs=1,
    metavar='WHEN',
    choices=['leaving', 'arriving', 'first', 'last'],
    default=['leaving'],
    type=str,
    required=False,
    help='when to leave relative to the other options')
parser_plan.add_argument(
    '--allow-non-direct',
    action='store_true',
    default=False,
    required=False,
    help='allow non-direct trains in query')


# Main-scope code
if __name__ == '__main__':
    # Parse arguments
    args = parser.parse_args()
    # Set up Query object
    from nationalrail.query import Query
    q = Query(args)
    # Process according to selected command
    if args.command == 'plan':
        q.plan()
