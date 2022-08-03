# encoding:utf-8
import pandas as pd
import random
import math


def uygunlukKontrol(mevcutSaat, dersUzunlugu):
    if(mevcutSaat <12 and mevcutSaat + dersUzunlugu <=12):
        return True
    elif(mevcutSaat >= 13 and mevcutSaat + dersUzunlugu <= 17):
        return True
    elif(mevcutSaat >= 17 and mevcutSaat + dersUzunlugu <= 22):
        return True
    else:
        return False

def karsilastir(dersKodu, dersProgrami): #False İçinde Yok Demek
    if(int(len(dersProgrami)) == 0):
        return False 
    else:
        j = int(len(dersProgrami))-1
        while True:
            if(dersKodu == dersProgrami['DersKodu'][j]):
                return True # İçinde Var Demek
            else:
                j -= 1
            if j < 0:
                return False
                break    

def saatGunKontrol(saat, dersUzunlugu, gun, dersProgrami): # True Eklenebilir Demek 
    if(int(len(dersProgrami)) == 0):
        return True
    else:
        j = int(len(dersProgrami))-1
        saatX = 0
        while True:
            tempSaat = dersProgrami['Ders Saati'][j]
            saatX = int(str(tempSaat[0]) + str(tempSaat[1]))
                
            if(gun == dersProgrami['Gun'][j] and saatX == saat):
                    
                return False # İçinde Var Demek
            elif(dersUzunlugu == 3 and((saat - 1 == saatX or saat - 2 == saatX) or ((saat + 1 == saatX or saat + 2 == saatX)))):
                return False
            elif(dersUzunlugu == 2 and (saat- 1 == saatX or saat + 1 == saatX)):
                return False
            else:
                j -= 1
            if j < 0:
                return True
                break

"""
def donguMusaitlik(uzunluk, dersProgrami):

    if(int(len(dersProgrami)) == 0):
        return True
    kontrol = True # Boş yer var demek
    gunler = ['Pazartesi', 'Sali','Carsamba', 'Persembe', 'Cuma', 'Cumartesi']
    sonuc = 0
    sayacGun = 0
    while sayacGun < 6:
        i = 0
        while i < int(len(dersProgrami)):
            tempSaat = dersProgrami['Ders Saati'][i]
            saatBaslangic = int(str(tempSaat[0]) + str(tempSaat[1]))

            if(uzunluk == 3 and gunler[sayacGun] == dersProgrami['Gun'][i] and (saatBaslangic == 9 or saatBaslangic == 10 or saatBaslangic == 11 or saatBaslangic == 15 or saatBaslangic == 16)):
                kontrol = False
                print("Girdi 3")
            elif(uzunluk == 2 and gunler[sayacGun] == dersProgrami['Gun'][i] and(saatBaslangic == 10 or saatBaslangic == 11 or saatBaslangic == 16)):
                kontrol = False
                print("Girdi 2")
            else:
                return True
            
            i += 1
        sayacGun += 1
        if(sayacGun >= 6):
            return False
"""
sinif = 2
gunduz = True
gameOver = False

def dersProgramiOlustur(fakulteIsim, bolumIsim):
    global sinif
    global gunduz
    global gameOver

    if(gameOver):
        gameOver = False
        exit()
    fileName = ""

    if(fakulteIsim == "Mühendislik Fakültesi"):
        fileName = 'Dersler_Veri.csv'
        fileNameDerslik = 'Derslikler_Muhendislik_Bilgisayar.csv'
    elif fakulteIsim == "Yabancı Dil Fakültesi":
        fileName = 'Ders_Listesi_Yabanci_Dil.csv'
    elif fakulteIsim == "Fen Fakültesi":
        fileName = 'Ders_Listesi_Fen.csv'
    elif fakulteIsim == "Sosyal Bilimler Fakültesi":
        fileName = 'Ders_Listesi_Sosyal_Bilimler.csv'
    elif fakulteIsim == "Tıp Fakültesi":
        fileName = 'Ders_Listesi_Tip.csv'
    
    
    dersListesiDf = pd.read_csv(fileName, sep = r';', skipinitialspace = True, encoding= 'latin1')
    dersliklerDF = pd.read_csv(fileNameDerslik, sep = r';', skipinitialspace = True, encoding= 'latin1')
    
    #print(dersListesiDf)
    dersProgrami = pd.DataFrame(columns=['DersKodu', 'DersAdi', 'DersiVeren', 'DersUzunluk', 'Gun', 'Ders Saati', 'Derslik', 'AKTS', 'Donem']) #Yeni Program Dataframesi
    i = 0
    sayac = 0
    dersSayisi = 0
    sendBolumName = bolumIsim

    
    if gunduz:
        bolumIsim = bolumIsim + " Programı"
    else:
        bolumIsim = bolumIsim + " (İ.Ö.) Programı"

    if bolumIsim == "Bilgisayar Mühendisliği (İ.Ö.) Programı":
        bolumIsim = "Bilgisayar Mühendisliði (Ý.Ö.) Programý"
    elif bolumIsim == "Bilgisayar Mühendisliği Programı":
        bolumIsim = "Bilgisayar Mühendisliði Programý"

    while i < int(len(dersListesiDf)):
        if(int(dersListesiDf['Donem'][i]) == sinif and (bolumIsim == dersListesiDf['AcildigiProgram'][i]) and int(dersListesiDf['DersUzunluk'][i]) <= 3):
            dersSayisi += 1
        i += 1
    ######
    print(dersSayisi)
    i = 0
    sayaccc = 0
    while True:
        rastgeleDers = random.randint(0, int(len(dersListesiDf))-1)
        rastgeleDerslik = random.randint(0, (int(len(dersliklerDF))-1))
        if(gunduz == True):
            rastgeleSaat = random.randint(9, 17)
            gunler = ['Pazartesi', 'Sali', 'Carsamba', 'Persembe', 'Cuma', 'Cumartesi', 'Pazar']
        else:
            rastgeleSaat = random.randint(17, 22)
            gunler = ['Pazartesi', 'Sali', 'Carsamba', 'Persembe', 'Cuma', 'Cumartesi', 'Pazar']
        
        
        gun = random.choice(gunler)

        if rastgeleSaat == 12 or rastgeleSaat == 22 or (gunduz == True and rastgeleSaat == 17):
            continue

        if(karsilastir(dersListesiDf['DersKodu'][rastgeleDers], dersProgrami) ):
            continue
        else:
            sayaccc += 1
            if(sayaccc > 20000 ):
                if(sinif == 8 and gunduz == False):
                    sinif = 8
                    gunduz = False
                    dersProgramiOlustur(fakulteIsim, sendBolumName)
                else:
                    dersProgramiOlustur(fakulteIsim, sendBolumName) ###########################################################
        
            i = rastgeleDers
            if int(dersListesiDf['DersUzunluk'][i]) > 3:
                continue

            elif uygunlukKontrol(rastgeleSaat, dersListesiDf['DersUzunluk'][i]) and saatGunKontrol(rastgeleSaat, int(dersListesiDf['DersUzunluk'][i]), gun, dersProgrami) and int(dersListesiDf['Donem'][i]) == sinif and dersListesiDf['AcildigiProgram'][i] == bolumIsim:
                if rastgeleSaat < 10:
                    joinClock = str("0") + str(rastgeleSaat) + ":00-" + str(rastgeleSaat + int(dersListesiDf['DersUzunluk'][i])) + ":00"
                else:
                    joinClock = str(rastgeleSaat) + ":00-" + str(rastgeleSaat + int(dersListesiDf['DersUzunluk'][i])) + ":00"
                
                dersProgrami = dersProgrami.append({'DersKodu': dersListesiDf.at[i,'DersKodu'], 'DersAdi': dersListesiDf.at[i,'DersAdi'],
                 'DersiVeren': dersListesiDf.at[i,'DersiVeren'], 'DersUzunluk': dersListesiDf.at[i,'DersUzunluk'],
                 'Gun': gun ,'Ders Saati': joinClock,'Derslik': dersliklerDF.at[rastgeleDerslik, 'Derslik'], 'AKTS': dersListesiDf.at[i,'AKTS'],
                 'Donem': dersListesiDf.at[i,'Donem']}, ignore_index=True)
                sayac += 1

        if (sayac >= dersSayisi-1):
            break
    
    print("------------\n\n\n")
    if(gunduz == True):
        print(str(sinif) + ". Sınıf Örgün Öğretim Programı...")
        gunduz = False
        print(dersProgrami)
        dersProgramiOlustur(fakulteIsim, sendBolumName)
    else:
        print(str(sinif) + ". Sınıf İkinci Öğretim Programı...")
        print(dersProgrami)

    if(sinif == 8 and gunduz == False):
        print("Bittiiii")
        gameOver = True
        sinif = 8
        gunduz = False
        return 0
    else:
        if(sinif < 4):
            sinif += 2
            gunduz = True
            dersProgramiOlustur(fakulteIsim, sendBolumName)

    

    ###########


def anaMenu():

    while True:
        print("\n***************************************")
        print("Ders Hazırlama Programına Hoş Geldiniz")
        print("***************************************")
        
        print("1- Ders Programı Hazırla")
        print("2- Kayıtlı Fakülteleri Gör")
        print("3- Nasıl Çalışır")
        print("4- Program Hakkında")
        print("5- Çıkış")

        choice = int(input("\nLütfen Bir Seçenek Seçiniz(1,2,3,4,5): "))

        if choice == 1:
            while True:
                global sinif
                global gunduz
                sinf = 1
                gunduz = True
                print("\n*** Ders Programı Hazırlama Menüsü ***\n")
                print("1- Mühendislik Fakültesi")
                print("2- Yabancı Dil Fakültesi")
                print("3- Fen Fakültesi")
                print("4- Sosyal Bilimler Fakültesi")
                print("5- Tıp Fakültesi")
                print("6- Ana Menüye Dön")

                choice2 = int(input("\nLütfen Bir Seçenek Seçiniz(1,2,3,4,5,6): "))

                if choice2 == 1:
                    #dersProgramiOlustur("Muhendislik Fakültesi")
                    #exit()
                    while True:
                        print("\n*** Mühendislik Bölümleri ***\n")
                        print("1- Bilgisayar Mühendisliği Programı")
                        print("2- Makine Mühendisliği Programı")
                        print("3- Elektrik-Elektronik Mühendisliği Programı")
                        print("4- İnşaat Mühendisliğ Programı")
                        print("5- Kimya Mühendisliği Programı")
                        print("6- Çevre Mühendisliği Programı")
                        print("7- Endüstri Mühendisliği Programı")
                        print("8- Metalurji ve Malzeme Mühendisliği Programı")
                        print("9- Yazılım Mühendisliği Programı")
                        print("10- Çıkış")

                        choice3 = int(input("\nLütfen Bir Seçenek Seçiniz(1,2,3,...,10): "))

                        if choice3 == 1:
                            dersProgramiOlustur("Mühendislik Fakültesi", "Bilgisayar Mühendisliği")
                        elif choice3 == 2:
                            dersProgramiOlustur("Mühendislik Fakültesi", "Makine Mühendisliği")
                        elif choice3 == 3:
                            dersProgramiOlustur("Mühendislik Fakültesi", "Elektrik-Elektronik Mühendisliği")
                        elif choice3 == 4:
                            dersProgramiOlustur("Mühendislik Fakültesi", "İnşaat Mühendisliği")
                        elif choice3 == 5:
                            dersProgramiOlustur("Mühendislik Fakültesi", "Kimya Mühendisliği")
                        elif choice3 == 6:
                            dersProgramiOlustur("Mühendislik Fakültesi", "Çevre Mühendisliği")
                        elif choice3 == 7:
                            dersProgramiOlustur("Mühendislik Fakültesi", "Endüstri Mühendisliği")
                        elif choice3 == 8:
                            dersProgramiOlustur("Mühendislik Fakültesi", "Metalurji ve Malzeme Mühendisliği")
                        elif choice3 == 9:
                            dersProgramiOlustur("Mühendislik Fakültesi", "Yazılım Mühendisliği")
                        elif choice3 == 10:
                            exit()
                        else:
                            print("Yanlış bir değer girdiniz. Lütfen 1-10 arasında bir sayi giriniz !")
                            continue
                    
                elif choice2 == 2:
                    dersProgramiOlustur("Yabancı Dil Fakültesi")
                elif choice2 == 3:
                    dersProgramiOlustur("Fen Fakültesi")
                elif choice2 == 4:
                    dersProgramiOlustur("Sosyal Bilimler Fakültesi")
                elif choice2 == 5:
                    dersProgramiOlustur("Tıp Fakültesi")
                elif choice2 == 6:
                    break
                else:
                    print("Yanlış bir değer girdiniz. Lütfen 1-6 arasında bir sayi giriniz !")
                    continue
        elif choice == 2:
            print("\nMühendislik Fakültesi")
            print("Sosyal Bilimler Fakültesi")
            print("Fen Bilimleri Fakültesi")
        elif choice == 3:
            print("\nProgramın olduğu klasörde formata uygun bir şekilde herhangi bir fakültenin CSV dosyası ve ilgili Fakültenin Derslikleri Girilir.")
            print("Daha sonrasından programın menüsünden adımlar takip edilerek ders programı oluşturulur.")
        elif choice == 4:
            print("Bu program Berfin Sayılır Tarafından Geliştirilmektedir.")
            print("Detaylı Bilgi için mail atabilirsiniz. E-mail: brfnsylr@gmail.com")
        elif choice == 5:
            print("Programdan Çıkış Yapılıyor, İyi Günler.\n")
            break
        else:
            print("Yanlış bir değer girdiniz. Lütfen 1-5 arasında bir sayi giriniz !")
            continue


    

anaMenu()