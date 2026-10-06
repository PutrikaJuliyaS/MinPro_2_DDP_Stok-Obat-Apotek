from prettytable import PrettyTable

print("daftar pegawai")
tabel = PrettyTable()
tabel.field_names = ["no", "nama", "role"]
tabel.add_row(["1", "putri", "admin"])
tabel.add_row(["2", "juli", "user"])
print(tabel)

kategori_obat = (
    "pereda nyeri dan demam",
    "batuk dan flu",
    "alergi",
    "vitamin"
    )

stok_obat = {
    ("pereda nyeri dan demam"): {
        "paracetamol": 20,
        "ibuprofen": 20,
        "aspirin": 20
    },
    ("batuk dan flu"): {
        "guaifenesin": 20,
        "dextromethorphan": 20
    },
    ("alergi"): {
        "cetirizine": 20,
        "ctm": 20
    },
    ("vitamin"): {
        "vitamin c": 20,
        "vitamin b complex": 20,
        "multivitamin": 20
    }
}
import pwinput

user = {
    "putri": {"password": "12345", "role": "admin"},
    "juli": {"password": "54321", "role": "user"}
}

username = input("username: ").strip()
password = pwinput.pwinput("password: ").strip()

if username in user and user[username]["password"] == password:
    print(f"selamat datang, {username}")

#buat tuple kategori obat
def tambah_obat():
    print("TAMBAH DATA OBAT")
    nama = input("Nama Obat: ")
    print(f"Kategori tersedia: {kategori_obat}")
    kategori = input("Kategori: ").lower()
    if kategori in kategori_obat:
        stok = int(input("Jumlah Stok: "))
        stok_obat[nama] = stok
        print("Data berhasil ditambahkan!")
    else:
        print("input invalid")

def menu_admin():
    
    print("1. tampilkan semua stok obat")
    print("2. tambah obat baru")
    print("3. ubah jumlah stok")
    print("4. hapus obat")
    print("0. keluar")
    print(input ("masukkan nomor menu(0-4): "))

def menu_user():
    print("1. tampilkan semua stok obat")
    print("0. keluar")
    print(input ("masukkan nomor menu(0-1): "))

def login():
    print("Silakan Login")
    username = input("Username: ")
    password = input("Password: ")
    
    if username in user and user[username]["password"] == password:
        role = user[username]["role"]
        print(f"\nLogin berhasil sebagai {role}!")
        return role
    else:
        print("\nUsername atau password salah!")
        return None

#menu pilihan berulang (while) sampai user memilih keluar
while True:
    pilihan = input("Pilih menu (1-5): ")
#conditional statement
    if pilihan == "1":
        print("DAFTAR STOK OBAT")
        for kategori, obat_list in stok_obat.items():
            print("kategori:", kategori)
            for nama_obat, jumlah_stok in obat_list.items():
                print("  -", nama_obat, ":", jumlah_stok, "pcs")
            print()

#Menambahkan data baru
    elif pilihan == "2":
        print("MENAMBAH OBAT BARU")
        print(f"Kategori tersedia: {kategori_obat}")
        kategori = input("masukkan kategori obat: ")
        nama_obat = input("masukkan nama obat: ")
        jumlah_stok = int(input("masukkan jumlah stok obat: "))
        if kategori in stok_obat:
            stok_obat[kategori][nama_obat] = jumlah_stok
        else:
            stok_obat[kategori] = {nama_obat: jumlah_stok}
        print("obat berhasil ditambahkan ke kategori.")
#Mengubah data yang sudah ada
    elif pilihan == "3":
        print("MENGUBAH JUMLAH STOK OBAT")
        print(f"kategori terrsedia: {kategori_obat}")
        kategori = input("masukkan kategori obat: ")
        nama_obat = input("masukkan nama obat: ")
        jumlah_stok = int(input("masukkan jumlah stok baru: "))
        if kategori in stok_obat and nama_obat in stok_obat[kategori]:
            stok_obat[kategori][nama_obat] = jumlah_stok
        else:
            print("obat tidak ada")
        print("stok obat berhasil diubah.")
#Menghapus data
    elif pilihan == "4":
        print("MENGHAPUS OBAT")
        kategori = input("masukkan kategori obat: ")
        nama_obat = input("masukkan nama obat: ")
        if kategori in stok_obat and nama_obat in stok_obat[kategori]:
            del stok_obat[kategori][nama_obat]
        else:
            print("obat tidak ada")
        print("obat berhasil dihapus dari stok.")

    elif pilihan == "0":
        print("anda keluar.")
        login()
#input salah diminta ulang, bukan error/crash
    else:
        print("input tidak valid, silahkan masukkan pilihan yang benar")