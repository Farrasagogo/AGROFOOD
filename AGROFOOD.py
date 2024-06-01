import pandas as pd
import csv
import prettytable
import os
import datetime
import numpy as np


def login(username,password):
    login = False
    with open("DataUSER.txt","r") as f:
        for i in f :
            user,pw = i.split(",")
            pw = pw.strip()
            if (user == username and pw == password):
                login = True 
                break
    if (login) :
        print('Login berhasil')
        os.system('cls')
        menuuser()
    else:
        print('Username atau password anda salah, jika belum membuat akun silahkan register')
        mulai()
  

def register(username,password):
    f = open('DataUSER.txt', 'a',newline="")
    f.write('\n'+username+','+password)
    f.close()
    mulai()
    

def loginadmin(username,password):
    login = False
    with open("DataAdmin.txt","r") as f:
        for i in f :
            user,pw = i.split(",")
            pw = pw.strip()
            if (user == username and pw == password):
                login = True 
                break
    if (login) :
        print('Login berhasil')
        menuadmin()
    else:
        print('Username atau password anda salah')
        mulai()
      
        
def mulai():
    global opsi
    print("""
+----------------------------+
| Selamat Datang di AGROFOOD |
+----------------------------+""")
    print ('[1] Login Sebagai User')
    print ('[2] Register Sebagai User')
    print ('[3] Login Sebagai Admin')
    opsi = input('Pilih Menu: ')
    os.system('cls')
    if(opsi == '1'):
        username = input('Masukkan Username: ')
        password = input('Masukkan password: ')
        os.system('cls')
        login(username,password)
    elif(opsi == '2'):
        print('Masukkan username dan password anda untuk membuat akun')
        username = input('Masukkan username: ')
        password = input('Masukkan password: ')
        print("akun anda berhasil di daftarkan")
        register(username,password)
    elif(opsi == "3"):
        username = input('Masukkan username admin: ')
        password = input("Masukkan password admin: ")
        loginadmin(username,password)
    else: 
        print('Menu yang anda pilih tidak ada dalam daftar')
        mulai()

def menuadmin():
    print("""
+----------------------------+
|         Menu Admin         |
+----------------------------+""")
    print('[1] Menambah Barang')
    print('[2] Menghapus Barang')    
    print('[3] Resep')
    print('[4] Tambah Resep')
    print("[5] Liat History Pembelian")
    print("[6] Keluar Dari Aplikasi")
    pilihmenuadmin = input('Pilih Menu: ')
    if pilihmenuadmin == ("1") :
        os.system('cls')
        menambahbarang()
    elif pilihmenuadmin == ("2") :
        os.system('cls')
        menghapusbarang()
    elif pilihmenuadmin == ("3") :
        os.system('cls')
        resep()
    elif pilihmenuadmin == ("4") :
        os.system('cls')
        tambahresep()
    elif pilihmenuadmin == ("5") :
        os.system('cls')
        history()
    elif pilihmenuadmin == ("6") :
        quit()
    else: print('Menu yang anda pilih tidak ada dalam daftar'),menuadmin()

def menambahbarang():
    with open ('LIST.csv', 'r') as df:
        print ((prettytable.from_csv(df)))
    df.close()
    kode = int(input('Masukkan kode makanan: '))
    nama = str(input('Masukkan nama makanan: '))
    harga = int(input('Masukkan harga makanan/250 gram: '))
    with open('LIST.csv', 'a+', newline='') as csv_file :
            tulis_data = csv.writer(csv_file,delimiter=',')
            data = [kode, nama, harga]
            tulis_data.writerow(data)
            csv_file.close()
            print('Makanan berhasil ditambahkan')
            menuadmin()
            
def menghapusbarang():
    with open ('LIST.csv', 'r') as df:
        print ((prettytable.from_csv(df)))
    df.close()
    lines = list()
    memberName = input("Masukkan kode barang yang ingin dihapus: ")
    with open('LIST.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for rows in row:
                if rows == memberName:
                    lines.remove(row)
        readFile.close()
    with open('LIST.csv', 'w' ,newline='') as writeFile:
        writer = csv.writer(writeFile, delimiter=',')
        writer.writerows(lines)
        writeFile.close()
        print('\nBarang berhasil dihapus')
        menuadmin()

def resep():
    menu = "RESEPLIST.csv"
    df = pd.read_csv(menu)
    print (df[['Daftar Makanan']])
    reseppilih = int(input('Pilih Resep Menu: '))
    print ('Bahan: ')
    print (df['Bahan'][reseppilih])
    print ("Cara Masak: ")
    print (df['Cara Masak'][reseppilih])
    print ('[1] Cari Resep Lainnya\n[2] Kembali Ke Menu')
    pilihmenuresep = int(input("Pilih Menu: "))
    if pilihmenuresep == 1:
        resep()
    if pilihmenuresep == 2:
        menuadmin()
    else: print('Menu yang and pilih tidak tersedia'),menuadmin()

def tambahresep():
    menu = "RESEPLIST.csv"
    df = pd.read_csv(menu)
    print (df[['Daftar Makanan']])
    list = []
    list2 =[]
    daftarmakanan = str(input('Masukkan Nama Makanan: '))
    jumlahbahan= int(input('Masukkan Jumlah Bahan: '))
    for i in range(jumlahbahan):
        bahan = input('Masukkan Bahan Yang Dibutuhkan: ')
        list.append(bahan)
    jumlahtahap= int(input('Masukkan jumlah tahap resep: '))
    for i in range(jumlahtahap):
        caramasak = input('Masukkan Cara Masak: ')
        list2.append(caramasak)
    hasil1='\n'.join(list)
    hasil2="\n".join(list2)
    with open('RESEPLIST.csv', 'a+', newline='') as csv_file :
            tulis_data = csv.writer(csv_file, delimiter=',')
            data = [daftarmakanan,hasil1,hasil2]
            tulis_data.writerow(data)
            print('Makanan berhasil ditambahkan')
            csv_file.close()
            menuadmin()

def menuuser():
    print("""
+----------------------------+
|         Menu User          |
+----------------------------+""")
    print("[1] Belanja \n[2] Keluar dari aplikasi")
    menupilih = int(input('Pilih menu:'))
    if menupilih == (2):
        quit()
    if menupilih == (1):
        os.system('cls')
        menubelanja()
    else: 
        print('Menu yang anda masukkan tidak ada dalam daftar')
        menuuser()
        
def menubelanja():
    print("""
+----------------------------+
|       Menu Belanja         |
+----------------------------+ 
[1] Tambah barang dalam struk
[2] Hapus barang dalam struk
[3] Edit jumlah barang
[4] Lihat struk
[5] Konfirmasi pembelian""")
    x = input('Pilih Menu: ')
    if x == '1':
        os.system('cls')
        tambahstruk()
    if x == '2':
        os.system('cls')
        hapusstruk()
    if x == '3':
        os.system('cls')
        editjumlah()
    if x == '4':
        os.system('cls')
        liatstruk()
    if x == '5':
        os.system('cls')
        pilihankonfirm()
    else:
        print('Menu yang anda pilih tidak ada dalam daftar')
        menubelanja()

def liatstruk():
    with open ('STRUK.csv', 'r') as df:
        print ((prettytable.from_csv(df)))
    df.close()
    menubelanja()


def tambahstruk():
    with open ('LIST.csv', 'r') as df:
        print ((prettytable.from_csv(df)))
    df.close()
    x = input('Masukkan kode barang: ')
    y = input ('Jumlah barang yang dibeli: ')
    dict ={'Jumlah Barang': y}
    field = ['Kode','Daftar Makanan','Harga/250gram','Jumlah Barang']
    with open('LIST.csv', 'r') as f, open('STRUK.csv', 'a+', newline='') as f_out:
        reader = csv.DictReader(f)
        writer = csv.DictWriter(f_out,fieldnames=field,delimiter=',')
        for row in reader:
            if row['Kode'] == x:
                dict1=row.copy()
                dict1.update(dict)
        writer.writerow(dict1)
    df = pd.read_csv('STRUK.csv')
    df.drop_duplicates(subset=['Kode'],inplace=True,keep='last')
    df.to_csv('STRUK.csv', index=False)
    f_out.close(), f.close()
    menubelanja()
    
def hapusstruk():
    with open ('STRUK.csv', 'r') as df:
        print ((prettytable.from_csv(df)))
    df.close() 
    list=[]
    kode = input('Masukkan kode yang ingin di hapus: ')
    with open('STRUK.csv', mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            list.append(row)
    indeks = 0
    for data in list:
        if (data['Kode'] == kode):
            list.remove(list[indeks])
        indeks = indeks + 1 
    with open('STRUK.csv', mode="w",newline='') as csv_file:
        fieldnames = ['Kode', 'Daftar Makanan', 'Harga/250gram','Jumlah Barang']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in list:
            writer.writerow({'Kode': new_data['Kode'], 'Daftar Makanan': new_data['Daftar Makanan'], 'Harga/250gram': new_data['Harga/250gram'], 'Jumlah Barang': new_data['Jumlah Barang']})
    print ('Jumlah barang berhasil diubah')
    csv_file.close()
    menubelanja()

def editjumlah():
    with open ('STRUK.csv', 'r') as pp:
        print ((prettytable.from_csv(pp)))
    pp.close
    list=[]
    kode = input('Masukkan kode yang ingin di edit: ')
    jmlh = input('Masukkan jumlah barang yang baru: ')
    with open('STRUK.csv', mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            list.append(row)
    indeks = 0
    for data in list:
        if (data['Kode'] == kode):
            list[indeks]['Jumlah Barang'] = jmlh
        indeks = indeks + 1 
    with open('STRUK.csv', mode="w",newline='') as csv_file:
        fieldnames = ['Kode', 'Daftar Makanan', 'Harga/250gram','Jumlah Barang']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in list:
            writer.writerow({'Kode': new_data['Kode'], 'Daftar Makanan': new_data['Daftar Makanan'], 'Harga/250gram': new_data['Harga/250gram'], 'Jumlah Barang': new_data['Jumlah Barang']})
        csv_file.close()
    print ('Jumlah barang berhasil diubah')
    menubelanja()

def pilihankonfirm():
    x = input('Apakah anda yakin untuk mengonfirmasi pembelian y/n: ')
    if  x == 'y':
        os.system('cls')
        konfirm()
    elif x == "n":
        os.system('cls')
        menubelanja()
    else: pilihankonfirm()
        
def konfirm():
    data = pd. read_csv('STRUK.csv')
    df = pd. DataFrame(data)
    x = datetime.datetime.now()
    sum_column = df["Harga/250gram"] * df["Jumlah Barang"]
    df["Total"] = sum_column
    total = df.apply(np.sum)
    total['Kode'] = 'Total'
    df.loc['Total'] = df.sum(numeric_only=True)
    df.iloc[-1, df.columns.get_loc('Kode')]="Tanggal"
    df.iloc[-1, df.columns.get_loc('Daftar Makanan')]=x
    df.iloc[-1, df.columns.get_loc('Harga/250gram')]=""
    df.iloc[-1, df.columns.get_loc('Jumlah Barang')]="Total Harga"
    df.to_csv(r'STRUK.csv', index=False)
    with open ('STRUK.csv', 'r') as pp:
        print ((prettytable.from_csv(pp)))    
    pp.close
    print('Jadi total harga yang harus anda bayar', df.iloc[-1, df.columns.get_loc('Total')])
    with open('History.txt', "a") as my_output_file:
        with open('STRUK.csv', "r") as my_input_file:
            [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()
    struktemp()

def struktemp():
    with open('STRUKTEMP.csv', 'r') as f:
        with open('STRUK.csv', 'w', newline='') as f_out:
            reader = csv.reader(f)
            writer = csv.writer(f_out,delimiter=',')
            writer.writerows(reader)
            f_out.close()
            menuakhir()

def menuakhir():
    print("""
+----------------------------------------+
| Terimakasih telah belanja di toko kami |
+----------------------------------------+
[1] Kembali ke menu user
[2] Keluar dari aplikasi
    """)
    x = int(input("Pilih Menu: "))
    if x == 1:
        menuuser()
    if x == 2:
        quit()
    else: print('Menu yang anda pilih tidak ada'), menuakhir()

def history():
    f = open('History.txt', 'r')
    file_contents = f.read()
    print (file_contents)
    menuadmin()


        


    





    
    

    
       
    
        

    





        
mulai()


