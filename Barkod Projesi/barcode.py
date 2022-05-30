"""
--- openCV, Pyzbar ve Time paketlerimizi dosyaya ekliyoruz---
openCV : OpenCV, gerçek zamanlı uygulamaların yapımında kullanılan tum görüntü-görme temelli açık kodlu bir kütüphane olarak karşımıza çıkmaktadır ve bu alanın öncüsü bir kütüphanedir.

Pyzbar:Barkod çözme işlevini barkodu algılamak ve kodunu çözmek için kullanilir.
"""

import cv2
from pyzbar.pyzbar import decode
import time
import sqlite3 as db
# Hata alinan kodlar
from arayuz import *
from tkinter import messagebox

connection = db.connect('kayitlar.db')
cursor = connection.cursor()
cursor.execute("SELECT Barkod_Numarasi FROM kayitlar")
""" 
Burada imlecimizin bir methodu olan fetchall() methodu ile SELECT Barkod_Numarasi FROM kayitlar 
sorgumuzdaki verileri cekip used_codes adindaki degiskene atadik.
"""
used_codes = cursor.fetchall()
""" 
print(used_codes) Calistirildiginda bir dizinin icinde her elemani Tuple olan veri setleri karsimiza cikti. 
Bu used_codes adli listemizin elemanlari uzerinde gezinip 0. indislerini barkod listemize ekledik.
"""
barkodList = []
for item in used_codes:
    barkodList.append(item[0])
#print(barkodList)

#cap = cv2.VideoCapture(0) satırı, varsayılan webcam cihazını aktif hale getirerek, görüntüleri yakalamasını sağlamaktadır.
cap = cv2.VideoCapture(0)
#cap.set() metodu ile görüntünün en ve yükseklik değerleri belirleniyor.
cap.set(3,640) #en
cap.set(4,640) #yukseklik


#Sonsuz while döngümüzün içinde görüntü yakalama işlemi cap.read() metodu tarafından gerçekleştirilmekte ve “frame” değişkenine aktarılmaktadır.
camera =True
while camera == True :
    success, frame = cap.read()
    for code in decode(frame):
        """ 
        Okutulan barkodlar utf-8 formati ile birlikte barcode1 degiskenine atanir. 
        Ve barkod barkod listesinde olup olmama durumu kontrol edildi.
        Eger yoksa yeni kayit acilacak.
        """
        barcode1 = code.data.decode('utf-8')
        if barcode1 not in barkodList:
            print(barcode1)
            #hata alinan kod
            urunKayitArayuz()
            #time.sleep(2) kodlarin islenmesi durumunda 2 saniye duraklar.
            time.sleep(2)
        elif barcode1 in barkodList:
            print()
            messagebox.showwarning('Warning!', 'This barcode has been already read.. ' + str(barcode1))
            time.sleep(2)
        else:
            pass
    #cv2.imshow() metodu barkodun görünür hale getirmek için kullanılır. Parametre olarak barkod okuyucu arayuzunun ismini alir..
    cv2.imshow('-- Barcode Reader --',frame)
    """ 
    cv2.imshow() ile görüntülediğimiz resmin ekranda kalma süresini belirler.
    Parantez içine ms cinsinden görüntünün ekranda kalma süresini belirleyebiliriz. cv2.waitKey(1)
    """
    cv2.waitKey(1)







