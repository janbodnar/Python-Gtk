#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

class MyWindow(Gtk.Window):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.init_ui()

    def init_ui(self):    
        
        self.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(6400, 6400, 6440))

        self.bardejov = GdkPixbuf.Pixbuf.new_from_file("bardejov.jpg")
        self.rotunda = GdkPixbuf.Pixbuf.new_from_file("rotunda.jpg")
        self.mincol = GdkPixbuf.Pixbuf.new_from_file("mincol.jpg")
        
        image1 = Gtk.Image()
        image2 = Gtk.Image()
        image3 = Gtk.Image()
        
        image1.set_from_pixbuf(self.bardejov)
        image2.set_from_pixbuf(self.rotunda)
        image3.set_from_pixbuf(self.mincol)
               
        fixed = Gtk.Fixed()
           
        fixed.put(image1, 10, 10)
        fixed.put(image2, 40, 160)
        fixed.put(image3, 170, 50)

        self.add(fixed)

        self.set_border_width(20)
        self.set_title("Fixed")
        
        self.connect("destroy", Gtk.main_quit)

win = MyWindow()
win.show_all()
Gtk.main()


