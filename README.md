# HIMP: H\*\*l\*\* Image Manipulation Program
The name is just a clickbait.
A script that enables minimal screenshot utility annotation function.
Since most screenshot programs with annotate functionality are bloated, I wrote this script to do the same thing for me. 
As those bloatware are usually a few dozens of megabytes, one can assume a mere few kilobytes script is worthy of being called minimal.

*While the drawing are easy as hell with OpenCV library, what's really tricky are **preview while drawing**, **eraser** and **undo**.*

## Demo 

![record](record.gif)

At the very beginning when selecting screenshot region, the cursor wasn't recorded for some reason.
The flickerings are only observed in recording.

---

## Dependencies
-   Python3
-   OpenCV
-   a minimal screenshot utility (in my case, imagemagick)
-   a clipboard utility (only needed for copy function, in my case, xclip)
-   a hotkey daemon (in my case, i3)

Those above had been already installed before i had the idea, so i never sacrifice anything, just calling existing system resources.

---

## Installation

1. change the locations of the temporary files in the script accordingly to the directory where you store this script.
2. change the screenshot utility and clipboard usage in the script accordingly if you are using different ones.
3. make the scripts executable.
```
chmod +x main.py copy.sh
```
4. bind the script to your hotkey daemon,
in my case, in ~/.config/i3/config:
```
bindsym Mod1+Shift+2 exec ~/Scripts/python/cv/screenshot/main.py
```

---

## Usage:

after executing the script, select the region of which you wish to screenshot using cursor, a window with the screenshot should pop up.

#### Mode:
    - a                                              arrow
    - b                                              blur
    - c                                              circle   
    - e                                              eraser
    - l                                              line
    - r                                              rectangle

#### Operation:
    - f                                              Toggle filling/hollow mode 
    - q                                              Quit
    - s                                              save modified image to the preset location and quit
    - y                                              yank (copy modified image to clipboard)
    - z                                              undo 

Use the trackbar to modify color and width.
