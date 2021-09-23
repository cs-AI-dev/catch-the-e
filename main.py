# Here is my source code
# Copy and paste into Pycharm?

from tkinter import *
from random import randint as r

pre = Tk()
pre.title("Catch Game")

preLabel = Label(pre, text="Catch the Dopamine! Be happy!")
preLabel.grid(row=1, column=1)

preBtn = Button(pre, text="Go", command=pre.destroy)
preBtn.grid(row=2, column=1)

pre.mainloop()


main = Tk()
main.title("Catch Game")

btns = {}

xn = 0
yn = 0

pts = 0

def kill():
  main.destroy()
  
  death = Tk()
  dLabel = Label(death, text="You lost!\nPoints: " + str(pts) + ".")
  dLabel.grid(row=1, column=1)

def switch():
  pts += 1
  
  xn = r(2, 9)
  yn = r(2, 9)

  for y in range(10):
    btns[y] = {}
    for x in range(10):
      if x == xn and y == yn:
        btns[y][x] = Button(main, text=" ", font=("OCR A Extended", 14), command=switch, bg="black", fg="white")
        btns[y][x].grid(row=x, column=y)
      else:
        btns[y][x] = Button(main, text=" ", font=("OCR A Extended", 14), command=switch, bg="black", fg="white")
        btns[y][x].grid(row=x, column=y)

  btns[yn][xn]["text"] = "C8H11NO2"

for y in range(10):
  btns[y] = {}
  for x in range(10):
    btns[y][x] = Button(main, text=" ", font=("OCR A Extended", 14), command=switch, bg="black", fg="white")
    btns[y][x].grid(row=x, column=y)

main.mainloop()
