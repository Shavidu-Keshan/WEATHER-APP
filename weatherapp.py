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
        
        #Variables#
        self.var_city=StringVar()
        self.var_txtcity=StringVar()
        self.var_latitude=StringVar()
        self.var_temppreture=StringVar()
        
        self.var_humidity=StringVar()
        self.var_pressure=StringVar()
        self.var_wind=StringVar()
        self.var_des=StringVar()
        self.var_localtime=StringVar()
        
        #our data#
        self.var_txtcity=Label(self.root,text="",font=("times 30 bold"),fg='black',bg="#08f7f7",justify=CENTER)
        self.var_txtcity.place(x=0,y=70)
        self.var_txtcity.focus()
        
        self.var_latitude=Label(self.root,text="",font=("times 12 bold"),fg='black',bg="#08f7f7",justify=CENTER)
        self.var_latitude.place(x=0,y=70)
        
        self.var_temppreture=Label(self.root,text="",font=("times 40 bold"),fg='black',bg="#08f7f7",justify=CENTER)
        self.var_temppreture.place(x=20,y=150)
        
        self.var_localtime=Label(self.root,text="",font=("times 15 bold"),fg='black',bg="#08f7f7",justify=CENTER)
        self.var_localtime.place(x=165,y=220,width=150)
        
        self.var_des=Label(self.root,text="",font=("times 14 bold"),fg='black',bg="#08f7f7",justify=CENTER)
        self.var_des.place(x=90,y=330)
        
        self.var_wind=Label(self.root,text="",font=("times 14 bold"),fg='black',bg="#08f7f7",justify=CENTER)
        self.var_wind.place(x=250,y=330)
        
        self.var_humidity=Label(self.root,text="",font=("times 15 bold"),fg='black',bg="#08f7f7",justify=CENTER)
        self.var_humidity.place(x=370,y=330)
        
        self.var_pressure=Label(self.root,text="",font=("times 15 bold"),fg='black',bg="#08f7f7",justify=CENTER)
        self.var_pressure.place(x=500,y=330)
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = weatherClass(root)
    root.mainloop()
    

