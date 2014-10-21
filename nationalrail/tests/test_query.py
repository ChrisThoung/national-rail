# -*- coding: utf-8 -*-


from nose.tools import with_setup

import nationalrail.query


def setup():
    global q
    q = nationalrail.query.Query(None)


@with_setup(setup)
def test_match_station():
    pass


if __name__ == '__main__':
    import nose
    nose.runmodule()
