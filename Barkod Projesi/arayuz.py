"""
---Tkinter ve Sqlite paketlerimizi dosyaya ekliyoruz---

Tkinter : Tkinter, Pythonun fiili standart GUI(Graphical User Interface) paketidir. Python kutuphanesidir.
Yazilan kodlarin ve programlarin son kullaniciya hitap etmesi gerekir. Bu yuzden Tkinter kullanimi oldukca yaygindir.

SQLite : SQL ile uyumlu ilişkisel bir veritabanıdır. Sunucusuz internetsiz calisabiliyor .Tüm program, uygulamalara entegre edilmiş bir C kütüphanesinde bulunur.
Veritabanı, yoğun kaynak kullanan bağımsız süreçleri ortadan kaldırarak verilerini tek bir platformlar arası dosyada saklar.
"""

import sqlite3 as db
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as pet

def urunKayitArayuz():
    frame = tk.Tk() #Burada default bir arayuz olusturduk. Burada arayuz anlik olarak acilip kapandi. Sureklilik saglanmasi icin mainloop() ifade methodu kullanilir.

    ''' 
    frame1 = Frame(frame, highlightbackground="red", highlightthickness=22)
    frame1.pack(padx=20, pady=20)
    '''
    frame.title('Urun Kayit Arayuz') #Arayuze baslik verir.
    frame.configure(bg='dodgerblue') #Arayuzun arka fon rengini degistirebiliriz.
    frame.geometry('900x800+400+100') #Bu method arayuzun yatay ve dikey boyutunu belirler.Soldan kaydirma ve yukaridan kaydirarak arayuzun konumu belirlenir.


    # frame.state('zoomed') Kullanilarak arayuzu tam ekran hale getirlir.
    # frame.wm_attributes('-alpha',0.9) opacity verilebilir. Saydamlik olusturulur.

    # Labels tk.Label() methodunun ilk parametresinde Labelin bulunacagi arayuz belirtilir. Ardindan font,renk,ve arka fon renkleri belirtilir.
    urunID = tk.Label(frame, text='Urun ID :', font='Verdana 22 bold', fg='black', bg='dodgerblue')
    boarcodeNum = tk.Label(frame, text='Barkod Numarasi :', font='Verdana 22 bold', fg='black', bg='dodgerblue')
    urunAdi = tk.Label(frame, text='Urun Adi :', font='Verdana 22 bold', fg='black', bg='dodgerblue')
    urunKategorisi = tk.Label(frame, text='Urun Kategorisi :', font='Verdana 22 bold', fg='black', bg='dodgerblue')
    urunGirisTarihi = tk.Label(frame, text='Urun Giris Tarihi :', font='Verdana 22 bold', fg='black', bg='dodgerblue')
    urunAdedi = tk.Label(frame, text='Urunun Adedi :', font='Verdana 22 bold', fg='black', bg='dodgerblue')
    urunFiyati = tk.Label(frame, text='Urunun Fiyati :', font='Verdana 22 bold', fg='black', bg='dodgerblue')

    # entry (TextFields)
    entryUrunID = tk.Entry(frame, fg='black', bg='white')
    entryBarcodeNum = tk.Entry(frame, fg='black', bg='white')
    entryUrunAdi = tk.Entry(frame, fg='black', bg='white')
    entryUrunKategorisi = tk.Entry(frame, fg='black', bg='white')
    entryUrunGirisTarihi = tk.Entry(frame, fg='black', bg='white')
    entryUrunAdedi = tk.Entry(frame, fg='black', bg='white')
    entryUrunFiyati = tk.Entry(frame, fg='black', bg='white')

    # pack() componentleri 2 serli olarak yan yana sikistirmaya yarar.
    # grid() arayuzun parcalara bolundugunu bildirir.
    # place() kordinatlari verilerek konumlandirma gerceklestirilir.

    # place relx(Yatay),rely(Dikey) 0-1 arasinda kesirli oranlar ile konumlandirdik.
    entryBarcodeNum.place(relx=0.8, rely=0) #Arayuzun yatay uzunlugun %80 inden itibaren yazdirmaya baslar.
    boarcodeNum.place(relx=0, rely=0)
    entryUrunAdi.place(relx=0.8, rely=0.05)
    urunAdi.place(relx=0, rely=0.05)
    entryUrunKategorisi.place(relx=0.8, rely=0.1)
    urunKategorisi.place(relx=0, rely=0.1)
    entryUrunGirisTarihi.place(relx=0.8, rely=0.15)
    urunGirisTarihi.place(relx=0, rely=0.15)
    entryUrunAdedi.place(relx=0.8, rely=0.2)
    urunAdedi.place(relx=0, rely=0.2)
    entryUrunFiyati.place(relx=0.8, rely=0.25)
    urunFiyati.place(relx=0, rely=0.25)

    #Burada agac yapimizi tanimladik. Frame diye tanimladigimiz arayuzumuzde oldugunu belirttik ve sutunlarimiza id numarasi veriyoruz.
    table = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6), show='headings', height=20)
    table.place(relx=0.1, rely=0.4)

    #Tablodaki kolonlarin id numarasina gore boyutlarini ve metinlerimizi hizaliyoruz.Ortalandi.
    table.column('#1', width=120, minwidth=60, anchor='center')
    table.column('#2', width=120, minwidth=60, anchor='center')
    table.column('#3', width=120, minwidth=60, anchor='center')
    table.column('#4', width=120, minwidth=60, anchor='center')
    table.column('#5', width=120, minwidth=60, anchor='center')
    table.column('#6', width=120, minwidth=60, anchor='center')

    #Tablodaki sutunlarimizin id numarasina gore textlerimizi belirtiyoruz.
    table.heading('#1', text='Barkod Numarasi')
    table.heading('#2', text='Urun Adi')
    table.heading('#3', text='Urun Kategorisi')
    table.heading('#4', text='Urun Giris Tarihi')
    table.heading('#5', text='Urunun Adedi')
    table.heading('#6', text='Urunun Fiyati')



    entryList = [] #Bir entry listesi olusturduk.
    kayitList = [] #Bir kayit listesi olusturduk.

    #Burada entrylerimizi entryList listemize ekledik.
    entryList.append(entryBarcodeNum)
    entryList.append(entryUrunAdi)
    entryList.append(entryUrunKategorisi)
    entryList.append(entryUrunGirisTarihi)
    entryList.append(entryUrunAdedi)
    entryList.append(entryUrunFiyati)

    #Urun kaydet adinda bir fonksiyon olusturduk. Ve bu fonksiyon vasitasiyla butona action verdik.

    def urunKaydet():
        """
        entryList elemanlari uzerinde gezinerek item.get()=='' entrylere metin girilip girilmedigini kontrol ettik.
        Eger bos ise kayitList temizlenecek ve donguden cikilacak. Eger dolu ise entrylere girilen metinler kayitListesine eklenecek.
        """
        for item in entryList:
            if item.get() == '':
                kayitList.clear()
                break
            else:
                kayitList.append(item.get())

        try:
            #Burada kayilList listesindeki verileri tabloya ekledik.
            row1 = table.insert("", 1, text='',
                                values=(
                                kayitList[0], kayitList[1], kayitList[2], kayitList[3], kayitList[4], kayitList[5]))

        except IndexError:
            #Entry lerin bos birakilmasi durumunda kayitlistesi bos oldugu icin bir exception yakalandi. Ve uyari mesaji verildi.
            messagebox.showwarning('Warning!', 'Please fill in the gaps!')


         # Database islemleri
         
        connection = db.connect('kayitlar.db') #Burada database olusturuldu.Eger yoksa olusturulacak.Varsa direk baglanacak.
        cursor = connection.cursor() #cursor() methodunu kullanarak imlec olusturduk.

        #kayitTablosuOlustur() fonksiyonumuzda imlecimizin execute() methodunu kullanarak veri tabanimizda kayitlar adinda bir tablo olusturduk. Burada verilen sql komutlari birer karakter dizileridir.Degiskenlere atanabilir.
        def kayitTablosuOlustur():
            #Burada kolon isimlerini ve veri tiplerini belirttik.
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS kayitlar(Barkod_Numarasi TEXT,Urun_Adi TEXT,Urun_Kategorisi TEXT,Urun_Giris_Tarihi TEXT,Urunun_Adedi INT,Urunun_Fiyati INT)')

        def kayitTablosuDoldurma():
            try:
                cursor.execute(
                    f"INSERT INTO kayitlar VALUES('{kayitList[0]}','{kayitList[1]}','{kayitList[2]}','{kayitList[3]}',{kayitList[4]},{kayitList[5]})")
            except IndexError:
                pass

            #Burada commit() methodu ile verilerimizi veri tabanina isledik. commit() imlecin degil baglanti nesnesinin bir methodudur.
            connection.commit()
            #Veritabanini uzerinde yapacagimiz islemleri tamamladiktan sonra veri tabanini kapatmamiz gerekir.Alternatif olarak veri tabani baglantisini olusturdugumuzda with keywordu kullanirsak islemler bittikten sonra Python baglantiyi otomatik sonlandiracaktir.
            connection.close()

        """
        def kayitTablosuElemanSilme():
            #cursor.execute(" DELETE FROM kayitlar WHERE Urunun_Fiyati = 26 And Urun_Giris_Tarihi='1905' ")
            cursor.execute("DELETE FROM kayitlar WHERE Urun_Adi = 'dasda'")
            connection.commit()
            print('Silindi')


       myList=[]
       def yazdir():
           cursor.execute("Select * from kayitlar")
           goster = cursor.fetchall()
           for satir in goster:
               myList.append(satir)
               print(satir)

           connection.commit()
           connection.close()
       """

        kayitTablosuOlustur()
        kayitTablosuDoldurma()
        # kayitTablosuElemanSilme()
        # yazdir()


        #Burada entryList listemizi delete() methodu vasitasiyla 0. indisten itibaren en son indise kadar silme islemi gerceklesti.
        for entry in entryList:
            entry.delete(0, END)

    # Burada butonumuzu olusturduk ve urunKaydet() fonksiyonunu action olarak verdigimiz icin buton tiklandiginda islemler gerceklesiyor.
    buton = tk.Button(frame, fg='dodgerblue', text='Kaydet', command=urunKaydet)
    buton.place(relx=0.8, rely=0.3) #butonun arayuzdeki konumu

    frame.mainloop()

urunKayitArayuz()



