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
import mysql.connector as database




def time_table_generator():
    def get_check(CLASS,EXAM,STREaM,cid):
        CLASS = int(CLASS)
        from datetime import date
            
        # Set the exam date
        exam_year = 2023
        exam_month = 2
        exam_day = 15
        exam_date = date(exam_year, exam_month, exam_day)
        current_time = datetime.datetime.now()
        # Calculate the number of days left until the exam
        current_date = date.today()
        days_left = exam_date - current_date
        productive_hours = 8
        no_days_left = days_left.days
        hours_left = productive_hours*no_days_left
        print("hours left",hours_left)
        if CLASS == 12 and EXAM == "CBSE" and STREaM == "s":#science
            n_chem_syllabus = 10 
            n_phy_syllabus = 14
            n__math_syllabus = 13
            n_CS_syllabus = 9
            n_english_syllabus = 19
            ### chapter coverage ###
            # Chemistry Time per chapter per day 
            n_hour_per_chapter_chem_theory = 1
            n_hour_per_chapter_chem_practice = 2
            per_day_chem = n_hour_per_chapter_chem_practice + n_hour_per_chapter_chem_theory
            # Physics Time per chapter per day 
            n_hour_per_chapter_phy_revise = 1
            n_hour_per_chapter_phy_practice = 2
            per_day_phy = n_hour_per_chapter_phy_practice + n_hour_per_chapter_phy_revise
            # English Time per chapter per day 
            n_hour_per_chapter_eng_chapter_summanry = 1
            n_hour_per_chapter_eng_practice = 2
            per_day_eng = n_hour_per_chapter_eng_chapter_summanry + n_hour_per_chapter_eng_practice

            # CS Time per chapter per day 
            n_hour_per_chapter_CS_chapter_summary = 1
            n_hour_per_chapter_CS_practice = 2
            per_day_CS = n_hour_per_chapter_CS_chapter_summary + n_hour_per_chapter_CS_practice

            # Math Time per chapter per day 
            n_hour_per_chapter_Maths_formula_revision = 0.5
            n_hour_per_chapter_Maths_practice = 2.5
            per_day_math = n_hour_per_chapter_Maths_practice + n_hour_per_chapter_Maths_formula_revision
            # Total time required 
            total_time_required = int(((n_chem_syllabus)*(per_day_chem)) +((n__math_syllabus)*(per_day_math)) +((n_phy_syllabus)*(per_day_phy)) +((n_CS_syllabus)*(per_day_CS)) +((n_english_syllabus)*(per_day_eng)) )
            print(total_time_required)
            # per day coverage 
            subjects_coverage = [per_day_chem,per_day_CS,per_day_eng,per_day_math,per_day_phy]
            SUBJECTS = ['PHYSICS','CHEMISTRY','MATHEMATICS','ENGLISH','COMPUTER SCIENCE']
            # for subjects in SUBJECTS:
                # print(subjects)
            per_day_study_compulsory = ['MATHEMATICS','PHYSICS'] # MATH and PHYSICS complete time and CS 1 hr and english 1 hr and next day chemistry 2 hr 
            per_study_left = ["CHEMISTRY","ENGLISH","COMPUTER SCIENCE"]
            file_c_id = "plan of customer with ID {}.txt".format(cid)
            with open(file_c_id,'a') as plan_intro_maker:
                plan_intro_maker.write("Study According to this plan\n\nMaths formula revision = 0.5hr and Math Practice = 2.5hr\nPhysics theory and formula revision for 1 hr and 2hr practice \nEnglish and Computer Science revise theory for 1 hr and practice 2hr\n\n")
            count = 1
            print("days left",days_left.days)
            for i in range(days_left.days):    
                # global count
                for a,b in zip(per_day_study_compulsory,per_study_left):
                    if count>days_left.days:
                        break
                    data_print = "Day{}\nSubject 1: {}\nSubject 2: {}\nTake breaks of 30 mins after every 3 hours\n\n".format(count,a,b)
                    with open(file_c_id,'a') as plan_maker:
                        plan_maker.write(data_print)
                        # print(type(data_print))
                    count += 1
            print(count)

    get_check(12,"CBSE",'s',1)
    messagebox.showinfo("Info","Your Time Table is Generated please check in this folder")




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

getting_user_info()
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
        try:
            mixer.music.load('try3.mp3')
            mixer.music.play()
        except:
            print('Could not play audio , playsound module error, please re-install')
        win32api.MessageBox(0, text_weather_display, 'Weather Reports ')

            
    except:
        speak("unable to get weather reports")
        try:
            mixer.music.load('try3.mp3')
            mixer.music.play()
        except:
            print('Could not play audio , playsound module error, please re-install')

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




with open('mysql_password.txt','r') as passwrd_read:
    PASSWORD_SQL = passwrd_read.read()
DATABASE = database.connect(host='localhost',user='root',passwd=PASSWORD_SQL)

if DATABASE.is_connected():

    global C_ID
    with open('ID.txt','r') as ID_READER:   
        C_ID = ID_READER.read()
        print(C_ID)
        print("System Connected to database..")
        with open('ID.txt','w') as ID_writerrr:
            try:
                os.close(ID_writerrr)
                os.remove('ID.dat')
            except:
                ID_writerrr.truncate()
    global data
    cust_directory = 'customers/cust{}.txt'.format(C_ID)
    with open(cust_directory,'a+') as READER:
        READER.seek(0)
        data = READER.read()
else:
        print("System cannot connect to database")

cursor_use = DATABASE.cursor()
cursor_use.execute("use togle")




try:
    mixer.music.load('try3.mp3')
    mixer.music.play(loops=10)
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

def log_out():
         
    try:
        mixer.music.load(button_sound)
        mixer.music.play()
    except:
        print('Could not play audio , playsound module error, please re-install')

    main_screen.destroy()
    sleep(1)
    os.system('python main.py')
    exit()


def contact():
         
    try:
        mixer.music.load(button_sound)
        mixer.music.play()
    except:
        print('Could not play audio , playsound module error, please re-install')

    win32api.MessageBox(0, 'Contact no. 9502943646 ,email address : syedadnanali0106@gmail.com', 'Contact !')




log_in_btn = customtkinter.CTkButton(main_screen,text='Logout',text_font=("Arial",20),border_color='white',command=log_out,hover_color='green',fg_color=main_bg_color)
log_in_btn.place(relx=0.8,rely=0.06)
today = date.today()

current_time = datetime.datetime.now()


month__ = datetime.datetime.now()
Month= str(month__.strftime("%B"))
DAY = str(current_time.day)
YEAR = str(current_time.year)


# varr = "{}".format(YEAR)
Wel = Label(main_screen,text='Toggle',font=("hooge 05_54",70))
Wel.config(background=main_bg_color,foreground='yellow')
Wel.place(relx=0.01,rely=0.02)

n = Label(main_screen,text='Your Profile',font=("Matura MT Script Capitals",36))
n.config(background=main_bg_color,foreground='magenta')
n.place(relx=0.02,rely=0.23)


def drink(bMi,age,gender):
    # from datetime import datetime
    # noww = datetime.now()
    # hour = noww.hour
    # minute = noww.minute
    # second = noww.second
    # print('Time is now\n',hour,':',minute,':',second)
    messagebox.showinfo('Info',"You must drink water after every 3 hours to be hydrated.")
    # if age > 1 and age < 4:
    #     water_cups = 4
    #     water_drink_time_after_must = 'You must drink water after every {} hours to be hydrated.'.format(24/water_cups)
    #     print('Info: ',water_drink_time_after_must)
    #     messagebox.showinfo('show info',water_drink_time_after_must)
    # elif age > 3 and age < 9:
    #     water_cups = 5
    #     water_drink_time_after_must = 'You must drink water after every {} hours to be hydrated.'.format(24/water_cups)
    #     print('Info: ',water_drink_time_after_must)
    #     messagebox.showinfo('show info',water_drink_time_after_must)
    # elif age >10  and age < 14 :
    #     water_cups = 6
    #     water_drink_time_after_must = 'You must drink water after every {} hours to be hydrated.'.format(24/water_cups)
    #     print('Info: ',water_drink_time_after_must)
    #     messagebox.showinfo('show info',water_drink_time_after_must)
    # elif age > 15 and age < 18 and gender == 'm':
    #     water_cups = 8
    #     water_drink_time_after_must = 'You must drink water after every {} hours to be hydrated.'.format(24/water_cups)
    #     print('Info: ',water_drink_time_after_must)
    #     messagebox.showinfo('show info',water_drink_time_after_must)
    # elif age > 15 and age < 18 and gender == 'f':
    #     water_cups = 7
    #     water_drink_time_after_must = 'You must drink water after every {} hours to be hydrated.'.format(24/water_cups)
    #     print('Info: ',water_drink_time_after_must)
    #     messagebox.showinfo('show info',water_drink_time_after_must)
    # elif age > 17:
    #     water_cups = 10
    #     water_drink_time_after_must = 'You must drink water after every {} hours to be hydrated.'.format(24/water_cups)
    #     print('Info: ',water_drink_time_after_must)
    #     messagebox.showinfo('show info',water_drink_time_after_must)

    

    print()


def male_logo():              
    image1 = Image.open("M.png")
    test = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(image=test)
    label1.image = test
    label1.config(background=main_bg_color)
    label1.place(relx=0.9,rely=0.04)

def female_logo():              
    image1 = Image.open("F.png")
    test = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(image=test)
    label1.image = test
    label1.config(background=main_bg_color)
    label1.place(relx=0.9,rely=0.04)

for i in range(len(data)):
    global bmi_got
    global age
    if 'male' in data[i]:
        gender = 'm'
        male_logo()
    elif 'female' in data[i]:
        gender = 'f'
        female_logo()
    elif 'BMI: ' in data[i]:
        bmi_get = data[i]
        res = [int(i) for i in bmi_get.split() if i.isdigit()]
        res = str(res)
        res = res.replace('[','')
        res = res.replace(']','')
        res = res.replace(' ','')
        bmi_got = float(res.replace(',',''))
    elif 'Age: ' in data[i]:
        age = data[i]
        age = age.replace('Age: ','')
        Age = int(age)

    else:
        male_logo()

def hydrate():
    Bmi = 0
    global aGe
    global gEnDer
    gEnDer = ''
    aGe = 0
    for i in range(len(data)):
        global bmi_got
        global age
        if 'male' in data[i]:
            gEnDer += 'm'
            male_logo()
        elif 'female' in data[i]:
            gEnDer += 'f'
            female_logo()
        elif 'BMI: ' in data[i]:
            bmi_get = data[i]
            res = [int(i) for i in bmi_get.split() if i.isdigit()]
            res = str(res)
            res = res.replace('[','')
            res = res.replace(']','')
            res = res.replace(' ','')
            bmi_got = float(res.replace(',',''))
            Bmi += bmi_got
        elif 'Age: ' in data[i]:
            age = data[i]
            age = age.replace('Age: ','')
            Age = int(age)
            aGe += Age
    drink(bMi=Bmi,age=aGe,gender=gEnDer)

def generate_time_table():
    print()
    



d = Label(main_screen,text=data,font=("Arial",26))
d.config(background=main_bg_color,foreground='cyan')
d.place(relx=0.02,rely=0.32)

DATE = "{} {} {}".format(DAY,Month,YEAR)

dateee = Label(main_screen,text=DATE,font=("Forte",28))
dateee.config(background=main_bg_color,foreground='white')
dateee.place(relx=0.8,rely=0.94)


canvas= Canvas(main_screen, width= 700, height= 500)
canvas.place(relx=0.5,rely=0.3)
img= ImageTk.PhotoImage(Image.open("time.png"))
canvas.create_image(10,10,anchor=NW,image=img)
# canvas.create_text(0,0,text='Tips to be healty')




##############################################


task_bar_type_menusbar = Menu(main_screen)

welcome_Toggle_button = Menu(task_bar_type_menusbar, tearoff = 0)

task_bar_type_menusbar.add_cascade(label ='☰    ',font=('Roboto Medium',50), menu = welcome_Toggle_button)
welcome_Toggle_button.add_command(label ='Get weather reports', command = weather_reports_from_menu)
welcome_Toggle_button.add_separator()
welcome_Toggle_button.add_command(label ='Hydrated status', command = hydrate)
welcome_Toggle_button.add_command(label ='Generate Time Table', command = time_table_generator)
welcome_Toggle_button.add_separator()

power_options = Menu(task_bar_type_menusbar, tearoff = 0)
task_bar_type_menusbar.add_cascade(label ='power options',font=('Roboto Medium',50), menu = power_options ,command=exit )
power_options.add_command(label ='Exit', command = exit)
power_options.add_command(label ='Restart', command = system_restart)
power_options.add_separator()


def contact():
    win32api.MessageBox(0, 'Let us know your query at syedadnanali0106@gmail.com', 'Contact !')




# drink(bMi=19,age=17,gender='m')

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

