# Wifi Bible Clock
Wifi Bible Clock that displays the bible's Book, Chapter and Verse which indicates the current time.
Based on similar gadgets available for sale online, albeit at a premium price.

This utilizes a Raspberry Pi and a 5" touch display to display the bible verses. The verses change every minute and the verse indicates the current time.

This software is written so that it must have Wifi access to display the verses. It uses a free Bible API at https://github.com/wldeh/bible-api. There are many versions to choose from. The software uses a dictionary listing 10 or so of these. This file is called bible_dict.py and can be edited to add or remove versions. The software will randomly pick a version, and book to display. So if the same version is desired each time, you will want to delete all but the desired version from this file.
The software has 6 hidden buttons that can be touched to change the behavior. These 6 buttons are;
<ul>
<li></li>12/24 hour display
<li>Light or Dark Display Mode
<li>Change Display Mode Based on Time
<li>Quit to Desktop
<li>Reboot Raspberry Pi
<li>Shutdown Raspberry Pi
</ul>

There is a config file that keeps track of the desired behavior of the clock. This can be edited to change items like the times used to change between Light and Dark modes. Also you can change the colors used for both display modes here.

While the unit built used a 5 inch display, the software was written in hopes that most any display size could be used. However this has not been widely tested. Your mileage may very. You can change the font sizes in the config.py file to help adjust the look of the display to better work with different sizes of displays.

The software was written to work with the latest version of the RPi operating system and imager; https://www.raspberrypi.com/software/. Most all of the dependecies are included with the latest image. The one that will need to be manually installes is 'Requests'. For information on this see; https://docs.python-requests.org/en/stable/user/install/

Using the information in the file 'autostart_instructions.txt' setup your RPi to automatically run bible_clock.py. You can also add a shortcut to the Unix desktop if desired.

Finally, use the display configuration on the desktop to invert the display so that the power is pointing down, rather than up. This made putting a frame together much easier. Obviously this is optional.
