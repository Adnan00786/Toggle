import logging
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

# Import Libraries
import os
from time import sleep
import sys
import logging
import datetime

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
    import pyttsx3
except:
    print('Installing pyttsx3 module')
    os.system('pip install pyttsx3')
    import pyttsx3    

# Tkinter
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import messagebox
from tkinter import ttk
try:
    import winsound
except:
    print('Installing winsound module')
    os.system('pip install winsound')
# CustomTkinter
import customtkinter # pip install customtkinter
customtkinter.set_appearance_mode("dark")

# Resolution
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

# Image Library
from PIL import Image, ImageTk # pip install Pillow

# - Global Variables - #
LOG = ""

# Tkinter Varibles
ROOT = customtkinter.CTk()
ROOT.iconbitmap(r'logo.ico')
TKINTER_WIDGETS = {}
APP_WIDTH = 380
APP_HEIGHT = 430

# Current Script Name
CURRENT_SCRIPT_NAME = os.path.basename(__file__).split('.')[0]

# Directories
CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
CONFIG_DIRECTORY = os.path.join(CURRENT_DIRECTORY, "Config")
IMAGES_DIRECTORY = os.path.join(CONFIG_DIRECTORY, "Images")
LOGS_DIRECTORY = os.path.join(CURRENT_DIRECTORY, "Logs")


with open('mysql_password.txt','r') as passwrd_read:
    PASSWORD_SQL = passwrd_read.read()

# SQL CONNECTOR ##############################################
import mysql.connector as DATABASE
try:
    use_db = DATABASE.connect(host='localhost',user='root',passwd=PASSWORD_SQL)
    cur_use = use_db.cursor(buffered=True)
    cur_use.execute("use togle;")
    print("Connected to database")
    cur_use.execute("SELECT * from customers")
    row_count = cur_use.rowcount
except:
    logging.critical("CRITICAL MESSAGE: Unable to connect to Database")
    logging.critical("CRITICAL MESSAGE: Can't Login now")
    logging.critical("CRITICAL MESSAGE: Exitting System")
    exit()

##############################################################


def GETTING_ID(us,psw):
    global CUSTOMER_ID
    for i in range(row_count+1):
        if i == 0:
            pass 
        else:
            cust_try_1_directory = 'customers/cust{}'.format(i)
            with open(cust_try_1_directory,'a+') as try1READ:
                data = try1READ.readlines()
                for j in range(len(data)):
                    if us in data[j]:
                        try1READ.seek(0)
                        for k in range(len(data)):
                            if psw in data[k]:
                                try1READ.seek(0)
                                for L in range(len(data)):
                                    if 'Customer ID: ' in data[L]:
                                        CUSTOMER_ID = data[L]
                                        CUSTOMER_ID = CUSTOMER_ID.replace('Customer ID: ','')
                                        print(CUSTOMER_ID)

# Logger
def logger():
    
    global LOG

    LOG = logging.getLogger(__name__)
    LOG.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(funcName)s : %(lineno)d : %(message)s', datefmt="%Y-%m-%d %H:%M:%S")

    # Current Year-Month
    current_year_month = datetime.datetime.now().strftime("%Y-%m")

    # Logger file name
    log_file_name = f"{current_year_month}_{CURRENT_SCRIPT_NAME}.log"

    # Create Logs Folder if it does not exist
    os.makedirs(LOGS_DIRECTORY, exist_ok=True)

    # Log file path
    log_file = os.path.join(LOGS_DIRECTORY, log_file_name)

    # File Handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    LOG.addHandler(file_handler)
    
    # StreamHandler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    LOG.addHandler(stream_handler)


# Quit Homepage
def quit_homepage():
    LOG.debug("- Quit Homepage -")

    global ROOT
    
    # Quit Homepage
    ROOT.destroy()


# Exit Bot
def exit_bot():
    LOG.debug("- Exit Bot -")

    # Quit Homepage
    quit_homepage()

    # Exit
    LOG.debug("Exit Bot")
    sys.exit(0)

       

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


# Homepage
def homepage():
    LOG.debug("- Homepage -")
    speak("Login to proceed")
    global ROOT
    global TKINTER_WIDGETS
    
    def old_user():
        quit_homepage()
        os.system('python signin.py')

    try:
        # Read the Image
        img = Image.open(os.path.join(IMAGES_DIRECTORY, "logo.png"))
        img_resized = img.resize((100, 100))
        img = ImageTk.PhotoImage(img_resized)

        # Label Image
        TKINTER_WIDGETS['label_img'] =  customtkinter.CTkLabel(master=ROOT, image=img, corner_radius=7)
        TKINTER_WIDGETS['label_img'].image = img
        TKINTER_WIDGETS['label_img'].grid(row=0, column=0, columnspan=2, padx=15, pady=10)

        # - Frame Login - #
        frame_login = customtkinter.CTkFrame(master=ROOT, corner_radius=10)
        frame_login.grid(row=1, column=0, padx=15, pady=20)

        # Label Username
        TKINTER_WIDGETS['label_username'] =  customtkinter.CTkLabel(master=frame_login, text="Username: ", width=30, height=25, corner_radius=7)
        TKINTER_WIDGETS['label_username'].grid(row=0, column=0, padx=10, pady=20)

        # Entry Username
        TKINTER_WIDGETS['entry_username'] = customtkinter.CTkEntry(master=frame_login, placeholder_text="Enter Username", width=200, height=30, border_width=2, corner_radius=10)
        TKINTER_WIDGETS['entry_username'].grid(row=0, column=1, padx=10, columnspan=2)

        # Label Password
        TKINTER_WIDGETS['entry_password'] = customtkinter.CTkLabel(master=frame_login, text="Password: ", width=30, height=25, corner_radius=7)
        TKINTER_WIDGETS['entry_password'].grid(row=1, column=0, padx=10, pady=5, sticky='e')

        # Entry Password
        TKINTER_WIDGETS['entry_password'] = customtkinter.CTkEntry(master=frame_login, placeholder_text="Enter Password", width=200, height=30, border_width=2, corner_radius=10, show="•", text_font=('Roboto-Medium', 10))
        TKINTER_WIDGETS['entry_password'].grid(row=1, column=1, padx=10, columnspan=2, pady=20)

        # Label Customer ID
        TKINTER_WIDGETS['entry_cust_id'] = customtkinter.CTkLabel(master=frame_login, text="Customer ID ", width=30, height=25, corner_radius=7)
        TKINTER_WIDGETS['entry_cust_id'].grid(row=2, column=0, padx=10, pady=5, sticky='e')

        # Entry Customer ID
        TKINTER_WIDGETS['entry_cust_id'] = customtkinter.CTkEntry(master=frame_login, placeholder_text="Enter Cust id", width=200, height=30, border_width=2, corner_radius=10, show="•", text_font=('Roboto-Medium', 10))
        TKINTER_WIDGETS['entry_cust_id'].grid(row=2, column=1, padx=10, columnspan=2, pady=20)

        # Button Login
        TKINTER_WIDGETS['button_login'] = customtkinter.CTkButton(master=ROOT, text="Login", width=70, fg_color="#36719F", hover_color="#3B8ED0", command=login_try,text_color="#FFF")
        TKINTER_WIDGETS['button_login'].grid(row=3, column=0, padx=100, sticky='e')

        # Button Cancel
        TKINTER_WIDGETS['button_cancel'] = customtkinter.CTkButton(master=ROOT, text="Cancel", fg_color="gray74", hover_color="#EEE", text_color="#000", width=70, command=exit_bot)
        TKINTER_WIDGETS['button_cancel'].grid(row=3, column=0, padx=20, sticky='e')

        # Button sign-in
        TKINTER_WIDGETS['button_sign'] = customtkinter.CTkButton(master=ROOT, text="Don't have a account\nsign-in", fg_color="green", hover_color="#EEE", text_color="#000", width=70, command=old_user)
        TKINTER_WIDGETS['button_sign'].grid(row=5, column=0, padx=20, sticky='e')
        
    except Exception as e:
        LOG.error("Failed")
        LOG.error(e, exc_info=True)

    

def login_succes_cmd(name_of_user,pw):
    with open('customer_login.txt','w') as write_user:
        write_user.write(name_of_user)
        quit_homepage()
        sleep(2)
    os.system('python login_success.py')



def login_check(Record,Name,PASSWORD_CHECK,cust__id_):
    global Login__name
    global Login__pass
    global Login__cust_id
    global username
    Login__name = False #actually false
    Login_success = False
    Login__cust_id = False
    count_name = 0
    for cust_detail in Record:
        while Login__name == False and count_name<row_count :
            global CUST_NAME
            CUST_NAME = cust_detail[0]
            if CUST_NAME == Name :
                print("Name verified..")
                Login__name = True
                for cust_detail_id in Record:
                    while Login__cust_id == False and count_name<row_count :
                        global CUST_Id
                        CUST_Id = str(cust_detail_id[1])
                        if CUST_Id == CUST_Id:
                            print("Customer ID verified..")
                            with open('ID.txt','a') as ID_writer:
                                ID_writer.write(CUST_Id)
                            Login__cust_id = True
                        count_name += 1
            count_name += 1

    
    def pass_check():
        global Login__pass
        Login__pass = False #actually false
        global CUST_NAME
        count_pass = 0
        for cust_pass in Record:
            while count_pass<=row_count  :
                CUST_PASS = str(cust_pass[2])
                if  PASSWORD_CHECK == CUST_PASS and  type(CUST_PASS) == type(PASSWORD_CHECK) :
                    print("Password verified")
                    Login__pass = True
                    print("Login successful")
                    global password
                    password = CUST_PASS

                count_pass += 1

        if Login__pass == True and Login__name == True:
            speak("LOGIN Successful")
            global username
            username = CUST_NAME
            login_succes_cmd(name_of_user=username,pw=password)

            print('User Verified: ',username)

        return username


                # elif count_pass >= row_count and Login__pass == False:
                #     print("wrong Password")


    if Login__name == True and Login__cust_id == True:
        pass_check()
    elif Login__name == False:
        LOGIN_STATUS = ("User not found please sign-in to use toggle")
        print(LOGIN_STATUS)
    elif Login__cust_id == False:
        LOGIN_STATUS_ = ("Wrong Customer ID")
        print(LOGIN_STATUS_)

    if pass_check == True:
        print("login success")
    # else:
    #     speak("No such user found please sign in")
    #     quit_homepage()
    #     os.system('python signin.py')

    return username





def login_try():
    
    name=TKINTER_WIDGETS['entry_username'].get()
    passwrd = TKINTER_WIDGETS['entry_password'].get()
    cusssttt__id = TKINTER_WIDGETS['entry_cust_id'].get()

    cur_use.execute("select * from customers")
    record = cur_use.fetchall()
    # print(name,passwrd)
    # print(record)
    try:
        login_check(Record=record,Name=name,PASSWORD_CHECK=passwrd,cust__id_=cusssttt__id)

    except:
        print("Error in logging-in")

# Load UI
def load_ui():

    LOG.debug("- Load UI -")

    global ROOT

    # Properties
    ROOT.title("Toggle - Login")

    # Homepage
    homepage()

    #  - Set Window to appear in the middle when program runs -
    screen_width = ROOT.winfo_screenwidth()
    screen_height = ROOT.winfo_screenheight()

    app_center_coordinate_x = (screen_width / 3) - (APP_WIDTH / 3)
    app_center_coordinate_y = (screen_height / 3) - (APP_HEIGHT / 3)

    # Position App to the Centre of the Screen
    ROOT.geometry(f"{APP_WIDTH}x{APP_HEIGHT}+{int(app_center_coordinate_x)}+{int(app_center_coordinate_y)}")

    # Prevent User from Resizing the Window
    ROOT.resizable(width=False, height=False)

    # Close 'X' Button
    ROOT.protocol("WM_DELETE_WINDOW", exit_bot)

    # Infinite Loop
    ROOT.mainloop()





# Main
if __name__ == "__main__":

    logger()

    load_ui()

    print("Toggle_Verified user: ",username)