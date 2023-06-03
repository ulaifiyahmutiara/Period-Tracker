#INPUT TANGGAL PERTAMA KALI

from datetime import datetime, timedelta

def hitung_siklus_mens(rata_durasi_mens, tanggal_terakhir_mens):
    tanggal_terakhir_mens = datetime.strptime(tanggal_terakhir_mens, '%Y-%m-%d')

    tanggal_awal_ovulasi = tanggal_terakhir_mens + timedelta(days=int(rata_durasi_mens) - 14)
    tanggal_terakhir_ovulasi = tanggal_awal_ovulasi + timedelta(days=4)

    tanggal_awal_siklus_berikutnya = tanggal_terakhir_mens + timedelta(days=int(rata_durasi_mens))
    tanggal_akhir_siklus_berikutnya = tanggal_awal_siklus_berikutnya + timedelta(days=int(rata_durasi_mens))

    tanggal_awal_folikular = tanggal_awal_siklus_berikutnya - timedelta(days=14)
    durasi_folikular = 14
    
    tanggal_awal_mens = tanggal_awal_siklus_berikutnya
    durasi_mens = int(rata_durasi_mens)

    tanggal_awal_luteal = tanggal_awal_siklus_berikutnya + timedelta(days=int(rata_durasi_mens) - 14)
    durasi_luteal = 14
    
    return tanggal_awal_ovulasi.strftime('%Y-%m-%d'), tanggal_awal_folikular.strftime('%Y-%m-%d'), durasi_folikular, tanggal_awal_mens.strftime('%Y-%m-%d'), durasi_mens, tanggal_awal_luteal.strftime('%Y-%m-%d'), durasi_luteal

rata_durasi_mens = input("Masukkan rata-rata durasi menstruasi (dalam hari): ")
tanggal_terakhir_mens = input("Masukkan tanggal terakhir menstruasi (format: YYYY-MM-DD): ")

tanggal_awal_ovulasi, tanggal_awal_folikular, durasi_folikular, tanggal_awal_mens, durasi_mens, tanggal_awal_luteal, durasi_luteal = hitung_siklus_mens(rata_durasi_mens, tanggal_terakhir_mens)

    # tgl_terakhir_mens = (input(f'Masukkan Tanggal Terakhir Mens Kamu: '))
    # bln = (input(f'Masukkan Bulan Terakhir Mens Kamu: '))
    # rata_durasi_mens = (input(f'Kamu Biasanya Mens Berapa Hari Sih? '))

    # tanggal = '''
    #     {}       {}        {}'''.format(tgl_terakhir_mens, bln, rata_durasi_mens)

    # database = open('databasetanggal.csv', 'a')
    # database.write(tanggal)
    # database.close()


    