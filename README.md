# video_collector
A simple Python tool to query from the command line and obtain Youtube video data from the last 24 hrs relating to a keyword. This is a *basic* introduction to natural disaster detection with social media sentiment.

## Getting Started
This tool utilizes the Youtube Data API. In order to use this tool you **must** register for an API key here: https://developers.google.com/youtube/v3/. Place your developer key in *app.ini*.

## Example
Generating a report for the term *"Cactus"* and saving the report to *"cactus.txt"*:
```
bin/python2.7 report.py --term Cactus --report cactus.txt
cat cactus.txt
09/09/17 13:30:36	10/09/17 13:30:36
piLGXY6WLUA	DOS NOOBS VS TRAMPAS DE CACTUS EN MINECRAFT 😆 NOOBS VS PARKOUR MAPA MINECRAFT	530898
01xpr6sDjo0	CACTUS TORTURE!! PvZ Garden Warfare PVZ mod 2017 | IULITM | Plants vs Zombies	69608
eajHZiwFnW0	Travis Scott - Huncho Farm Cactus Jack Alarm Freestyle	3670
ecMYMRiayrI	My Epiphyllum oxypetalum - 'Queen of the Night' Cactus Plant in beautiful Flower	455
5E1mL4rYzYY	Haz Bonitos Cactus y Decora tus Macetas I Craftabulous	346
XSzxFkriGpY	Alumilite Cholla Cactus Pen Blanks | Dunkin Junk	237
j7Od0wfF1yw	Guys Removes Cactus From Hawk	161
P1cmfQmHVYY	A.C.E – CACTUS (선인장) (English Version) (Color Coded English Lyrics)	149
ANIL2sRt7m0	Crazy Cacti Clan Meet Up #3	128
PMK_vELRKDY	A.C.E - Cactus x iKon - Bling Bling (Remix) Dance Cover by 2SI16	99
```
