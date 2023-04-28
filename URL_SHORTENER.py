import pandas as pd
import pyshorteners
import tkinter as tk
from tkinter import *

#long_url = input("Enter the URL to shorten: ")
 
url_shortener=tk.Tk()
url_shortener.title("URL shortener")
url_shortener.geometry("600x600")

def url():
    short_url=''
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(long_url.get())
    res.set(short_url)
    
Label(url_shortener, text= "Enter the Long URL:", fg="Black",font="Arial").place(x=10,y=65)
long_url=StringVar()
Entry(url_shortener,textvariable = long_url,bg = "white",width = 60).place(x=210,y=70)
Button(url_shortener,text = "Enter",font=40,fg="blue",width = 10,command = url).place(x =150,y=150)
Label(url_shortener, text= "The generated short URL:", fg="Black",font="Arial").place(x=10,y=95)
res=StringVar()
Entry(url_shortener,textvariable = res,bg = "white",width = 50).place(x=270,y=100)

url_shortener.mainloop()
