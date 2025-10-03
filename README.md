# Bible Verse Clock
Bible Verse Clock is a RPi project that displays the bible's Book, Chapter and Verse indicating the current time.
This project is based on similar gadgets available for sale retail, albeit at a premium price.

This utilizes a Raspberry Pi and a 5" touch screen to display the bible verses. The verses change every minute and the verse indicates the current time.

This software is written so that it must have Wifi access to display the verses. It uses a free Bible API at https://github.com/wldeh/bible-api. There are many Bible versions to choose from. The software uses a dictionary listing 10 or so of these. This file is called 'bible_dict.py' and can be edited to add or remove versions. The software will randomly pick a Bible version, and book to display. So if the same version is desired each time, you will want to delete all but the desired version from this file.
if the verse is not properly returned from the API or if there is not a book, chapter and verse that matches the time, then the time alone will be displayed.

The software has 6 hidden buttons that can be touched to change the behavior. These 6 buttons are;
<ul>
<li>12/24 hour display (upper right hand corner) 
<li>Light or Dark Display Mode (below the previous button)
<li>Change Display Mode Based on Time (below the previous button)
<li>Quit to Desktop (Upper left hand corner)
<li>Reboot Raspberry Pi (Lower right hand corner)
<li>Shutdown Raspberry Pi (lower left hand corner)
</ul>

These buttons are transparent till the mouse is over them. Then they will display. When the mouse is no longer over the area, the button goes away again.

There is a config file that keeps track of the desired behavior of the clock. This can be edited to change items like the times used to change between Light and Dark modes. Also you can change the colors used for both display modes here.

While the unit built used a 5 inch display, the software was written in hopes that most any display size could be used. However this has not been widely tested. Your mileage may very. You can change the font sizes in the 'config.py' file and the font used in the 'bible_dict.py' to help adjust the look of the display to better work with different sizes of displays.

The software was written to work with the latest version of the RPi operating system and imager; https://www.raspberrypi.com/software/. Most all of the dependecies are included with the latest image. The one that will need to be manually installed is 'Requests'. For information on installing this see; https://docs.python-requests.org/en/stable/user/install/

Using the information in the file 'autostart_instructions.txt' setup your RPi to automatically run 'bible_clock.py'. You can also add a shortcut to the Unix desktop if desired. An icon is provided that can be used as the icon on the desktop if desired.

Finally, use the display configuration menu on the desktop to invert the display so that the power plug is pointing down, rather than up. This made putting a frame together much easier. Obviously this is optional. A 90 degree micro usb adapter really helped the display frame look clean.

<h2>Summary of the build</h2>
<ul>
<li>Use the Raspberry Pi imager (https://www.raspberrypi.com/software/) to install the latest version of the OS onto an SD card. 8 gigs or bigger seem to work fine.
<li>Put SD card into the RPi and boot up. Give it time, since the first boot may take a while. It may be preferable to have it connected to a monitor and keyboard temporarily.
<li>Update the software if necessary on your RPi by entering the terminal program from the desktop and enter;
<code>sudo apt update</code>
<code>sudo apt full-upgrade</code>
<code>sudo reboot</code>
<li>Clone the bible_clock software onto your RPi by entering
<code>sudo mkdir bible_clock</code>
<cold>cd bible_clock</code>
<code>sudo clone https://github.com/markyharris/bible_clock.git</code>
<li>Test software by entering;
<code>sudo python3 bible_clock.py</code>


Good luck and enjoy.
