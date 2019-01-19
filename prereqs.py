import subprocess as sb

def importModule(s):
    x = sb.call(["pip","install",s])
    if x > 0:
        print(f'ERROR: SOMETHING WENT WRONG\nEXIT CODE: {x}\nMODULE: {s}')

try:
    import keyboard
except ModuleNotFoundError:
    importModule("keyboard")
try:
    import win10toast
except ModuleNotFoundError:
    importModule("win10toast")
try:
    import pyperclip
except ModuleNotFoundError:
    importModule("pyperclip")
