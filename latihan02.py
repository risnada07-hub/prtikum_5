import os

# Dictionary utama untuk menyimpan data nilai
data_nilai = {}

def hitung_nilai_akhir(tugas, uts, uas):
    """Menghitung Nilai Akhir berdasarkan bobot: Tugas (30%), UTS (35%), UAS (35%)."""
    nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)
    return round(nilai_akhir, 2)

def tambah_data():
    """Menu: Tambah Data Mahasiswa"""
    nama = input("Masukkan Nama Mahasiswa: ").strip()
    
    # Meminta input nilai dan memvalidasi sebagai angka
    try:
        tugas = float(input("Masukkan Nilai Tugas (0-100): "))
        uts = float(input("Masukkan Nilai UTS (0-100): "))
        uas = float(input("Masukkan Nilai UAS (0-100): "))
    except ValueError:
        print("\n Input nilai harus berupa angka!")
        return

    # Hitung nilai akhir
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

    # Simpan data ke dictionary
    data_nilai[nama] = {
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "nilai_akhir": nilai_akhir
    }
    print(f"\n Data {nama} berhasil ditambahkan dengan Nilai Akhir: {nilai_akhir}")

def tampilkan_data(nama=None):
    """Menu: Tampilkan Data Mahasiswa (Semua atau Spesifik)"""
    if not data_nilai:
        print("\n Data mahasiswa masih kosong.")
        return

    print("\n-----------------------------------------------------------")
    print("| Nama Mahasiswa | Tugas (30%) | UTS (35%) | UAS (35%) | Nilai Akhir |")
    print("-----------------------------------------------------------")

    if nama:
        # Tampilkan data spesifik
        if nama in data_nilai:
            data = data_nilai[nama]
            print(f"| {nama:<14} | {data['tugas']:<11} | {data['uts']:<9} | {data['uas']:<9} | {data['nilai_akhir']:<11} |")
        else:
            print(f"| Mahasiswa dengan nama '{nama}' tidak ditemukan. |")
    else:
        # Tampilkan semua data
        for nama, data in data_nilai.items():
            print(f"| {nama:<14} | {data['tugas']:<11} | {data['uts']:<9} | {data['uas']:<9} | {data['nilai_akhir']:<11} |")
    
    print("-----------------------------------------------------------")

def ubah_data():
    """Menu: Ubah Data Mahasiswa"""
    nama = input("Masukkan Nama Mahasiswa yang ingin diubah: ").strip()
    
    if nama in data_nilai:
        print(f"Mengubah data untuk {nama}. Data saat ini: {data_nilai[nama]}")
        
        # Meminta input nilai baru dan memvalidasi sebagai angka
        try:
            tugas = float(input("Masukkan Nilai Tugas Baru (kosongkan jika tidak diubah): ") or data_nilai[nama]['tugas'])
            uts = float(input("Masukkan Nilai UTS Baru (kosongkan jika tidak diubah): ") or data_nilai[nama]['uts'])
            uas = float(input("Masukkan Nilai UAS Baru (kosongkan jika tidak diubah): ") or data_nilai[nama]['uas'])
        except ValueError:
            print("\n Input nilai harus berupa angka!")
            return
            
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        
        # Update dictionary
        data_nilai[nama].update({
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "nilai_akhir": nilai_akhir
        })
        print(f"\n Data {nama} berhasil diperbarui. Nilai Akhir baru: {nilai_akhir}")
    else:
        print(f"\n Mahasiswa dengan nama '{nama}' tidak ditemukan.")

def hapus_data():
    """Menu: Hapus Data Mahasiswa"""
    nama = input("Masukkan Nama Mahasiswa yang ingin dihapus: ").strip()
    
    if nama in data_nilai:
        del data_nilai[nama]
        print(f"\n Data {nama} berhasil dihapus.")
    else:
        print(f"\n Mahasiswa dengan nama '{nama}' tidak ditemukan.")

def cari_data():
    """Menu: Cari Data Mahasiswa"""
    nama = input("Masukkan Nama Mahasiswa yang ingin dicari: ").strip()
    tampilkan_data(nama)

def main_menu():
    """Menampilkan menu utama program."""
    while True:
        # os.system('cls' if os.name == 'nt' else 'clear') # Untuk membersihkan layar
        print("\n\n=== MENU PROGRAM NILAI MAHASISWA ===")
        print("1. Tambah Data")
        print("2. Ubah Data")
        print("3. Hapus Data")
        print("4. Tampilkan Data (Semua)")
        print("5. Cari Data (Berdasarkan Nama)")
        print("6. Keluar")
        print("------------------------------------")
        
        pilihan = input("Masukkan pilihan (1-6): ").strip()
        
        if pilihan == '1':
            tambah_data()
        elif pilihan == '2':
            ubah_data()
        elif pilihan == '3':
            hapus_data()
        elif pilihan == '4':
            tampilkan_data()
        elif pilihan == '5':
            cari_data()
        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("\n Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main_menu()