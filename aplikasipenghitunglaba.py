#syachra indyra puteri

# membuat variabel nama barang 
# membuat variabel harga barang
# membuat variabel persentasi harga
# input nama barang
# input harga barang
# menghitung haraga barang
# harga barang * persen / 100
# print harga beserta harga barang

while(True):
    nama_barang = input('masukan nama barang : ')
    harga_barang = int(input('masukan harga barang : '))
    besaran_untung = int(input('masukan besaran untung: '))

    harga_keuntungan = int(harga_barang) * besaran_untung / 100 
    harga_jual = int(harga_barang) + harga_keuntungan

    print (nama_barang, 'dijual dengan harga :',harga_jual)

    apakah_lanjut = input('apakah akan menghitung barang lain ? Y lanjut N tidak')
    if(apakah_lanjut != 'Y'):
        break

    



