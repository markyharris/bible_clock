# Wifi Bible Clock
Wifi Bible Clock that displays the bible's Book, Chapter and Verse which indicates the current time.
Based on similar gadgets available for sale online, albeit at a premium price.

This utilizes a Raspberry Pi and a 5" touch display to display the bible verses. The verses change every minute and the verse indicates the current time.

This software is written so that it must have Wifi access to display the verses. It uses a free Bible API at https://github.com/wldeh/bible-api. There are many versions to choose from. The software uses a dictionary listing 10 or so of these. This file is called bible_dict.py and can be edited to add or remove versions. The software will randomly pick a version, and book to display. So if the same version is desired each time, you will want to delete all but the desired version from this file.
