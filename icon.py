#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.init_ui()

    def init_ui(self):    

        self.set_icon_from_file("web.png")

        self.set_title("Icon")
        self.set_default_size(280, 180)
        
        self.connect("destroy", Gtk.main_quit)


win = MyWindow()
win.show()
Gtk.main()
