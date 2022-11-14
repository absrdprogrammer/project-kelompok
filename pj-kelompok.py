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