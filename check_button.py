#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.init_ui()

    def init_ui(self):    
        
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        cbtn = Gtk.CheckButton("Show title")
        cbtn.set_active(True)
        cbtn.set_valign(Gtk.Align.START)
        cbtn.connect("clicked", self.on_clicked)

        hbox.pack_start(cbtn, False, False, 0)

        self.add(hbox)

        self.set_border_width(10)
        self.set_title("CheckButton")
        self.set_default_size(300, 180)
        self.connect("destroy", Gtk.main_quit)

    def on_clicked(self, wid):

        if wid.get_active():
            self.set_title("CheckButton")
        else:
           self.set_title("")


win = MyWindow()
win.show_all()
Gtk.main()


