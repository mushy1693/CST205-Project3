import pyglet #to play sound
import sys, os, random, png  #png used for the initial image
from random import randrange #used for music
from random import shuffle
from Tkinter import * #all for convenience 
from PIL import Image, ImageTk, ImageOps 
#Image is Pillow, ImageTK is the way to use images within tkinter, ImageOps used to work with the image after resizing
from math import *

def main():

   root = Tk()
   root.configure(background='gray70')

   # Center the windows
   def center_window(w=300, h=200):
       # get screen width and height
       ws = root.winfo_screenwidth()
       hs = root.winfo_screenheight()
       # calculate position x, y
       x = (ws/2) - (w/2)
       y = (hs/2) - (h/2)
       root.geometry('%dx%d+%d+%d' % (w, h, x, y))

   center_window(800,800)       
   frame = Frame(root)
   frame.pack()
   top_can = Canvas(frame, bg='peachpuff4', width=600, height=50)
   top_can.pack()
   canvas = Canvas(frame, bg='white', width=600, height=600)
   canvas.pack()

   def removeWidget(widget):
      widget.destroy()

#http://www.java2s.com/Tutorial/Python/0360__Tkinker/Canvaspaintprogram.htm
   def draw( event ):
      x1, y1 = ( event.x - 1 ), ( event.y - 1 )
      x2, y2 = ( event.x + 1 ), ( event.y + 1 )
      canvas.create_rectangle( x1, y1, x2, y2, fill = "black" )

   def end():
      canvas.delete("all")

   def halt():
      canvas.bind("<B1-Motion>", lambda e: "break")

   def removeWidget(widget):
      widget.destroy()

   def game():
   
      def newGame():
         removeWidget(clear_button)
         removeWidget(submit_button)
         removeWidget(switch_button)
         game()
   
      canvas.bind( "<B1-Motion>", draw )
      clear_button=Button(text="CLEAR", command=lambda: end())
      clear_button.pack()
      submit_button=Button(text="Submit", command=lambda: halt())
      submit_button.pack()
      switch_button=Button(text="Switch", command=lambda: newGame())
      switch_button.pack()

   game()
   root.mainloop()  

main()