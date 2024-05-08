print( " Nama : Muhammad Fajar Adha " )
print( " NIM  : 2310432040 " )
print( " Program Harga barang " )
print()

n = int ( input( " Masukkan banyak barang : " ) )

nb = []
hr = []
st = []

for i in range (n):
    nb1 = input ( f" Masukkan nama barang ke-{i+1} : " )
    hr1 = float ( input( f" Masukkan harga {nb1} : " ) )
    st1 = int ( input( f" Masukkan stok {nb1} : " ) )
    nb.append(nb1)
    hr.append(hr1)
    st.append(st1)
print()

print( " TABEL HARGA DAN STOK BARANG TOKO KELONTONG " )
print( " ======================================================== " )
print( f" | {'Barang':<10} | {'Harga':<10} | {'Stok':<10} | " )
print( " ======================================================== " )
for i in range (n):
    print( f" | {nb[i]:<10} | {hr[i]:<10} | {st[i]:<10} | " )
    print( " -------------------------------------------------------- " )
print()

ku = []
for i in range (n):
    ku1 = hr[i]*st[i]
    ku.append(ku1)

bt = nb[0]
br = nb[0]
kut = ku[0]
kur = ku[0]

for i in range (1, n):
    if ( ku[i] > kut ):
        bt = nb[i]
        kut = ku[i]
    elif ( ku[i] < kur ):
        br = nb[i]
        kur = ku[i]

tku = 0
for i in range (n):
    tku += ku[i]

print( f" Barang yang untungnya paling besar adalah : {bt} || dengan harga : {kut} " )
print( f" Barang yang untungnya paling kecil adalah : {br} || dengan harga : {kur} " )
print( f" Total keuntungan dari penjualan semua barang adalah : {tku} " )

