# 1. Buat Dictionary daftar kontak
# Nama sebagai key, dan nomor sebagai value
daftar_kontak = {
    "Ari": "081267888",
    "Dina": "0876777776"
}
print("--- Latihan 1 ---")
print(f"1. Dictionary Awal: {daftar_kontak}")

# 2. Tampilkan kontaknya Ari
print(f"2. Nomor kontak Ari: {daftar_kontak['Ari']}")

# 3. Tambah kontak baru dengan nama Riko, nomor 087654544
daftar_kontak["Riko"] = "087654544"
print(f"3. Dictionary setelah tambah Riko: {daftar_kontak}")

# 4. Ubah kontak Dina dengan nomor baru 088999776
daftar_kontak["Dina"] = "088999776"
print(f"4. Dictionary setelah ubah Dina: {daftar_kontak}")

# 5. Tampilkan semua Nama (Keys)
print(f"5. Semua Nama (Keys): {list(daftar_kontak.keys())}")

# 6. Tampilkan semua Nomor (Values)
print(f"6. Semua Nomor (Values): {list(daftar_kontak.values())}")

# 7. Tampilkan daftar Nama dan nomornya (Items)
print("7. Daftar Nama dan Nomor:")
for nama, nomor in daftar_kontak.items():
    print(f"- {nama}: {nomor}")

# 8. Hapus kontak Dina.
del daftar_kontak["Dina"]
# atau daftar_kontak.pop("Dina")
print(f"8. Dictionary setelah hapus Dina: {daftar_kontak}")