def tambah(a, b):
    """Fungsi untuk penjumlahan"""
    return a + b

def kurang(a, b):
    """Fungsi untuk pengurangan"""
    return a - b

def kali(a, b):
    """Fungsi untuk perkalian"""
    return a * b

def bagi(a, b):
    """Fungsi untuk pembagian"""
    if b == 0:
        return "Tidak bisa dibagi dengan nol!"
    else:
        return a / b

def pangkat(a, b):
    """Fungsi untuk perpangkatan"""
    return a ** b

def modulus(a, b):
    """Fungsi untuk modulus"""
    return a % b
