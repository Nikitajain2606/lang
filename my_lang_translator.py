# -*- coding: utf-8 -*-
"""

@author: Ideapad
"""

from google_trans_new import google_translator
from tkinter import *

def convert(e):

    lang=e.widget["text"]
    code = Lang[lang]
    t = google_translator()
    s = t.translate(msg.get(),lang_tgt=code)
    convmsg.set(s)

root=Tk()
root.title("NIKITA and SEEMA Language Translator")
root.geometry("500x500")
root["bg"]="orange"
lbl=Label(root,text="Enter Text in Any Language",font=5)

lbl.grid(row=0,column=0,columnspan=3,sticky=E+W+N+S,padx=30,pady=20)
msg=StringVar()
entmsg=Entry(root,textvariable=msg,font=3)
entmsg.grid(row=1,column=0,columnspan=3,sticky=E+W+N+S,padx=30)
Lang={"Hindi":"hi","English":"en","Punjabi":"pa","German":"de","Russian":"ru","Gujrati":"gu", "French":"fr","Spanish":"su"
      ,"Tamil":"ta"}
LangNames=list(Lang.keys())

for i in range(3):
    btn=Button(root,text=f"{LangNames[i]}",font=1,bg="yellow",width=10)
    btn.bind("<1>",convert)
    btn.grid(row=2,column=i,padx=30,pady=30)
for i in range(3):
    btn=Button(root,text=f"{LangNames[i+3]}",font=1,bg="yellow",width=10)
    btn.bind("<1>",convert)
    btn.grid(row=3,column=i,padx=30,pady=30)
for i in range(3):
    btn=Button(root,text=f"{LangNames[i+6]}",font=1,bg="yellow",width=10)
    btn.bind("<1>",convert)
    btn.grid(row=4,column=i,padx=30,pady=30)

convmsg=StringVar()
entconvmsg=Entry(root,textvariable=convmsg,font=4)
entconvmsg.grid(row=5,column=0,columnspan=3,sticky=E+W+N+S,padx=10,pady=10)
root.mainloop()