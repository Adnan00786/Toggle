import os
import tkinter
import logging
from tkinter import *
from tkinter import messagebox
from random import *
from time import sleep
from datetime import date
import sys
import pyautogui
import mysql.connector as database
import customtkinter  # <- import the CustomTkinter module
try:
    import pyttsx3
except:
    print('Installing pyttsx3 module')
    os.system('pip install pyttsx3')
    import pyttsx3
try:
    import winsound
except:
    print('Installing winsound module')
    os.system('pip install winsound')



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



def cust_data_inputs_(CUST_NAME,CUST_ID,CUST_GENDER,CUST_AGE,CUST_WEIGHT,CUST_MAIL_ID,CUST_HEIGHT,BMI,BMI_st):
    CUST_AGE = str(CUST_AGE)
    CUST_ID = str(CUST_ID)
    CUST_HEIGHT = str(CUST_HEIGHT)
    CUST_WEIGHT = str(CUST_WEIGHT)
    BMI = str(BMI)
    CUSTOMERS__DIRECTORY = ('customers/cust{}.txt').format(CUST_ID)
    with open(CUSTOMERS__DIRECTORY,'a') as cust01_data:
        cust01_data.write('Customer details\n')
        cust01_data.write('Name: ')
        cust01_data.write(CUST_NAME)
        cust01_data.write('\n')

        cust01_data.write('Customer ID: ')
        cust01_data.write(CUST_ID)
        cust01_data.write('\n')

        CUST_GENDER = CUST_GENDER.lower()
        if CUST_GENDER == 'm':
            CUST_GENDER = 'Male'
        elif CUST_GENDER == "f":
            CUST_GENDER = "Female"
        

        cust01_data.write('Gender: ')
        cust01_data.write(CUST_GENDER)
        cust01_data.write('\n')

        cust01_data.write('Age: ')
        cust01_data.write(CUST_AGE)
        cust01_data.write('\n')

        cust01_data.write('Weight: ')
        cust01_data.write(CUST_WEIGHT)
        cust01_data.write(' Kg')
        cust01_data.write('\n')

        cust01_data.write('Height: ')
        cust01_data.write(CUST_HEIGHT)
        cust01_data.write(' Cms')
        cust01_data.write('\n')

        cust01_data.write('Email: ')
        cust01_data.write(CUST_MAIL_ID)
        cust01_data.write('\n')

        cust01_data.write('BMI: ')
        cust01_data.write(BMI)
        cust01_data.write('(')
        cust01_data.write(BMI_st)
        cust01_data.write(')')
        cust01_data.write('\n')



with open('mysql_password.txt','r') as passwrd_read:
    PASSWORD_SQL = passwrd_read.read()

DATABASE = database.connect(host='localhost',user='root',passwd=PASSWORD_SQL)

if DATABASE.is_connected():
        print("System Connected to database..")
else:
        print("System cannot connect to database")

cursor_use = DATABASE.cursor()
cursor_use.execute("use togle")


window_tk = customtkinter.CTk()  # create CTk window like you do with the Tk window
window_tk.geometry("400x240")
window_tk.title("Toggle-sign in")
window_tk.iconbitmap(r'logo.ico')
customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("System")


def quit_homepage():
        
    global LOG

    LOG = logging.getLogger(__name__)
    LOG.setLevel(logging.DEBUG)

    LOG.debug("- Quit Homepage -")

    global app
    
    # Quit Homepage
    app.destroy()

name_var = StringVar()
gen_var = StringVar()
birth_var = StringVar()
pass_var = StringVar()
email_var = StringVar()
weight_var = StringVar()
height_var = StringVar()


def password_approval(PASSWD):
    aproval = False
    LEN_PASS = len(PASSWD)
    global approval
    SPECIAL_CHARACTERS = ['!','@','#','$','^','&','*']
    for chr in SPECIAL_CHARACTERS:
        if chr in PASSWD and LEN_PASS==8 and '&' not in PASSWD:
            print("approved")
            aproval = True
        else:
            continue
    if aproval == False:
        print("Password rejected")
    
    return aproval


def old_user_():
    app.destroy()
    os.system('python login.py')

class Login_app(customtkinter.CTk):
    
    WIDTH = 900
    HEIGHT = 550

    def __init__(self):
        super().__init__()
            # exit()

        
       

        self.title("Toggle-Signin")
        self.resizable(width=False, height=False)
        self.geometry(f"{Login_app.WIDTH}x{Login_app.HEIGHT}")
        self.iconbitmap('logo.ico')
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        speak("Sign in to proceed")
######### Frames ######################################################################
        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing
##########################################################################################

#######  Label & Button ##################################################################
        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Sign in Window",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Old User Log-in",
                                                command=old_user_)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)
##########################################################################################




###### Name Entry &  Label ################## 
        self.name_label = customtkinter.CTkLabel(master=self.frame_right, text = 'Username', text_font=('calibre',10, 'bold'))
        self.name_label.grid(row=1, column=0, pady=10, padx=10)


        self.name_entry = customtkinter.CTkEntry(master=self.frame_right,show='',placeholder_text="Enter name",textvariable = name_var, text_font=('calibre',10,'normal'))
        self.name_entry.grid(row=1, column=2, columnspan=4, pady=20, padx=20, sticky="we")
        # text = self.name_entry.get()
        # print(text)
#############################################

###### Gender Entry &  Label ################## 
        self.Gender_label = customtkinter.CTkLabel(master=self.frame_right, text = 'Enter your Gender', text_font = ('calibre',10,'bold'))

        self.Gender_label.grid(row=2, column=0, pady=10, padx=10)

        self.Gender_entry=customtkinter.CTkEntry(master=self.frame_right,placeholder_text="Enter Gender M Or F", textvariable = gen_var, text_font = ('calibre',10,'normal'))

        self.Gender_entry.grid(row=2, column=2, columnspan=4, pady=20, padx=20, sticky="we")

#############################################

###### Birth Entry &  Label & Submit button ################## 
        self.birth_label = customtkinter.CTkLabel(master=self.frame_right, text = 'Enter birth year', text_font = ('calibre',10,'bold'))

        self.birth_label.grid(row=3, column=0, pady=10, padx=10)

        self.birth_entry=customtkinter.CTkEntry(master=self.frame_right,placeholder_text="YYYY", textvariable = birth_var, text_font = ('calibre',10,'normal'))

        self.birth_entry.grid(row=3, column=2, columnspan=4, pady=20, padx=20, sticky="we")
#############################################

###### passsword Entry &  Label & Submit button ################## 
        self.pass_label = customtkinter.CTkLabel(master=self.frame_right, text = 'Create Strong 8 \nelements Password', text_font = ('calibre',10,'bold'))

        self.pass_label.grid(row=8, column=0, pady=10, padx=10)
        # show_text = '*'
        def cmd():
                if self.pass_entry.get() :
                        print('Checkbox 1 selected')
                        show_text = ''
                        self.pass_entry.configure(show=show_text)
                else :
                        show_text = '*'
                        self.pass_entry.configure(show=show_text)
                        print('Checkbox 1 unselected')

                
        self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_right,
                                                     text="Show Password",command=cmd)
        self.check_box_2.grid(row=8, column=7, pady=10, padx=20, sticky="w")
        self.pass_entry = customtkinter.CTkEntry(master=self.frame_right,placeholder_text="password",textvariable=pass_var,show='*',  text_font = ('calibre',10,'normal'))
        self.pass_entry.grid(row=8, column=2, columnspan=4, pady=20, padx=20, sticky="we")


###### email number Entry &  Label & Submit button ################## 
        self.email_label = customtkinter.CTkLabel(master=self.frame_right, text = 'Enter Email_id', text_font = ('calibre',10,'bold'))

        self.email_label.grid(row=6, column=0, pady=10, padx=10)

        self.email_entry=customtkinter.CTkEntry(master=self.frame_right,placeholder_text="email",textvariable=email_var, text_font = ('calibre',10,'normal'))

        self.email_entry.grid(row=6, column=2, columnspan=4, pady=20, padx=20, sticky="we")
#############################################


###### height Entry &  Label & Submit button ################## 
        self.height_label = customtkinter.CTkLabel(master=self.frame_right, text = 'Enter your height\n(in cms)', text_font = ('calibre',10,'bold'))

        self.height_label.grid(row=7, column=0, pady=10, padx=10)

        self.height_entry=customtkinter.CTkEntry(master=self.frame_right,placeholder_text="height", textvariable=height_var,text_font = ('calibre',10,'normal'))

        self.height_entry.grid(row=7, column=2, columnspan=4, pady=20, padx=20, sticky="we")
#############################################

###### weight Entry &  Label & Submit button ################## 
        self.weight_label = customtkinter.CTkLabel(master=self.frame_right, text = 'Enter your weight\n(in Kg)', text_font = ('calibre',10,'bold'))

        self.weight_label.grid(row=4, column=0, pady=10, padx=10)

        self.weight_entry=customtkinter.CTkEntry(master=self.frame_right,placeholder_text="weight", textvariable=weight_var,text_font = ('calibre',10,'normal'))

        self.weight_entry.grid(row=4, column=2, columnspan=4, pady=20, padx=20, sticky="we")
#############################################


################################ submit button ############################################################

        self.button_s = customtkinter.CTkButton(master=self.frame_right,text = 'Submit', command = self.submit)
        self.button_s.grid(row=9, column=9)

###########################################################################################################

################################ Modes ############################################################

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Dark", "Light", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")


###########################################################################################################
    def submit(self):
        username = str(self.name_entry.get())
        weight = self.weight_entry.get()
        gender__= str(self.Gender_entry.get())
        password = str(self.pass_entry.get())
        birth = self.birth_entry.get()
        height = self.height_entry.get()
        email = str(self.email_entry.get())

        if len(gender__) == 1:
                print()
        else:
                messagebox.showerror("Error", "Please Enter 'M' for Male and 'F' for Female")
                quit_homepage()
                speak('Wrong credentials Provided, Sign in again')
                os.system('python signin.py')

        def isfloat(num):
                try:
                        float(num)
                        return True 
                except ValueError:
                        return False

        if birth.isnumeric():
                print()
                try:
                        birth = int(birth)
                except:
                        messagebox.showerror("Error", "Please enter Birth-year in numbers")
                        quit_homepage()
                        speak('Wrong credentials Provided, Sign in again')
                        os.system('python signin.py')

        else:   
                messagebox.showerror("Error", "Please enter Birth-year in numbers")
                quit_homepage()
                speak('Wrong credentials Provided, Sign in again')
                os.system('python signin.py')

        
        if isfloat(weight) :
                weight = float(weight)
                print()
        else:
                messagebox.showerror("Error", "Please enter weight in numbers")
                quit_homepage()
                speak('Wrong credentials Provided, Sign in again')
                os.system('python signin.py')

        

        if '@' in email and '.' in email:
                print()
        else:
                speak("Please Input valid email address")
                messagebox.showerror("Error", "Please Input valid email address")
                quit_homepage()
                speak('Wrong credentials Provided, Sign in again')
                os.system('python signin.py')


        if isfloat(height):
                height = float(height)
                print()
        else:
                messagebox.showerror("Error", "Please enter height in numbers")
                quit_homepage()
                speak('Wrong credentials Provided, Sign in again')
                os.system('python signin.py')

        if password_approval(PASSWD=password) and '& in ':
                print()
        else:
                speak("Please Create 8 element strong password and use speacial character and don't use & in password")
                messagebox.showerror("Error", "Please Create 8 element strong password and use speacial character with ['!' , '@' , '#' , '$' , '^' , '&' , '*']\n and don't use & in password ")
                quit_homepage()
                speak('Wrong credentials Provided, Sign in again')
                os.system('python signin.py')



        BIRTH = int(birth)
        CURRENT_YEAR = date.today().year
        cust_age = int(CURRENT_YEAR - BIRTH)

        # details = {"name":name,"Gender":gender__,"Birth-year":birth,"Age":cust_age}
        # enter_details = "Insert into customers(cust_name,cust_pass,cust_gender,cust_birth_date,cust_Weight,cust_email,cust_height,cust_age) values(%s,%s,%s,%s,%s,%s,%s,%s)"%(name,password,gender__,birth,weight,email,height,cust_age)
        # enter_details = "Insert into customers(cust_name,cust_pass,cust_gender,cust_birth_date,cust_Weight,cust_email,cust_height,cust_age) values(%s,%s,%s,%d,%d,%s,%d,%d);"%(name,password,gender__,birth,weight,email,height,cust_age)
        enter_details = "Insert into customers(cust_name,cust_pass,cust_gender,cust_birth_date,cust_Weight,cust_email,cust_height,cust_age) values('{}','{}','{}','{}','{}','{}','{}','{}');".format(username,password,gender__,birth,weight,email,height,cust_age)

        BMI__ = round((weight)/((height/100)**2),2)

        if BMI__ < 18.5:
                BMI_status = "underweight"
        elif BMI__ > 18.5 and BMI__ < 24.9:
                BMI_status = 'Healthy weight'
        elif BMI__ > 24.9 and BMI__ < 30.0:
                BMI_status = 'overweight'
        elif BMI__ > 30.0:
                BMI_status = 'Obesity'



        def GETT_ID(p,b):
                global ID
                try:
                        get_cust_id = "select cust_id from customers where cust_pass like '{}%' and cust_birth_date like '{}%';".format(p,b)
                        cursor_use.execute(get_cust_id)
                        ID = cursor_use.fetchall()
                        ID = str(ID)
                        ID = ID.replace('(','')
                        ID = ID.replace(')','')
                        ID = ID.replace(']','')
                        ID = ID.replace('[','')
                        ID = ID.replace(',','')
                        print("Your CUSTOMER ID is: ",ID)
                except:
                        pass

                
        def ID_wRITER(iD):
                with open('ID.txt','a') as ID_WRITER:
                        iD = str(iD)
                        ID_WRITER.write(iD)


        try:
                cursor_use.execute(enter_details)
                DATABASE.commit()
                speak("Sign in successful")
                print("Data stored in Toggle-database")
                GETT_ID(p=password,b=birth)
                ID_wRITER(iD=ID)
                T_D = "Your Customer ID is {}, Remember it while logging in".format(ID)
                messagebox.showinfo("Info", T_D)
                cust_data_inputs_(CUST_ID=ID,CUST_NAME=username,CUST_AGE=cust_age,CUST_GENDER=gender__,CUST_HEIGHT=height,CUST_WEIGHT=weight,CUST_MAIL_ID=email,BMI=BMI__,BMI_st=BMI_status)
                self.on_closing()
                sign_success_getting(username)
        except Exception as e:
                print(e)

    
    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    
    def on_closing(self, event=0):
        self.destroy()



def sign_success_getting(name_of_user):
        with open('customer_signin.txt','w') as write_user:
                write_user.write(name_of_user)
        sleep(2)

        os.system('python sign_in_success.py')



if __name__ == "__main__":
    app = Login_app()
    app.mainloop()

