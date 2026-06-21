import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="pythonuser",
    password="Yahya18+",
    database="perpustakaan"
)

cursor = db.cursor()
def tambah_buku():
    judul = input("Judul buku: ")
    penulis = input("Penulis: ")
    tahun = int(input("Tahun: "))  
    sql = """
    INSERT INTO buku (judul, tahun, penulis)
    VALUES (%s, %s, %s)
    """
    data = (judul, tahun, penulis)
    cursor.execute(sql, data)
    db.commit()
    print("Buku berhasil ditambahkan!")

def lihat_buku():
    cursor.execute("SELECT * FROM buku")
    hasil = cursor.fetchall()
    print("\n=== DAFTAR BUKU ===")
    for data in hasil:
        print(f"\nID      : {data[0]}")
        print(f"Judul   : {data[1]}")
        print(f"Penulis : {data[2]}")
        print(f"Tahun   : {data[3]}")

def cari_buku():
    kata_kunci = input("Masukkan judul buku: ")
    sql = """
    SELECT * FROM buku
    WHERE judul LIKE %s
    """
    cursor.execute(sql, ("%" + kata_kunci + "%",))
    hasil = cursor.fetchall()
    if len(hasil) == 0:
        print("Buku tidak di temukan.")
    else:
        print("\n=== HASIL PENCARIAN ===")
        for data in hasil:
            print(f"\nID      : {data[0]}")
            print(f"Judul   : {data[1]}")
            print(f"Penulis : {data[2]}")
            print(f"Tahun   : {data[3]}")

def hapus_buku():
    id_buku = input("Masukkan ID buku yang akan dihapus: ")
    sql = "DELETE FROM buku WHERE id = %s"
    cursor.execute(sql, (id_buku,))
    db.commit()
    if cursor.rowcount > 0:
        print("Buku berhasil dihapus!")
    else:
        print("ID buku tidak ditemukan!")
def edit_buku():
    id_buku = input("Masukkan ID buku yang akan diedit: ")

    judul = input("Judul baru: ")
    penulis = input("Penulis baru: ")
    tahun = input("Tahun baru: ")

    sql = """
    UPDATE buku
    SET judul=%s, tahun=%s, penulis=%s
    WHERE id=%s
    """

    data = (judul, tahun, penulis, id_buku)
    cursor.execute(sql, data)
    db.commit()

    if cursor.rowcount > 0:
        print("Buku berhasil diupdate!")
    else:
        print("ID tidak  ditemukan!")

while True:
    print("\n== MENU ==")
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

    else:
        print("Pilihan tidak valid!")