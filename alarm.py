# Import Required Library
from tkinter import *
import datetime
import time
import winsound
from threading import *
from plyer import notification
import random

# ALL IMPLEMENTATIONS BY CALVIN
# 5-second ping system after alarm (8/8/2022) - OMITTED
# Custom Pop-up message when alarm prompts (8/8/2022)
# Current Clock Time (8/9/2022)
# Notification System (8/9/2022)
# AM/PM System (8/25/2022)
# Random Alarm Option (9/7/2022)

# PLANNED IMPLEMENTATIONS
# When notification is clicked, bring to a popup message
# Option to stop notifications for the rest of the day
# Running in the background

# Create Object
root = Tk()
 
# Set geometry
root.geometry("500x325")
 
# Use Threading
def Threading():
    t1=Thread(target=alarm)
    t1.start()
    
current_clock = Label(root,font=("helvetica 35 bold"),fg="black")
current_clock.pack(anchor='center')

def clock():
    # Set clock
    date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
    date,time1 = date_time.split()
    time2,time3 = time1.split('/')
    hour,minutes,seconds =  time2.split(':')
    if int(hour) > 12 and int(hour) < 24:
        time = str(int(hour) - 12) + ':' + minutes + ':' + seconds + ' ' + time3
    else:
        time = time2 + ' ' + time3
    current_clock.config(text = time)
    current_clock.after(1000, clock)
    return time


def alarm():
    # Infinite Loop

    # Grabs a randomized time (optimized so that no time between 9 PM - 12 PM is allowed)
    hours_1 = ('00', '01', '02', '03', '04', '05', '06',
         '07', '08', '09', '10', '11', '12', '13', '14',
         '15', '16', '17', '18', '19', '20',
    )
    hr = random.choice(hours_1)
    ms = random.choice(minutes)
    ss = random.choice(seconds)
    current_time1 = datetime.datetime.now().strftime("%H:%M:%S")

    # Confirms that hour time is after the current hour time
    while int(hr) <= int(current_time1[:2]):
        print(int(hr))
        hr = random.choice(hours_1)
        
    while True:
        # Set Alarm
        if randoming.get() == 'Random':
            set_alarm_time = f"{hr}:{ms}:{ss}"
        elif day.get() == 'PM' and hour.get() != '12':
            set_alarm_time = f"{str(int(hour.get())+12)}:{minute.get()}:{second.get()}"
        elif day.get() == 'AM' and hour.get() == '12':
            set_alarm_time = f"{str(int(hour.get())-12)}:{minute.get()}:{second.get()}"
        else:
            set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        # Wait for one seconds
        time.sleep(1)
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            # Notification for computer
            notification.notify(
                title="New notification for Calvin!",
                message="It is currently {time}.\nLet's do a Leetcode problem!\n".format(time=clock()),
                app_icon="Paomedia-Small-N-Flat-Bell.ico",
                timeout=10 # time notification remains on screen
            )
            # Notification repeats after every 2 hrs
            time.sleep(60 * 60 * 2)
            Label(root,text="Time to Leetcode!",font=("Helvetica 20 bold"),fg="red").pack(pady=10)

# Add Labels, Frame, Button, Optionmenus
Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
Label(root,text="Set Time",font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()
 
hour = StringVar(root)
hours = ('12', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11'
        )
hour.set(hours[0])
 
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)
 
minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])
 
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)
 
second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])
 
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

day = StringVar(root)
days = ('AM', 'PM')
day.set(days[0])
d = OptionMenu(frame, day, *days)
d.pack(side=LEFT)

randoming = StringVar(root)
randoms = ('Alarm', 'Random')
randoming.set(randoms[0])
r = OptionMenu(frame, randoming, *randoms)
r.pack(side=LEFT)

Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=20)
# Execute Tkinter
clock()
root.mainloop()
