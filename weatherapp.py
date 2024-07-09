from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests 
import pytz
from PIL import Image, ImageTk
import time 

class weatherClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x400+325+150")
        self.root.title("Weather App")
        self.root.resizable(False, False)
        self.root.config(bg='#f8ea28', bd=1)
        
        #background image#
        self.image = Image.open("weather2.jpg")  # Update with your image path
        self.resized_image = self.image.resize((700, 400))
        self.photo_image = ImageTk.PhotoImage(self.resized_image)
        self.image_label = Label(self.root, image=self.photo_image)
        self.image_label.place(x=0, y=0)
        
if __name__ == "__main__":
    root = Tk()
    obj = weatherClass(root)
    root.mainloop()
    

