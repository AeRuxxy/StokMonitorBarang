from barang import Barang
from data_manager import simpan_data, muat_data

class Inventaris:
    def __init__(self):
        self.daftar_barang = {}
        self.load_data()

    def load_data(self):
        data = muat_data()
        for nama, jumlah in data.items():
            self.daftar_barang[nama] = Barang(nama, jumlah)

    def save_data(self):
        data = {nama: barang.jumlah for nama, barang in self.daftar_barang.items()}
        simpan_data(data)

    def tambah_barang(self, nama, jumlah):
        if nama in self.daftar_barang:
            self.daftar_barang[nama].jumlah += jumlah
        else:
            self.daftar_barang[nama] = Barang(nama, jumlah)
        self.save_data()

    def lihat_stok(self):
        return [(nama, barang.jumlah) for nama, barang in self.daftar_barang.items()]

    def update_barang(self, nama, jumlah_baru):
        if nama in self.daftar_barang:
            self.daftar_barang[nama].update_stok(jumlah_baru)
            self.save_data()
            return True
        return False

    def hapus_barang(self, nama):
        if nama in self.daftar_barang:
            del self.daftar_barang[nama]
            self.save_data()
            return True
        return False

    def cek_stok_minimum(self, batas):
        hasil = []
        for barang in self.daftar_barang.values():
            if barang.jumlah <= batas:
                hasil.append(barang)
        return hasil