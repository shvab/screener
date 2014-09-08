#!/usr/bin/env python
# encoding: utf-8
"""
screener.py

Created by Shvab Ostap on 2014-09-08.
"""
import time
import gtk.gdk

while True:
    ts = str(time.time())[:-3]
    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    if (pb != None):
        pb.save("/home/Ostap/Screens/" + ts + ".png","png")
        print "Screenshot saved to " + ts + ".png."
    else:
        print "Unable to get the screenshot."
    time.sleep(60)

