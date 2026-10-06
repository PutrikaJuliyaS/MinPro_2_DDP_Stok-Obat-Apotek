# MinPro_2_DDP_Stok-Obat-Apotek
nama: PUTRIKA JULIYA SARI

NIM: 057

# PENGELOLAAN STOK OBAT DI APOTEK

## FLOWCHART
<img width="6548" height="4096" alt="image" src="https://github.com/user-attachments/assets/36300139-0793-46a2-8937-1dfdf028bd2f" />
1. menginput username dan password
   
### user

menampilkan dua pilihan dalam menu yaitu:

1. tampilkan semua stok obat

pereda nyeri dan demam:
paracetamol, 20 pcs
ibuprofen, 20 pcs
aspirin, 20 pcs
    
Batuk dan flu:
Guaifenesin, 20 pcs
Dextromethorphan, 20 pcs
    
Alergi:
Cetirizine, 20 pcs
CTM, 20 pcs
    
Vitamin:
Vitamin, 20 pcs
Vitamin b complex, 20 pcs
Multivitamin, 20 pcs

2. keluar

kembali ke halaman login

### admin

terdiri dari 5 pilihan menu:

1. tampilkan semua stok obat
   
pereda nyeri dan demam:
paracetamol, 20 pcs
ibuprofen, 20 pcs
aspirin, 20 pcs
    
Batuk dan flu:
Guaifenesin, 20 pcs
Dextromethorphan, 20 pcs
    
Alergi:
Cetirizine, 20 pcs
CTM, 20 pcs
    
Vitamin:
Vitamin, 20 pcs
Vitamin b complex, 20 pcs
Multivitamin, 20 pcs

2. tambah obat baru
   
   input kategori, nama obat dan jumlah stok
   
   output obat berhasil ditambahkan

3. ubah jumlah stok
   input kategori, nama obat dan jumlah stok
   
   output stok berhasil diubah
   
4. hapus obat
   
   input kategori, nama obat

   output obat berhasil dihapus

5. keluar

   kembali ke halaman login
   
## CODE PYTHON

<img width="1266" height="1040" alt="image" src="https://github.com/user-attachments/assets/aab9796c-d82d-477c-a976-b4ed08c04c7e" />

<img width="977" height="1025" alt="image" src="https://github.com/user-attachments/assets/5e71c3c2-acba-4b39-8bf0-ca941712e27f" />


1. tampilan awal
   
PrettyTable: di bagian atas, program membuat tabel sederhana untuk menampilkan daftar pegawai 

menggunakan library pwinput agar password yang diketik tidak terlihat di layar. Sistem mencocokkan input dengan dictionary user.

2. data stok obat
   
kategori_obat/ tuple: menyimpan daftar kategori obat secara tetap (pereda nyeri/demam, batuk/flu, alergi, dan vitamin).

stok_obat/ Dictionary: menyimpan data obat dengan format yang rapi

3. Functions
   
tambah_obat(): fungsi untuk menambah data obat baru

menu_admin(), menu_user(): untuk mencetak daftar menu pilihan sesuai role

login(): Fungsi untuk memverifikasi ulang username dan password

4. while True

Bagian ini mengatur menu interaktif CRUD (Create, Read, Update, Delete) yang terus berjalan sampai pengguna memilih opsi keluar (0):

Menu 1 (Read): menampilkan semua daftar obat beserta jumlah stoknya per kategori menggunakan loop

Menu 2 (Create): menambahkan obat baru ke dalam kategori yang ditentukan

Menu 3 (Update): mengubah jumlah stok obat yang sudah terdaftar di sistem.

Menu 4 (Delete): menghapus obat dari kategori tertentu menggunakan perintah del.

Menu 0 (Exit): memutus dan memanggil kembali fungsi login().

Else: Menangani input menu yang tidak valid agar program tidak berhenti tiba-tiba (crash).




