from tkinter import Label, Tk
import time
text_font= ("Boulder", 68, 'bold')
background = "yellow"
foreground= "#363529"
border_width = 58

window = Tk()

window.title("Digital Clock")
window.geometry("420x150")
window.resizable(1,1)


label = Label(window, font=text_font, bg=background, fg=foreground, bd=border_width, highlightthickness=0)
label.grid(row=0, column=0)

def digital_clock():
    time_live_12 = time.strftime("%I:%M:%S")
    label.config(text=time_live_12)
    label.after(200,digital_clock)

digital_clock()

window.mainloop()