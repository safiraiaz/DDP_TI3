nilai = int(input("masukkan nilai: "))

def kelulusan(nilai):
    if nilai < 0:
        return "Nilai tidak valid"
    elif nilai <= 60:
        return "Gagal"
    elif nilai <= 70:
        return "Baik"
    elif nilai <= 80:
        return "Sangat Baik"
    elif nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai tidak valid"
    
    print(Kelulusan(nilai))


def cari_ganjil(*angka):
    for i in angka:
        if i % 2 == 1:
            print("Angka ganjil ditemukan: ", i)
            return
        
cari_ganjil(2, 446, 884, 974, 276, 798, 123, 776, 13, 871)