import tkinter as tk
from tkinter import ttk, font

# Warna
PRIMARY_BLUE = "#0284C7"
LIGHT_BLUE   = "#E0F2FE"
BG_WHITE     = "#FFFFFF"
TEXT_DARK    = "#1E293B"
TEXT_LIGHT   = "#64748B"

def setup_styles(root):
    style = ttk.Style()
    style.theme_use('clam')

    # Font default
    default_font = font.nametofont("TkDefaultFont")
    default_font.configure(family="Segoe UI", size=10)
    root.option_add("*Font", default_font)

    # Frame
    style.configure("White.TFrame", background=BG_WHITE)
    style.configure("Card.TFrame", background=BG_WHITE,
                    relief="solid", borderwidth=1, bordercolor="#E2E8F0")

    # Label
    style.configure("Title.TLabel", background=BG_WHITE,
                    foreground=PRIMARY_BLUE, font=("Segoe UI", 18, "bold"))
    style.configure("Input.TLabel", background=BG_WHITE,
                    foreground=TEXT_DARK, font=("Segoe UI", 10))

    # Entry
    style.configure("Modern.TEntry", fieldbackground=BG_WHITE,
                    borderwidth=1, relief="solid", bordercolor="#CBD5E1", padding=8)
    style.map("Modern.TEntry", bordercolor=[("focus", PRIMARY_BLUE)])

    # Button
    style.configure("Primary.TButton", background=PRIMARY_BLUE,
                    foreground="white", borderwidth=0, focuscolor="none",
                    relief="flat", padding=(15, 8), font=("Segoe UI", 10, "bold"))
    style.map("Primary.TButton", background=[("active", "#0369A1")])

    style.configure("Secondary.TButton", background=BG_WHITE,
                    foreground=PRIMARY_BLUE, borderwidth=1,
                    bordercolor=PRIMARY_BLUE, relief="flat", padding=(15, 8))
    style.map("Secondary.TButton", background=[("active", LIGHT_BLUE)])

    # Treeview
    style.configure("Treeview", background=BG_WHITE,
                    foreground=TEXT_DARK, rowheight=35, borderwidth=0)
    style.configure("Treeview.Heading", background="#F1F5F9",
                    foreground=TEXT_DARK, font=("Segoe UI", 10, "bold"))
    style.map("Treeview", background=[("selected", LIGHT_BLUE)])

    return style