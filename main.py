buku = []

try:
    with open("buku.txt", "r") as file:
        buku = file.read().splitlines()
except FileNotFoundError:
        pass

anggota =[]

try:
    with open("anggota.txt", "r") as file:
        anggota = file.read().splitlines()
except FileNotFoundError:
    pass

peminjaman =[]

try:
    with open("peminjaman.txt", "r") as file:
        peminjaman = file.read().splitlines()
except FileNotFoundError:
    pass

def tambah_buku():
    judul = input("Masukkan judul buku: ")
    buku.append(judul)
    with open("buku.txt", "a") as file:
        file.write(judul + "\n")
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
    with open("buku.txt", "w") as file:
        for item in buku:
            file.write(item + "\n")
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

def tambah_anggota():
    nama = input("Masukkan nama anggota: ")
    anggota.append(nama)
    with open ("anggota.txt", "a") as file:
        file.write(nama + "\n")

    print("Anggota berhasil ditambahkan!")

def lihat_anggota():
    if len(anggota) == 0:
        print("Belum ada anggota.")
    else:
        print("\nDaftar Anggota")
        for i, item in enumerate(anggota, start=1):
            print(f"{i}. {item}")

def hapus_anggota():
    lihat_anggota()
    nomor = input("Pilih nomor anggota yang dihapus: ")
    anggota.pop()
    with open ("angggota.txt", "w") as file:
        for item in anggota:
            file.write(item + "\n")
        print("Anggota berhasil dihapus.")

def pinjam_buku():
    lihat_anggota()
    anggota_pilih = int(input("Pilih nomor anggota: ")) -1
    lihat_buku()
    buku_pilih = int(input("Pilih nomor buku: ")) -1
    data = f"{anggota[anggota_pilih]} meminjam {buku[buku_pilih]}"
    peminjaman.append(data)
    with open ("peminjaman.txt", "a") as file:
        file.write(data + "\n")
    print("Peminjaman berhasil!")

def lihat_peminjaman():
    if len(peminjaman) == 0:
        print("Belum ada peminjaman.")
    else:
        print("\nDaftar peminjaman")
        for i, item in enumerate(peminjaman, start=1):
            print(f"{i}. {item}")

def kembalikan_buku():
    lihat_peminjaman()

    nomor = int(input("Pilih nomor peminjaman yang dikembalikan: "))
    peminjaman.pop(nomor - 1)
    with open("peminjaman.txt", "w")as file:
        file.write("\n".join(peminjaman))
    print("Buku berhasil dikembalikan!")
    
while True:
    print("\n==== MENU ====")
    print("1. Tambah Buku")
    print("2. Lihat Buku")
    print("3. Hapus Buku")
    print("4. Cari Buku")
    print("5. Tambah Anggota")
    print("6. Hapus Anggota")
    print("7. Pinjam Buku")
    print("8. Lihat Peminjaman")
    print("9. Kembalikan Buku")
    print("10. Keluar")

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
        tambah_anggota()

    if pilihan == "6":
        hapus_anggota()

    elif pilihan == "7":
        pinjam_buku()

    elif pilihan == "8":
        lihat_peminjaman()
        
    elif pilihan == "9":
        kembalikan_buku()

    elif pilihan == "10":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")