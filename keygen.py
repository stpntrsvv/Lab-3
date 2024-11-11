import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import string
from time import sleep
from pygame import mixer
from tkinter.ttk import Progressbar
import threading


def play_music():
    mixer.init()
    sound = mixer.Sound("true.mp3")
    sound.play()


def random_string(length):
    return ''.join(random.choices(string.ascii_uppercase, k=length))


def progress_bar():
    bar['value'] = 0
    for i in range(0, 10):
        bar['value'] += 10
        sleep(.2)


def keygen():
    user_input = entry.get()
    if not user_input.isdigit() or len(user_input) != 6:
        messagebox.showerror("Ошибка!", "Введите шестизначное число")
    else:
        block1 = user_input[1:4] + random_string(2)
        block2 = user_input[0:3] + random_string(2)
        sum_value = int(user_input[1:4]) + int(user_input[0:3])
        block3 = f"{sum_value:04d}"
        key = f"{block1}-{block2} {block3}"
        output_var.set(key)


def pb_and_keygen():
    threading.Thread(target=progress_bar).start()
    threading.Timer(2.3, keygen).start()


window = tk.Tk()
window.title("KeyGen")
window_length = 850
window_width = 480
window.geometry(f'{window_length}x{window_width}')
window.resizable(width=False, height=False)

background_image = Image.open("background.png")
background_image = background_image.resize((window_length, window_width))
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

bar = Progressbar(window, mode="determinate", length=300)
bar.place(x=275, y=350)

entry = tk.Entry(window, font=("Times New Roman", 14))
entry.place(x=275, y=200, width=300)

generate_button = tk.Button(window, text="Сгенерировать", font=("Arial", 13), command=pb_and_keygen)
generate_button.place(x=365, y=275)

output_var = tk.StringVar()
output_label = tk.Label(window, textvariable=output_var, font=("Times New Roman", 14), bg="white")
output_label.place(x=275, y=400, width=300)

sleep(2)
play_music()

window.mainloop()
