# AdvCopyPaste.pyw

A better copy-paste mechanism using the keyboard Python module

Read the list of prerequisites, but I also have a prereqs.py that does a rough check and install of all 3rd party modules

# Prerequisites:
  * [Keyboard](https://github.com/boppreh/keyboard)
  * Win10Toast (more of a nice to have really, but I have no idea if not having this will break the script or not)
  * Pyperclip
  
Here is how to actually use the script:

  * SUPERKEY by default is the windows key
  * SUPERKEY+Ctrl+C copies the text in the clipboard to the currently active buffer (so you must copy the text first)
  * SUPERKEY+Ctrl+V to have Python type all strings in the current buffer
    * SUPERKEY+Ctrl+Shift+V will have Python type the strings then clear the buffer
  * SUPERKEY+Ctrl+X will copy the text stored in the clipboard then press the delete key to simulate cutting
  * SUPERKEY+Ctrl+Space-bar will clear the current buffer
    * SUPERKEY+Ctrl+Shift+Space-bar will clear all buffers
  * SUPERKEY+Ctrl+N will select a new buffer (where N is a number on the number row)
  * SUPERKEY+Ctrl+Esc will stop the script
  
You'll also notice some notifications when certain actions are performed. To disable this, simply change the NOTIFICATION_LEVEL variable to 0

# WARNINGS:
  * These scripts only work with Python 3.6 or later
  * As previously mentioned, you have to copy text to the clipboard before adding it to the buffer
  * The script will press the enter key between each string in the buffer
  * Certain programs cannot seem to keep up with the typing speed; it misses key presses and gets messed up. Cmd.exe is one of them
  * This script SHOULD be cross platform, but is untested
  * Copying a string that is too long will result in it being garbled (don't copy the Bee movie script)
