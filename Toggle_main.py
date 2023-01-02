############ WELCOME TO THIS CODE #######################
# This is  Time table management system TOGGLE #####################
# T - 
# O - 
# G - 
# G - 
# L - 
# E - 

'''
This is a Time management system interface coded by Adnan 

'''


import os
import random
print(' ')
print('Initiating System...')
try:
    import PIL
    from PIL import Image, ImageTk
except:
    print('Installing PIL module')
    os.system("pip install Pillow")
    import PIL
    from PIL import Image, ImageTk
try:
    import requests
except:
    print('Installing requests module')
    os.system('pip install requests')
try:
    import tkinter
    from tkinter import *
    from tkinter import messagebox
    from tkinter.ttk import *
except:
    print('Installing Tkinter module ')
    os.system('pip install tk')
    import tkinter
    from tkinter import messagebox
    from tkinter import *
    from tkinter.ttk import *

try:
    import psutil
except:
    print('Installing psutil module ')
    os.system('pip install psutil')
    import psutil

import math,random,os

try:
    import win32gui, win32con
except:
    print('Installing win32gui')
    os.system('pip install win32gui')
    print('Installing pywin32')
    os.system('pip install pywin32')
    import win32gui, win32con
try:
    import pygame
    from pygame import *
    mixer.init()
    mixer.music.set_volume(0.4)
except:
    print('Installing pygame Module')
    os.system('pip install pygame')
    from pygame import *
    import pygame
    mixer.init()
    mixer.music.set_volume(0.4)

try:
    from PIL import ImageTk, Image
except:
    print('Installing PIL module')
    os.system('pip install Pillow')
    from PIL import ImageTk, Image


try:
    import win32api
except:
    print('Installing win32api module')
    os.system('pip install win32api')
    import win32api
try:
    import pyttsx3
except:
    print('Installing pyttsx3 module')
    os.system('pip install pyttsx3')
    import pyttsx3
from time import *
try:
    import win32com.client
except:
    print('Installing win32com.client')
    os.system('pip install pypiwin32')
    import win32com.client
try:
    import winsound
except:
    print('Installing winsound module')
    os.system('pip install winsound')
try:
    import webbrowser
except:
    print('Installing Webbrowser module')
    os.system('pip install webbrowser')
    import webbrowser
import customtkinter
import datetime
from datetime import date



####################### Getting user Information #####################
def getting_user_info():
    global city
    try:# location finder in try
        ipAdd = requests.get('https://api.ipify.org').text
        print("Extracting Data from IP")
        print(ipAdd)
        print("Accessing Geo data")
        url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
        geo_requests = requests.get(url)
        geo_data = geo_requests.json()
        city = geo_data['city']
        # print(geo_data)
        country = geo_data['country']
        my_current_location = city,country
    except:# location error
        print('Unable to get location')
        country = 'Error'
        city = 'Error'
        my_current_location = "Error"

# getting_user_info()
#######################################################################


##################### DATA ###########################
button_sound = 'button_sound.mp3'
######################################################


def speak(audio):
    try:
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[0].id)
        engine.setProperty('rate',170)
        print(f"Toggle: ",audio)
        engine.say(audio)
        engine.runAndWait()
    except:
        try:
            import win32com.client
            # Calling the Disptach method of the module which
            # interact with Microsoft Speech SDK to speak
            # the given input from the keyboard
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak(audio)
        except:
            print('')
            print('Could not speak , tried my best ..Apologies for that')
            try:
                winsound.Beep(797,900)
                winsound.Beep(797,900)
                winsound.Beep(797,900)
                winsound.Beep(797,900)
            except:
                print('Serious Code error ...')


def internet_connectivity_():
    url = "http://www.youtube.com/hobbymaster_real" 
    # My youtube channel , consider subscribering thank you 😀
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        print("Connected to the Internet")
        speak("INTERNET connection detected")
        speak("all systems have been activated")
      
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection  ")
        speak("No internet connection detected .")
        speak("Shutting down the program.")
        win32api.MessageBox(0, 'you are not connected to internet , please make sure you connected to wi-fi or internet to start  program', 'ALERT !')
        messagebox.askretrycancel("Warning", "No internet connection detected ,Try again?")
        speak("Thanks for giving me your time")
        exit()



def weather_reports_from_menu():
             
    try:
        mixer.music.load(button_sound)
        mixer.music.play()
    except:
        print('Could not play audio , playsound module error, please re-install')

    try:
        api_key = "fa5aab4feceb62541bf13bfa84259779"

        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        # city_name = 'jodhpur'
        city_name = city

        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        response = requests.get(complete_url)

        x = response.json()

        if x["cod"] != "404":

            y = x["main"]

            current_temperature = y["temp"]

            current_pressure = y["pressure"]

            current_humidity = y["humidity"]

            z = x["weather"]

            weather_description = z[0]["description"]
            temperature = round(float(float(current_temperature)-273.15)),"°C"
            pressure = round(float(current_pressure*0.000987)),"atm"
            humidity = current_humidity,"%"
            weather_description = z[0]["description"]
            description = weather_description

            print(" Temperature (in kelvin unit) = " +
                            str(current_temperature) +
                "\n atmospheric pressure (in hPa unit) = " +
                            str(current_pressure) +
                "\n humidity (in percentage) = " +
                            str(current_humidity) +
                "\n description = " +
                            str(weather_description))

        temp___ = str(temperature)
        text_weather_display = 'Temperature in '+str(city_name)+ ' is '+str(temperature)+', '+ ', '+ 'Humidity is '+str(humidity)+' , '+'sky description is ' +str(description)
        text_weather_display = text_weather_display.replace('(','')
        text_weather_display = text_weather_display.replace(')','')
        text_weather_display = text_weather_display.replace(',','')
        text_weather_display = text_weather_display.replace("'",'')
        text_weather_display = text_weather_display.replace('"','')
        win32api.MessageBox(0, text_weather_display, 'Weather Reports ')
            
    except:
        print("Getting errors")
        weather_description = "Error"
        temperature = "Error"
        pressure = "Error"
        humidity = "Error"
        weather_description = "Error"
        description = "Error"

    else:
        print(" ")


def system_restart():
        
    try:
        mixer.music.load(button_sound)
        mixer.music.play()
    except:
        print('Could not play audio , playsound module error, please re-install')

    win32api.MessageBox(0, "Program will automatically restart , please don't use mouse or keyboard until the program restarts.", 'Info')
    os.startfile('restart_code.py')
    exit()

try:
    mixer.music.load('try3.mp3')
    mixer.music.play()
except:
    print('Could not play audio , playsound module error, please re-install')

main_bg_color = '#31717E'
main_screen = tkinter.Tk()
main_screen.configure(background=main_bg_color)
main_screen.title('Toggle')
main_screen.iconbitmap('logo.ico')
main_screen.attributes('-fullscreen',True)



def sign_in():
        
    try:
        mixer.music.load(button_sound)
        mixer.music.play()
    except:
        print('Could not play audio , playsound module error, please re-install')

    main_screen.destroy()
    sleep(1)
    os.system('python signin.py')
    exit()

def log_in():
         
    try:
        mixer.music.load(button_sound)
        mixer.music.play()
    except:
        print('Could not play audio , playsound module error, please re-install')

    main_screen.destroy()
    sleep(1)
    os.system('python login.py')
    exit()


def contact():
         
    try:
        mixer.music.load(button_sound)
        mixer.music.play()
    except:
        print('Could not play audio , playsound module error, please re-install')

    win32api.MessageBox(0, 'Contact no. 9502943646 ,email address : syedadnanali0106@gmail.com', 'Contact !')




log_in_btn = customtkinter.CTkButton(main_screen,text='Already have an account\nLogin',text_font=("Forte",23),border_color='white',command=log_in,hover_color='green',fg_color=main_bg_color)
log_in_btn.place(relx=0.7,rely=0.04)
today = date.today()

current_time = datetime.datetime.now()


month__ = datetime.datetime.now()
Month= str(month__.strftime("%B"))
DAY = str(current_time.day)
YEAR = str(current_time.year)



varr = "{}".format(YEAR)
Wel = Label(main_screen,text='Toggle',font=("hooge 05_54",70))
Wel.config(background=main_bg_color,foreground='yellow')
Wel.place(relx=0.01,rely=0.02)

n = Label(main_screen,text='Manage your time\neffectively with Toggle and\nimprove daily.',font=("Matura MT Script Capitals",36))
n.config(background=main_bg_color,foreground='white')
n.place(relx=0.01,rely=0.4)

DATE = "{} {}\n  {}".format(DAY,Month,YEAR)

dateee = Label(main_screen,text=DATE,font=("Forte",28))
dateee.config(background=main_bg_color,foreground='white')
dateee.place(relx=0.01,rely=0.9)


canvas= Canvas(main_screen, width= 700, height= 500)
canvas.place(relx=0.5,rely=0.3)
img= ImageTk.PhotoImage(Image.open("time.png"))
canvas.create_image(10,10,anchor=NW,image=img)


get_start = customtkinter.CTkButton(main_screen,
                                                text="Get Started",text_font=("Forte",28),
                                                border_width=2,  # <- custom border_width
                                                fg_color=main_bg_color,  # <- no fg_color
                                                command=sign_in,hover_color='green')
get_start.place(relx=0.25,rely=0.6)

##############################################


task_bar_type_menusbar = Menu(main_screen)

welcome_Toggle_button = Menu(task_bar_type_menusbar, tearoff = 0)

task_bar_type_menusbar.add_cascade(label ='☰    ',font=('Roboto Medium',50), menu = welcome_Toggle_button)
welcome_Toggle_button.add_command(label ='Get weather reports', command = weather_reports_from_menu)
welcome_Toggle_button.add_separator()

login_options = Menu(task_bar_type_menusbar, tearoff = 0)
task_bar_type_menusbar.add_cascade(label ='Old user',font=('Roboto Medium',50), menu = login_options ,command=None )
login_options.add_command(label ='login', command = log_in)
login_options.add_separator()

signin_options = Menu(task_bar_type_menusbar, tearoff = 0)
task_bar_type_menusbar.add_cascade(label ='New user',font=('Roboto Medium',50), menu = signin_options ,command=None )
signin_options.add_command(label ='signin', command = sign_in)
signin_options.add_separator()

power_options = Menu(task_bar_type_menusbar, tearoff = 0)
task_bar_type_menusbar.add_cascade(label ='power options',font=('Roboto Medium',50), menu = power_options ,command=exit )
power_options.add_command(label ='Exit', command = exit)
power_options.add_command(label ='Restart', command = system_restart)
power_options.add_separator()


def contact():
    win32api.MessageBox(0, 'Let us know your query at syedadnanali0106@gmail.com', 'Contact !')



help_options = Menu(task_bar_type_menusbar, tearoff = 0)
task_bar_type_menusbar.add_cascade(label ='Help', menu = help_options ,command=exit )
help_options.add_command(label ='Contact', command = contact)
help_options.add_separator()

main_screen.config(menu=task_bar_type_menusbar)


######################################### System Information #############################
System_name = "TOGGLE" #  
System_Coder = owner_of_the_program = "Adnan"
##########################################################################################






main_screen.mainloop()

