def rumus_diskon(harga, diskon):
    diskon = int(diskon / 100 * harga)
    jumlah_bayar = int(harga - diskon)
    print("===============Hasil=================")
    print("Harga barang :", harga)
    print("Total diskon :", diskon)
    print("Jumlah yg harus dibayar :", jumlah_bayar)

harga = int(input("Harga barang :"))
diskon = int(input("Total diskon (dalam persen, ex : 5) : "))
