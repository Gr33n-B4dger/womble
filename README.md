# womble

Wobbly Womble is a python script for checking IPs against the IPVoid database of blacklists

IPVoid scans more than 60 DNS blacklists and returns the results.

Wobbly Womble has been built using selenium to interface with websites that do not necessarily have APIs

Chrome browser enables this, however a driver is required to allow it to interface please download and install this from: https://sites.google.com/a/chromium.org/chromedriver/

This initial commit allows singular IPs to be queries before returning to the start and enabling further queries.

V2 aims to enable a list to be queried before exporting to a CSV or txt file
