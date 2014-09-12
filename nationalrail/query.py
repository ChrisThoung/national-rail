# -*- coding: utf-8 -*-
"""
query
=====
Define the Query class to handle web URL queries.

"""


import datetime
import re
import webbrowser

from nationalrail.codes import lookup


class Query:
    """Class, to generate a URL request from a set of command-line arguments.

    """

    def __init__(self, args):
        """Store command-line arguments.

        Parameters
        ==========
        args : argparse ArgumentParser object
            Arguments extracted from `nationalrail.py`

        """
        self.args = args
        # Mapping of command-line `when` arguments to URL codes
        self.when_map = {
            'leaving': 'dep',
            'arriving': 'arr',
            'first': 'first',
            'last': 'last', }

    def plan(self):
        """Generate and call the journey-planning API.

        """
        # Extract arguments to a dictionary
        args = vars(self.args)
        # Parse arguments
        origin = self.match_station(args['from'][0])
        destination = self.match_station(args['to'][0])
        date = self.parse_date(args['date'][0])
        time = self.parse_time(args['time'][0])
        when = self.when_map[args['when']]
        # Form argument list and join
        pieces = [
            'http://ojp.nationalrail.co.uk/service/timesandfares',
            origin,
            destination,
            date,
            time,
            when, ]
        url = '/'.join(pieces)
        # Add direct switch if required
        if args['direct']:
            url = url + '?directonly'
        # Call
        webbrowser.open(url, new=2, autoraise=True)

    def match_station(self, station):
        """Match `station` to a specific station code.

        Parameters
        ==========
        station : string
            Either a station code or a search pattern (regular expressions are
            permitted) for a station

        Returns
        =======
        station : string
            Closest station match

        Notes
        =====
        If `station` is specified as a three-letter code in `lookup`, then this
        function simply returns the string, unmodified.

        Otherwise, this function proceeds to carry out a search in the list of
        'long' station names and return the closest match, if possible.

        In the case of multiple matches, a warning message is printed.

        Where there is no match, an error is raised.

        """
        if station not in lookup.values():
            raise ValueError('Unable to locate %s in station list' % (station))
        return station

    def parse_date(self, date):
        """Parse `date` as required.

        Parameters
        ==========
        date : string
            User-specified date

        Returns
        =======
        date : string
            Processed date argument for web query

        Notes
        =====
        If `date` is not a six-digit string, this function checks for a special
        date case and generates an appropriate date argument as required.

        """
        # Test for six-digit string
        if re.match('^[0-9]{6}$', date) is None:
            # Use current date and time to form a `datetime` object
            now = datetime.datetime(2000, 1, 1).today()
            # Test for special cases
            if date == 'today':
                date = ('%02d' % (now.day) +
                        '%02d' % (now.month) +
                        str(now.year)[2:4])
            elif date == 'tomorrow':
                date = ('%02d' % (now.day) +
                        '%02d' % (now.month + 1) +
                        str(now.year)[2:4])
            else:
                raise ValueError('Invalid `date` argument: %s' % (date))
        # Return
        return date

    def parse_time(self, time):
        """Parse `time` as required.

        Parameters
        ==========
        time : string
            User-specified time

        Returns
        =======
        time : string
            Processed time argument for web query

        Notes
        =====
        If `time` is not a four-digit string, this function checks for an
        argument value of 'now' and generates an appropriate time argument as
        required.

        """
        # Test for four-digit string
        if re.match('^[0-9]{4}$', time) is None:
            # Use current date and time to form a `datetime` object
            now = datetime.datetime(2000, 1, 1).today()
            # Test for special cases
            if time == 'now':
                time = '%02d' % (now.hour) + '%02d' % (now.minute)
            else:
                raise ValueError('Invalid `time` argument: %s' % (time))
        # Return
        return time
