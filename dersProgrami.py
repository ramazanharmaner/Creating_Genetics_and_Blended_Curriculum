import csv
from fileinput import filename
from turtle import Turtle
import pandas as pd


#Öncelikleri CSV den Okuyup Belirleyen Fonksiyon
def OncelikBelirle():
    dosyaAdi ='Oncelik_Sirasi.csv'
    data = pd.read_csv(dosyaAdi, sep = r';', skipinitialspace = True, encoding= 'latin1')

    boyut = len(data)
    oncelikSira = 1
    i = 0
    while True:
        if(data['Oncelik'][i] == oncelikSira):
            CreateProgram(data['Ad'][i])
        
        if(i == boyut -1 and oncelikSira<4):
            i = 0
            oncelikSira += 1 
        i += 1
        if(oncelikSira >= 4):
            break



#Ders Programı Oluşturma Fonksiyonu
def CreateProgram(name):
    fileName ='Eski_Program.csv'
    data = pd.read_csv(fileName, sep = r';', skipinitialspace = True, encoding= 'latin1')
    global Yeni_Ders
    boyut = len(data)

    for i in range(boyut):
        if(data['Hoca'][i] == name):
            #satir = data.iloc[[i]]
            Yeni_Ders = Yeni_Ders.append({'Gun': data.at[i,'Gun'], 'Hoca': data.at[i,'Hoca'], 'Ders': data.at[i,'Ders'], 'Saat': data.at[i,'Saat']}, ignore_index=True) #ekleme
            Yeni_Ders.to_csv('Yeni_Program.csv')


Yeni_Ders = pd.DataFrame(columns=['Gun', 'Hoca', 'Ders', 'Saat']) #Yeni Program Dataframesi

OncelikBelirle()