def rumus_diskon(harga, diskon):
    """Rumus Diskon"""
    diskon = int(diskon / 100 * harga)
    jumlah_bayar = int(harga - diskon)
    print("===============Hasil=================")
    print("Harga barang :", harga)
    print("Total diskon :", diskon)
    print("Jumlah yg harus dibayar :", jumlah_bayar)

rumus_diskon(100_000, 10)