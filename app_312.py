import os
import tkinter as tk

def enable_32():
    old_directory = r'C:\Program Files (x86)\Python312-32-blocked'
    new_directory = r'C:\Program Files (x86)\Python312-32'
    try:
        os.rename(old_directory, new_directory)
    except:
        pass
    update_button_color(buttons)  

def disable_32():
    old_directory = r'C:\Program Files (x86)\Python312-32'
    new_directory = r'C:\Program Files (x86)\Python312-32-blocked'
    try:
        os.rename(old_directory, new_directory)
    except:
        pass
    update_button_color(buttons)  

def enable_64():
    old_directory = r'C:\Program Files\Python312-blocked'
    new_directory = r'C:\Program Files\Python312'
    try:
        os.rename(old_directory, new_directory)
    except:
        pass
    update_button_color(buttons)  

def disable_64():
    old_directory = r'C:\Program Files\Python312'
    new_directory = r'C:\Program Files\Python312-blocked'
    try:
        os.rename(old_directory, new_directory)
    except:
        pass
    update_button_color(buttons)  

def enable_arm():
    old_directory = r'C:\Program Files (Arm)\Python312-arm64-blocked'
    new_directory = r'C:\Program Files (Arm)\Python312-arm64'
    try:
        os.rename(old_directory, new_directory)
    except:
        pass
    update_button_color(buttons)  

def disable_arm():
    old_directory = r'C:\Program Files (Arm)\Python312-arm64'
    new_directory = r'C:\Program Files (Arm)\Python312-arm64-blocked'
    try:
        os.rename(old_directory, new_directory)
    except:
        pass
    update_button_color(buttons)  

def identify_python():
    python_dirs = [
        r'C:\Program Files (x86)\Python312-32',
        r'C:\Program Files\Python312',
        r'C:\Program Files (Arm)\Python312-arm64'
    ]

    exists = [os.path.exists(directory) for directory in python_dirs]

    return exists

def update_button_color(buttons):
    exists = identify_python()
    for i, button in enumerate(buttons):
        if exists[i]:
            button.config(bg='pink')
        else:
            button.config(bg='blue')

def on_button_click(text):
    if text == 'Python x86':
        disable_64()
        disable_arm()
        enable_32()
    elif text == 'Python x64':
        disable_32()
        disable_arm()
        enable_64()
    elif text == 'Python xARM':
        disable_32()
        disable_64()
        enable_arm()
    update_button_color(buttons)  

root = tk.Tk()
root.title("Python Switcher")

buttons = []

button_texts = ["Python x86", "Python x64", "Python xARM"]
for text in button_texts:
    button = tk.Button(root, text=text, bg='blue', command=lambda t=text: on_button_click(t))
    button.pack(pady=5)
    buttons.append(button)

update_button_color(buttons)  

root.mainloop()
