def rumus_diskon(harga, diskon):
    """Rumus Diskon"""
    diskon = int(diskon / 100 * harga)
    jumlah_bayar = int(harga - diskon)
    print("===============Hasil=================")
    print("Harga barang :", harga)
    print("Total diskon :", diskon)
    print("Jumlah yg harus dibayar :", jumlah_bayar)


# choice = "barisan"
# if choice=="barisan":
#     list = (input("Silahkan input barisan, pisahkan dengan spasi. (Contoh : 1 2 3 4 5) : ").split(" "))
#     suku = int(input("Silahkan input suku yg ingin diketahui. (Contoh : 25) : "))
#     a = int(list[0])
#     b = int(list[1]) - int(list[0])
#     hasil = a + (suku - 1) * b
#     print(f"Suku ke-{suku} dari barisan tersebut adalah {hasil}")
