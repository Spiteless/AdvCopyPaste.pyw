import win32clipboard

def set(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text)
    win32clipboard.CloseClipboard()

def get():
    win32clipboard.OpenClipboard()
    try:
        data = win32clipboard.GetClipboardData()
    except TypeError:
        print(f"Unsupported data format, returning {type(None)}")
        data = None
    win32clipboard.CloseClipboard()
    return data

def clear():
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.CloseClipboard()
