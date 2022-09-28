import tkinter as ui
import time
import math

window = ui.Tk()
window.title("Analog Clock")
window.geometry("600x600") # set size for window

def updateClock():
    # update times from string to integer
    hours = int(time.strftime("%H"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

    # Remember clock origin position is not (0,0) but (300,300)
    # define the seconds(x,y) final positions with formulas achieved:
    # x'last position' = r*(sin(radians(t))) + x'1st position'
    seconds_x = seconds_hand_len * math.sin(math.radians(seconds * 6)) + center_x # seconds*6 because it changes 6º/second
    # y'last position' = -r*(cos(radians(t))) + y'1st position'
    seconds_y = -seconds_hand_len * math.cos(math.radians(seconds * 6)) + center_y # seconds*6 because it changes 6º/second
    # coordenates of seconds_hand
    canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)

    # Do the same for minutes
    minutes_x = minutes_hand_len * math.sin(math.radians(minutes * 6)) + center_x  # minutes*6 because it changes 6º/minute
    minutes_y = -minutes_hand_len * math.cos(math.radians(minutes * 6)) + center_y  # minutes*6 because it changes 6º/minute
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

    # Do the same for hours
    hours_x = hours_hand_len * math.sin(math.radians(hours * 30)) + center_x  # hours*30 because it changes 30º/hour
    hours_y = -hours_hand_len * math.cos(math.radians(hours * 30)) + center_y  # hours*30 because it changes 30º/hour
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)

    # update coordenates every second
    window.after(1000, updateClock)


# canvas to build/drawing layouts
canvas = ui.Canvas(window, width=600, height=600, bg="light blue")
canvas.pack(expand=True, fill="both")

# get background image of analog clock
analogbg = ui.PhotoImage(file='analogbg.png')
canvas.create_image(300, 300, image=analogbg) # create image with half size of window

# define clock hands
center_x = 300 #mid point
center_y = 300 #mid point
seconds_hand_len = 220
minutes_hand_len = 170
hours_hand_len = 120

#Draw clock hands using canvas.create_line
# creates line that connects: x0,y0 -> x1=(x0+len), y1=(y0+len)  ===> (x0,y0,x0+len,y0+len)
# seconds hand
seconds_hand = canvas.create_line(300, 300,
                                  300 + seconds_hand_len,
                                  300 + seconds_hand_len,
                                  width=3, fill="blue")
# minutes hand
minutes_hand = canvas.create_line(300, 300,
                                  300 + minutes_hand_len,
                                  300 + minutes_hand_len,
                                  width=4, fill="black")
#hours hand
hours_hand = canvas.create_line(300, 300,
                                300 + hours_hand_len,
                                300 + hours_hand_len,
                                width=8, fill="black")

updateClock()

window.mainloop()

# radian = 57.3º
# 360/60 = 6º/sec
# seconds hand has 60secs to complete 360º -> need to move 6º per second

# r = radius(hypotenuse) = 190; 90º triangle w/ inverted base of x; y=adjacent; radian of (t) angle
# Need to calculate x and y to with radians(t) point position (x=?,y=?)

# cos(radians(t)) = adjacent/hypotenuse = y/r
# <=> y = r*(cos(radians(t)))
# sin(radians(t)) = opposite/hypotenuse = x/r
# <=> x = r*(sin(radians(t)))
# In computers the y increases downwards so:
# y = r*(cos(radians(t))) ===> needs to be negative ===> y = -r*(cos(radians(t)))
# Explanation: computers are weird. Joking.
# https://www.eevblog.com/forum/vintage-computing/why-does-y-increase-going-down-the-screen/



