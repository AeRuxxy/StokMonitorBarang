class Barang:
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    def update_stok(self, jumlah_baru):
        self.jumlah = jumlah_baru

    def __str__(self):
        return f"{self.nama}: {self.jumlah}"