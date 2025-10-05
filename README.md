# Bible Verse Clock
Bible Verse Clock is an RPi project that displays the bible's Book, Chapter and Verse to indicate the current time.
This project is based on similar gadgets available for sale retail, albeit without the premium price.

The verses randomaly change every minute to display a new Version and book.

This software is written so that it must have Wifi access to display the verses. It uses a free Bible API at https://github.com/wldeh/bible-api. There are many Bible versions to choose from. The software uses a dictionary listing 10 or so of the available versions. This file is called 'bible_dict.py' and can be edited to add or remove versions. The software will randomly pick a Bible version, and book to display. So if the same version is desired each time, you will want to delete all but the desired version from this file.

If the verse is not properly returned from the API or if there is not a book, chapter and verse that matches the current time, then the current time alone will be displayed.

The software has 6 hidden buttons that can be touched to change the behavior. These 6 buttons are;
<ul>
<li>12/24 hour display (upper right hand corner) 
<li>Light or Dark Display Mode (below the previous button)
<li>Change Display Mode Based on Time (below the previous button)
<li>Quit to Desktop (Upper left hand corner)
<li>Reboot Raspberry Pi (Lower right hand corner)
<li>Shutdown Raspberry Pi (lower left hand corner)
</ul>

These buttons are transparent till the mouse is hovered over one of them. Then it will display the function. When the mouse is no longer over the area, the button hides again.

There is a config file that keeps track of the desired behavior of the clock. This can be edited to change items like the times used to change between Light and Dark modes. Also you can change the colors used for both the Light and Dark display modes.

While the unit built during development used an <a href="https://www.elecrow.com/hdmi-5-inch-800x480-tft-display-for-raspberry-pi-b-p-1384.html?srsltid=AfmBOopdu3iTrjXjR9FxFRh_uzjL6nvhWNImvfrW12346wcKIUp9Ezqk" target="_blank">Elecrow 5 inch display</a>, the software was written in hopes that most any display size could be used. However this has not been widely tested. Your mileage may very. You can change the font sizes in the 'config.py' file and the font used in the 'bible_dict.py' to help adjust the look of the display to better work with different sizes of displays.<br>
<b>NOTE:</b> The main program 'bible_clock.py' must not be running when making edits to the 'config.py' file, as the program locks this file so it can't be overwritten while the program is runnning. 

The software was written to work with the latest version of the RPi operating system and imager; https://www.raspberrypi.com/software/. Most all of the dependecies are included with the latest image. The one that will need to be manually installed is 'Requests'. For information on installing this see; https://docs.python-requests.org/en/stable/user/install/

To make the process easier, the imager will ask if you would like to change settings. Answer 'Yes' and enable SSH, and Wifi for your system. Also, change the password for the RPi, to something like 'bible', rather than the ubiquitous 'raspberry'. You can watch this video for more info; https://youtu.be/yqGsOCZzXec?si=ecWkq4q0Hs-8otca

Using the information in the file 'autostart_instructions.txt' setup your RPi to automatically run 'bible_clock.py'. You can also add a shortcut to the Unix desktop if desired. An icon is provided that can be used as the icon on the desktop if desired. <b>NOTE:</b> On rare occasions the program will not display full screen when first powered up. If this happens, reboot the RPi, and it will display full screen.

Another tool to help with development is to enable VNC on your RPi and use RealVNC on your computer to help install and run Bible Verse Clock. To enable VNC, from the RPi's desktop select 'Preferences/Raspberry Pi Configuration/Interfaces' and enable 'VNC'. If it's not already, enable 'SSH' on the same page. This will give you 2 ways to remotely control your project.

Finally, If needed for your frame, use the display configuration menu on the desktop to invert the display so that the power plug is pointing down, rather than up. Go to 'Preferences/Screen Configuration'. When the next window appears, right click on the HDMI screen provided and select 'Orientation/Inverted'. This makes putting a frame together much easier. A 90 degree micro usb adapter really helped the display frame look clean. Obviously this is optional. 

<h2>Summary of the build</h2>
<ul>
<li>Use the Raspberry Pi imager (https://www.raspberrypi.com/software/) to install the latest version of the OS onto an SD card. 8 gigs or bigger seem to work fine. Change the settings to enable SSH, Wifi and Password.
<li>Put SD card into the RPi and boot up. Give it time, since the first boot may take a while. It may be preferable to have it connected to a monitor and keyboard temporarily.
<li>Update the software if necessary on your RPi by entering the terminal program from the desktop and enter;<p></p>
<code>sudo apt update</code><p>
<code>sudo apt full-upgrade</code><p>
<code>sudo reboot</code><p></p>
<b>Note:<b> you can also use the update mode on the desktop if you prefer.
<li>From the Terminal program, Clone the bible_clock software onto your RPi by entering<p>
<code>sudo mkdir bible_clock</code><p>
<code>cd bible_clock</code><p>
<code>sudo clone https://github.com/markyharris/bible_clock.git</code><p>
<li>Test software by entering;<p>
<code>sudo python3 bible_clock.py</code>
</ul><p>

Connect the display screen you plan to use.
If the display also is a touchscreen, then install the necessary driver and calibrate it. Also, as mentioned enable 'VNC' from the Preferences menu on the desktop.

The development unit built used a 5" touch display that mounted directly to RPi header, so a 90 degree power adapter was needed so the power cord came out the back.

Build a frame as desired. The development unit used a 3d printed case taken from Thingyverse, but a nice wood frame would be nice too.

Good luck and enjoy.
