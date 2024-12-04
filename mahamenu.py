from mahaclass import mahasiswa as a

# isinya adalah kode warna menggunakan ANSII escape
r = "\033[0m"
h = "\033[1;32m"
b = "\033[1;34m"
m = "\033[1;31m"
k = "\033[1;33m"
u = "\033[1;35m"
p = "\033[1;37m"

# ini juga dictionary
# tugas nya memamnggil method yang dipanggil
menu = {
    "1": a.lihat,   "l" : a.lihat,
    "2": a.tambah,  "t" : a.tambah,
    "3": a.ubah,    "u" : a.ubah,
    "4": a.hapus,   "h" : a.hapus,
    "5": a.cari,    "c" : a.cari,
    "6": exit,      "k" : exit
}

# perulangan yang akan menampilkan menu pilihan
while True:
    print(
        f"{p}L{r}ihat |", 
        f"{h}T{r}ambah |", 
        f"{b}U{r}bah |", 
        f"{m}H{r}apus |", 
        f"{k}C{r}ari |", 
        f"{u}K{r}eluar"
    )
    opsi = input("Masukkan pilihan: ").lower()
    if opsi in menu:
        menu[opsi]()
    else:
        print("pilih yang ada saja.")