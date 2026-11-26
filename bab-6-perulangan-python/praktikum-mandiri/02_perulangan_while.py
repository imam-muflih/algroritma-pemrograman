
x=9
angka=1
jumlah_tampil=0
angka_lewati =x+1
angka_berhenti=x+10

print("x=",x)
print("angka lewati=",angka_lewati)
print("angka berhenti=",angka_berhenti)

while True:
    if angka == angka_berhenti:
        break
    if angka == angka_lewati:
        angka+=1
        continue
    print(angka,end=",")

    jumlah_tampil+=1
    angka+=1
print()
print("jumlah tampil=",jumlah_tampil)
print("program selesai")