import os
from tkinter import *

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




with open('customer_login.txt','r') as read_user:
        user = str(read_user.readlines())
        user = user.replace('[','')
        user = user.replace(']','')
        user = user.replace("'",'')
        spqq = ('Welcome Back',user)
        speak(spqq)
        with open('customer_login.txt','w') as delete_user:
                delete_user.truncate()
        



def login_success(username):

        from tkinter.ttk import Progressbar
        from tkinter import ttk
        import os
        import customtkinter

        wel=Tk()


        width_of_window = 427
        height_of_window = 250
        screen_width = wel.winfo_screenwidth()
        screen_height = wel.winfo_screenheight()
        x_coordinate = (screen_width/2)-(width_of_window/2)
        y_coordinate = (screen_height/2)-(height_of_window/2)
        wel.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))


        wel.overrideredirect(1)


        s = ttk.Style()
        s.theme_use('clam')
        s.configure("red.Horizontal.TProgressbar", foreground='red', background='#19547b')
        progress=Progressbar(wel,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)

        #############progressbar         
        def main_win():
                os.system('python Toggle_verified.py')




        def bar():

                l4=Label(wel,text='Loading...',fg='white',bg=a)
                lst4=('Calibri (Body)',10)
                l4.config(font=lst4)
                l4.place(x=18,y=210)
                
                import time
                r=0
                for i in range(100):
                        progress['value']=r
                        wel.update_idletasks()
                        time.sleep(0.03)
                        r=r+1
                
                wel.destroy()
                main_win()
                
        
        progress.place(x=-10,y=235)



        # a='#243b55'
        a='#141e30'
        # a='#249794'
        Frame(wel,width=427,height=241,bg=a).place(x=0,y=0)  #249794
        b1=customtkinter.CTkButton(wel,width=60,height=8,text_font=('Calibri (Body)',18),text='Get Started',hover_color='green',command=bar,border=2,fg_color=a,bg='white')
        b1.place(x=270,y=190)


        ######## Label

        login_success_text = 'Welcome Back %s'%(username)
        print(login_success_text)

        l1=Label(wel,text=login_success_text,fg='white',bg=a)
        lst1=('Calibri (Body)',18,'bold')
        l1.config(font=lst1)
        l1.place(x=50,y=80)

        l2=Label(wel,text='TOGGLE',fg='Yellow',bg=a)
        lst2=('Calibri (Body)',18)
        l2.config(font=lst2)
        l2.place(x=10,y=10)

        l3=Label(wel,text='Loading Interface',fg='white',bg=a)
        lst3=('Calibri (Body)',13)
        l3.config(font=lst3)
        l3.place(x=50,y=120)

        


        wel.mainloop()



login_success(username=user)