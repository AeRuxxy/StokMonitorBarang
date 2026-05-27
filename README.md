# Sistem Monitoring Stok Barang

Aplikasi desktop sederhana untuk mengelola dan memantau stok barang. Dibangun dengan **Python** dan **Tkinter**, serta menyimpan data secara persisten dalam file JSON.

## Fitur Utama

- **Tambah barang** baru atau tambah stok jika barang sudah ada.
- **Update stok** barang yang sudah terdaftar.
- **Hapus barang** dari daftar inventaris.
- **Cek stok minimum** – menampilkan barang dengan stok di bawah batas tertentu.
- **Penyimpanan otomatis** ke file `data_stok.json` (setiap perubahan langsung tersimpan).

## Teknologi yang Digunakan

- Python 3.x
- Tkinter (GUI bawaan Python)
- JSON (penyimpanan data)

## Cara Menjalankan Program

1. **Pastikan Python 3.x sudah terinstal** di sistem Anda.
2. **Ekstrak atau simpan semua file** berikut dalam satu folder:
   - `main.py`
   - `gui.py`
   - `inventaris.py`
   - `barang.py`
   - `data_manager.py`
   - `styles.py`
3. **Jalankan file utama**:
   ```bash
   python main.py