#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox
import time

def set_alarm():
    alarm_time = entry.get()
    current_time = time.strftime("%H:%M")

    while current_time != alarm_time:
        current_time = time.strftime("%H:%M")
        time.sleep(1)

    messagebox.showinfo("Alarm", "Time's up!")

app = tk.Tk()
app.title("Alarm Clock")
app.geometry("300x150")

label = tk.Label(app, text="Enter alarm time (HH:MM):")
label.pack(pady=10)

entry = tk.Entry(app, font=("Arial", 20))
entry.pack(pady=10)

set_button = tk.Button(app, text="Set Alarm", command=set_alarm)
set_button.pack(pady=10)

app.mainloop()


# In[ ]:




