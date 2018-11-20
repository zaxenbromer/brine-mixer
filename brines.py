# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:46:30 2018

@author: YINKA
"""

print('A program created by SAMUEL AKOSA to compute the Brine volume')
print('------------------------------------------------------------------------------------')
print('\n')
print('\n')
print('\n')
Formation_Pressure=float(input('Enter Formation Pressure in psi  = '))
True_Depth=float(input('Enter True_depth in ft  = '))
True_Vertical_Depth=float(input('Enter True Vertical depth in ft  = ' ))
Casing_Outer_Diameter =float(input('Enter Production Casing Outer Diameter (casing OD) in inches = '))
Casing_Norminal_Weight =float(input('Enter Production Casing Norminal Weight in lbs/ft  = ' ))
print('User should enter the correction for the Formation pressure. if none given enter the value 100psi')
Formation_pessure_adjuster=float(input("Enter Formation pressure adjuster/correction in psi = "))
#Fp=float(Fop1.get())
Fp,TD,TVD, Cas_OD, Cas_Wt,FpA=Formation_Pressure,True_Depth,True_Vertical_Depth, Casing_Outer_Diameter,Casing_Norminal_Weight,Formation_pessure_adjuster

import pandas
import xlrd
 
dbrine= pandas.read_excel('C:/Users/YINKA/Documents/samuel_akosa/Casing-Data-Sheet.xlsx')
#print(dbrine.columns)

#count=0
k=[]
for i in range(len(dbrine['Casing Data Sheet'])):
    if dbrine['Casing Data Sheet'][i]==Cas_OD and dbrine['Unnamed: 1'][i]==Cas_Wt:
        #count=count+1
        k.append(i+2)
j=k[-3]
#print(j)
#getting Casing capacity 
Cas_cap=dbrine['Unnamed: 16'][j]
Cas_Cap=round(Cas_cap,5)
#print(g)

def brine_calc(Fp,TD,TVD, Cas_Cap,FpA):
    Pressure_gradient=(Fp+FpA)/TVD
    Pg=round(Pressure_gradient,2)
    Brine_Weight=Pg/0.052
    BW=round(Brine_Weight,2)
    def roundup(x):
        import math
        return (int(math.ceil(x/100.0))*100)
    Hole_volume=Cas_Cap*TD
    Hv=roundup(Hole_volume)
    Brine_volume=3*Hv
    def round500(x):
        import math
        k=int(math.ceil(x/500.0))*500
        h=k-x
        if h>=300:
            p=int(math.floor(x/500.0))*500
            return(p)
        else:
            return(k)
    BV=round500(Brine_volume)
    data=[['Pressure Gradient',Pg, 'psi/ft'],['Brine Weight',BW,'ppg'],['Design Hole Volume',Hv,'bbl'],['Design Brine Volume',BV,'bbl']]
    df=pandas.DataFrame(data,columns=['Parameter','Value','Unit'],index=['1','2','3','4'])
    print('\n')
    print('--------------------------------------------------------------')
    print('\n')
    print(df)
    print('Pressure gradient = ',str(Pg) +' psi/ft')
    print('Brine_Weight = ', str(BW) +' ppg')
    
    
brine_calc(Fp,TD,TVD, Cas_Cap,FpA)

def amountOsalt(Brine_volume,BW):
    from scipy.interpolate import interpld
    