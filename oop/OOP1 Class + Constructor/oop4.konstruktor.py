#nama class diawali huruf besar dan tanpa karakter
class Biodata:
    
    def __init__(self):
        #construktor
        print("\n")
        print("INI KONTRUKTOR")

    def tampilkan(self): #ini untuk menampilkan function
        print("\n")
        print("Nama Saya\t\t: " + sayasendiri.nama)
        print("NIM mahasiswa saya\t: " + sayasendiri.NIM)
        print("Prodi yang saya ikuti\t: " + sayasendiri.prodi)
        print("Asal sekolah saya\t: " + sayasendiri.asalsekolah)
        print("Alamat rumah saya\t: " + sayasendiri.alamat)
        print("\n")

sayasendiri = Biodata() #objek
sayasendiri0 = Biodata() #konstruktor otomatis dieksekusi sejumlah objek
sayasendiri1 = Biodata()

sayasendiri.nama = "Andhi" #artribut / property
sayasendiri.NIM = "C20010004"
sayasendiri.prodi = "Teknik Informatika"
sayasendiri.asalsekolah = "SMA Negeri 1 Boyolali"
sayasendiri.alamat = "Cepogo, Boyolali"

sayasendiri.tampilkan()

#properti yang dimiliki class = class variabel => statis
#fungsi = perintah yang dapat dimiliki objek
