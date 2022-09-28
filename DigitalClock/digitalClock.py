import time
import tkinter as ui

window = ui.Tk()
window.title("Magical Clock")

def update_clock():
    hours = time.strftime("%H")
    minutes =  time.strftime("%M")
    seconds = time.strftime("%S")

    timeText = hours + ":" + minutes + ":" + seconds
    clockLabel.config(text=timeText)
    clockLabel.after(200, update_clock)

#clockFrame = ui.LabelFrame(window, text="blue")
clockLabel = ui.Label(window, font="Verdana 80 bold", background="silver", foreground="black")
clockLabel.pack()

update_clock()

window.mainloop()