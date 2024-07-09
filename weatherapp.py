from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests 
import pytz
from PIL import Image, ImageTK
import time 

class weatherClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("700x400+325+150")
        
        
if __name__=="_main_":
    root=Tk()
    obj=weatherClass(root)
    root.mainloop()
