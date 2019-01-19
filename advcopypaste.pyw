import keyboard as kb # the magic sauce; handles keyboard presses and hotkeys
import pyperclip as clip # cross platform, but could use win32clipboard for a windows-only solution
from time import sleep # i sleep
from win10toast import ToastNotifier as toast # this handles the windows10 notifications
from platform import platform

superKey = "windows" # can be changed to whatever the user wants
currentBuffer = [] # this is just a holder for the data that will be saved in the other buffers
activeBuffer = 1 # moving index for the bufferList
buff0=[] # A buffer for every number
buff1=[] # I mean technically you could have one for each character too
buff2=[] # but that's just a lot
buff3=[] # actually wait how many would that be
buff4=[] # I think realistically you could get like 46
buff5=[] # But like there is no reason to actually do that
buff6=[] # Seriously you need more than 10??
buff7=[] # Also I know this code sucks with all the same line being repeated with a slightly different variable name
buff8=[] # but I had an issue where doing buf0=buf1=buf2...=[] lead to the buffers all being linked to each other
buff9=[] # so that was weird
bufferList = [buff0,buff1,buff2,buff3,buff4,buff5,buff6,buff7,buff8,buff9] # this is just a list of every buffer; allows for easy switching
ENTER = "enter" # change this to something else if you don't want the program to press enter after it types something
# ENTER = "f"

# notification settings
NOTIFICATION_LEVEL = 1 if platform().find("Windows") == 0 else 0 # 0 = no, 1 = some, 2 = some but it's also shows what you just put in the buffer
notify = toast() # this object handles the actual notification process
TOAST_TITLE_STR = "AdvCopyPaste.pyw" # ensure a consistent title with no typos

def copyStringBuffer(cutTxt): # copies the string in the clipboard to the current buffer
    global currentBuffer # python has really weird variable scope sometimes
    currentBuffer.append(clip.paste())
    if cutTxt: # if you still have the text highlighted and want it gone
        kb.press("delete")
    if NOTIFICATION_LEVEL == 2: # if we want to be obnoxious
        msg(f"Appended \"{clip.paste()}\" to buffer {activeBuffer}")

def typeStringBuffer(toCut): # type the actual strings in the buffer
    kb.press(ENTER) # this kind of helps with programs that don't handle this script well, but only sometimes
    sleep(.15) 
    for string in currentBuffer:
        kb.write(string)
        sleep(.15)
        kb.press(ENTER)
        sleep(.25)
    if toCut: # if we wanna erase the text when we are done
        clearCurrentBuffer()

def clearCurrentBuffer(): # well the function name kinda says it all, huh?
    global currentBuffer, bufferList, activeBuffer # sometimes python makes you import variables I litERALLY ALREADY DEFINED
    currentBuffer = []
    bufferList[activeBuffer] = currentBuffer # set the buffer in the buffer list to an empty list as well
    msg(f"Buffer {activeBuffer} cleared")

def clearAllBuffers(): # again, let's hear it for descriptive function names
    global currentBuffer, bufferList, activeBuffer # it really is the most irritating thing ever like wtf
    currentBuffer = []
    for i in range(len(bufferList)):
        bufferList[i] = [] # get rid of all the things
    msg("All buffers cleared")

def changeCurrentBuffer(n): # man, I should give a Ted talk on how little comment bloat this naming style creates
    global currentBuffer, bufferList, activeBuffer # i hate programming
    bufferList[activeBuffer] = currentBuffer # ensure the buffer in the list is persistent
    activeBuffer = n
    currentBuffer = bufferList[activeBuffer] # pull the old contents from memory
    msg(f"Switching to buffer {n}") # so this might not always show up immediately if you switch quickly, but the switching works

def msg(s): # this method handles the notifications even more than it already has been abstracted
    if NOTIFICATION_LEVEL > 0:
        try:
            notify.show_toast(TOAST_TITLE_STR,s)
        except Exception: # so in theory if the user tries to run this on Linux it should come through here
            return False # this is of course untested. what is QC?

def init(): # prepare for r/programminghorror
    kb.add_hotkey(f"{superKey}+ctrl+c",copyStringBuffer, args=[False])
    kb.add_hotkey(f"{superKey}+ctrl+v",typeStringBuffer, args=[False])
    kb.add_hotkey(f"{superKey}+ctrl+x",copyStringBuffer, args=[True])
    kb.add_hotkey(f"{superKey}+ctrl+shift+x",typeStringBuffer, args=[True])
    kb.add_hotkey(f"{superKey}+ctrl+space",clearCurrentBuffer,args=None)
    kb.add_hotkey(f"{superKey}+ctrl+shift+space",clearAllBuffers,args=None)
    kb.add_hotkey(f"{superKey}+ctrl+0",changeCurrentBuffer, args=[0])
    kb.add_hotkey(f"{superKey}+ctrl+1",changeCurrentBuffer, args=[1])
    kb.add_hotkey(f"{superKey}+ctrl+2",changeCurrentBuffer, args=[2])
    kb.add_hotkey(f"{superKey}+ctrl+3",changeCurrentBuffer, args=[3])
    kb.add_hotkey(f"{superKey}+ctrl+4",changeCurrentBuffer, args=[4])
    kb.add_hotkey(f"{superKey}+ctrl+5",changeCurrentBuffer, args=[5])
    kb.add_hotkey(f"{superKey}+ctrl+6",changeCurrentBuffer, args=[6])
    kb.add_hotkey(f"{superKey}+ctrl+7",changeCurrentBuffer, args=[7])
    kb.add_hotkey(f"{superKey}+ctrl+8",changeCurrentBuffer, args=[8])
    kb.add_hotkey(f"{superKey}+ctrl+9",changeCurrentBuffer, args=[9])
    kb.wait(f"{superKey}+ctrl+esc") # here we listen to this keypress and then exit the program
    msg("Shutting down script...") # one final peace out fam

if __name__ == '__main__': # if you just run the script by itself instead of importing it into another script
    init() # run the init method