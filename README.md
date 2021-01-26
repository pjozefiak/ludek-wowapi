# WoW API Client (Ludek)

From time to time, when I need to process some bigger amount of data for my favorite MMORPG I tend to write some small scripts to be used with pseudo-client framework for WoW API which I made couple of years ago.

Now it's the time of need again, yet this time - Blizzard made some bigger changes to the API, so I decided to rewrite my pseudo-client.

Also planing probably bigger project with it, but who knows if I have time and will to finish it before next rewrite

## General purpose of this
Pseudo-client and data dumper for **World of Warcraft API**, including some scripts for personal use.

## Installation guide
Install required packages
```
$ pip install -r requirements.txt
```
Fill your API credentials in `data/config.ini`

Run the setup script to dump basic data
```
$ python client_startup.py
```

Have fun (as it does almost nothing at the moment)

## Changelog
[CHANGELOG.md](https://github.com/pjozefiak/ludek-wowapi/blob/master/CHANGELOG.md)

## Author
[Piotr "Ludek" Józefiak](https://github.com/pjozefiak)