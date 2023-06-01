#INPUT TANGGAL PERTAMA KALI

import datetime as dt

tgl = (input(f'Masukkan Tanggal Terakhir Mens Kamu: '))
bln = (input(f'Masukkan Bulan Terakhir Mens Kamu: '))
rata = (input(f'Kamu Biasanya Mens Berapa Hari Sih? '))

tanggal = '''
Tanggal    Bulan   Rata-rata
    {}       {}        {}'''.format(tgl, bln, rata)

database = open('databasetanggal.csv', 'a')
database.write(tanggal)
database.close()