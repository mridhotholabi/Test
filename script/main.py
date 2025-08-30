import os
from keyword_filter import filter_keyword
from preprocessing import bersihkan_teks

DATA_FOLDER = "../data/artikel"
OUTPUT_FOLDER = "../output"

def proses_artikel(nama_file):
    path = os.path.join(DATA_FOLDER, nama_file)
    with open(path, "r", encoding="utf-8") as f:
        isi = f.read()
    isi_bersih = bersihkan_teks(isi)
    if filter_keyword(isi_bersih):
        status = "TERLARANG"
    else:
        status = "AMAN"
    return status

def simpan_hasil(nama_file, status):
    hasil_path = os.path.join(OUTPUT_FOLDER, "hasil_filter.txt")
    with open(hasil_path, "a", encoding="utf-8") as f:
        f.write(f"{nama_file}: {status}\n")

def main():
    print("=== Mulai proses filter artikel ===")
    semua_file = os.listdir(DATA_FOLDER)
    for nama_file in semua_file:
        if nama_file.endswith(".txt"):
            status = proses_artikel(nama_file)
            simpan_hasil(nama_file, status)
            print(f"{nama_file} => {status}")
    print("=== Selesai ===")

if __name__ == "__main__":
    main()
