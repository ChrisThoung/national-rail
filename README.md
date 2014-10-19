# national-rail

Python package to perform UK National Rail queries.

## Usage

### Train times

The following command-line operation will open a browser containing the train
times from London Kings Cross (KGX) to Cambridge (CBG), departing as soon as
possible:

```
python national-rail.py plan KGX CBG
```

If the station code is unknown, the script will pick the first possible match
(alphabetically) out of a search of the station names:

```
python national-rail.py plan London Cambridge
```

A web-brower instance will still be opened (using the first match), but the
candidate stations will also be listed for reference:

```
python national-rail.py plan London Cambridge

Multiple matches found for 'London':
   BFR London Blackfriars
   LBG London Bridge
   CST London Cannon Street
   CHX London Charing Cross
   EUS London Euston
   FST London Fenchurch Street
   LOF London Fields
   KGX London Kings Cross
   LST London Liverpool Street
   MYB London Marylebone
   PAD London Paddington
   LRB London Road (Brighton)
   LRD London Road (Guildford)
   SPX London St Pancras (Intl)
   STP London St Pancras International
   VIC London Victoria
   WAT London Waterloo
   WAE London Waterloo East
Selecting first match (BFR: London Blackfriars)
Multiple matches found for 'Cambridge':
   CBG Cambridge
   CBH Cambridge Heath
Selecting first match (CBG: Cambridge)
```

The user can also set the date and time as follows:

```
python national-rail.py plan KGX CBG --date 251014 --time 0800
```

(`tomorrow` is also a valid `--date` argument.)

By default, date and time information are taken to be the preferred departure
date and time (`leaving`). This can be changed with the `--when` option:

```
python national-rail.py plan KGX CBG --date 251014 --time 1100 --when arriving
```

Other valid options are:

* `leaving`: the default
* `first`: the first train out in the morning
* `last`: the last train out at night

## Installation

This package needs a list of station codes. These are available
(here)[http://www.nationalrail.co.uk/stations_destinations/48541.aspx] in the
required format.

The necesary format is a CSV file with two columns as follows:

Station name |Code
-------------|-----
Abbey Wood   |ABW
Aber         |ABE
Abercynon    |ACY

Save the file with name `station_codes.csv` to the same folder as `setup.py`
before installing:

```
python setup.py install
```
