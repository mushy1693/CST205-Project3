import pyglet #to play sound
import sys, os, random, png  #png used for the initial image
from random import randrange #used for music
from random import shuffle
from Tkinter import * #all for convenience
from PIL import Image, ImageTk, ImageOps
#Image is Pillow, ImageTK is the way to use images within tkinter, ImageOps used to work with the image after resizing
from math import *

score1 = 0
score2 = 0
pturn = "p1"
p1Color = "khaki3"
p2Color = "khaki3"
word = "bunny"
getWord = ""
time = 30

def main():

   root = Tk()
   root.configure(background='khaki3')

   # Center the windows
   def center_window(w=300, h=200):
       # get screen width and height
       ws = root.winfo_screenwidth()
       hs = root.winfo_screenheight()
       # calculate position x, y
       x = (ws/2) - (w/2)
       y = (hs/2) - (h/2)
       root.geometry('%dx%d+%d+%d' % (w, h, x, y))

   center_window(618,650)

   playerAndScore = Frame(root)
   playerAndScore.pack()
   wordPanel = Frame(root)
   wordPanel.pack()
   drawingframe = Frame(root)
   drawingframe.pack()
   inputPanel = Frame(root)
   inputPanel.pack()
   submitAndNextPanel = Frame(root)
   submitAndNextPanel.pack()

   canvas = Canvas(drawingframe, bg='white', width=610, height=500)

   def draw( event ):
      x1, y1 = ( event.x - 1 ), ( event.y - 1 )
      x2, y2 = ( event.x + 1 ), ( event.y + 1 )
      canvas.create_rectangle( x1, y1, x2, y2, fill = "black" )
      #http://www.java2s.com/Tutorial/Python/0360__Tkinker/Canvaspaintprogram.htm

   def check(getCheck):
      if(getCheck == "correct"):
        correctLabel = 'correct'
        photo = PhotoImage(file="pic/correct.gif")
      else:
        correctLabel = 'incorrect'
        photo = PhotoImage(file="pic/incorrect.gif")

      toplevel = Toplevel()
      toplevel.geometry('%dx%d+%d+%d' % (200, 200, 620, 350))
      label1 = Label(toplevel, text=correctLabel, background = "tan4", image = photo)
      label1.photo = photo
      label1.pack()

   def clearCanvas():
      canvas.delete("all")

   def word_label(label):
      def count():
        label.config(text= "")
      count()

   def submit_label(label):
      def count():
        label.config(text= "Click next for your turn to draw")
      count()

   def turn_label(label):
      def count():
        global pturn
        if(pturn == "p1"):
            label.config(text= "Player 2 Guess" + "\n" + "Tip: Click 'Submit' when ready")
        else:
            label.config(text= "Player 1 Guess" + "\n" + "Tip: Click 'Submit' when ready")
      count()

   def counter_label(label, score):
      def count():
        if(score == "score1"):
            global score1
            label.config(text= "Player 1 Turn" + "\n" + "Score: " + str(score1))
        else:
            global score2
            label.config(text= "Player 2 Turn" + "\n" + "Score: " + str(score2))
      count()

   def halt(label1):
      canvas.bind("<B1-Motion>", lambda e: "break")
      word_label(label1)
      turn_label(label1)

   def removeWidget(widget):
      widget.destroy()

   def choosePlayer():
       global pturn
       if(pturn == "p1"):
           pturn = "p2"
       else:
           pturn = "p1"

   def chooseColor():
       global pturn
       global p1Color
       global p2Color
       if(pturn == "p1"):
           p1Color = "SkyBlue2"
           p2Color = "khaki3"
       else:
           p1Color = "khaki3"
           p2Color = "SkyBlue2"

   def game():

      global score1
      global score2
      global pturn
      global time
      global word

      def newGame():

         choosePlayer()

         removeWidget(player1label)
         removeWidget(player2label)
         removeWidget(wordlabel)
         removeWidget(clear_button)
         removeWidget(done_button)
         removeWidget(submit_button)
         removeWidget(next_button)
         removeWidget(inputBox)
         canvas.delete(ALL)
         game()

      chooseColor()

      player1label = Label(playerAndScore, text="~Player 1 Turn~" + "\n" + "Score: " + str(score1), width = 16, height = 5, background = p1Color)
      player1label.pack(side = LEFT)

      wordlabel= Label(playerAndScore, text="Word: " + word + "\n" + "Time Left: " + str(time) + "\n" + "Tip: Click 'Done' when finish drawing", width = 53, height = 5, background = "goldenrod4")
      wordlabel.pack(side = LEFT)

      player2label = Label(playerAndScore, text="~Player 2 Turn~" + "\n" + "Score: " + str(score2), width = 16, height = 5, background = p2Color)
      player2label.pack(side = LEFT)

      canvas.pack()
      canvas.bind( "<B1-Motion>", draw )

      inputBox = Entry(inputPanel,width=50)
      inputBox.pack()

      def submit():
          global getWord
          global score1
          global score2
          getWord = inputBox.get()
          if(getWord == word):
              if(pturn == "p1"):
                  score2+=1
                  counter_label(player2label, "score2")
                  check("correct")
                  submit_label(wordlabel)
              else:
                  score1+=1
                  counter_label(player1label, "score1")
                  check("correct")
                  submit_label(wordlabel)
          else:
              check("incorrect")
              submit_label(wordlabel)


      clear_button=Button(submitAndNextPanel, text="Clear", command=lambda: clearCanvas())
      clear_button.pack(side = LEFT)

      if(pturn == "p1"):
          done_button=Button(submitAndNextPanel, text="Done", command=lambda: halt(wordlabel))
      else:
          done_button=Button(submitAndNextPanel, text="Done", command=lambda: halt(wordlabel))
      done_button.pack(side = LEFT)

      submit_button=Button(submitAndNextPanel, text="Submit", command=lambda: submit())
      submit_button.pack(side = LEFT)
      next_button=Button(submitAndNextPanel, text="Next", command=lambda: newGame())
      next_button.pack(side = LEFT)

   game()
   root.mainloop()

main()
