#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        super().__init__()

        self.init_ui()


    def init_ui(self):

        grid = Gtk.Grid()
        self.add(grid)

        quitBtn = Gtk.Button(label="Quit")
        quitBtn.set_size_request(80, 30)
        quitBtn.connect("clicked", self.on_button_clicked)

        grid.attach(quitBtn, 0, 0, 1, 1)

        self.set_border_width(10)
        self.set_title("Quit button")
        self.set_default_size(280, 180)
        self.connect("destroy", Gtk.main_quit)

    def on_button_clicked(self, widget):
        Gtk.main_quit()

win = MyWindow()
win.show_all()
Gtk.main()
