from tkinter import *
import os

#implementing functions for restart restart with time logout and shutdown
def restart():
    os.system("shutdown /r /t 1 ")
    
def restart_time():
    os.system("shutdown /r /t 20 ")#shutdown after 20 seconds

def logout():
    os.system("shutdown -l")
    
def shutDown():
    os.system("shutdown /s /t 1 ")



st = Tk()

#user interface section below:
st.title("Shutdown App")
st.geometry("500x500")
st.config(bg="blue")

r_button = Button(st,text="Restart",font=("Time New Roman",30,"bold"),relief=RAISED,cursor="plus",command=restart)#command is used to call a function using button
r_button.place(x=150,y=60,height=50,width=200)

rt_button = Button(st,text="Restart Time",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart_time())
rt_button.place(x=150,y=170,height=50,width=200)

lg_button = Button(st,text="Logout",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=logout())
lg_button.place(x=150,y=270,height=50,width=200)

sd_button = Button(st,text="ShutDown",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=shutDown())
sd_button.place(x=150,y=370,height=50,width=200)
st.mainloop()
#------------------------------------------------------------------------------------------------------------------------

