x=9
z=9

persen_diskon=5+x
batas_diskon=50000+(z*1000)

total_belanja=0
jumlah_transaksi=0

print("X=",x)
print("z=",z)
print("diskon:",persen_diskon,"%")
print("batas diskon:Rp",batas_diskon)

while True:
    print("=====menu=====")
    print("1.nasi goreng (Rp 12.000)")
    print("2.mie goreng (Rp 10.000)")
    print("3.es teh (Rp 3.000)")
    print("4.es jeruk (Rp 5.000)")
    print("0.selesai")

    pilihan = int(input("pilih menu:"))
    if pilihan==0:
        break

    if pilihan == 1:
        nama="nasi goreng"
        harga=12000
    elif pilihan ==2:
        nama="mie goreng"
        harga=10000
    elif pilihan ==3:
        nama="es teh"
        harga=3000
    elif pilihan ==4:
        nama="es jeruk"
        harga=5000
    else:
        print("pilihan tidak tersedia!")
        continue

    jumlah=int(input("masukkan jumlah pembelian:"))
    if jumlah <1:
        print("jumlah harus minimal 1!")
        continue

    subtotal=harga*jumlah
    total_belanja += subtotal
    jumlah_transaksi+=1
    print(f"subtotal:Rp{subtotal}")

if total_belanja>= batas_diskon:
    diskon=total_belanja*persen_diskon // 100
else:
    diskon=0

total_bayar=total_belanja-diskon

print("\n=====struk pembelian=====")
print(f"jumlah transaksi:{jumlah_transaksi}")
print(f"total sebelum diskon:Rp{total_belanja}")
print(f"diskon({persen_diskon}%):Rp {diskon}")
print(f"total bayar : Rp {total_bayar}")
print("program selesai")