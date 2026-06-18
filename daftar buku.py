import json

try:
    with open("buku.json", "r") as file:
        daftar_buku = json.load(file)
except ValueError:
    daftar_buku = []

def simpan_data():
    with open ("buku.json", "w") as file:
        json.dump(daftar_buku, file, indent=4)

def tambah_buku():
    buku ={
            "judul": input("Judul: "),
            "penulis": input("Penulis: "),
            "tahun": input("Tahun: ")
        }
    daftar_buku.append(buku)
    simpan_data()
    print("Buku berhasil ditambahkan!")

def lihat_buku():
    if len (daftar_buku) == 0:
        print("Belum ada buku.")
        return
    print("=== DAFTAR BUKU ===")
    for buku in daftar_buku:
            print("\nJudul :", buku["judul"])
            print("Penulis :", buku["penulis"])
            print("Tahun :", buku["tahun"])

def cari_buku():
     kata_kunci = input("Masukkan judul buku: ")
     ditemukan = False
     for buku in daftar_buku:
            if kata_kunci.lower() in buku["judul"].lower():
                print("\nBuku ditemukan!")
                print("Judul :", buku["judul"])
                print("Penulis :", buku["penulis"])
                print("Tahun :", buku["tahun"])
                ditemukan = True
            if ditemukan == False:
                print("Buku tidak ditemukan.")

def hapus_buku():
    print("\n=== DAFTAR BUKU ===")
    for i, buku in enumerate(daftar_buku, start=1):
        print(f"{i}. {buku['judul']}")
    try:
        nomor = int(input("Pilih nomor buku yang dihapus: "))
        if nomor >= 1 and nomor <= len(daftar_buku):
            daftar_buku.pop(nomor - 1)
            simpan_data()
            print("Buku berhasil dihapus!")
        else: 
            print("Nomor tidak valid!")
    except ValueError:
        print("Masukkan angka, bukan huruf!")

def edit_buku():
    if len(daftar_buku) == 0:
        print("Belum ada buku.")
        return
    print("\n=== DAFTAR BUKU ===")
    for i, buku in enumerate(daftar_buku, start=1):
        print(f"{i}. {buku["judul"]}")
    try:
        nomor = int(input("Pilih nomor buku: "))
        if nomor >= 1 and nomor <= len (daftar_buku):
            daftar_buku[nomor - 1]["judul"] = input("Judul baru: ")
            daftar_buku[nomor - 1]["penulis"] = input("Penulis baru: ")
            daftar_buku[nomor - 1]["tahun"] = input("Tahun baru: ")
            simpan_data()
            print("Buku berhasil diperbarui!")
        else:
            print("Nomor buku tidak valid!")
    except ValueError:
        print("Masukkan angka!")


while True:
    print("\n=== MENU ===")
    print("1. Tambah Buku")
    print("2. Lihat Buku")
    print("3. Cari Buku")
    print("4. Hapus Buku")
    print("5. Edit Buku")
    print("6. Keluar")

    pilihan = input("Pilih: ")

    if pilihan == "1":
        tambah_buku()

    elif pilihan == "2":
        lihat_buku()

    elif pilihan == "3":
        cari_buku()

    elif pilihan == "4":
        hapus_buku()

    elif pilihan == "5":
        edit_buku()
        
    elif pilihan == "6":
        print("Program selesai.")
        break
