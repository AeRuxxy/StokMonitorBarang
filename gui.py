import tkinter as tk
from tkinter import ttk, messagebox
from inventaris import Inventaris
import styles

class StokMonitoringApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Monitoring Stok")
        self.geometry("1280x720")
        self.configure(bg='#F8FAFC')
        self.inv = Inventaris()

        styles.setup_styles(self)
        self._build_ui()
        self.refresh_table()
        self.update_status()

    def _build_ui(self):
        main_frame = ttk.Frame(self, style="White.TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

        # Header
        ttk.Label(main_frame, text="📦 SISTEM MONITORING STOK",
                  style="Title.TLabel").pack(anchor="w", pady=(0, 20))

        # Input
        card = ttk.Frame(main_frame, style="Card.TFrame", padding=20)
        card.pack(fill=tk.X, pady=(0, 20))
        card.columnconfigure(1, weight=1)

        ttk.Label(card, text="Nama Barang", style="Input.TLabel").grid(
            row=0, column=0, sticky="w", padx=(0, 10))
        self.entry_nama = ttk.Entry(card, style="Modern.TEntry")
        self.entry_nama.grid(row=0, column=1, sticky="ew", pady=5)

        ttk.Label(card, text="Jumlah Stok", style="Input.TLabel").grid(
            row=1, column=0, sticky="w", padx=(0, 10))
        self.entry_jumlah = ttk.Entry(card, style="Modern.TEntry")
        self.entry_jumlah.grid(row=1, column=1, sticky="ew", pady=5)

        btn_frame = ttk.Frame(card, style="White.TFrame")
        btn_frame.grid(row=2, column=0, columnspan=2, pady=(20, 0))
        ttk.Button(btn_frame, text="➕ Tambah", style="Primary.TButton",
                   command=self.tambah_barang).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="✏️ Update", style="Secondary.TButton",
                   command=self.update_barang).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="🗑️ Hapus", style="Secondary.TButton",
                   command=self.hapus_barang).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="⚠️ Cek Minimum", style="Secondary.TButton",
                   command=self.cek_stok).pack(side=tk.LEFT, padx=5)

        # Table
        table_frame = ttk.Frame(main_frame, style="Card.TFrame", padding=2)
        table_frame.pack(fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(table_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree = ttk.Treeview(table_frame, columns=("Nama", "Stok"),
                                 show="headings", yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tree.yview)
        self.tree.heading("Nama", text="Nama Barang")
        self.tree.heading("Stok", text="Jumlah Stok")
        self.tree.column("Nama", width=400)
        self.tree.column("Stok", width=150, anchor="center")
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.pilih_item)
        self.tree.bind("<Enter>", lambda e: self.tree.config(cursor="hand2"))
        self.tree.bind("<Leave>", lambda e: self.tree.config(cursor=""))

        # Bottom Frame
        bottom_frame = ttk.Frame(main_frame, style="White.TFrame")
        bottom_frame.pack(fill=tk.X, pady=(10, 0))

        self.status_label = ttk.Label(bottom_frame, text="", foreground=styles.TEXT_LIGHT)
        self.status_label.pack(side=tk.LEFT)

        watermark_text = "Muhamad Rangga Aldiyan Pasha\n212514028"
        watermark_label = tk.Label(bottom_frame, text=watermark_text,
                                   fg="#94A3B8", bg=styles.BG_WHITE,
                                   font=("Segoe UI", 9), justify=tk.RIGHT)
        watermark_label.pack(side=tk.RIGHT)

        self._setup_placeholders()

    def _setup_placeholders(self):
        def on_click(event, entry, placeholder):
            if entry.get() == placeholder:
                entry.delete(0, tk.END)
                entry.config(foreground=styles.TEXT_DARK)

        def on_focusout(event, entry, placeholder):
            if entry.get() == "":
                entry.insert(0, placeholder)
                entry.config(foreground=styles.TEXT_LIGHT)

        self.entry_nama.insert(0, "Contoh: Laptop")
        self.entry_nama.config(foreground=styles.TEXT_LIGHT)
        self.entry_nama.bind("<FocusIn>", lambda e: on_click(e, self.entry_nama, "Contoh: Laptop"))
        self.entry_nama.bind("<FocusOut>", lambda e: on_focusout(e, self.entry_nama, "Contoh: Laptop"))

        self.entry_jumlah.insert(0, "0")
        self.entry_jumlah.config(foreground=styles.TEXT_LIGHT)
        self.entry_jumlah.bind("<FocusIn>", lambda e: on_click(e, self.entry_jumlah, "0"))
        self.entry_jumlah.bind("<FocusOut>", lambda e: on_focusout(e, self.entry_jumlah, "0"))

    # Fungsi
    def refresh_table(self):
        self.tree.delete(*self.tree.get_children())
        for barang in self.inv.daftar_barang.values():
            self.tree.insert("", "end", values=(barang.nama, barang.jumlah))

    def tambah_barang(self):
        nama = self.entry_nama.get()
        try:
            jumlah = int(self.entry_jumlah.get())
            self.inv.tambah_barang(nama, jumlah)
            self.refresh_table()
            self._clear_entries()
        except ValueError:
            messagebox.showerror("Error", "Jumlah harus angka!")

    def update_barang(self):
        nama = self.entry_nama.get()
        try:
            jumlah = int(self.entry_jumlah.get())
            self.inv.update_barang(nama, jumlah)
            self.refresh_table()
            self._clear_entries()
        except ValueError:
            messagebox.showerror("Error", "Jumlah harus angka!")

    def hapus_barang(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Pilih barang dulu!")
            return
        nama = self.tree.item(selected[0])["values"][0]
        self.inv.hapus_barang(nama)
        self.refresh_table()
        self._clear_entries()

    def cek_stok(self):
        try:
            batas = int(self.entry_jumlah.get())
            hasil = [f"{b.nama}: {b.jumlah}" for b in self.inv.daftar_barang.values()
                     if b.jumlah <= batas]
            messagebox.showinfo("Stok Rendah", "\n".join(hasil) if hasil else "Tidak ada stok rendah")
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka batas!")

    def pilih_item(self, event):
        selected = self.tree.selection()
        if selected:
            nama, jumlah = self.tree.item(selected[0])["values"]
            self.entry_nama.delete(0, tk.END)
            self.entry_nama.insert(0, nama)
            self.entry_jumlah.delete(0, tk.END)
            self.entry_jumlah.insert(0, jumlah)

    def _clear_entries(self):
        self.entry_nama.delete(0, tk.END)
        self.entry_nama.insert(0, "Contoh: Laptop")
        self.entry_nama.config(foreground=styles.TEXT_LIGHT)
        self.entry_jumlah.delete(0, tk.END)
        self.entry_jumlah.insert(0, "0")
        self.entry_jumlah.config(foreground=styles.TEXT_LIGHT)

    def update_status(self):
        total = len(self.inv.daftar_barang)
        total_stok = sum(b.jumlah for b in self.inv.daftar_barang.values())
        self.status_label.config(text=f"✅ Total {total} jenis barang | Total stok: {total_stok} unit")
        self.after(1000, self.update_status)