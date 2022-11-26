def rumus_diskon(harga, diskon):
    diskon = int(diskon / 100 * harga)
    jumlah_bayar = int(harga - diskon)
    print("Harga barang :", harga)
    print("Total diskon :", diskon)
    print("Jumlah yg harus dibayar :", jumlah_bayar)

def barisan_deret():
    fitur = ["Barisan", "Deret"]
    for i in range(2):
        print(f"{i+1}. {fitur[i]}")
    pilihan = input("Input nomor program yang akan dipakai : ")
    if pilihan=="1":
        list = (input("Silahkan input barisan, pisahkan dengan spasi. (Contoh : 1 2 3 4 5) : ").split(" "))
        suku = int(input("Silahkan input suku yg ingin diketahui. (Contoh : 25) : "))
        a = float(list[0])
        b = float(list[1]) - float(list[0])
        hasil = a + (suku - 1) * b
        print(f"Suku ke-{suku} dari barisan tersebut adalah {hasil}")
    elif pilihan=="2":
        list = (input("Silahkan input deret, pisahkan dengan spasi. (Contoh : 1 2 3 4 5) : ").split(" "))
        suku = int(input("Silahkan input jumlah dari berapa suku pertama yg ingin diketahui. (Contoh : 25) : "))
        a = float(list[0])
        b = float(list[1]) - float(list[0])
        hasil = float(suku / 2 * (2* a + (suku - 1) * b))
        print(f"Jumlah {suku} suku pertama dari deret tersebut adalah {hasil}")
    else:
        print("Perintah tidak ditemukan. Program exit.")

def kec_jrk_wkt():
    fitur = ["Kecepatan", "Jarak", "Waktu"]
    for i in range(3):
        print(str(i+1) + ". " + fitur[i])
    pilihan = input("Input nomor program yang akan dipakai : ")
    if pilihan=="1":
        jarak = float(input("Masukkan jarak dalam km : "))
        waktu = float(input("Masukkan waktu dalam jam : "))
        kecepatan = round(jarak/waktu,2)
        print(f"Kecepatan yang diperlukan untuk menempuh jarak {jarak} km dalam waktu {waktu} jam adalah {kecepatan} km/jam")
    elif pilihan=="2":
        kecepatan = float(input("Masukkan kecepatan dalam km/jam : "))
        waktu = float(input("Masukkan waktu dalam jam : "))
        jarak = round(kecepatan*waktu,2)
        print(f"Jarak yang ditempuh dalam waktu {waktu} jam dengan kecepatan {kecepatan} km/jam adalah {jarak} km")
    elif pilihan=="3":
        jarak = float(input("Masukkan jarak dalam km : "))
        kecepatan = float(input("Masukkan kecepatan dalam km/jam : "))
        waktu = round(jarak/kecepatan,2)
        print(f"Waktu yang diperlukan untuk menempuh jarak {jarak} km dengan kecepatan {kecepatan} km/jam adalah {waktu} jam")
    else:
        print("Perintah tidak ditemukan. Program exit.")

def volume():
    phi = 3.14
    fitur = ['Kubus', 'Balok', 'Limas', 'Kerucut', 'Tabung', 'Bola']
    print("Menu")
    for i in range(len(fitur)):
        print(f"{i+1}. {fitur[i]}" )
    pilihan = input("Input nomor program yang akan dipakai : ")
    if pilihan=="1":
        sisi = float(input("Masukan sisi (dalam meter): "))
        volume = round(sisi**3,2)
    elif pilihan=="2":
        panjang = float(input("Masukan panjang (dalam meter): "))
        lebar = float(input("Masukan lebar (dalam meter): "))
        tinggi = float(input("Masukan tinggi (dalam meter): "))
        volume = round(panjang * lebar * tinggi,2)
    elif pilihan=="3":
        la = float(input("Masukan luas alas (dalam meter): "))
        tinggi = float(input("Masukan tinggi (dalam meter): "))
        volume = round(1/3 * la * tinggi,2)
    elif pilihan=="4":
        r = float(input("Masukan nilai jari jari (dalam meter): "))
        tinggi = float(input("Masukan tinggi (dalam meter): "))
        volume = round(1/3 * phi * r * r * tinggi,2)
    elif pilihan=="5":
        r = float(input("Masukan nilai jari jari (dalam meter): "))
        tinggi = float(input("Masukan tinggi (dalam meter): "))
        volume = round(phi * r * r * tinggi,2)
    elif pilihan=="6":
        r = float(input("masukan nilai jari jari (dalam meter): "))
        tinggi = float(input("masukan tinggi (dalam meter): "))
        volume = round(4/3 * phi * r * r * r,2)
    else:
        print("Perintah tidak ditemukan. Program exit.")
        exit()
    print(f"Volume : {volume} meter kubik")

def himpunan():
    fitur = ["Gabungan", "Irisan", "Selisih"]
    for h in range(3):
        print(f"{h+1}. {fitur[h]}")
    pilihan = input("Input nomor program yang akan dipakai : ")
    h1 = input("Silahkan masukan himpunan A, pisah sengan spasi( ) : ").split(" ")
    h2 = input("Silahkan masukan himpunan B, pisah dengan spasi( ) : ").split(" ")
    hasil = []
    if pilihan == "1" :
        for i in range(len(h2)):
            hasil.append(h2[i])
        for j in range(len(h1)):
            if h1[j] not in hasil:
                hasil.append(h1[j])
    elif pilihan == "2" :
        for k in range(len(h2)):
            for l in range(len(h1)):
                if h2[k] == h1[l]:
                    hasil.append(h2[k])
    elif pilihan == "3" : 
        print("Jenis selisih yg akan dipakai\n1. A-B\n2. B-A")
        masukan = input("Silahkan input nomor program yang akan dipakai : " )
        if masukan == "1":
            for m in range(len(h1)):
                if h1[m] not in h2:
                    hasil.append(h1[m])
        elif masukan == "2":
            for n in range(len(h2)):
                if h2[n] not in h1:
                    hasil.append(h2[n])
    else:
        print("Input Invalid. Program Exit.")
        exit()
    hasil.sort()
    print("Hasil :", hasil)

def luas():
    fitur = ["Persegi", "Persegi Panjang", "Segitiga", "Jajar Genjang", "Trapesium", "Belah Ketupat", "Layang-Layang", "Lingkaran"]
    print("Menu Luas Bangun Datar")
    for i in range(len(fitur)):
        print(f"{i+1}. {fitur[i]}")
    pilihan = input("Input nomor program yang akan dipakai : ")
    if pilihan=="1":
        sisi = int(input("Masukkan panjang sisi (dalam meter): "))
        luas = sisi*sisi
    elif pilihan=="2":
        panjang = int(input("Masukkan panjang (dalam meter): "))
        lebar = int(input("Masukkan panjang lebar (dalam meter): "))
        luas = panjang * lebar   
    elif pilihan=="3":
        alas = int(input("Masukkan panjang alas (dalam meter): "))
        tinggi = int(input("Masukkan panjang tinggi (dalam meter): "))
        luas = alas * tinggi / 2
    elif pilihan=="4":
        alas = int(input("Masukkan panjang alas (dalam meter): "))
        tinggi = int(input("Masukkan panjang tinggi (dalam meter): "))
        luas = alas * tinggi
    elif pilihan=="5":
        sisiatas = int(input("Masukkan panjang sisi atas (dalam meter): "))
        sisibawah = int(input("Masukkan panjang sisi bawah (dalam meter): "))
        tinggi = int(input("Masukkan tinggi : "))
        luas = (sisiatas+sisibawah) * tinggi / 2
    elif pilihan=="6":
        diagonal1 = int(input("Masukkan panjang diagonal pertama (dalam meter): "))
        diagonal2 = int(input("Masukkan panjang diagonal kedua (dalam meter): "))
        luas = diagonal1 * diagonal2 / 2
    elif pilihan=="7":
        diagonal1 = int(input("Masukkan panjang diagonal pertama (dalam meter): "))
        diagonal2 = int(input("Masukkan panjang diagonal kedua (dalam meter): "))
        luas = diagonal1 * diagonal2 / 2
    elif pilihan=="8":
        phi = 3.14
        r = int(input("Masukkan panjang jari-jari (dalam meter): "))
        luas = phi * r * r
    else:
        print("Input Invalid. Program Exit.")
        exit()
    print(f"Luas : {luas} meter persegi")

 