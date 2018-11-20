# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 21:26:35 2018

@author: YINKA
"""
import os
import time
import math
import numpy as np
import random
from tkinter import *
import tkinter.messagebox as box
import pandas
#import xlrd
import tkinter.ttk as ttk
from PIL import ImageTk,Image
import sqlite3
#dbrine= pandas.read_excel('C:/Users/YINKA/Documents/samuel_akosa/Casing-Data-Sheet.xlsx')
#KCLr=pandas.read_excel('C:/Users/YINKA/Documents/samuel_akosa/Casing-Data-Sheet.xlsx',sheetname='KCL')
#NaClr=pandas.read_excel('C:/Users/YINKA/Documents/samuel_akosa/Casing-Data-Sheet.xlsx',sheetname='NACL')
#NH4Cl=pandas.read_excel('C:/Users/YINKA/Documents/samuel_akosa/Casing-Data-Sheet.xlsx',sheetname='NH4CL')
#CaCl2P=pandas.read_excel('C:/Users/YINKA/Documents/samuel_akosa/Casing-Data-Sheet.xlsx',sheetname='CACL2-P')
#CaCl2D=pandas.read_excel('C:/Users/YINKA/Documents/samuel_akosa/Casing-Data-Sheet.xlsx',sheetname='CACL2-D')
#Na_CaP=pandas.read_excel('C:/Users/YINKA/Documents/samuel_akosa/Casing-Data-Sheet.xlsx',sheetname='NACL-CACL2-P')
#Na_CaD=pandas.read_excel('C:/Users/YINKA/Documents/samuel_akosa/Casing-Data-Sheet.xlsx', sheetname='NACL-CACL2-D')
#pandas.read_excel('C:/Users/YINKA/Documents/samuel_akosa/Casing-Data-Sheet.xlsx')
   
root=Tk()
root.title("Brine Mixer")

#root.wm_iconbitmap('pic.ico')
#root.geometry(width=1000,height=2500)
#+++++++++++++++++++++MENU AND TOOLBAR++++++++++++++++++++++++++++++++++++++++
def Exit():
    result = box.askquestion('Brine Mix', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.quit()
        root.destroy()
        exit()
def Kalc():
    os.system('start calc.exe')

def table():
    d=str(CaCl2P)
    box.showinfo("CaCl2-Peladow Table",str(CaCl2P))
def ruth():
    b="""\n\tBrine Mixer 
    \tVersion 1.0.0.1 
    \tAuthor: Samuel Prince Akosa
    \tDate Created: **/**/2018
    \tEmail: samuel.akosa@outlook.com"""
    box.showinfo('Documentation',b)
def buchi():
    b='''------------------------Formulae-------------------------------------------------------\n
    \n(1) Pressure gradient: This is the quotient of the Formation pressure in psi(lbs/in2) and the True Vertical depth in feet(ft). It is usually measured in psi/ft
    \n Mathematically ,
    
    \tPressure gradient =  (Formation pressure + Pressure Adjuster)/True Vertical Depth
    \n\t The pressure adjuster is usually given in well pogrammes , however if not given assume a value of 100psi , but always check before assumptions (ref: John Ahiwe)
    \tNB:This program rounds up its value to 2.d.p\n
    (2) Brine Weight: This is the density of the brine formulated. \n Mathematically it is \n 
    Brine Weight =\tPressure gradient/0.052 \n
    \tNB:This programme rounds up the value to 2.d.p\n
    (3) Hole Volume: This is the volume of fluid that will contain a full length of the True or Measured depth in ft, TD. It is the product of the casing capacity and the True depth. The casing capacity is a function of the Casing Outer diameter (OD) in inches and the Casing Norminal Weight in lbs/ft. \nNB: Casing referred to here is the production casing string.
    Casing Capacity =f(casing_OD,Casing Norminal Weight )
    \tHole Volume= Casing Capacity *True depth\n
    (4) Design Hole volume: This is the approximate hole volume, set to cater for descrepancies and anomalies (Ref:John Ahiwe)
    It is a rounded form of the hole volume.
    (5) Brine Volume: This is the volume of brine needed to fill up the whole hole volume. Since one volume of brine, equivalent to the whole volume of the hole must always be stored in the storage tanks on surface, at least the brine volume must be greater than twice the hole volume.
    John Ahiwe thus set this as three times the hole volume to allow for safety.\n Thus,\n
    \tBrine volume=3 * Design Hole volume
    (6) Design Brine volume: This is the approximate volume of brine needed for an operation. Its entirely based on experience. Figures here are basically from John Ahiwe's experience
    (7) Salt Concentration: the salts listed here include Sodium Chloride(NaCl),Potassium Chloride(KCl),Ammonium Chloride (NH4Cl),Calcium Chloride (CaCl2) and a combination of Sodium Chloride-Calcium Chloride mix. These salts are usually used in the oil industry for the fomation of brines and as such calculations have been limited to just these ones
    \t For Calcium Chloride , two type of formulations are used which include Peladow and Dowflakes. Peladow refer to 94-97% by weight CaCl2 while Dowflakes refer to 77-80% by weight CaCl2 formulation.
    The values not present in the tables are obtained by linear interpolation.
    (8) Assumptions: The assumptions used here include: 
        1kg= 2.2 lbs, 1 Metic tonne(MT) =1000kg, 1Trailer= 100MT bags, Design Amt. of Salt = 1.5*Calculated amt of salt
    (9)Examples
        example 1: to calculate the Design brine volume.
        Given : Well Pressure= 2000psi, Measured depth= 6000ft, True vertical Depth= 7200ft, Casing size = 9-5/8", 47# , Salt =NaCl
    
    '''
    
    box.showinfo('Tutorial',b)
def about():
    j='''This is a program created by Samuel Prince Akosa for the swift calculation of parameters needed in mixing and formulating brine using different salts. 
    \nThe assumptions used here for design purposes are taken from the words and field experiences of John Iheanacho Ahiwe, a renowned Supervisor in the field of Mixing and filtering brines at TechDaer Services Ltd.
    \n We thank him for his selfless time in explaining various concepts and for giving the reasons the for these assumptions'''
    #def dialog3():
    box.showinfo('About Brine Mixer', j)  
#Calc1=Text(f1,font=('arial',8,'bold'), bd=4, insertwidth=100,textvariable=Calcu4,bg='white').grid(row=8,column=6)
#calculot = Image.open('calculo.png')
#calcula=ImageTk.PhotoImage(calculot)
def sayYes():
    print("Oh Yea!!")

menu=Menu(root)
root.config(menu=menu)
root.iconify()

menu= Menu(root)
root.config(menu=menu)
root.config(bg='green')
filemenu = Menu(menu)
menu.config(bg='red')



#=====================================Casing section===========
SEARCH1 = DoubleVar()
caso=['O.D. (inch)',
 'Nominal Weight T & C lbs/ft',
 'Grade',
 'Collapse Pressure (psi)',
 'Internal Yield Pressure Minimum PE',
 'Internal Yield Pressure Minimum STC',
 'Internal Yield Pressure Minimum LTC',
 'Internal Yield Pressure Minimum BTC',
 'Joint Strength 1000 lbs STC',
 'Joint Strength 1000 lbs LTC',
 'Joint Strength 1000 lbs BTC',
 'Body Yield 1000 lbs',
 'Wall (inch)',
 'I.D. (inch)',
 'Drift Diameter (inch)',
 'Displacement (bbl/ft)',
 'Capacity (bbl/ft)']

def Database():
    global conn, cursor
    conn = sqlite3.connect("Brine_Salt.sql")
    cursor = conn.cursor()
    

Database()
    #conn,cursor
    #gl=gg.cursor()#cursor object
gl=cursor
    
f1=gl.execute('SELECT * FROM "KCL" ')
f1K=f1.fetchall()
KCLr=pandas.DataFrame(f1K)
gl.close()
conn.close()
Database() #conn,cursor #gl=gg.cursor()#cursor object
gl=cursor #gl.execute('SELECT * FROM "Casing-Data" ') # gl.fetchone()  #gl.fetchall()
f2=gl.execute('SELECT * FROM "NACL" ')
f2K=f2.fetchall()
NaClr=pandas.DataFrame(f2K)
gl.close()
conn.close()
Database() #conn,cursor #gl=gg.cursor()#cursor object
gl=cursor 
f3=gl.execute('SELECT * FROM "NH4CL" ')
f3K=f3.fetchall()
NH4Cl=pandas.DataFrame(f3K)
gl.close()
conn.close()
Database() #conn,cursor #gl=gg.cursor()#cursor object
gl=cursor 
f4=gl.execute('SELECT * FROM "CACL2P" ')
f4K=f4.fetchall()
CaCl2P=pandas.DataFrame(f4K)
gl.close()
conn.close()
Database() #conn,cursor #gl=gg.cursor()#cursor object
gl=cursor 
f5=gl.execute('SELECT * FROM "CACL2D" ')
f5K=f5.fetchall()
CaCl2D =pandas.DataFrame(f5K)
gl.close()
conn.close()
Database() #conn,cursor #gl=gg.cursor()#cursor object
gl=cursor 
f6=gl.execute('SELECT * FROM "NA_CAP" ')
f6K=f6.fetchall()
Na_CaP=pandas.DataFrame(f6K)
gl.close()
conn.close()
Database() #conn,cursor #gl=gg.cursor()#cursor object
gl=cursor 
f7=gl.execute('SELECT * FROM "NA_CAD" ')
f7K=f7.fetchall()
Na_CaD=pandas.DataFrame(f7K)
gl.close()
conn.close()





def ViewForm1():
    global tree1
    TopViewForm1 = Frame(viewform1, width=600, bd=1, relief=SUNKEN,bg='purple')
    TopViewForm1.pack(side=TOP, fill=X)
    LeftViewForm1 = Frame(viewform1, width=600, bg='grey')
    LeftViewForm1.pack(side=LEFT, fill=Y)
    MidViewForm1 = Frame(viewform1, width=600)
    MidViewForm1.pack(side=RIGHT)
    lbl_text = Label(TopViewForm1, text="Casing Data",bg='grey', font=('arial', 12,'italic'), width=600)
    lbl_text.pack(fill=X)
    txtsearch = Label(LeftViewForm1, text="Search\n O.D",bg='grey',fg='black', font=('arial', 9,'italic'))
    txtsearch.pack(side=TOP)
    search = Entry(LeftViewForm1, textvariable=SEARCH1, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm1, text="Search", command=Searchy)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm1, text="Reset", command=Resety)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    #btn_delete = Button(LeftViewForm1, text="Delete", command=Delete)
    #btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm1, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm1, orient=VERTICAL)
    tree1 = ttk.Treeview(MidViewForm1 ,columns=("Index", 'ii', 'ji','do','li','mi','ni','qi','ri', 'si','ti','ui','vi','wi','xi','yi','zi','xxi'), 
                        selectmode="extended", height=100, 
                        yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree1.yview)
    scrollbarx.config(command=tree1.xview)
    #scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    #scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree1.pack()
    scroly=Scrollbar(LeftViewForm1,orient=VERTICAL)
    scroly.pack(side=RIGHT,fill=Y)
    listbox1=Listbox(LeftViewForm1,yscrollcommand=scroly)
    listbox1.insert(END,'Casing')
    listbox1.select_set(0) 
    listbox1.pack(side=BOTTOM)
    tree1.heading('Index', text="Index",anchor=W)
    tree1.heading('ii', text=caso[0],anchor=W)
    tree1.heading('ji', text=caso[1],anchor=W)
    tree1.heading('do', text=caso[2],anchor=W)
    tree1.heading('li', text=caso[3],anchor=W)
    tree1.heading('mi', text=caso[4],anchor=W)
    tree1.heading('ni', text=caso[5],anchor=W)
    tree1.heading('qi', text=caso[6],anchor=W)
    tree1.heading('ri', text=caso[7],anchor=W)
    tree1.heading('si', text=caso[8],anchor=W)
    tree1.heading('ti', text=caso[9],anchor=W)
    tree1.heading('ui', text=caso[10],anchor=W)
    tree1.heading('vi', text=caso[11],anchor=W)
    tree1.heading('wi', text=caso[12],anchor=W)
    tree1.heading('xi', text=caso[13],anchor=W)
    tree1.heading('yi', text=caso[14],anchor=W)
    tree1.heading('zi', text=caso[15],anchor=W)
    tree1.heading('xxi', text=caso[16],anchor=W)
    tree1.column('#0', stretch=NO, minwidth=0, width=0)
    tree1.column('#1', stretch=NO, minwidth=0, width=0)
    tree1.column('#2', stretch=NO, minwidth=0, width=200)
    tree1.column('#3', stretch=NO, minwidth=0, width=120)
    tree1.column('#4', stretch=NO, minwidth=0, width=120)
    tree1.column('#5', stretch=NO, minwidth=0, width=120)
    tree1.column('#6', stretch=NO, minwidth=0, width=120)
    tree1.column('#7', stretch=NO, minwidth=0, width=120)
    tree1.column('#8', stretch=NO, minwidth=0, width=120)
    tree1.column('#9', stretch=NO, minwidth=0, width=120)
    tree1.column('#10', stretch=NO, minwidth=0, width=120)
    tree1.column('#11', stretch=NO, minwidth=0, width=120)
    tree1.column('#15', stretch=NO, minwidth=0, width=120)
    tree1.column('#13', stretch=NO, minwidth=0, width=120)
    tree1.column('#14', stretch=NO, minwidth=0, width=120)
    tree1.column('#15', stretch=NO, minwidth=0, width=120)
    tree1.column('#16', stretch=NO, minwidth=0, width=120)
    tree1.column('#17', stretch=NO, minwidth=0, width=120)
    

def ShowView1():
    global viewform1
    viewform1 = Toplevel()
    #viewform1.title("Casing Tables")
    width = 600
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform1.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform1.wm_iconbitmap('pic.ico')
    viewform1.resizable(2, 2)
    ViewForm1()
def casing():
    ShowView1()
    Database()
    cursor.execute("SELECT * FROM Casing")
    fetch = cursor.fetchall()
    for data in fetch:
        tree1.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
def DisplayCasing():
    Database()
    cursor.execute("SELECT * FROM Casing")
    fetch = cursor.fetchall()
    for data in fetch:
        tree1.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

           
def Searchy():
    if SEARCH1.get() != "":
        tree1.delete(*tree1.get_children())
        Database()
        cursor.execute('SELECT * FROM Casing WHERE "O.D. (inch)" LIKE ?',('%'+str(SEARCH1.get())+'%',))#.fetchone()
        fetch=cursor.fetchall()
        for data in fetch:
            tree1.insert('', 'end', values=(data))
        cursor.close()
        conn.close()            
        
def Resety():
    tree1.delete(*tree1.get_children())
    DisplayCasing()
    SEARCH1.set("")
#=============================================



#==========================salt side======================
SEARCH = DoubleVar()
gk={1:'KCl',2:'NaCl',3:'NH4Cl',4:'CaCl2-Peladow',5:'CaCl2-Dowflakes',6:'NaCl-CaCl2-Peladow',7:'NaCl-CaCl2-Dowflakes'}
kk={1:'sp.gr @ 60degF',
    2:'solution weight (60 degF) in lbs/galUS',
    3:'KCl in lbm/bbl'
    ,4:' Water in galUS/Sol'
    ,5:'Freezing Point in degF',
    6:'pressure gradient in psi/ft'
    ,7:'Approx. % KCL'}

nk={1:'sp.gr @ 60degF',
    2:'solution weight (60 degF) in lbs/galUS',
    3:'NaCl in lbm/bbl'
    ,4:' Water in galUS/Sol'
    ,5:'Freezing Point in degF',
    6:'pressure gradient in psi/ft'
    ,7:'Approx. % NaCL'}
nh={1:'sp.gr @ 60degF',
    2:'solution weight (60 degF) in lbs/galUS',
    3:'NH4Cl in lbm/bbl'
    ,4:' Water in galUS/Sol'
    ,5:'Freezing Point in degF',
    6:'pressure gradient in psi/ft'
    ,7:'Approx. % NH4CL'}
cap={1:'sp.gr @ 60degF',
    2:'solution weight (60 degF) in lbs/galUS',
    3:'CACl2-P in lbm/bbl'
    ,4:' Water in galUS/Sol'
    ,5:'Freezing Point in degF',
    6:'pressure gradient in psi/ft'
    ,7:'Approx. % CACl2-P'}
cad={1:'sp.gr @ 60degF',
    2:'solution weight (60 degF) in lbs/galUS',
    3:'CaCl2D in lbm/bbl'
    ,4:' Water in galUS/Sol'
    ,5:'Freezing Point in degF',
    6:'pressure gradient in psi/ft'
    ,7:'Approx. % CaClD'}
nacp={1:'sp.gr @ 60degF',
    2:'solution weight (60 degF) in lbs/galUS',
    3:' Peladow(94-97%CaCl2&NaCl) in lbm/bbl'
    ,4:' NaCL in lbm/bbl'
    ,5:' Water in galUS/Sol'
    ,6:'pressure gradient in psi/ft'
    ,7:'Freezing Point in degF'}
nacd={1:'sp.gr @ 60degF',
    2:'solution weight (60 degF) in lbs/galUS',
    3:' Peladow(77-80%CaCl2&NaCl) in lbm/bbl'
    ,4:' NaCL in lbm/bbl'
    ,5:' Water in galUS/Sol'
    ,6:'pressure gradient in psi/ft'
    ,7:'Freezing Point in degF'}

#------------------------------------------------------------------ 
                
def ViewForm():
    #global lbl_text
    global tree
    global listbox
    global TopViewForm
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SUNKEN, bg='purple')
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600, bg='grey')
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600, bg='grey')
    MidViewForm.pack(side=RIGHT)
    lbl_txtsearch = Label(LeftViewForm, text="Search\n Brine Weight",bg='gray', font=('arial', 10, 'italic'))
    lbl_txtsearch.pack(side=TOP)
    scroly=Scrollbar(LeftViewForm,orient=VERTICAL)
    listbox=Listbox(LeftViewForm,yscrollcommand=scroly)
    
    for i in gk:
        listbox.insert(END,gk[i])
     
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    #btn_reset.configure(state=DISABLED)
    listbox.pack(padx=10,pady=10, fill=Y)
    tree = ttk.Treeview(MidViewForm ,columns=("Index", 'ii', 'ji','do','li','mi','ni','qi'), 
                        selectmode="extended", height=100, 
                        yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    
    tree.pack()
    #DisplayData()
    
    
def ShowView():
    global viewform
    viewform = Toplevel()
    viewform.title("Amount of Salt")
    width = 600
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.wm_iconbitmap('pic.ico')
    viewform.resizable(2, 2)
    ViewForm()

def kcl():
    ShowView()
    lbl_text = Label(TopViewForm, text="Salt Type = "+gk[1], font=('arial', 10), width=600)
    lbl_text.pack(fill=X)
    listbox.select_set(0) 
    tree.heading('Index', text="Index",anchor=W)
    tree.heading('ii', text=kk[1],anchor=W)
    tree.heading('ji', text=kk[2],anchor=W)
    tree.heading('do', text=kk[3],anchor=W)
    tree.heading('li', text=kk[4],anchor=W)
    tree.heading('mi', text=kk[5],anchor=W)
    tree.heading('ni', text=kk[6],anchor=W)
    tree.heading('qi', text=kk[7],anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.column('#5', stretch=NO, minwidth=0, width=120)
    tree.column('#6', stretch=NO, minwidth=0, width=120)
    tree.column('#7', stretch=NO, minwidth=0, width=120)
    Database()
    cursor.execute("SELECT * FROM KCL")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()



def nacl():
    ShowView()
    listbox.select_set(1)
    lbl_text = Label(TopViewForm, text="Salt Type= "+gk[2], font=('arial', 10), width=600)
    lbl_text.pack(fill=X)
    tree.heading('Index', text="Index",anchor=W)
    tree.heading('ii', text=nk[1],anchor=W)
    tree.heading('ji', text=nk[2],anchor=W)
    tree.heading('do', text=nk[3],anchor=W)
    tree.heading('li', text=nk[4],anchor=W)
    tree.heading('mi', text=nk[5],anchor=W)
    tree.heading('ni', text=nk[6],anchor=W)
    tree.heading('qi', text=nk[7],anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.column('#5', stretch=NO, minwidth=0, width=120)
    tree.column('#6', stretch=NO, minwidth=0, width=120)
    tree.column('#7', stretch=NO, minwidth=0, width=120)
    Database()
    cursor.execute("SELECT * FROM NACL")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def nhcl():
    ShowView()
    listbox.select_set(2) 
    lbl_text = Label(TopViewForm, text="Salt Type= "+gk[3], font=('arial', 10), width=600)
    lbl_text.pack(fill=X)
    tree.heading('Index', text="Index",anchor=W)
    tree.heading('ii', text=nh[1],anchor=W)
    tree.heading('ji', text=nh[2],anchor=W)
    tree.heading('do', text=nh[3],anchor=W)
    tree.heading('li', text=nh[4],anchor=W)
    tree.heading('mi', text=nh[5],anchor=W)
    tree.heading('ni', text=nh[6],anchor=W)
    tree.heading('qi', text=nh[7],anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.column('#5', stretch=NO, minwidth=0, width=120)
    tree.column('#6', stretch=NO, minwidth=0, width=120)
    tree.column('#7', stretch=NO, minwidth=0, width=120)
    Database()
    cursor.execute("SELECT * FROM NH4CL")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def ncp():
    ShowView()
    listbox.select_set(5)
    lbl_text = Label(TopViewForm, text="Salt Type = "+gk[6], font=('arial', 10), width=600)
    lbl_text.pack(fill=X)
    tree.heading('Index', text="Index",anchor=W)
    tree.heading('ii', text=nacp[1],anchor=W)
    tree.heading('ji', text=nacp[2],anchor=W)
    tree.heading('do', text=nacp[3],anchor=W)
    tree.heading('li', text=nacp[4],anchor=W)
    tree.heading('mi', text=nacp[5],anchor=W)
    tree.heading('ni', text=nacp[6],anchor=W)
    tree.heading('qi', text=nacp[7],anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.column('#5', stretch=NO, minwidth=0, width=120)
    tree.column('#6', stretch=NO, minwidth=0, width=120)
    tree.column('#7', stretch=NO, minwidth=0, width=120)
    Database()
    cursor.execute("SELECT * FROM NA_CAP")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def ncd():
    ShowView()
    listbox.select_set(6) 
    lbl_text = Label(TopViewForm, text="Salt Type = "+gk[7], font=('arial', 10), width=600)
    lbl_text.pack(fill=X)
    tree.heading('Index', text="Index",anchor=W)
    tree.heading('ii', text=nacd[1],anchor=W)
    tree.heading('ji', text=nacd[2],anchor=W)
    tree.heading('do', text=nacd[3],anchor=W)
    tree.heading('li', text=nacd[4],anchor=W)
    tree.heading('mi', text=nacd[5],anchor=W)
    tree.heading('ni', text=nacd[6],anchor=W)
    tree.heading('qi', text=nacd[7],anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.column('#5', stretch=NO, minwidth=0, width=120)
    tree.column('#6', stretch=NO, minwidth=0, width=120)
    tree.column('#7', stretch=NO, minwidth=0, width=120)
    Database()
    cursor.execute("SELECT * FROM NA_CAD")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
           
              
                

def cp():
    ShowView()
    listbox.select_set(3) 
    lbl_text = Label(TopViewForm, text="Salt Type = "+gk[4], font=('arial', 10), width=600)
    lbl_text.pack(fill=X)
    tree.heading('Index', text="Index",anchor=W)
    tree.heading('ii', text=cap[1],anchor=W)
    tree.heading('ji', text=cap[2],anchor=W)
    tree.heading('do', text=cap[3],anchor=W)
    tree.heading('li', text=cap[4],anchor=W)
    tree.heading('mi', text=cap[5],anchor=W)
    tree.heading('ni', text=cap[6],anchor=W)
    tree.heading('qi', text=cap[7],anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.column('#5', stretch=NO, minwidth=0, width=120)
    tree.column('#6', stretch=NO, minwidth=0, width=120)
    tree.column('#7', stretch=NO, minwidth=0, width=120)
    Database()
    cursor.execute("SELECT * FROM CACL2P")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def cd():
    ShowView()
    listbox.select_set(4) 
    lbl_text = Label(TopViewForm, text="Salt Type = "+gk[5], font=('arial', 10), width=600)
    lbl_text.pack(fill=X)
    tree.heading('Index', text="Index",anchor=W)
    tree.heading('ii', text=cad[1],anchor=W)
    tree.heading('ji', text=cad[2],anchor=W)
    tree.heading('do', text=cad[3],anchor=W)
    tree.heading('li', text=cad[4],anchor=W)
    tree.heading('mi', text=cad[5],anchor=W)
    tree.heading('ni', text=cad[6],anchor=W)
    tree.heading('qi', text=cad[7],anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.column('#5', stretch=NO, minwidth=0, width=120)
    tree.column('#6', stretch=NO, minwidth=0, width=120)
    tree.column('#7', stretch=NO, minwidth=0, width=120)
    Database()
    cursor.execute("SELECT * FROM CACL2D")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        if kcl:
            cursor.execute('SELECT * FROM KCL WHERE "solution weight (60 deg F) in lbs/galUS" LIKE ?',('%'+str(SEARCH.get())+'%',))#.fetchone()
        #cursor.execute("SELECT 'sp.gr @ 60degF' FROM `KCL` WHERE 'sp.gr @ 60degF'="+str(SEARCH.get())).fetchone()
        #fetch = cursor.fetchone()
            fetch=cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()
        elif nacl:
            cursor.execute('SELECT * FROM NACL WHERE "solution weight (60 deg F) in lbs/galUS" LIKE ?',('%'+str(SEARCH.get())+'%',))#.fetchone()
        #cursor.execute("SELECT 'sp.gr @ 60degF' FROM `KCL` WHERE 'sp.gr @ 60degF'="+str(SEARCH.get())).fetchone()
        #fetch = cursor.fetchone()
            fetch=cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()    
        elif nhcl:
            cursor.execute('SELECT * FROM NH4CL WHERE "solution weight (60 deg F) in lbs/galUS" LIKE ?',('%'+str(SEARCH.get())+'%',))#.fetchone()
        #cursor.execute("SELECT 'sp.gr @ 60degF' FROM `KCL` WHERE 'sp.gr @ 60degF'="+str(SEARCH.get())).fetchone()
        #fetch = cursor.fetchone()
            fetch=cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()    
        elif cp:
            cursor.execute('SELECT * FROM CACL2P WHERE "solution weight (60 deg F) in lbs/galUS" LIKE ?',('%'+str(SEARCH.get())+'%',))#.fetchone()
        #cursor.execute("SELECT 'sp.gr @ 60degF' FROM `KCL` WHERE 'sp.gr @ 60degF'="+str(SEARCH.get())).fetchone()
        #fetch = cursor.fetchone()
            fetch=cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()    
        elif cd:
            cursor.execute('SELECT * FROM CACL2D WHERE "solution weight (60 deg F) in lbs/galUS" LIKE ?',('%'+str(SEARCH.get())+'%',))#.fetchone()
        #cursor.execute("SELECT 'sp.gr @ 60degF' FROM `KCL` WHERE 'sp.gr @ 60degF'="+str(SEARCH.get())).fetchone()
        #fetch = cursor.fetchone()
            fetch=cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()    
        elif nacp:
            cursor.execute('SELECT * FROM NA_CAP WHERE "solution weight (60 deg F) in lbs/galUS" LIKE ?',('%'+str(SEARCH.get())+'%',))#.fetchone()
        #cursor.execute("SELECT 'sp.gr @ 60degF' FROM `KCL` WHERE 'sp.gr @ 60degF'="+str(SEARCH.get())).fetchone()
        #fetch = cursor.fetchone()
            fetch=cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()
        elif nacd:
            cursor.execute('SELECT * FROM NA_CAD WHERE "solution weight (60 deg F) in lbs/galUS" LIKE ?',('%'+str(SEARCH.get())+'%',))#.fetchone()
        #cursor.execute("SELECT 'sp.gr @ 60degF' FROM `KCL` WHERE 'sp.gr @ 60degF'="+str(SEARCH.get())).fetchone()
        #fetch = cursor.fetchone()
            fetch=cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()    
def DisplayData():
    Database()
    if kcl:
        cursor.execute("SELECT * FROM KCL")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

    elif nacl:
        cursor.execute('SELECT * FROM NACL' )
        #cursor.execute("SELECT 'sp.gr @ 60degF' FROM `KCL` WHERE 'sp.gr @ 60degF'="+str(SEARCH.get())).fetchone()
        #fetch = cursor.fetchone()
        fetch=cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()    
    elif nhcl:
        cursor.execute('SELECT * FROM NH4CL')#.fetchone()
        #cursor.execute("SELECT 'sp.gr @ 60degF' FROM `KCL` WHERE 'sp.gr @ 60degF'="+str(SEARCH.get())).fetchone()
        #fetch = cursor.fetchone()
        fetch=cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()    
    elif cp:
        cursor.execute('SELECT * FROM CACL2P')#.fetchone()
        #cursor.execute("SELECT 'sp.gr @ 60degF' FROM `KCL` WHERE 'sp.gr @ 60degF'="+str(SEARCH.get())).fetchone()
        #fetch = cursor.fetchone()
        fetch=cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()    
    elif cd:
        cursor.execute('SELECT * FROM CACL2D')#.fetchone()
        #cursor.execute("SELECT 'sp.gr @ 60degF' FROM `KCL` WHERE 'sp.gr @ 60degF'="+str(SEARCH.get())).fetchone()
        #fetch = cursor.fetchone()
        fetch=cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()    
    elif nacp:
        cursor.execute('SELECT * FROM NA_CAP')#.fetchone()
        #cursor.execute("SELECT 'sp.gr @ 60degF' FROM `KCL` WHERE 'sp.gr @ 60degF'="+str(SEARCH.get())).fetchone()
        #fetch = cursor.fetchone()
        fetch=cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
    elif nacd:
        cursor.execute('SELECT * FROM NA_CAD ')#.fetchone()
        #cursor.execute("SELECT 'sp.gr @ 60degF' FROM `KCL` WHERE 'sp.gr @ 60degF'="+str(SEARCH.get())).fetchone()
        #fetch = cursor.fetchone()
        fetch=cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()    


def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")
                
    
def Example():
    box.showinfo('Example','User should check setup\n documents for file: Examples.doc')

#++++++++++++++++++++++++END of salt cmma+++++++++++++++





menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New Project...", command=sayYes)
filemenu.add_command(label="New", command=sayYes)
filemenu.add_command(label="Open", command="")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)

editmenu =Menu(menu)
menu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Redo Ctrl+Y", command=sayYes)


viewmenu = Menu(menu)
menu.add_cascade(label="Tables", menu=viewmenu)
#logoc=PhotoImage(file='calculo.bmp')
viewmenu.add_command(label="Casing Tables" , command=casing)#, image=logoc)
viewmenu.add_separator()
viewmenu.add_command(label="NaCl Tables", command=nacl)
viewmenu.add_command(label="KCl Tables", command=kcl)
viewmenu.add_command(label="NH4Cl Tables", command=nhcl)
viewmenu.add_command(label="CaCl2-P Tables", command=cp)
viewmenu.add_command(label="CaCl2-D Tables", command=cd)
viewmenu.add_command(label="NaCl_CaCl2-P Tables", command=ncp)
viewmenu.add_command(label="NaCl_CaCl2-D Tables", command=ncd)
#viewmenu.add_command(label="CaCl2 Tables", command="")
viewmenu.add_separator()
viewmenu.add_command(label="API*", command="")
#-----------------------------------------------------------------------------------#
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)

helpmenu.add_command(label=" Documentation", command=ruth)#image=iconPhotoImage, compound="left")
helpmenu.add_command(label="Tutorial", command=buchi)
helpmenu.add_command(label="Examples", command=Example)
helpmenu.add_separator()
helpmenu.add_command(label="Online Support", command="")
helpmenu.add_command(label="Updates", command="")
helpmenu.add_separator()
helpmenu.add_command(label="About Brine Mixer", command=about)


#****Toolbar***********
toolbar = Frame(root, bg="RoyalBlue",bd=4)

insertButt = Button(toolbar, text="Calculo", command=Kalc,compound=LEFT)
#insertButt.config(image=calcula)
insertButt.pack(side=LEFT,padx=2,pady=2)

toolbar.pack(side=TOP,fill=X)


#****statusbar***********
statusbar=Frame(root)
statusbar.pack(side=BOTTOM,fill=X, expand=False)              
time1=''

clock=Label(statusbar,font=('arial',8,'italic'),anchor=E)
def tick():
    global time1
    time2=time.strftime('%H:%M:%S')
    if time2!=time1:
        time1=time2
        clock.config(text=time2)
    clock.after(200,tick)

tick()
status=Label(statusbar, text='Welcome to Brine Mixer ',bd=1,relief=RAISED,anchor=W)
status.pack(in_=statusbar, side=LEFT,fill=BOTH,expand=True)
clock.pack(in_=statusbar, side=RIGHT,fill=BOTH,expand=False)







#==================TEXT============================================
Tops = Frame(root, width=500,height=5,bd=8, bg="green", relief=RAISED)
Tops.pack(side=TOP)

f1=Frame(root, width=600, height= 1700, bd=8,bg="green", relief=RAISED, cursor="plus",highlightcolor='blue')
f1.pack(side=LEFT)

f2=Frame(root, width=200,height=700,bd=8, bg="green", relief=GROOVE)
f2.pack(side=RIGHT)
#+++++++++++++++++++++++Time++++++++++++++++++++++++
localtime=time.asctime(time.localtime(time.time()))
#=======================info===============================
lbLinfo=Label(Tops, font=("San Serif",15,"bold"), text="Created by Samuel Prince Akosa"
              ,fg='steel blue',bg='black',bd=10, anchor='w')
lbLinfo.grid(row=0,column=0)

#Timer=Label(root, font=("Verdana",7,"italic"), text=localtime
              #,fg='steel blue',bg='pink',bd=10, anchor='w')
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Timer.pack(side=BOTTOM)
              


#tick()
#status=Label(root, text='v1.0',bd=1,relief=RAISED,anchor=E)
#status.pack(in_=statusbar, side=LEFT,fill=BOTH,expand=True)
#clock.pack(in_=statusbar, side=RIGHT,fill=Y,expand=False)
#status2 =Label(clock,text= tick, bd=1, relief=SUNKEN, anchor=E)#relief is how

#status2.pack(side=RIGHT,fill=X)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++---------------------------

#Fop=Label(f1, text= 'Formation Pressure')
#Fop.pack(side=LEFT)
Fop=Label(f1,padx=2,pady=2,bd=4,fg="black",bg='green', font=('arial',8,'bold'),
            text='Formation Pressure').grid(row=1,column=0)

Fop1=Entry(f1,font=('arial',8,'bold'), bd=4, insertwidth=2,bg='white',textvariable=DoubleVar,justify='right')
#Fop1.pack(side=RIGHT,padx=5)
Fop1.grid(columnspan=2,row=1,column=1)
Fopunit=Button(f1,text='lbs/in2', bg='green',fg='black',padx=2,pady=2).grid(row=1,column=3)
#++++++++TD++++++++++++++
TrD=Label(f1,padx=2,pady=2,bd=4,fg="black",bg='green', font=('arial',8,'bold'),
            text='True Depth').grid(row=2,column=0)

TrD1=Entry(f1,font=('arial',8,'bold'), bd=4, insertwidth=2,bg='white',justify='right')
#Fop1.pack(side=RIGHT,padx=5)
TrD1.grid(columnspan=2,row=2,column=1)
TrDunit=Button(f1,text='feet',bg='green',fg='black', padx=2,pady=2).grid(row=2,column=3)
#---------TVD-----------------
TvDi=Label(f1,padx=2,pady=2,bd=4,fg="black",bg='green', font=('arial',8,'bold'),
            text='True Vertical Depth').grid(row=3,column=0)

TvDi1=Entry(f1,font=('arial',8,'bold'), bd=4, insertwidth=2,bg='white',justify='right')
#Fop1.pack(side=RIGHT,padx=5)
TvDi1.grid(columnspan=2,row=3,column=1)
TvDiunit=Button(f1,text='feet',bg='green',fg='black', padx=2,pady=2).grid(row=3,column=3)
#------casing od--------------
CasOd=Label(f1,padx=2,pady=2,bd=4,fg="black",bg='green', font=('arial',8,'bold'),
            text='Casing Outer diameter').grid(row=4,column=0)

CasOd1=Entry(f1,font=('arial',8,'bold'), bd=4, insertwidth=2,bg='white',justify='right')
#Fop1.pack(side=RIGHT,padx=5)
CasOd1.grid(columnspan=2,row=4,column=1)
CasOdunit=Button(f1,text='inches',bg='green',fg='black', padx=2,pady=2).grid(row=4,column=3)
#---------Casing Weight--------------
CasWt=Label(f1,padx=2,pady=2,bd=4,fg="black",bg='green', font=('arial',8,'bold'),
            text='Casing Norminal Weight').grid(row=5,column=0)

CasWt1=Entry(f1,font=('arial',8,'bold'), bd=4, insertwidth=2,bg='white',justify='right')
#Fop1.pack(side=RIGHT,padx=5)
CasWt1.grid(columnspan=2,row=5,column=1)
CasWtunit=Button(f1,text='lbs/ft',bg='green',fg='black', padx=2,pady=2).grid(row=5,column=3)

#---------formAdj--------------------------
FopAdji=Label(f1,padx=2,pady=2,bd=4,fg="black",bg='green', font=('arial',8,'bold'),
            text='User should enter the correction for the Formation pressure. if none given enter the value 100psi').grid(row=7,column=0, columnspan=4)

FopAdj=Label(f1,padx=2,pady=2,bd=4,fg="black",bg='green', font=('arial',8,'bold'),
            text='Formation Pressure Adjuster').grid(row=8,column=0)

FopAdj1=Entry(f1,font=('arial',8,'bold'), bd=4, insertwidth=2,bg='white',justify='right')
#Fop1.pack(side=RIGHT,padx=5)
#FopAdj1.set('100')
FopAdj1.grid(columnspan=2,row=8,column=1)
FopAdjunit=Button(f1,text='lbs/in2', bg='green',fg='black',padx=2,pady=2).grid(row=8,column=3)

#--------------------------------------------------
#Fp,TD,TVD, Cas_OD, Cas_Wt,FpA=float(Fop1.get()),float(TrD1.get()),float(TvDi1.get()), float(CasOd1.get()),float(CasWt1.get()),float(FopAdj1.get())
#Casing_Outer_Diameter,Casing_Norminal_Weight,Formation_pessure_adjuster


#Fopunit.pack(side=RIGHT,padx=5)
#Fop1.grid(columnspan=2)
#Formation_Pressure= float(input("Enter Formation Pressure in psi = "))

def press_grad():
    try:
        Fp,TVD, FpA=float(Fop1.get()),float(TvDi1.get()),float(FopAdj1.get())
        Pressure_gradient=(Fp+FpA)/TVD
        Pg=round(Pressure_gradient,2)
        #return('Age is approximately ' + str(count)+" " + 'years')
        return(' pressure gradient is =  ' +str(Pg) + ' psi/ft')
    except ValueError or TypeError:
        box.showinfo('No Value','User should insert value for TVD\nFormation pressure & Adjuster')
def dialog():
    box.showinfo('Pressure gradient', 'The '+press_grad())
Calcu1=Button(f1,text='Calculate Press gradient',bg='orange',fg='black',command=dialog, padx=2,pady=2).grid(row=1,column=5)

#------brine weight-----------

def brine_weight():
    try:
        Fp,TD,TVD, Cas_OD, Cas_Wt,FpA=float(Fop1.get()),float(TrD1.get()),float(TvDi1.get()), float(CasOd1.get()),float(CasWt1.get()),float(FopAdj1.get())
        Pressure_gradient=(Fp+FpA)/TVD
        Pg=round(Pressure_gradient,2)
        Brine_Weight=Pg/0.052
        BW=round(Brine_Weight,2)    
        return(' Brine Weight is = ' +str(BW) + ' lbs/gal')
    except ValueError or TypeError:
        box.showinfo('No value','User should input required values')
def dialog1():
    box.showinfo('Brine Weight', 'The '+brine_weight())  
Calcu2=Button(f1,text='Calculate Brine Weight',bg='orange',fg='black',command=dialog1, padx=2,pady=2).grid(row=3,column=5)

#----hole volume-------
def hole_vol():
#    Pressure_gradient=(Fp+FpA)/TVD
    try:
        
        Fp,TD,TVD, Cas_OD, Cas_Wt,FpA=float(Fop1.get()),float(TrD1.get()),float(TvDi1.get()), float(CasOd1.get()),float(CasWt1.get()),float(FopAdj1.get())
    except ValueError or TypeError:
        box.showinfo('No value', 'User should input required values')
    #import pandas
    #import xlrd
    #dbrine= pandas.read_excel('C:/Users/YINKA/Documents/samuel_akosa/Casing-Data-Sheet.xlsx')
    '''k=[]
    for i in range(len(dbrine['Casing Data Sheet'])):
        if dbrine['Casing Data Sheet'][i]==Cas_OD and dbrine['Unnamed: 1'][i]==Cas_Wt:
            k.append(i+2)
    j=k[-3]
#getting Casing capacity 
    Cas_cap=dbrine['Unnamed: 16'][j]
    Cas_Cap=round(Cas_cap,5)'''
    Database()
    #conn,cursor
    #gl=gg.cursor()#cursor object
    gl=cursor
    
    
       
    f=gl.execute('SELECT * FROM "Casing" ')
    fk=f.fetchall();
    gm=pandas.DataFrame(fk)
    #dbrine=gm
    cursor.close()
    conn.close()
    ki=[]
        #Cas_OD=20
        #Cas_Wt=169
    
    for i in range(len(gm[1])):
        
        if gm[1][i]==Cas_OD and gm[2][i]==Cas_Wt:
            ki.append(i+2)
    
    print(ki[-3])        
    j=ki[-3]    
    print(ki)
        #getting Casing capacity 
    Cas_cap=float(gm[17][j])
    Cas_Cap=round(Cas_cap,5)
    
    Pressure_gradient=(Fp+FpA)/TVD
    Pg=round(Pressure_gradient,2)
    Brine_Weight=Pg/0.052
    BW=round(Brine_Weight,2)
    def roundup(x):
        import math
        return (int(math.ceil(x/100.0))*100)
    Hole_volume=Cas_Cap*TD
    Hv=roundup(Hole_volume)
    return('Design Hole Volume is = ' +str(Hv) + ' bbl')
def dialog2():
    box.showinfo('Design Hole Volume', 'The '+ hole_vol())    
Calcu3=Button(f1,text='Calculate Hole Volume',bg='orange',fg='black',command=dialog2, padx=2,pady=2).grid(row=6,column=5)

#-----------------------brine volume-------------------------
def brine_vol():
#   Pressure_gradient=(Fp+FpA)/TVD
    try:
        Fp,TD,TVD, Cas_OD, Cas_Wt,FpA=float(Fop1.get()),float(TrD1.get()),float(TvDi1.get()), float(CasOd1.get()),float(CasWt1.get()),float(FopAdj1.get())
    except ValueError:
        box.showinfo('No input', 'User should input all required values')
    
    Database()
    gl=cursor
          
    f=gl.execute('SELECT * FROM "Casing" ')
    fk=f.fetchall()
    
    gm=pandas.DataFrame(fk)
    cursor.close()
    conn.close()
    #dbrine=gm
    
    ki=[]
          
    for i in range(len(gm[1])):
        
        if gm[1][i]==Cas_OD and gm[2][i]==Cas_Wt:
            ki.append(i+2)
    
    print(ki[-3])        
    j=ki[-3]    
    print(ki)
        #getting Casing capacity 
    Cas_cap=float(gm[17][j])
    Cas_Cap=round(Cas_cap,5)
    
    Pressure_gradient=(Fp+FpA)/TVD
    Pg=round(Pressure_gradient,2)
    Brine_Weight=Pg/0.052
    BW=round(Brine_Weight,2)
    
    
    def roundup(x):
        #import math
        return (int(math.ceil(x/100.0))*100)
    Hole_volume=Cas_Cap*TD
    Hv=roundup(Hole_volume)
    Brine_volume=3*Hv
    def round500(x):
        #import math
        k=int(math.ceil(x/500.0))*500
        h=k-x
        if h>=300:
            p=int(math.floor(x/500.0))*500
            return(p)
        else:
            return(k)
    BV=round500(Brine_volume)
    c1=Canvas(f1,height=300,width=300,
                bg='white')
    c1.grid(row=9,column=0)
    l1=c1.create_line(100,5,100,200 , width=5)#casing left line
    lk=c1.create_line(60,5,240,5)
    lb=c1.create_line(189,120,227,139, arrow=FIRST)#hole volume label line
    #lz=c1.create_polygon(210,200,200,200,200,180)
    d3=c1.create_text(249,153,font=('arial',8,'bold'),text='Hole\nVolume =' +str(Hv) +' bbl')
    lk=c1.create_line(60,5,240,5)#casing head line
    lg=c1.create_polygon(101,6,199,6,199,200,101,200, fill='cyan',tag='anime')
    lp=c1.create_polygon(100,200,102,203,100,203,108,205,
                     104,208,119,220,126,230,128,242,150,250,
                     155,246,165,250,172,245,180,250,185,245,188,249,
                     195,230,196,215,194,210,200,200,fill='cyan',tag='kilo')
    l2=c1.create_line(200,5,200,200 , width=5)#casing right line
    l3=c1.create_polygon(90,200,100,200,100,180)#casing shoe
    l4=c1.create_polygon(210,200,200,200,200,180)#casing shoe
    l5=c1.create_line(150,5,150,170,width=9)#tubing
    l7=c1.create_rectangle(100,150,150,160)#ist packer
    l8=c1.create_rectangle(200,150,150,160)#second packer
    l9=c1.create_line(100,150,150,160)#packer lines
    l10=c1.create_line(100,160,150,150)#packer lines
    l11=c1.create_line(200,150,150,160)#packer lines
    l2=c1.create_line(200,160,150,150)#packer lines
    lp=c1.create_line(100,200,102,203,100,203,108,205,104,208,119,220,126,230,128,242,150,250,155,246,165,250,172,245,180,250,185,245,188,249,195,230,196,215,194,210,200,200)
    d=c1.create_text(75,200,font=('arial',8,'bold'),text=str(Cas_OD)+'"')
    d1=c1.create_text(75,210,font=('arial',8,'bold'),text=str(Cas_Wt) +'#')
    d2=c1.create_text(55,269,font=('arial',8,'bold'),text='Well TD= ' +str(TD)+' ft')
    d5=c1.create_text(143,290,font=('arial',8,'bold'),text='Schematic of Well Profile')
    dt=c1.create_text(125,110,font=('arial',8,'italic'),text=' 1 brine\n volume ', tag='sen')
    dx=0
    dy=1
    
    #c1.pack()
    data=[['Pressure Gradient',Pg, 'psi/ft'],['Brine Weight',BW,'ppg'],['Calculated Hole Volume',Hole_volume,'bbl'],['Design Hole Volume',Hv,'bbl'],['Calculated Brine Volume',Brine_volume,'bbl'],['Design Brine Volume',BV,'bbl']]
    dk=pandas.DataFrame(data,columns=['Parameter','Value','Unit'],index=['1','2','3','4','5','6'])
    dq=str(dk)
    #print('\n')
    #print('--------------------------------------------------------------')
    #print('\n')
    #return(df)
    Calc1=Message(f1,font=('arial',8,'bold'),padx=2,pady=2, bd=4,text=dq,bg='white').grid(row=9,column=3)
    try:
        while True:
            c1.move('anime',dx,dy)
            c1.move('kilo',dx,dy)
            c1.move('sen',dx,dy)
            c1.after(400)
            c1.update()
    except:
        pass
    qy='As at '+localtime+'\t'+str(time.time())+ ' seconds'
    dw='Input values include the following\n\n'
    j='\n'
    dj='Formation Press='+ str(Fp)+' lbs/in2'+j+'True depth=' +str(TD)+'ft'+j+'True Vertical Depth='+str(TVD)+'ft'+j+'Casing Outer diameter= '+str(Cas_OD)+'"'+j+'Casing Weight ='+str(Cas_Wt)+'#'+j+'Formation Pressure Adjustment= '+str(FpA)+' lbs/in2'
    dy='Output Values include'
    dg='________________________'
    c2=str(c1)
    return(qy+j+j+dw+j+dj+j+j+j+dy+j+dg+j+j+j+dq+j+j+j+c2)
   # finally:

    
    #print('Pressure gradient = ',str(Pg) +' psi/ft')
    #print('Brine_Weight = ', str(BW) +' ppg')
    #print('The Hole Volume is = ' +str(Hv) + ' bbl')
#def dialog3():
    #box.showinfo('Brine volume', brine_vol())  
#Calcu3=Button(f1,text='Calculate Brine Volume',bg='orange',fg='black',command=dialog3, padx=2,pady=2).grid(row=8,column=5)
Calcu4=Button(f1,text='Calculate Brine Volume',bg='orange',fg='black',command=brine_vol, padx=2,pady=2).grid(row=8,column=5)
#Calc1=Text(f1,font=('arial',8,'bold'), bd=4, insertwidth=100,textvariable=Calcu4,bg='white').grid(row=8,column=6)











#----------------
lin=Label(f2,padx=2,pady=2,bd=4,fg="black",bg='green', font=('arial',8,'bold'),
            text='+++++++++++++++++++Salt Section+++++++++++++++++++++++++++++++++++++++++++++++++++++++++').grid(row=0,column=0, columnspan=10)

#-----------------------#
#f1=Frame(root, width=1400, height= 700, bg="green", relief=SUNKEN)
#f1.pack(side=LEFT)

# Create a Tkinter variable
tkvar = StringVar(root)
 
# Dictionary with options
choices = [ "KCL", "NACL",'NH4CL', "CACL2-PELADOW","CACL2-DOWFLAKES",'NACL_CACL2-PELADOW',"NACL_CACL2-DOWFLAKES"]
tkvar.set('KCL') # set the default option
 
popupMenu = OptionMenu(f2, tkvar, *choices)
hi=Label(f2,padx=2,pady=2,text="Choose a salt",fg='black',bg='green', font=('arial',8,'bold')).grid(row =5, column =0)
popupMenu.grid(row = 7, column =0)

#-----------------------#
lq=Label(f2,font=('arial',8,'bold'),text='Brine Weight',fg='black', bg='green',padx=2,pady=2).grid(row=2,column=0)
lv=Label(f2,font=('arial',8,'bold'), text= "Design Brine Volume",fg='black',bg='green',padx=2,pady=2).grid(row=3,column=0)
lqjunit=Button(f2,text='lbs/gal', bg='green',fg='black',padx=2,pady=2).grid(row=2,column=2)
lvunit=Button(f2,text='bbl', bg='green',fg='black',padx=2,pady=2).grid(row=3,column=2)
BQ=Entry(f2,font=('arial',8,'bold'), bd=4, insertwidth=4,bg='white',justify='right')
BQ.grid(row=2,column=1)
BV=Entry(f2,font=('arial',8,'bold'), bd=4, insertwidth=4,bg='white',justify='right')
BV.grid(row=3,column=1)
#Fop1.pack(side=RIGHT,padx=5)



def josh():
    global df
    try:
        Bf=float(BQ.get())
        BW=Bf
        hk=float(BV.get())
        brine_vol=hk
    except ValueError:
        box.showinfo('No Input','Input value of brine weight and desired volumes')
        
    #l=h.upper()
    
    if tkvar.get()=='KCL':
        p=[]
        for i in range(len(KCLr[1])):
            if KCLr[2][i]==BW:
                p.append(i)
                g=p[0]
                f=KCLr[3][g]
                y=KCLr[4][g]
                d=KCLr[7][g]
                w=KCLr[5][g]
                l=brine_vol*f
                q=l/2.2#unit in kg
                ki=q/1000#unit in Metric tonnes
                #1 trailer load is 100 metic tonnes
                ku=math.ceil(ki)#rounded up unit in metric tonnes
                k=ku*1.5#design metric tonnes
                Nt=k/20
                NT=math.ceil(Nt)#number of trailers
                t=y*brine_vol#Amt of water
                
                
                dat=[['solution Density',BW, 'lbs/gal'],['Desired brine volume',brine_vol,'bbl'],['KCL required',l,'lbm'],['KCL required',q,'kg'],['Design KCL required',k,'MT'],['Approx. No. of Trailers',NT,'trailer'],['Amount of water required',t,'bbl'],['% Conc. KCL',d,'%'],['Freezing Point',w,'degF']]
                df=pandas.DataFrame(dat,columns=['Parameter','Value','Unit'],index=['1','2','3','4','5','6','7','8','9'])
                Calc1=Label(f2,font=('arial',8,'bold'),padx=2,pady=2, bd=4,text=df,bg='white').grid(row=9,column=1,columnspan=10)
                ss=str(df)
                #print(df)
                
                break
            elif KCLr[2][i] !=BW:
                ju=min(KCLr[2])
                ja=max(KCLr[2])
                if BW<ja and BW>ju:
                    #from scipy.interpolate import interp1d
                    #import numpy as np
                    x=KCLr[2]
                    y=KCLr[3]
                    yd=KCLr[4]
                    d=KCLr[7]
                    w=KCLr[5]
                    #xi=x.as_matrix()
                    #x_interp=interp(y,x)
                    y_interp=np.interp(BW,x,y)#materials,KCl in lbm
                    yd_interp=np.interp(BW,x,yd)#water in galUS
                    d_interp=np.interp(BW,x,d)#Approx %KCL
                    w_interp=np.interp(BW,x,w)
                    l=brine_vol*y_interp#amount of kcl needed
                    q=l/2.2#unit in kg
                    ki=q/1000#unit in Metric tonnes
                #1 trailer load is 100 metic tonnes
                    ku=math.ceil(ki)#rounded up unit in metric tonnes
                    k=ku*1.5#design metric tonnes
                    Nt=k/20
                    NT=math.ceil(Nt)#number of trailers
                    t=yd_interp*brine_vol#amount of water requied
                    #print(y_interp)
                    #print(yd_interp)
                    #print(d_interp)
                    #print(l)
                    dat=[['solution Density',BW, 'lbs/gal'],['Desired brine volume',brine_vol,'bbl'],['KCL required',l,'lbm'],['KCL required',q,'kg'],['Design KCL required',k,'MT'],['Approx. No. of Trailers',NT,'trailer'],['Amount of water required',t,'bbl'],['% Conc. KCL',d_interp,'%'],['Freezing Point',w_interp,'degF']]
                    df=pandas.DataFrame(dat,columns=['Parameter','Value','Unit'],index=['1','2','3','4','5','6','7','8','9'])
                    Calc1=Label(f2,font=('arial',8,'bold'),padx=2,pady=2, bd=4,text=df,bg='white').grid(row=9,column=1,columnspan=10)
                    ss=str(df)
                    #print(df)
                    break
                else:
                    box.showinfo('KCL','Brine weight should be between '+str(ju)+' and '+str(ja))
                    break
    elif tkvar.get()=='NACL':
        p=[]
        for i in range(len(NaClr[1])):
            if NaClr[2][i]==BW:
                p.append(i)
                g=p[0]
                f=NaClr[3][g]
                y=NaClr[4][g]
                d=NaClr[7][g]
                w=NaClr[5][g]
                l=brine_vol*f
                q=l/2.2#unit in kg
                ki=q/1000#unit in Metric tonnes
                #1 trailer load is 100 metic tonnes
                ku=math.ceil(ki)#rounded up unit in metric tonnes
                k=ku*1.5#design metric tonnes
                Nt=k/20
                
                NT=math.ceil(Nt)#number of trailers
                t=y*brine_vol
                dat=[['solution Density',BW, 'lbs/gal'],['Desired brine volume',brine_vol,'bbl'],['NaCl required',l,'lbm'],['NaCL required',q,'kg'],['Design NaCL required',k,'MT'],['Approx. No. of Trailers',NT,'trailer'],['Amount of water required',t,'bbl'],['% Conc. NaCl',d,'%'],['Freezing Point',w,'degF']]
                df=pandas.DataFrame(dat,columns=['Parameter','Value','Unit'],index=['1','2','3','4','5','6','7','8','9'])
                Calc1=Label(f2,font=('arial',8,'bold'),padx=2,pady=2, bd=4,text=df,bg='white').grid(row=9,column=1,columnspan=10)
                ss=str(df)
                
                
                break
            elif NaClr[2][i] !=BW:
                ju=min(NaClr[2])
                ja=max(NaClr[2])
                if BW<ja and BW>ju:
                    #from scipy.interpolate import interp1d
                    #import numpy as np
                    x=NaClr[2]
                    y=NaClr[3]
                    yd=NaClr[4]
                    d=NaClr[7]
                    w=NaClr[5]
                    
                    y_interp=np.interp(BW,x,y)#materials,NaCl in lbm
                    yd_interp=np.interp(BW,x,yd)#water in galUS
                    d_interp=np.interp(BW,x,d)#Approx % NaCL
                    l=brine_vol*y_interp
                    w_interp=np.interp(BW,x,w)
                    q=l/2.2#unit in kg
                    ki=q/1000#unit in Metric tonnes
                #1 trailer load is 100 metic tonnes
                    ku=math.ceil(ki)#rounded up unit in metric tonnes
                    k=ku*1.5#design metric tonnes
                    Nt=k/20
                    NT=math.ceil(Nt)#number of trailers
                    t=yd_interp*brine_vol
                    dat=[['solution Density',BW, 'lbs/gal'],['Desired brine volume',brine_vol,'bbl'],['NaCl required',l,'lbm'],['NaCL required',q,'kg'],['Design NaCL required',k,'MT'],['Approx. No. of Trailers',NT,'trailer'],['Amt of water required',t,'bbl'],['% Conc. NaCl',d_interp,'%'],['Freezing Point',w_interp,'degF']]
                    df=pandas.DataFrame(dat,columns=['Parameter','Value','Unit'],index=['1','2','3','4','5','6','7','8','9'])
                    Calc1=Label(f2,font=('arial',8,'bold'),padx=2,pady=2, bd=4,text=df,bg='white').grid(row=9,column=1,columnspan=10)
                    ss=str(df)
                    
                 #   print(y_interp)
                  #  print(yd_interp)
                   # print(d_interp)
                    #print(l)
                    break
                
                else:
                    box.showinfo('NaCl','Brine weight should be between '+str(ju)+' and '+str(ja))
                    break
    elif tkvar.get()=='NH4CL':
        p=[]
        for i in range(len(NH4Cl[1])):
            if NH4Cl[2][i]==BW:
                p.append(i)
                g=p[0]
                f=NH4Cl[3][g]
                y=NH4Cl[4][g]
                d=NH4Cl[7][g]
                w=NH4Cl[5][g]
                l=brine_vol*f
                q=l/2.2#unit in kg
                ki=q/1000#unit in Metric tonnes
                #1 trailer load is 100 metic tonnes
                ku=math.ceil(ki)#rounded up unit in metric tonnes
                k=ku*1.5#design metric tonnes
                Nt=k/20
                NT=math.ceil(Nt)#number of trailers
                t=y*brine_vol
                dat=[['solution Density',BW, 'lbs/gal'],['Desired brine volume',brine_vol,'bbl'],['NH4CL required',l,'lbm'],['NH4CL required',q,'kg'],['Design NH4CL required',k,'MT'],['Approx. No. of Trailers',NT,'trailer'],['Amount of water required',t,'bbl'],['% Conc. NH4CL',d,'%'],['Freezing Point',w,'degF']]
                df=pandas.DataFrame(dat,columns=['Parameter','Value','Unit'],index=['1','2','3','4','5','6','7','8','9'])
                Calc1=Label(f2,font=('arial',8,'bold'),padx=2,pady=2, bd=4,text=df,bg='white').grid(row=9,column=1,columnspan=10)
                ss=str(df)
            #    print(f)
             #   print(y)
              #  print(d)
               # print(l)
                break
            elif NH4Cl[2][i] !=BW:
                ju=min(NH4Cl[2])
                ja=max(NH4Cl[2])
                if BW<ja and BW>ju:
                    #from scipy.interpolate import interp1d
                    #import numpy as np
                    x=NH4Cl[2]
                    y=NH4Cl[3]
                    yd=NH4Cl[4]
                    d=NH4Cl[7]
                    w=NH4Cl[5]
                    #xi=x.as_matrix()
                    #x_interp=interp(y,x)
                    y_interp=np.interp(BW,x,y)#materials,KCl in lbm
                    yd_interp=np.interp(BW,x,yd)#water in galUS
                    d_interp=np.interp(BW,x,d)#Approx %KCL
                    l=brine_vol*y_interp
                    q=l/2.2#unit in kg
                    ki=q/1000#unit in Metric tonnes
                #1 trailer load is 100 metic tonnes
                    ku=math.ceil(ki)#rounded up unit in metric tonnes
                    k=ku*1.5#design metric tonnes
                    Nt=k/20
                    NT=math.ceil(Nt)#number of trailers
                    w_interp=np.interp(BW,x,w)
                    wi=w_interp
                    t=yd_interp*brine_vol
                    dat=[['solution Density',BW, 'lbs/gal'],['Desired brine volume',brine_vol,'bbl'],['NH4CL required',l,'lbm'],['NH4CL required',q,'kg'],['Design NH4CL required',k,'MT'],['Approx. No. of Trailers',NT,'trailer'],['Amount of water required',t,'bbl'],['% Conc. NH4CL',d_interp,'%'],['Freezing Point',wi,'degF']]
                    df=pandas.DataFrame(dat,columns=['Parameter','Value','Unit'],index=['1','2','3','4','5','6','7','8','9'])
                    Calc1=Label(f2,font=('arial',8,'bold'),padx=2,pady=2, bd=4,text=df,bg='white').grid(row=9,column=1,columnspan=10)
                    ss=str(df)
                   
                    break
                
                else:
                    box.showinfo('NH4Cl','Brine weight should be between '+str(ju)+' and '+str(ja))
                    break
    elif tkvar.get()=='CACL2-PELADOW':
        p=[]
        for i in range(len(CaCl2P[1])):
            if CaCl2P[2][i]==BW:
                p.append(i)
                g=p[0]
                f=CaCl2P[3][g]
                y=CaCl2P[4][g]
                d=CaCl2P[7][g]
                w=CaCl2P[5][g]
                l=brine_vol*f
                q=l/2.2#unit in kg
                ki=q/1000#unit in Metric tonnes
                #1 trailer load is 100 metic tonnes
                ku=math.ceil(ki)#rounded up unit in metric tonnes
                k=ku*1.5#design metric tonnes
                Nt=k/20
                NT=math.ceil(Nt)#number of trailers
                t=y*brine_vol
                dat=[['solution Density',BW, 'lbs/gal'],['Desired brine volume',brine_vol,'bbl'],['CACL2-PELADOW required',l,'lbm'],['CACL2-PELADOW required',q,'kg'],['Design CACL2-PELADOW required',k,'MT'],['Approx. No. of Trailers',NT,'trailer'],['Amt of water required',t,'bbl'],['% Conc. CACL2-PELADOW',d,'%'],['Freezing Point',w,'degF']]
                df=pandas.DataFrame(dat,columns=['Parameter','Value','Unit'],index=['1','2','3','4','5','6','7','8','9'])
                Calc1=Label(f2,font=('arial',8,'bold'),padx=2,pady=2, bd=4,text=df,bg='white').grid(row=9,column=1,columnspan=10)
                ss=str(df)
                
               # print(f)
                #print(y)
                #print(d)
                #print(l)
                break
            elif CaCl2P[2][i] !=BW:
                ju=min(CaCl2P[2])
                ja=max(CaCl2P[2])
                if BW<ja and BW>ju:
                    #from scipy.interpolate import interp1d
                    #import numpy as np
                    x=CaCl2P[2]
                    y=CaCl2P[3]
                    yd=CaCl2P[4]
                    d=CaCl2P[7]
                    w=CaCl2P[5]
                    #xi=x.as_matrix()
                    #x_interp=interp(y,x)
                    y_interp=np.interp(BW,x,y)#materials,CaCl2-P in lbm
                    yd_interp=np.interp(BW,x,yd)#water in galUS
                    d_interp=np.interp(BW,x,d)#Approx %CaCL-P
                    l=brine_vol*y_interp
                    w_interp=np.interp(BW,x,w)
                    q=l/2.2#unit in kg
                    ki=q/1000#unit in Metric tonnes
                #1 trailer load is 100 metic tonnes
                    ku=math.ceil(ki)#rounded up unit in metric tonnes
                    k=ku*1.5#design metric tonnes
                    Nt=k/20
                    NT=math.ceil(Nt)#number of trailers
                    t=yd_interp*brine_vol
                    dat=[['solution Density',BW, 'lbs/gal'],['Desired brine volume',brine_vol,'bbl'],['CACL2-PELADOW required',l,'lbm'],['CACL2-PELADOW required',q,'kg'],['Design CACL2-PELADOW required',k,'MT'],['Approx. No. of Trailers',NT,'trailer'],['Amount of water required',t,'bbl'],['% Conc. CACL2-PELADOW',d_interp,'%'],['Freezing Point',w_interp,'degF']]
                    df=pandas.DataFrame(dat,columns=['Parameter','Value','Unit'],index=['1','2','3','4','5','6','7','8','9'])
                    Calc1=Label(f2,font=('arial',8,'bold'),padx=2,pady=2, bd=4,text=df,bg='white').grid(row=9,column=1,columnspan=10)
                    ss=str(df)
                    
                #    print(y_interp)
  #                  print(yd_interp)
   #                 print(d_interp)
    #                print(l)
                    break
                
                else:
                    box.showinfo('CaCl2-PELADOW','Brine weight should be between '+str(ju)+' and '+str(ja))
                    break
    elif tkvar.get()=='CACL2-DOWFLAKES':
        p=[]
        for i in range(len(CaCl2D[1])):
            if CaCl2D[2][i]==BW:
                p.append(i)
                g=p[0]
                f=CaCl2D[3][g]
                y=CaCl2D[4][g]
                d=CaCl2D[7][g]
                w=CaCl2D[5][g]
                l=brine_vol*f
                q=l/2.2#unit in kg
                ki=q/1000#unit in Metric tonnes
                #1 trailer load is 100 metic tonnes
                ku=math.ceil(ki)#rounded up unit in metric tonnes
                k=ku*1.5#design metric tonnes
                Nt=k/20
                NT=math.ceil(Nt)#number of trailers
                t=y*brine_vol
                dat=[['solution Density',BW, 'lbs/gal'],['Desired brine volume',brine_vol,'bbl'],['CACL2-DOWFLAKES required',l,'lbm'],['KCL required',q,'kg'],['Design CACL2-DOWFLAKES\n required',k,'MT'],['Approx. No.\n of Trailers',NT,'trailer'],['Amt of water required',t,'bbl'],['% Conc. CACL2-DOWFLAKES',d,'%'],['Freezing Point',w,'degF']]
                df=pandas.DataFrame(dat,columns=['Parameter','Value','Unit'],index=['1','2','3','4','5','6','7','8','9'])
                Calc1=Label(f2,font=('arial',8,'bold'),padx=2,pady=2, bd=4,text=df,bg='white').grid(row=9,column=1,columnspan=10)
                ss=str(df)
                
                #print(f)
                #print(y)
                #print(d)
                #print(l)
                break
            elif CaCl2D[2][i] !=BW:
                ju=min(CaCl2D[2])
                ja=max(CaCl2D[2])
                if BW<ja and BW>ju:
                    #from scipy.interpolate import interp1d
                    #import numpy as np
                    x=CaCl2D[2]
                    y=CaCl2D[3]
                    yd=CaCl2D[4]
                    d=CaCl2D[7]
                    w=CaCl2D[5]
                    #xi=x.as_matrix()
                    #x_interp=interp(y,x)
                    y_interp=np.interp(BW,x,y)#materials,CaCl2D in lbm
                    yd_interp=np.interp(BW,x,yd)#water in galUS
                    d_interp=np.interp(BW,x,d)#Approx %CaCl2D
                    l=brine_vol*y_interp
                    q=l/2.2#unit in kg
                    ki=q/1000#unit in Metric tonnes
                #1 trailer load is 100 metic tonnes
                    ku=math.ceil(ki)#rounded up unit in metric tonnes
                    k=ku*1.5#design metric tonnes
                    Nt=k/20
                    NT=math.ceil(Nt)#number of trailers
                    w_interp=np.interp(BW,x,w)
                    t=yd_interp*brine_vol
                    dat=[['solution Density',BW, 'lbs/gal'],['Desired brine volume',brine_vol,'bbl'],['CACL2-DOWFLAKES required',l,'lbm'],['CACL2-DOWFLAKES required',q,'kg'],['Design CACL2-DOWFLAKES required',k,'MT'],['Approx. No. of Trailers',NT,'trailer'],['Amt of water required',t,'bbl'],['% Conc. CACL2-DOWFLAKES',d_interp,'%'],['Freezing Point',w_interp,'degF']]
                    df=pandas.DataFrame(dat,columns=['Parameter','Value','Unit'],index=['1','2','3','4','5','6','7','8','9'])
                    Calc1=Label(f2,font=('arial',8,'bold'),padx=2,pady=2, bd=4,text=df,bg='white').grid(row=9,column=1,columnspan=10)
                    ss=str(df)
                    
                #    print(y_interp)
                 #   print(yd_interp)
                  #  print(d_interp)
                   # print(l)
                    break
                
                else:
                    box.showinfo('CACl2-DOWFLAKES','Brine weight should be between '+str(ju)+' and '+str(ja))
                    break
    elif tkvar.get()=='NACL_CACL2-PELADOW':
        p=[]
        for i in range(len(Na_CaP[1])):
            if Na_CaP[2][i]==BW:
                p.append(i)
                g=p[0]
                f=Na_CaP[3][g]
                y=Na_CaP[5][g]
                d=Na_CaP[4][g]
                w=Na_CaP[7][g]
                l=brine_vol*f
                dk=brine_vol*d
                q=l/2.2#unit in kg
                ki=q/1000#unit in Metric tonnes
                #1 trailer load is 100 metic tonnes
                ku=math.ceil(ki)#rounded up unit in metric tonnes
                k=ku*1.5#design metric tonnes
                qi=dk/2.2#unit in kg
                kw=qi/1000#unit in Metric tonnes
                #1 trailer load is 100 metic tonnes
                kj=math.ceil(kw)#rounded up unit in metric tonnes
                kn=kj*1.5#design metric tonnes
                Nt=(kn+k)/20
                NT=math.ceil(Nt)#number of trailers
                
                t=y*brine_vol
                dat=[['solution Density',BW, 'lbs/gal'],['Desired brine volume',brine_vol,'bbl'],['CACL required',l,'lbm'],['CACL2-PELADOW required',q,'kg'],['Design CACL2-PELADOW',k,'MT'],['NACL required',dk,'lbm'],['NACL required',qi,'kg'],['Design NACL required',kn,'MT'],['Approx. no. of Trailers',NT,'trailer'],['Amount of water required',t,'bbl'],['Freezing Point',w,'degF']]
                df=pandas.DataFrame(dat,columns=['Parameter','Value','Unit'],index=['1','2','3','4','5','6','7','8','9','10','11'])
                Calc1=Label(f2,font=('arial',8,'bold'),padx=2,pady=2, bd=4,text=df,bg='white').grid(row=9,column=1,columnspan=10)
                ss=str(df)
                
                #print(f)
                #print(y)
                #print(d)
                #print(l)
                break
            elif Na_CaP[2][i] !=BW:
                ju=min(Na_CaP[2])
                ja=max(Na_CaP[2])
                if BW<ja and BW>ju:
                    #from scipy.interpolate import interp1d
                    #import numpy as np
                    x=Na_CaP[2]
                    y=Na_CaP[3]
                    yd=Na_CaP[5]
                    d=Na_CaP[4]
                    w=Na_CaP[7]
                    #xi=x.as_matrix()
                    #x_interp=interp(y,x)
                    y_interp=np.interp(BW,x,y)#materials,CaCl2P in lbm
                    yd_interp=np.interp(BW,x,yd)#water in galUS
                    d_interp=np.interp(BW,x,d)# NaCl in lbm
                    l=brine_vol*y_interp
                    dk=brine_vol*d_interp
                    q=l/2.2#unit in kg
                    ki=q/1000#unit in Metric tonnes
                #1 trailer load is 100 metic tonnes
                    ku=math.ceil(ki)#rounded up unit in metric tonnes
                    k=ku*1.5#design metric tonnes
                    qi=dk/2.2#unit in kg
                    kw=qi/1000#unit in Metric tonnes
                #1 trailer load is 100 metic tonnes
                    kj=math.ceil(kw)#rounded up unit in metric tonnes
                    kn=kj*1.5#design metric tonnes
                    Nt=(kn+k)/20
                    NT=math.ceil(Nt)#number of trailers
                    w_interp=np.interp(BW,x,w)
                    t=yd_interp*brine_vol
                    di=d_interp*brine_vol
                    dat=[['solution Density',BW, 'lbs/gal'],['Desired brine volume',brine_vol,'bbl'],['CACL2-P required',l,'lbm'],['CACL2-PELADOW required',q,'kg'],['Design CACL2-PELADOW',k,'MT'],['NACL required',dk,'lbm'],['NACL required',qi,'kg'],['Design NACL required',kn,'MT'],['Approx. no. of Trailers',NT,'trailer'],['Amount of water required',t,'bbl'],['Freezing Point',w_interp,'degF']]
                    df=pandas.DataFrame(dat,columns=['Parameter','Value','Unit'],index=['1','2','3','4','5','6','7','8','9','10','11'])
                    Calc1=Label(f2,font=('arial',8,'bold'),padx=2,pady=2, bd=4,text=df,bg='white').grid(row=9,column=1,columnspan=10)
                    ss=str(df)
                    
                 #   print(y_interp)
                  #  print(yd_interp)
                   # print(d_interp)
                    #print(l)
                    break
                
                else:
                    box.showinfo('NaCl_CaCl2-PELADOW','Brine weight should be between '+str(ju)+' and '+str(ja))
                    break
    elif tkvar.get()=='NACL_CACL2-DOWFLAKES':
        p=[]
        for i in range(len(Na_CaD[1])):
            if Na_CaD[2][i]==BW:
                p.append(i)
                g=p[0]
                f=Na_CaD[3][g]
                y=Na_CaD[5][g]
                d=Na_CaD[4][g]
                w=Na_CaD[7][g]
                l=brine_vol*f
                dk=brine_vol*d
                q=l/2.2#unit in kg
                ki=q/1000#unit in Metric tonnes
                #1 trailer load is 100 metic tonnes
                ku=math.ceil(ki)#rounded up unit in metric tonnes
                k=ku*1.5#design metric tonnes
                qi=dk/2.2#unit in kg
                kw=qi/1000#unit in Metric tonnes
                #1 trailer load is 100 metic tonnes
                kj=math.ceil(kw)#rounded up unit in metric tonnes
                kn=kj*1.5#design metric tonnes
                Nt=(kn+k)/20
                NT=int(math.ceil(Nt))#number of trailers
                t=y*brine_vol
                dat=[['solution Density',BW, 'lbs/gal'],['Desired brine volume',brine_vol,'bbl'],['CACL2-DOWFLAKES required',l,'lbm'],['CACL2-PELADOW required',q,'kg'],['Design CACL2-PELADOW',k,'MT'],['NACL required',dk,'lbm'],['NACL required',qi,'kg'],['Design NACL required',kn,'MT'],['Approx. no. of Trailers',NT,'trailer'],['Amount of water required',t,'bbl'],['Freezing Point',w,'degF']]
                df=pandas.DataFrame(dat,columns=['Parameter','Value','Unit'],index=['1','2','3','4','5','6','7','8','9','10','11'])
                ss=str(df)
                
               # print(f)
               # print(y)
               # print(d)
                #print(l)
                break
            elif Na_CaD[2][i] !=BW:
                ju=min(Na_CaD[2])
                ja=max(Na_CaD[2])
                if BW<ja and BW>ju:
                    #from scipy.interpolate import interp1d
                    #import numpy as np
                    x=Na_CaD[2]
                    y=Na_CaD[3]
                    yd=Na_CaD[5]
                    d=Na_CaD[4]
                    w=Na_CaD[7]
                    #xi=x.as_matrix()
                    #x_interp=interp(y,x)
                    y_interp=np.interp(BW,x,y)#materials,CaClD in lbm
                    yd_interp=np.interp(BW,x,yd)#water in galUS
                    d_interp=np.interp(BW,x,d)#Approx %NaCl
                    l=brine_vol*y_interp
                    dk=brine_vol*d_interp
                    q=l/2.2#unit in kg
                    ki=q/1000#unit in Metric tonnes
                    #1 trailer load is 100 metic tonnes
                    ku=math.ceil(ki)#rounded up unit in metric tonnes
                    k=ku*1.5#design metric tonnes
                    qi=dk/2.2#unit in kg
                    kw=qi/1000#unit in Metric tonnes
                #1 trailer load is 100 metic tonnes
                    kj=math.ceil(kw)#rounded up unit in metric tonnes
                    kn=kj*1.5#design metric tonnes
                    Nt=(kn+k)/20
                    NT=int(math.ceil(Nt))#number of trailers
                    w_interp=np.interp(BW,x,w)
                    t=yd_interp*brine_vol
                    di=d_interp*brine_vol
                    dat=[['solution Density',BW, 'lbs/gal'],['Desired brine volume',brine_vol,'bbl'],['CaCL2-D required',l,'lbm'],['CACL2-PELADOW required',q,'kg'],['Design CACL2-PELADOW',k,'MT'],['NACL required',dk,'lbm'],['NACL required',qi,'kg'],['Design NACL required',kn,'MT'],['Approx. no. of Trailers',NT,'trailer'],['Amount of water required',t,'bbl'],['Freezing Point',w_interp,'degF']]
                    df=pandas.DataFrame(dat,columns=['Parameter','Value','Unit'],index=['1','2','3','4','5','6','7','8','9','10','11'])
                    Calc1=Label(f2,font=('arial',8,'bold'),padx=2,pady=2, bd=4,text=df,bg='white').grid(row=9,column=1,columnspan=10)
                    ss=str(df)
                    break
                
                else:
                    box.showinfo('NaCl_CaCl2-DOWFLAKES','Brine weight should be between '+str(ju)+' and '+str(ja))
                    break
    ji='\n'
    dp='Input Values include \n'
    dfg='Brine Weight or Solution density = ' +str(BW) +' lbs/gal\n'+'Design Brine Volume = '+str(brine_vol)+ ' bbl'            
    dr='\nOutput values include \n_____________________________\n'+ str(df)
    return(ji+dp+ji+dfg+ji+ji+dr+ji)

#josh()

def change_dropdown(*args):
    #print( tkvar.get() )
    #if tkvar.get()=='KCL':
    #   print(5+2)
    josh()
    
# link function to change dropdown
tkvar.trace('w', change_dropdown)





#-----------------------
def output():
    try:
        kt="Brine_mix_"+str(time.time())+'.doc'
        d=brine_vol()
        box.showinfo('Output', 'The  report file '+ kt +' already created')
        file=open(kt,'w+')
        file.write('----------Brine Volume Section---------------')
        file.write('\n\n')
        file.write(d)
        file.close()
    except:
        box.showinfo('No value',"User should input values")
    
def printo():
    try:
       qt="Salt_Concentration_"+str(time.time())+'.doc'
       qd=josh()
       qy='As at '+localtime+'\t'+str(time.time())+ ' seconds'
       box.showinfo('Output', 'The  report file '+ qt +' already created')
       file=open(qt,'w+')
       file.write(qy)
       file.write('\n\n')
       file.write(qd)
       file.close()
    except:
        box.showinfo('No value',"User should input values")
    
    
reportButt=Button(toolbar,text='Brine Vol. Report',command=output)
reportButt.pack(side=LEFT, padx=2,pady=2)
printButt = Button(toolbar, text="Salt Conc. Report", command=printo)
printButt.pack(side=LEFT, padx=2,pady=2)
    
scrollbar = Scrollbar(root, orient=VERTICAL)
#listbox = Listbox(master, fg='black',bg='green',yscrollcommand=scrollbar.set)
#scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
root.mainloop()