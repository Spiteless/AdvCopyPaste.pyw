import keyboard as kb # the magic sauce; handles keyboard presses and hotkeys
# import pyperclip as clip # cross platform, but could use win32clipboard for a windows-only solution
from time import sleep # i sleep
from win10toast import ToastNotifier as toast # this handles the windows10 notifications
from platform import platform

import clip # switching in personal clip library
clip.paste = clip.get #in my version I use clip.get() and clip.set()

import subprocess # script was failing during message calls so I foisted
                  # those calls onto a separate process


superKey = "windows" # can be changed to whatever the user wants

buffer = dict()
for i in range(10):
    buffer[i] = ""

buffer['active'] = 0

ENTER = "enter" # change this to something else if you don't want the program to press enter after it types something
NEWLINE = "\r\n"

# notification settings
NOTIFICATION_LEVEL = 1 if platform().find("Windows") == 0 else 0 # 0 = no, 1 = some, 2 = some but it's also shows what you just put in the buffer
notify = toast() # this object handles the actual notification process
TOAST_TITLE_STR = "AdvCopyPaste.pyw" # ensure a consistent title with no typos

hotkeys = []
# (func, keys, suppress, args)

def copyStringBuffer(): # copies the string in the clipboard to the current buffer
    kb.send('ctrl+c')
    buffer[buffer['active']] += clip.paste() + NEWLINE

    if NOTIFICATION_LEVEL == 2: # if we want to be obnoxious
        msg(f"Appended \"{clip.paste()}\" to buffer {buffer['active']}")
hotkeys.append((copyStringBuffer, f"{superKey}+ctrl+c", True, None))

def cutStringBuffer(): # copies the string in the clipboard to the current buffer
    kb.send('ctrl+x')
    buffer[buffer['active']] += clip.paste() + NEWLINE
    if NOTIFICATION_LEVEL == 2: # if we want to be obnoxious
        msg(f"Appended \"{clip.paste()}\" to buffer {buffer['active']}")
hotkeys.append((cutStringBuffer, f"{superKey}+ctrl+x", True, None))

def typeStringBuffer(toCut): # type the actual strings in the buffer
    outstr = buffer[buffer['active']]
    clip.set(outstr)
    kb.send('ctrl+v')

    if toCut: # if we wanna erase the text when we are done
        clearCurrentBuffer()
hotkeys.append((typeStringBuffer, f"{superKey}+ctrl+v", True, [False]))
hotkeys.append((typeStringBuffer, f"{superKey}+ctrl+shift+v", True, [True]))

def clearCurrentBuffer(): # well the function name kinda says it all, huh?
    buffer['active'] = ""
    msg(f"Buffer {buffer['active']} cleared")
hotkeys.append((clearCurrentBuffer, f"{superKey}+ctrl+space", True, None))

def clearAllBuffers(): # again, let's hear it for descriptive function names
    for i in range(10):
        buffer[i] = ""
    msg("All buffers cleared")
hotkeys.append((clearAllBuffers, f"{superKey}+ctrl+shift+space", True, None))

def changeCurrentBuffer(n): # man, I should give a Ted talk on how little comment bloat this naming style creates
    buffer['active'] = n
    msg(f"Switching to buffer {n}") # so this might not always show up immediately if you switch quickly, but the switching works
hotkeys += [(changeCurrentBuffer, f"{superKey}+ctrl+{i}", True, [{i}]) for i in range(10)]

def previewAllBuffers():
    outstr = f'Current Buffer: {buffer["active"]}\n\n'

    for num in range(10):
        temp = buffer[num]
        temp.replace(NEWLINE, "\\")
        if temp == None:
            temp = "( None )"

        outstr+=f'{num}: {temp[:30]}\n'

    msg(outstr, "popup")
hotkeys.append((previewAllBuffers, f"{superKey}+ctrl+slash", True, None))


def msg(s, alert_type="alert"): # this method handles the notifications even more than it already has been abstracted
    if NOTIFICATION_LEVEL > 0:
        try:
            subprocess.Popen(['py', 'alert.py', f'--{alert_type}="{s}"'])
            # notify.show_toast(TOAST_TITLE_STR,s)
        except: # so in theory if the user tries to run this on Linux it should come through here
            # return False # this is of course untested. what is QC?
            print("Boop")



def init(): # prepare for r/programminghorror
    for hotkey in hotkeys:
        func, keys, suppress, args = hotkey
        kb.add_hotkey(keys,func,suppress=suppress,args=args)

    kb.wait(f"{superKey}+ctrl+esc") # here we listen to this keypress and then exit the program

    msg("Shutting down script...") # one final peace out fam

if __name__ == '__main__': # if you just run the script by itself instead of importing it into another script
    init() # run the init method
