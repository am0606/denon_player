import sys
import telnetlib
from m3uparser import parsem3u
from tkinter import *
from myconfig import *

# classes

class ScrollableFrame:
    """A scrollable tkinter frame that will fill the whole window"""

    def __init__ (self, master, width, height, mousescroll=0):
        self.mousescroll = mousescroll
        self.master = master
        self.height = height
        self.width = width
        self.main_frame = Frame(self.master)
        self.main_frame.pack(fill=BOTH, expand=1)

        self.scrollbar = Scrollbar(self.main_frame, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas = Canvas(self.main_frame, yscrollcommand=self.scrollbar.set)
        self.canvas.pack(expand=True, fill=BOTH)

        self.scrollbar.config(command=self.canvas.yview)

        self.canvas.bind(
            '<Configure>',
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.frame = Frame(self.canvas, width=self.width, height=self.height)
        self.frame.pack(expand=True, fill=BOTH)
        self.canvas.create_window((0,0), window=self.frame, anchor="nw")

        self.frame.bind("<Enter>", self.entered)
        self.frame.bind("<Leave>", self.left)

    def _on_mouse_wheel(self,event):
        self.canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

    def entered(self,event):
        if self.mousescroll:
            self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)
        
    def left(self,event):
        if self.mousescroll:
            self.canvas.unbind_all("<MouseWheel>")

# functions

def telnet_send(myconf, xurl):
    tn = telnetlib.Telnet(myconf.ipx, myconf.portx)
    tn.write(str.encode(myconf.heos_prefix + xurl + '\n'))
    output = tn.read_until(b"FIN\n", timeout = 1).decode('ascii')
    print(output)

def play(myconf,value):
    for r in radios:
        if r["name"]==value:
            xurl = r["url"]
            break
    telnet_send(myconf,xurl)

def update_size(myconf):
    max_height = 0
    padding = 12

    for widget in widgets:
        widget_height = widget.winfo_reqheight()
        max_height += widget_height + padding

    max_height += padding

    root.geometry(f"{myconf.mygeometry_w}x{max_height}")

def test():
    print("test")

# main sequence
myconf = myconfig()
myconf.vimport('radio.ini')

if len(sys.argv) == 2:
    radios = parsem3u(sys.argv[1])
else:
    radios = parsem3u('radio.m3u')

widgets = []

root = Tk()
root.title(myconf.wtitle)
root.geometry(f"{myconf.mygeometry_w}x{myconf.mygeometry_h}")
sf = ScrollableFrame(
    root,
    height=300, # Total required height of canvas
    width=400 # Total width of master
)
frame = sf.frame

position = {"padx":6, "pady":6, "anchor":NW}
 
radio = StringVar(value=radios[0]["name"])
  
for r in radios:
    btn = Radiobutton(frame, value=r["name"], text=r["name"], variable=radio, compound="top")
    btn.pack(**position)
    widgets.append(btn)
 
btn = Button(frame,text="Play",command=lambda: play(myconf,radio.get()))
btn.pack()
widgets.append(btn)

update_size(myconf)

root.mainloop()
