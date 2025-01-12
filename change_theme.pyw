import imageio
from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path
import os
import pandas as pd

loc_data = pd.read_csv('Data\locus.csv')
geo = loc_data.iloc[0][0]
root = Tk()
root.geometry(geo)
video_name = 'resources\loading\load.MP4'
video = imageio.get_reader(video_name)
delay = int(1000 / video.get_meta_data()['fps'])

def start():
    os.startfile("let's calculate.pyw")
       
def stream(label):
  try:
    image = video.get_next_data()
  except:
    video.close()
    quit()
    return
  label.after(delay, lambda: stream(label))
  frame_image = ImageTk.PhotoImage(Image.fromarray(image))
  label.config(image=frame_image)
  label.image = frame_image
  
root.overrideredirect(True)
root.attributes("-transparentcolor","#434343")
root.config(bg="#434343")
root.after(5000,start)
root.attributes("-topmost",True)
pct = PhotoImage(file="resources\loading\Picture.png")
lab = Label(root,image = pct)
lab.place(x=-2,y=-2)
my_label = Label(root)
my_label.place(x=48,y=204,height=60,width=72)
my_label.after(delay, lambda: stream(my_label))
root.mainloop()
