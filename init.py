from tkinter import *

print("initializing screens ...")

ff = ("OCR A Extended", 20)

startWindow = Tk()
startLabel = Label(startWindow, text="Catch the E!", font=ff)
startLabel.grid(row=1, column=1)
startBtn = Button(startWindow, text="Start", font=ff, bg="#00FF00", command=startWindow.destroy)
startBtn.grid(row=2, column=1)

master = Tk()
btns = {}
for y in range(20):
  for x in range(20):
    btns[(x, y)] = Button(
