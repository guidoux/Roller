from tkinter import *
root = Tk()

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))

root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())
root.mainloop()