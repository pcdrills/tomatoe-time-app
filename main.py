# Tomatoe app by pcdrills
#  You can modify the values of the constants written but if you are unsure what a value represents, 
#  Then it's better you allow it as it is.

from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 
SHORT_BREAK_MIN = 5 
LONG_BREAK_MIN = 20 
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    check_mark.config(text="")
    session_info_label.config(text="...")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
# starts the timer and decides on the the amount of time it has to count and decideson whether 
# it's a break or short time or long break using the reps count value
def start_timer():
    # count_down(50)
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if(reps % 8) == 0:
        count_down(long_break_sec)
        session_info_label.config(text="Long Break", fg=RED)
    elif(reps % 2) == 1:
        count_down(work_sec)
        session_info_label.config(text="Work", fg=GREEN)
    elif (reps % 2) == 0:
        count_down(short_break_sec)
        session_info_label.config(text="Short Break", fg=PINK)
        
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# responsible for  timer counting down on the tomatoe and updating the values of the time
# and also the values of the reps displayed on the left of the tomatoe
import math

def count_down(count):
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        count_minutes = count / 60
        count_seconds = count % 60
        count_minutes = math.floor(count_minutes)
        count_seconds = math.floor(count_seconds)
        if count_seconds < 10:
            count_seconds = (f"0{count_seconds}")
        displayed_time = str(count_minutes) + ":" + str(count_seconds)
        print(displayed_time)
        # print(f"{f}:{s}")
        canvas.itemconfig(timer_text, text=displayed_time)
        session_count.config(text=f"REP:{reps}")
    else:
        start_timer()
        
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔️"
        check_mark.config(text=marks)
            
        
    
    


# ---------------------------- UI SETUP ------------------------------- #
# All the initial interface or display

window = Tk()
window.title("Tomatoe Timer - Work/Rest Time Management - #pcdrills")
window.config(padx=100, pady=50, bg=YELLOW)



#create the timer label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW,font=(FONT_NAME, 50))
timer_label.grid(column=2, row=0)

#create the session timer info under the title
session_info_label = Label(text="...", fg=GREEN, font=(FONT_NAME, 24), bg='yellow')
session_info_label.grid(column=2, row=1)
#show session info for reps
session_count = Label(text=f"REP: {reps}", fg=GREEN, bg=YELLOW,font=(FONT_NAME, 20))
session_count.grid(column=1, row=2)

#Create a canvas for the tomatoe image and the time on it
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# start_timer()

#Create the Start and Reset buttons
start_button = Button(width=10, text="Start", command=start_timer)
start_button.grid(column=1, row=3)
reset_button = Button(width=10, text="Reset", command=reset_timer)
reset_button.grid(column=3, row=3)

#create the green check mark
check_mark = Label(text="")
check_mark.grid(column=1, row=4)


#pc drills text written at the bottum
pcdrills_text = Label(text="github.com/pcdrills", fg='black', bg=YELLOW,font=(FONT_NAME, 12))
pcdrills_text.grid(column=2, row=5)

window.mainloop()