def rumus_diskon(harga, diskon):
    """Rumus Diskon"""
    diskon = int(diskon / 100 * harga)
    jumlah_bayar = int(harga - diskon)
    print("===============Hasil=================")
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

barisan_deret()

#############################Silmi###################################
def menghitung_waktu_tempuh():
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

menghitung_waktu_tempuh()

######################################################################