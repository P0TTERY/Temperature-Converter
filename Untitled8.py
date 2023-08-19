#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk

def convert_temperature():
    try:
        fahrenheit = float(entry_fahrenheit.get())
        celsius = (fahrenheit - 32) * 5/9
        label_result.config(text=f"{fahrenheit:.2f} °F = {celsius:.2f} °C")
    except ValueError:
        label_result.config(text="Invalid input")

root = tk.Tk()
root.title("Temperature Converter")

label_fahrenheit = tk.Label(root, text="Enter Fahrenheit:")
entry_fahrenheit = tk.Entry(root)
button_convert = tk.Button(root, text="Convert", command=convert_temperature)
label_result = tk.Label(root, text="", font=("Helvetica", 14, "bold"))

label_fahrenheit.grid(row=0, column=0, padx=10, pady=10)
entry_fahrenheit.grid(row=0, column=1, padx=10, pady=10)
button_convert.grid(row=1, columnspan=2, padx=10, pady=10)
label_result.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()


# In[ ]:




