#importing modules used in projects
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import time 
import imutils

stream = cv2.VideoCapture("clip.mp4")
flag = True
def play(speed):
    print(f"You clicked on play. Speed is {speed}")
    global flag
    # play video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="red", font="Times 26 bold", text="Decision Pending")
    flag = not flag

# making decsion pending function
def pending(decision):
    # 1 display decision pending image
    frame = cv2.cvtColor(cv2.imread("pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 2 wait 1.5 second
    time.sleep(1.5)

    # 3 display sponsor Image
    frame = cv2.cvtColor(cv2.imread("sponsor.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 4 wait 2.5 second
    time.sleep(2.5)

    # 5 display out/not out image
    if decision == "out":
        decisionimg = "out.png"
    else:
        decisionimg = "not_out.png"
    frame = cv2.cvtColor(cv2.imread(decisionimg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    pass

# makeing out function
def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("player is out")

# makeing not out function
def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("player is not out")

# main windows
SET_WIDTH = 650
SET_HEIGHT = 368

# tkinter gui download her
window = tkinter.Tk()
window.title("Ahamed Muhsin Third Umpire Decision review syestem")
cv_img = cv2.cvtColor(cv2.imread('welcome.png'), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()

# buttons for control syestem

btn = tkinter.Button(window, text=" << << Backward (fast) ", width=75, command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text=" << Backward (slow) ", width=75, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text=" Forward >> (slow) ", width=75, command=partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text=" Forward >> >> (fast) ", width=75, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text=" Give Out ", width=75, command=out)
btn.pack()

btn = tkinter.Button(window, text=" Give Not Out ", width=75, command=not_out)
btn.pack()

window.mainloop()