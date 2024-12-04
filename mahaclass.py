from mahatabel import tabel    

class mahasiswa:
    def __init__(self, mahadata={}):
    # inisialisasi class
    # ada dictionary untuk simpan data nilai mahasiswa juga
        self.m = mahadata

    def nilai(self, str):
    # method untuk memastikan input adalah angka
    # dan mengulangi permintaan jika input bukan angka
    # juga untuk membatasi nilai input yang diinputkan.
        while True:
            try:
                self.poin = float(input(str))
                if self.poin < 0 or self.poin > 100:
                    print(f"Nilai harus berkisar dari 0 hingga 100.")
                else:
                    return self.poin
            except ValueError:
                print("Input harus berupa angka!!")    
                
    def namamu(self, str, harus_ada=True):
    # method ini akan meminta input nama dari user
    # dan melihat apakah nama yang diinputkan tersebut ada di dictionary atau tidak
        while True:
            self.nama = input(str)
            if harus_ada and self.nama not in self.m:
                print("nama tidak ditemukan!")
            elif not harus_ada and self.nama in self.m:
                print("nama sudah ada di database. Masukkan nama lain!")
            else:
                return self.nama  
                
    def minta(self, nama):
    # method ini
    # gunanya untuk mendapatkan input dari user
        tugas, uts, uas = map(self.nilai, [
                "Masukkan Nilai Tugas: ", 
                "Masukkan Nilai UTS: ", 
                "Masukkan Nilai UAS: "
                ])
        akhir = (tugas*0.3) + (uts*0.35) + (uas*0.35)
        if nama not in self.m:
            NIM = input("Masukkan NIM (e.g. 123456789): ")
            return { # akan mengembalikan/menyerahkan data ke method yang memanggil
                "Nama": nama,
                "NIM": NIM,
                "Nilai Tugas": tugas,
                "Nilai UTS": uts,
                "Nilai UAS": uas,
                "Nilai Akhir": akhir
            }
        # sekaligus melihat apakah data dengan nama yang sama ada di dictionary
        elif nama in self.m:
            return { # lihat return diatas
                "Nama": nama,
                "NIM": self.m[nama]["NIM"], # NIM dari data lama
                "Nilai Tugas": tugas,
                "Nilai UTS": uts,
                "Nilai UAS": uas,
                "Nilai Akhir": akhir
            }
        
    def tambah(self):
    # method ini akan menambahkan data yang sudah diterima oleh method minta
    # ke dalam dictionary
        self.nama = self.namamu("Masukkan Nama: ",harus_ada=False)
        self.m[self.nama] = self.minta(self.nama)
        print("Data berhasil ditambahkan.")
        
    def ubah(self):
    # method akan mencari data dengan nama yang sesuai
    # kemudian meminta input data baru
    # input tersebut akan menggantikan data yang sudah ada
        self.nama = self.namamu("Masukkan Nama: ")
        # method namamu dipakai untuk membedakan antara method tambah dan ubah
        # untuk konteks lihat method minta
        self.m[self.nama] = self.minta(self.nama) 
        print("Data berhasil diubah.")
        
    def hapus(self):
    # method ini gunanya untuk hapus data dari dictionary
        self.nama = self.namamu("Masukkan Nama: ")
        # method namamu disini untuk memastikan bahwa nama yang diinput itu ada di dictionary
        del self.m[self.nama]
        print("Data berhasil dihapus.")
        
    def lihat(self):
    # method untuk menampilkan data yang ada di dictionary
        tabel(self.m, title="Data Mahasiswa") 

    def cari(self):
    # akan mencari dengan nama
    # data dengan nama tersebut akan ditamplikan kepada user
        self.nama = self.namamu("Masukkan Nama: ")
        # method namamu sama seperti yang ada di method hapus
        # untuk memastikan bahwa nama yang diinput itu ada di dictionary
        tabel({self.nama: self.m[self.nama]}, title=f"Data Mahasiswa dengan Nama {self.nama}")