# -*- coding: utf-8 -*-
"""
favourites
==========
Define the `nationalrail` Favourites class to handle frequent user-specified
trips.

"""


import os


class Favourites:

    def __init__(self):
        pass

    def load(self, path):
        home = os.path.expanduser('~')
