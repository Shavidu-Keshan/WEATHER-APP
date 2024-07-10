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
        self.var_city.set("Kandy")
        
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
        
        
        self.var_latitude=Label(self.root,text="",font=("times 12 bold"),fg='black',bg="#08f7f7",justify=CENTER)
        self.var_latitude.place(x=0,y=120)
        
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
        
        # Lable #
        lable1=Label(self.root,text="DESCRIPTION",font=("times 14 bold"),fg='white',bg="#4c7b7b").place(x=90,y=300)
        lable2=Label(self.root,text="WIND",font=("times 14 bold"),fg='white',bg="#4c7b7b").place(x=250,y=300)
        lable3=Label(self.root,text="HUMIDITY",font=("times 14 bold"),fg='white',bg="#4c7b7b").place(x=370,y=300)
        lable4=Label(self.root,text="PRESSURE",font=("times 14 bold"),fg='white',bg="#4c7b7b").place(x=500,y=300)
        
        # city entry #
        textfield = Entry(self.root, textvariable=self.var_city, justify=CENTER, width=15, font=("times 25 bold"), bg='#545a5a', fg='white', bd=0)

        textfield.place(x=383,y=35,width=225)
        textfield.focus()
        
        # search button #
        self.search_icon = PhotoImage(file="arrow1.png").subsample(9)
        self.myimage_icon = Button(self.root, image=self.search_icon, borderwidth=0, cursor='hand2', bg='#203243', activebackground='#203243',command=self.getweather)
        self.myimage_icon.place(x=615, y=34)
        
    def getweather(self):
        try:
            city=self.var_city.get()
            geolocator= Nominatim(user_agent='geoapiExercises')
            location=geolocator.geocode(city)
            obj=TimezoneFinder()
            
            # logitude & Latitude #
            
            result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
            
            self.var_txtcity.config(text=f"{result}")
            self.var_latitude.config(text=f"{round(location.latitude,4)}°N, {round(location.longitude,4)}°E")
            
            # local time of request city #
            home=pytz.timezone(result)
            local_time=datetime.now(home)
            current_time=local_time.strftime("%I:%M:%p")
            
            # request wether data #
            api="https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=fcdea6235b8827b03d529092b6f16e97"
            weather_data=requests.get(api).json()
            
            print(weather_data)
            
            
            
            
            
            
            
        except Exception as e:
            messagebox.showerror("Weather App","Invalied Entry....!")   

        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = weatherClass(root)
    root.mainloop()
    

