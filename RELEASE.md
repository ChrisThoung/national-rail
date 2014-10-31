# Release notes

Version: 0.2.0

Fixes:

* Correct station-matching code to search the whole of a station string. This
  ensures that, for example, 'Kings Cross' correctly matches 'London Kings
  Cross'. Previously, the match only search at the beginning of a string
* Correct handling of `tomorrow` in `--date` argument to increment the day, not
  the month, and roll over to the next month (and year) if currently the last
  day of the month
