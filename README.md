# prtikum_5 
# Program Manajemen Nilai Mahasiswa (Menggunakan Python Dictionary)

Program ini dibuat sebagai tugas praktikum yang bertujuan untuk mengimplementasikan penggunaan tipe data **Dictionary** pada Python untuk mengelola data nilai mahasiswa secara interaktif melalui sistem menu.

##  Struktur Data Program

Data mahasiswa disimpan dalam sebuah *dictionary* utama bernama `data_nilai`.

* **Key:** Nama Mahasiswa (string)
* **Value:** Dictionary bersarang yang berisi detail komponen nilai.

**Contoh Struktur Data:**

```python
data_nilai = {
    "Nama Mahasiswa": {
        "tugas": 80,
        "uts": 75,
        "uas": 90,
        "nilai_akhir": 82.25 
    },
    # ... data mahasiswa lain
}
