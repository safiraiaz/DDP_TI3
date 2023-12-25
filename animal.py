class animal:
    def __init__(self,nama,makanan,hidup,berkembangBiak):
        self.nama = nama
        self.makanan= makanan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak 
    def print(self):
        print("Nama hewan ", self.nama)
        print("Pemakan ", self.makanan)
        print("Hidup di ", self.hidup, "dan berkembangbiak dengan", self.berkembangBiak)

class Ikan(animal):
    def __init__(self,nama,makanan,hidup,berkembangBiak, ciriFisik,hobi):
        super().__init__(nama,makanan,hidup,berkembangBiak)
        self.ciriFisik = ciriFisik
        self.hobi = hobi
    def cetak(self):
        super().print()
        print("Ciri fisik ", self.ciriFisik, "Hobi", self.hobi)

class Badak(animal):
    def __init__(self,nama,makanan,hidup,berkembangBiak, masaHidup,waktuAktivitas):
        super().__init__(nama,makanan,hidup,berkembangBiak)
        self.masaHidup = masaHidup
        self.waktuAktivitas = waktuAktivitas
    def cetak(self):
        super().print()
        print("Masa hidup ", self.masaHidup, "tahun,", "Waktu aktivitas", self.waktuAktivitas)

class Ular(animal):
    def __init__(self,nama,makanan,hidup,berkembangBiak, kelas,ordo):
        super().__init__(nama,makanan,hidup,berkembangBiak)
        self.kelas = kelas
        self.ordo = ordo
    def cetak(self):
        super().print()
        print("Kelas ", self.kelas, "Ordo", self.ordo)


satu = Ikan("Dori", "plankton", "laut", "bertelur", "berwarna hijau abu-abu, ", "berenang")
satu.cetak()
dua = Badak("Badak", "rumput", "darat", "melahirkan", 35, "hampir sepanjang hari")
dua.cetak()
tiga = Ular("Ular", "daging", "darat dan air", "bertelur", "reptil, ", "serpentes")
tiga.cetak()
