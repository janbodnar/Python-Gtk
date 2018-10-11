#!/usr/bin/env python3

import gi, math
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.init_ui()

    def init_ui(self):    

        darea = Gtk.DrawingArea()
        darea.connect("draw", self.on_draw)
        self.add(darea)

        self.set_title("Basic shapes")
        self.set_default_size(390, 240)
        
        self.connect("destroy", Gtk.main_quit)

    def on_draw(self, da, ctx):

        ctx.set_source_rgb(0.6, 0.6, 0.6)

        ctx.rectangle(20, 20, 120, 80)
        ctx.rectangle(180, 20, 80, 80)
        ctx.fill()

        ctx.arc(330, 60, 40, 0, 2*math.pi)
        ctx.fill()
        
        ctx.arc(90, 160, 40, math.pi/4, math.pi)
        ctx.fill()

        ctx.translate(220, 180)
        ctx.scale(1, 0.7)
        ctx.arc(0, 0, 50, 0, 2*math.pi)
        ctx.fill()        


win = MyWindow()
win.show_all()
Gtk.main()
