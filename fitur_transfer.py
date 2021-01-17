data_a = open("transfer.txt")
data_x = open("nasabah.txt")
data_y = []
data_z = []
data_nama = []
data_rekening = []
data_saldo = []
data_mentah = []
data_transfer = []
data_g = []
for h in data_a:
    data_mentah.append(h.strip())
for i in data_mentah:
    data_transfer.append(i.split(","))
for g in range(len(data_transfer)):
  if data_transfer[g][1] not in data_g:
    data_g.append(data_transfer[g][1])
for p in data_x:
    data_y.append(p.strip())
for c in data_y:
    data_z.append(c.split(","))
for a in range(len(data_z)):
    data_rekening.append(data_z[a][0])
    data_nama.append(data_z[a][1])
    data_saldo.append(eval(data_z[a][2]))
data_tunai = dict(zip(data_rekening, data_saldo))
data_nasabah = dict(zip(data_rekening, data_nama))
def menu():
    print("Menu: ")
    print("[1] Buka Rekening Bank\n[2] Setoran Tunai\n[3] Tarik Tunai\n[4] Transfer\n[5] Lihat Daftar Transfer\n[6] Keluar")
print("** SELAMAT DATANG DI NF BANK **")
menu()
while True:
    pilih = input("Masukkan menu pilihan anda: ")
    if pilih == '1':
        nama = input("Masukkan nama anda: ")
        setoran = eval(input("Masukkan Setoran Awal: "))
        import random, string
        norek =  "REK" + ''.join(random.choice(string.digits) for _ in range(3))
        print("Pembukaan dengan nomor rekening", norek, "atas nama", nama, "berhasil.\n")
        data_nama.append(nama)
        data_saldo.append(setoran)
        data_rekening.append(norek)
        data_tunai[norek] = setoran
        data_nasabah[norek] = nama
        menu()
