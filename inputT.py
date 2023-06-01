#INPUT TANGGAL PERTAMA KALI

import datetime as dt

# tgl = (input(f'Masukkan Tanggal Terakhir Mens Kamu: '))
# bln = (input(f'Masukkan Bulan Terakhir Mens Kamu: '))
# rata = (input(f'Kamu Biasanya Mens Berapa Hari Sih? '))

# tanggal = '''
#     {}       {}        {}'''.format(tgl, bln, rata)

# database = open('databasetanggal.csv', 'a')
# database.write(tanggal)
# database.close()

kira_mens = []
durasi = 7
for lamanya in range(1, durasi + 1):
    kira_mens.append(lamanya)
    
kira_folikular = []
durasi = 4
for lamanya in range(1, durasi + 1):
    kira_folikular.append(lamanya)

kira_ovulasi = []
durasi = 7
for lamanya in range(1, durasi + 1):
    kira_ovulasi.append(lamanya)

kira_luteal = []
durasi = 13
for lamanya in range(1, durasi + 1):
    kira_luteal.append(lamanya)

print(kira_folikular)
print(kira_luteal)
print(kira_mens)
print(kira_ovulasi)