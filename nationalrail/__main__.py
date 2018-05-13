#!/usr/bin/python3
# -*- coding: utf-8 -*-

from nationalrail.cli import parser


def main():
    # Parse arguments
    args = parser.parse_args()

    # Set up Query object
    from nationalrail.query import Query
    q = Query(args)

    # Process according to selected command
    if args.command == 'plan':
        q.plan()


if __name__ == '__main__':
    main()
