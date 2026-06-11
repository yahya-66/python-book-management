buku = []

def tambah_buku():
    judul = input("Masukkan judul buku: ")
    buku.append(judul)
    print("Buku berhasil ditambahkan!")

def lihat_buku():
    if len(buku) == 0:
        print("Belum ada buku.")
    else:
        print("\nDaftar Buku.")
        for i, item in enumerate(buku, start=1):
            print(f"{i}, {item}")

def hapus_buku():
    lihat_buku()
    nomor = int(input("Pilih nomor buku yang dihapus: "))
    buku.pop(nomor -1)
    print("Buku berhasil dihapus!")

def cari_buku():
    kata_cari = input("Masukkan judul yang dicari: ")
    ditemukan = False
    for item in buku:
        if kata_cari.lower() in item.lower():
            print(item)
            ditemukan = True
    if ditemukan == False:
        print("Buku tidak ditemukan.")

while True:
    print("\n==== MENU ====")
    print("1. Tambah Buku")
    print("2. Lihat Buku")
    print("3. Hapus Buku")
    print("4. Cari Buku")
    print("5. Keluar")

    pilihan = input("Pilih input: ")

    if pilihan == "1":
        tambah_buku()
    
    elif pilihan == "2":
        lihat_buku()

    if pilihan == "3":
        hapus_buku()
    
    elif pilihan == "4":
        cari_buku()

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")