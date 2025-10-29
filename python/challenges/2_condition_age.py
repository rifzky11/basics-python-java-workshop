# Program Klasifikasi Usia

# 1. TODO: Baca input dari pengguna
usia = int(input("Masukkan usia: "))

# 2. TODO Tentukan kategori berdasarkan usia
if usia < 0:
    print("Usia tidak boleh negatif")
elif 0 <= usia <= 5:
    print(f"Usia anda {usia} adalah Balita")
elif 6 <= usia <= 11:
    print(f"Usia anda {usia} adalah Anak-anak")
elif 12 <= usia <= 16:
    print(f"Usia anda {usia} adalah Remaja Awal")
elif 17 <= usia <= 25:
    print(f"Usia anda {usia} adalah Remaja Akhir")
elif 26 <= usia <= 35:
    print(f"Usia anda {usia} adalah Dewasa Awal")
elif 36 <= usia <= 45:
    print(f"Usia anda {usia} adalah Dewasa Akhir")
elif 46 <= usia <= 55:
    print(f"Usia anda {usia} adalah Lansia Awal")
elif 56 <= usia <= 65:
    print(f"Usia anda {usia} adalah Lansia Akhir")
elif usia >= 65:
    print(f"Usia anda {usia} adalah Sepuh")

    
