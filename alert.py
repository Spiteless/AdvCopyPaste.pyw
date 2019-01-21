import click
from pymsgbox import alert as box
from win10toast import ToastNotifier as toast

notify = toast()

def msg(s): # this method handles the notifications even more than it already has been abstracted
    TOAST_TITLE_STR = "AdvCopyPaste"
    # if NOTIFICATION_LEVEL > 0:
    try:
        notify.show_toast(TOAST_TITLE_STR,s)
    except Exception: # so in theory if the user tries to run this on Linux it should come through here
            return False # this is of course untested. what is QC?

@click.command()
@click.option("--popup", default=None, help="An alert via pymsgbox.alert")
@click.option("--alert", default=None, help="An alert via win10toast.ToastNotifier")
# @click.option("--NOTIFICATION_LEVEL", default=0, help="Boiler plate")
def alert(
    popup,
    alert,
    # NOTIFICATION_LEVEL,
    ):
    if popup:
        box(popup)
    if alert:
        msg(alert)


if __name__ == '__main__':
    alert()
