class PersegiPanjang:
    # Konstruktor untuk inisialisasi(proses awal) properti panjang dan lebar
    def __init__(self, panjang, lebar):
        self.panjang = panjang #self = explisit
        self.lebar = lebar

    # Fungsi untuk menghitung keliling
    def keliling(self): # parameter yang digunakan di dalam metode kelas untuk merujuk ke instance (objek) tertentu dari kelas tersebut.
        return 2 * (self.panjang + self.lebar)

    # Fungsi untuk menghitung luas
    def luas(self):
        return self.panjang * self.lebar

    # Fungsi __str__ untuk representasi string dari objek
    def __str__(self):
        return f"Panjangnya adalah {self.panjang} cm dan lebarnya adalah {self.lebar} cm"

pp = PersegiPanjang(745, 195)

print(pp.__str__()) # Persegi Panjang, panjang 745 cm, dan lebar 195 cm
print("Keliling:", pp.keliling(), "cm")
print("Luas:", pp.luas(), "cm^2")