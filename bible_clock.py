# Bible Verse Clock v0.5 - Mark Harris
# Based on API at https://github.com/wldeh/bible-api
# tkinter color chart; https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
# This version displays to cmd line and to Display in Full Screen Mode
# See file 'autostart_instructions.txt' to setup RPi to automatically execute bible_clock.py
# See file 'config.py' to change colors, borders etc.
# See file 'bible_dict' for available bible versions from API, as well as fonts used.
# sudo apt install brightnessctl, sudo brightnessctl set <percentage>% for touch screen calibration
# Light and Dark modes now available.

# Imports
import sys
import os
import requests
import subprocess
import json
import time
import random
import tkinter as tk
from tkinter import *
from time import strftime
from bible_structure import *
from config import *
from bible_dict import *

# Variables and Constants
global font_label_size
global font_msg_size


# Routines
def toggle_time_mode():
    global hour_12,light_dark_mode,use_screen_mode,light_mode_on,dark_mode_on,dark_bg_color
    global dark_msg_color,dark_label_color,light_bg_color,light_msg_color,light_label_color
    global bg_color,msg_color,label_color,line_color,border_color,y_offset,bdr_width,font_label_size
    global font_msg_size,debug_toggle

    if debug_toggle == 1:
        print('use_screen_mode',use_screen_mode)
        
    if use_screen_mode == 1:
        use_screen_mode = 0
        button6_text = "Light/Dark\nMode Off"
    else:
        use_screen_mode = 1
        button6_text = "Light/Dark\nMode On"
        
    invisible_button6.config(text=button6_text)
    update_display_settings()


def check_time_and_toggle(): # Change the light/dark mode if use_screen_mode is set
    
    # if light_dark_mode = 1 then light, otherwise dark
    global hour_12,light_dark_mode,use_screen_mode,light_mode_on,dark_mode_on,dark_bg_color
    global dark_msg_color,dark_label_color,light_bg_color,light_msg_color,light_label_color
    global bg_color,msg_color,label_color,line_color,border_color,y_offset,bdr_width,font_label_size
    global font_msg_size,debug_toggle
    
    button6_text = "Light/Dark\nMode On" # newlines create a larger button

    current_time = [time.strftime("%H%M"),time.strftime("%-H%M"),time.strftime("%I%M"),time.strftime("%-I%M")]
    if debug_toggle == 1: print("time list=",current_time)
    if debug_toggle == 1: print("Light=",light_mode_on,"Dark=",dark_mode_on)
    
    if light_mode_on in current_time:
        light_dark_mode = 1
        bg_color = light_bg_color
        msg_color = light_msg_color
        label_color = light_label_color
    
    if dark_mode_on in current_time:
        light_dark_mode = 0
        bg_color = dark_bg_color
        msg_color = dark_msg_color
        label_color = dark_label_color
        
    if light_dark_mode == 0:
        button5_text = "Dark\nMode" # newlines create a larger button
    else:
        button5_text = "Light\nMode"

    invisible_button5.config(text=button5_text)
    update_display_settings()


def screen_mode():
    global hour_12,light_dark_mode,use_screen_mode,light_mode_on,dark_mode_on,dark_bg_color
    global dark_msg_color,dark_label_color,light_bg_color,light_msg_color,light_label_color
    global bg_color,msg_color,label_color,line_color,border_color,y_offset,bdr_width,font_label_size
    global font_msg_size,debug_toggle

    if light_dark_mode == 1:
        light_dark_mode = 0
        bg_color = dark_bg_color
        msg_color = dark_msg_color
        label_color = dark_label_color

    else:
        light_dark_mode = 1
        bg_color = light_bg_color
        msg_color = light_msg_color
        label_color = light_label_color
        
    if light_dark_mode == 0:
        button5_text = "Dark\nMode" # newlines create a larger button
    else:
        button5_text = "Light\nMode"

    if debug_toggle == 1: print("light_dark_mode =",light_dark_mode)
    invisible_button5.config(text=button5_text) #
    update_display_settings()


def get_verse(version_code="en-asv", book = "genesis", chapter = "1", verse_num = "1"):
    """Returns the text of a verse given book, chapter and verse number."""
    if debug_toggle == 1: print("https://cdn.jsdelivr.net/gh/wldeh/bible-api/bibles/"+version_code+"/books/"+book+"/chapters/"+chapter+"/verses/"+verse_num+".json") # debug
    response = requests.get("https://cdn.jsdelivr.net/gh/wldeh/bible-api/bibles/"+version_code+"/books/"+book+"/chapters/"+chapter+"/verses/"+verse_num+".json")
    data = response.json()
    return(data["text"])


def get_time():
    """Returns the current time, current hour and current minutes"""
    global hour_12
    if hour_12 == 1:
        current_time = strftime('%-I:%M %p') # 12 hour format
        current_hour = strftime('%-I')
        current_minutes = strftime('%M')
    else:
        current_time = strftime('%-H:%M %p') # 24 hour format
        current_hour = strftime('%-H')
        current_minutes = strftime('%M')

    return(current_time, current_hour, current_minutes)


def get_verses(book, chapter):
    """Returns the number of verses for a given book and chapter."""
    # Search for the book
    for book_data in bible_structure:
        if book_data["book"].lower() == book.lower() or book_data["abbr"].lower() == book.lower():
            # Search for the chapter
            for chapter_data in book_data["chapters"]:
                if chapter_data["chapter"] == str(chapter):
                    return int(chapter_data["verses"]) # Return the number of verses in chapter


def get_random_bible_book():
    """Returns a random book name from bible_structure."""
    book_data = random.choice(bible_structure)
    return book_data["book"]
    

def draw_line(y = 10):
    global bg_color
    """Create and draw horizontal separation line."""
    # Get the screen width
    screen_width = root.winfo_screenwidth()

    # Calculate the width for the line and canvas (2/3 of screen width)
    line_canvas_width = int(screen_width * (2 / 3))

    # Create the canvas
    # The height is set to a small value as it only needs to contain a horizontal line
    canvas_height = 6
    canvas = tk.Canvas(root, width=line_canvas_width, height=canvas_height, bg=bg_color, highlightthickness=0)
    canvas.pack()

    # Draw the horizontal line in the center of the canvas
    # The line starts at (0, y_center) and ends at (canvas_width, y_center)
    canvas.create_line(0, y, line_canvas_width, y, fill=line_color, width=4)


# Function to search dictionary by key and return value list
def get_bible_version_info(version_key):
    return version_key, bible_versions.get(version_key, ["Version not found", None, None])


# Function to return a random key and value list from the dictionary
def get_random_bible_version():
    key = random.choice(list(bible_versions.keys()))
    version_name, version_font, version_code = bible_versions[key]
    return key, version_name, version_font, version_code


def toggle_hours():
    global hour_12, bg_color
    if hour_12 == 1:
        hour_12 = 0
    else:
        hour_12 = 1
    
    if hour_12 == 1:
        button1_text = "12\nHour" # newlines create a larger button
    else:
        button1_text = "24\nHour"

    invisible_button1.config(text=button1_text) #,bg=bg_color
    update_display_settings()


def quit_clock():
    global bg_color
    print("Quitting Bible Clock to Desktop...")
    update_display_settings()
    sys.exit()
    
    
def shutdown_pi():
    global bg_color
    print("Initiating Raspberry Pi shutdown...")
    update_display_settings()
    os.system("sudo shutdown -h now")


def reboot_pi():
    global bg_color
    print("System reboot initiated.")
    update_display_settings()
    subprocess.run(["sudo", "reboot", "-n", "-f"], check=True)


def update_display_settings(): # Function to update variables and write to config.py
    global hour_12,light_dark_mode,use_screen_mode,light_mode_on,dark_mode_on,dark_bg_color
    global dark_msg_color,dark_label_color,light_bg_color,light_msg_color,light_label_color
    global bg_color,msg_color,label_color,line_color,border_color,y_offset,bdr_width,font_label_size
    global font_msg_size,debug_toggle
    
    # Write updated values to config.py
    with open("config.py", "w") as f:
        f.write(f'# Feel Free to change the first 11 parameters\n')
        f.write(f'hour_12 = {hour_12}    # 1 for 12 hour, 0 for 24 hour\n')
        f.write(f'light_dark_mode = {light_dark_mode}    # 1 = Light mode, 0 = Dark mode\n')
        f.write(f'use_screen_mode = {use_screen_mode}    # 1 = Turn on light/dark mode switching\n')
        f.write(f'light_mode_on = "{light_mode_on}"    # 4 digit 12 or 24 hour time in quotes, no :\n')
        f.write(f'dark_mode_on = "{dark_mode_on}"    # 4 digit 12 or 24 hour time in quotes, no :\n')
        f.write(f'\n')
        f.write(f'# specify colors for light and dark mode.\n') 
        f.write(f'dark_bg_color = "{dark_bg_color}"    # Specify color by name or Hex Code\n')
        f.write(f'dark_msg_color = "{dark_msg_color}"    # Specify color by name or Hex Code\n')
        f.write(f'dark_label_color = "{dark_label_color}"    # Specify color by name or Hex Code\n')
        f.write(f'light_bg_color = "{light_bg_color}"    # Specify color by name or Hex Code\n')
        f.write(f'light_msg_color = "{light_msg_color}"    # Specify color by name or Hex Code\n')
        f.write(f'light_label_color = "{light_label_color}"    # Specify color by name or Hex Code\n')
        f.write(f'\n')
        f.write(f'# No need to change below this line unless you want to experiment\n')
        f.write(f'bg_color = "{bg_color}"\n')
        f.write(f'msg_color = "{msg_color}"\n')
        f.write(f'label_color = "{label_color}"\n')
        f.write(f'line_color = "{line_color}"\n')
        f.write(f'border_color = "{border_color}"\n')
        f.write(f'y_offset = {y_offset}\n')
        f.write(f'bdr_width = {bdr_width}\n')
        f.write(f'font_label_size = {font_label_size}\n')
        f.write(f'font_msg_size = {font_msg_size}\n')
        f.write(f'debug_toggle = {debug_toggle}\n')

    
    return {
        "hour_12": hour_12,
        "light_dark_mode": light_dark_mode,
        "use_screen_mode": use_screen_mode,
        "light_mode_on": light_mode_on,
        "dark_mode_on": dark_mode_on,
        "dark_bg_color": dark_bg_color,
        "dark_msg_color": dark_msg_color,
        "dark_label_color": dark_label_color,
        "light_bg_color": light_bg_color,
        "light_msg_color": light_msg_color,
        "light_label_color": light_label_color,
        "bg_color": bg_color,
        "msg_color": msg_color,
        "label_color": label_color,
        "line_color": line_color,
        "border_color": border_color,
        "y_offset": y_offset,
        "bdr_width": bdr_width,
        "font_label_size": font_label_size,
        "font_msg_size": font_msg_size,
        "debug_toggle": debug_toggle
    }


def check_label_len(book):
    global font_label_size
    if debug_toggle: print("length=",len(book))
    if len(book) >= 15:
        temp_font_size = font_label_size - 30
    else:
        temp_font_size = font_label_size
    if debug_toggle: print("font size=",temp_font_size)
    return temp_font_size


def check_verse_len(verse_text):
    global font_msg_size
    if len(verse_text) >= 200:
        temp_font_size = font_msg_size - 10
    elif len(verse_text) >= 265:
        temp_font_size = font_msg_size - 20
    elif len(verse_text) >= 350:
        temp_font_size = font_msg_size - 30
    elif len(verse_text) >= 350:
        temp_font_size = font_msg_size - 40
        
    elif len(verse_text) <= 200:
        temp_font_size = font_msg_size + 0
    elif len(verse_text) <= 100:
        temp_font_size = font_msg_size + 10        
    elif len(verse_text) <= 50:
        temp_font_size = font_msg_size + 15        

    else:
        temp_font_size = font_msg_size
    return temp_font_size

 
def create_wipe(root, canvas):
    """
    Creates and starts a screen wipe animation.
    """
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    # Create the wiping rectangle just off the left edge of the canvas
    # The `wipe_rect` variable is assigned the ID of the created canvas item.
    wipe_rect = canvas.create_rectangle(
        -canvas_width, 0, 0, canvas_height, fill="black", outline="black"
    )

    # Start the animation loop
    animate_wipe(root, canvas, wipe_rect, canvas_width)


def animate_wipe(root, canvas, item_id, target_x):
    """
    Recursively moves the wipe rectangle across the canvas.
    """
    # Get the current position of the item
    coords = canvas.coords(item_id)
    current_x = coords[0]

    # If the wipe is not finished, move it and schedule the next step
    if current_x < target_x:
        canvas.move(item_id, 10, 0)  # Move 10 pixels to the right
        root.after(10, animate_wipe, root, canvas, item_id, target_x)
    else:
        # After the wipe is complete, clean up the rectangle.
        # Here you could load new screen elements.
        canvas.delete(item_id)
        print("Wipe complete. Ready to show new content.")
        
        
def update_time():
#    create_wipe(root, canvas_wipe)
    
    """Updates the clock label with the current time."""
    global hour_12,light_dark_mode,use_screen_mode,light_mode_on,dark_mode_on,dark_bg_color
    global dark_msg_color,dark_label_color,light_bg_color,light_msg_color,light_label_color
    global bg_color,msg_color,label_color,line_color,border_color,y_offset,bdr_width,font_label_size
    global font_msg_size,debug_toggle

    if use_screen_mode == 1:
        check_time_and_toggle() # Check the time to see if screen mode should change
    
    root.config(bg=bg_color)
    invisible_button1.config(bg=bg_color,fg=bg_color,activebackground=bg_color)
    invisible_button2.config(bg=bg_color,fg=bg_color,activebackground=bg_color)
    invisible_button3.config(bg=bg_color,fg=bg_color,activebackground=bg_color)
    invisible_button4.config(bg=bg_color,fg=bg_color,activebackground=bg_color)
    invisible_button5.config(bg=bg_color,fg=bg_color,activebackground=bg_color)
    invisible_button6.config(bg=bg_color,fg=bg_color,activebackground=bg_color)
    
    current_time, current_hour, current_minutes = get_time() # get time
    chapter = int(current_hour)
    if current_minutes == "00": current_minutes = "-1" # force display time at top of hour    
    current_minutes = current_minutes.lstrip('0') # fix for api call requirements
    
    # Pick random Version to display along with font to use
    version_key, version_name, version_font, version_code = get_random_bible_version()
    if debug_toggle: print(version_key, version_name, version_font, version_code) # debug

    # Pick random book to display. Check to see if the book has verse to display. If not try again.
    for j in range(len(bible_structure)): 
        book = get_random_bible_book().lower() # get a random book name
        book_label = book.capitalize()
        book = book.replace(" ", "") # fix for api call requirements

        verses = get_verses(book, chapter) # Get the number of verses in the book, chapter
        if verses == None: # if None, get another random book name
            continue
        if int(current_minutes) > int(verses): # If there aren't enough verses in chapter repeat
            continue
        break

    try: # Get verse from API, with error catching. If error occurs, just display the time.
        verse_text = get_verse(version_code, book, current_hour, current_minutes) # Get verse from API
        
        if verse_text != "":
            book = book.title() # Fix book name for display purposes
            print(f"\033[1m\033[91m{book} {current_hour}:{current_minutes}\033[0m - {verse_text}\n")
        else:
            print("\033[1m\033[91m"+current_time+"\033[0m"+"\n") # if there isn't a usable book, chapter, verse, then display time only
            verse_text = ":::"

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        error_info = exc_type, fname, exc_tb.tb_lineno
        print("\033[1m\033[91m"+current_time+str(error_info)+"\033[0m"+"\n") # if there isn't a usable book, chapter, verse, then display time only

        if debug_toggle == 1:
            verse_text = "Exception: "+str(e)+", "+str(exc_type)+", "+str(fname)+", "+str(exc_tb.tb_lineno)
        else: # If error occurred, display the current time alone.
            verse_text = ""
        
        clock_label.config(
            text=current_time,
            fg=label_color,bg=bg_color,
            font=(version_font,
            font_label_size+10)
            )
        
        msg.config(
            text = verse_text,
            aspect=200,fg=msg_color,bg=bg_color,
            font=(version_font,check_verse_len(verse_text),"italic")
            )
    
    clock_label.after(1000*60, update_time) # Schedule update_time to run again after 1000ms (60 second)
    if verse_text == "":
        return
    
    verse_text = '"'+verse_text+'"'
    if debug_toggle == 1:
        leng_of_verse = " - "+ str(len(verse_text)) # used only in debug mode
    else:
        leng_of_verse = ""
        
    clock_label.config(
        text=book_label+" "+current_hour+":"+current_minutes,
        fg=label_color,bg=bg_color,
        font=(version_font,check_label_len(book_label+" "+current_hour+":"+current_minutes))
        )
    
    msg.config(
        text = verse_text+"\n"+version_name +leng_of_verse,
        aspect=200,fg=msg_color,bg=bg_color,
        font=(version_font,check_verse_len(verse_text+"\n"+version_name +leng_of_verse),"italic")
        )
    

# Main Execution 
if __name__ == "__main__":    
    # Create the main window using tkinter
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.title("Bible Clock")
    root.configure(bg=bg_color, cursor="none", borderwidth=bdr_width, relief="groove") # arrow

    # Create Widgets
    # Create a Label widget to display the Book and time 
    clock_label = tk.Label(
        root,
        font=("Z003", font_label_size, 'bold'),
        background=bg_color,
        foreground=msg_color
    )
    clock_label.pack(anchor='center', expand=True)  # Center the label in the window
    
    # Create a Canvas widget for line
    canvas = tk.Canvas(root, bg=bg_color)
    root.update_idletasks() # Update the window to get accurate dimensions
    draw_line(y_offset) # pass the Y coordinate
    
#    canvas_wipe = tk.Canvas(root, width=500, height=400, bg="darkgrey")
#    canvas_wipe.pack(pady=10)

     
    # Create a Message widget to display the Verse Text
    msg = Message(root,
        background=bg_color,
        foreground=msg_color,
        font=("Z003", font_msg_size)
    )
    msg.pack(anchor='center', expand=True)
    
    # Create hidden buttons
    # 12/24 hour button hidden in upper right corner
    if hour_12 == 1:
        button1_text = "12\nHour"  # use newlines to make the button bigger for fingers
    else:
        button1_text = "24\nHour"  # use newlines to make the button bigger for fingers
    invisible_button1 = tk.Button(root, text=button1_text, command=lambda: toggle_hours(),
                                 bg=bg_color, fg=bg_color, borderwidth=0, 
                                 activebackground=bg_color, activeforeground="dark gray", highlightthickness=0)
    invisible_button1.pack() # , side=tk.TOP, anchor=tk.SE pady=20
    # Place the button in the upper-right corner
    invisible_button1.place(relx=1.0, y=0, anchor="ne") 

    # quit program to desktop button hidden in upper left corner
    button2_text = "Quit\nClock" # use newlines to make the button bigger for fingers
    invisible_button2 = tk.Button(root, text=button2_text, command=lambda: quit_clock(),
                                 bg=bg_color, fg=bg_color, borderwidth=0, 
                                 activebackground=bg_color, activeforeground="dark gray", highlightthickness=0)
    invisible_button2.pack() # , side=tk.TOP, anchor=tk.SE pady=20
    # Place the button in the upper-right corner
    invisible_button2.place(relx=0, y=0) 


    # quit program to desktop button hidden in upper left corner
    button3_text = "Shut\ndown" # use newlines to make the button bigger for fingers
    invisible_button3 = tk.Button(root, text=button3_text, command=lambda: shutdown_pi(),
                                 bg=bg_color, fg=bg_color, borderwidth=0,
                                 activebackground=bg_color, activeforeground="dark gray", highlightthickness=0)
    invisible_button3.pack() # , side=tk.TOP, anchor=tk.SE pady=20
    # Place the button in the upper-right corner
    invisible_button3.place(relx=0.0, rely=1.0, anchor='sw') 


    # quit program to desktop button hidden in upper left corner
    button4_text = "Reboot\nRPi" # use newlines to make the button bigger for fingers
    invisible_button4 = tk.Button(root, text=button4_text, command=lambda: reboot_pi(),
                                 bg=bg_color, fg=bg_color, borderwidth=0, 
                                 activebackground=bg_color, activeforeground="dark gray", highlightthickness=0)
    invisible_button4.pack() # , side=tk.TOP, anchor=tk.SE pady=20
    # Place the button in the upper-right corner
    invisible_button4.place(relx=1.0, rely=1.0, anchor='se') 


    # light or dark screen mode button
    if light_dark_mode == 1:
        button5_text = "Light\nMode"  # use newlines to make the button bigger for fingers
    else:
        button5_text = "Dark\nMode"  # use newlines to make the button bigger for fingers
    invisible_button5 = tk.Button(root, text=button5_text, command=lambda: screen_mode(),
                                 bg=bg_color, fg=bg_color, borderwidth=0, 
                                 activebackground=bg_color, activeforeground="dark gray", highlightthickness=0)
    invisible_button5.pack() # , side=tk.TOP, anchor=tk.SE pady=20
    # Place the button in the upper-right corner
    invisible_button5.place(relx=1.0, y=40, anchor="ne") 

    # Light/Dark Mode based on time of day
    if use_screen_mode == 1:
        button6_text = "Light/Dark\nMode On"  # use newlines to make the button bigger for fingers
    else:
        button6_text = "Light/Dark\nMode Off"  # use newlines to make the button bigger for fingers
    invisible_button6 = tk.Button(root, text=button6_text, command=lambda: toggle_time_mode(),
                                 bg=bg_color, fg=bg_color, borderwidth=0, 
                                 activebackground=bg_color, activeforeground="dark gray", highlightthickness=0)
    invisible_button6.pack() # , side=tk.TOP, anchor=tk.SE pady=20
    # Place the button in the upper-right corner
    invisible_button6.place(relx=1.0, y=85, anchor="ne") 


    # Initial call to update the time and verse 
    update_time()

    # Start the Tkinter event loop
    root.mainloop()

