print("Dibuat oleh Kelompok 08")
class Jadwal:
    def __init__(self):
        # Inisialisasi jadwal sebagai kamus kosong
        self.jadwal = {}

    def tambah_kelas(self, hari, waktu, mata_kuliah):
        # Menambahkan kelas baru ke jadwal
        if hari not in self.jadwal:
            self.jadwal[hari] = {}
        if waktu not in self.jadwal[hari]:
            self.jadwal[hari][waktu] = mata_kuliah
            print(f"Menambahkan kelas {mata_kuliah} pada hari {hari} jam {waktu}.")
        else:
            print("Sudah ada kelas yang terjadwal pada waktu tersebut.")

    def hapus_kelas(self, hari):
        # Menghapus semua kelas dari jadwal pada hari tertentu
        if hari in self.jadwal:
            del self.jadwal[hari]
            print(f"Semua kelas pada hari {hari} telah dihapus.")
        else:
            print("Tidak ditemukan kelas pada hari tersebut.")

     def tampilkan_jadwal(self):
        # Menampilkan jadwal
        print("Jadwal:")
        if not self.jadwal:
            print("Tidak ada kelas yang terjadwal.")
        else:
            for hari, kelas in self.jadwal.items():
                print(hari)
                for waktu, mata_kuliah in kelas.items():
                    print(f"\t{waktu}: {mata_kuliah}")

    def dapatkan_jadwal_pengguna() -> Jadwal:
    # Mendapatkan jadwal dari pengguna
    jadwal = Jadwal()
    print("Masukkan jadwal Anda dengan format (hari, waktu, mata kuliah), 'hapus, hari' untuk menghapus jadwal pada hari tertentu, 'jadwal' untuk menampilkan jadwal, atau 'selesai' untuk menyelesaikan:")
    while True:
        input_pengguna = input("Masukkan jadwal: ").split(",")
        command = input_pengguna[0].strip().lower()
        if command == 'selesai':
            break
        elif command == 'hapus':
            if len(input_pengguna) == 2:
                hari = input_pengguna[1].strip()
                jadwal.hapus_kelas(hari)
            else:
                print("Format input tidak valid. Masukkan dengan format: hapus, hari")
        elif command == 'jadwal':
            jadwal.tampilkan_jadwal()
        elif len(input_pengguna) == 3:
            hari, waktu, mata_kuliah = map(str.strip, input_pengguna)
            jadwal.tambah_kelas(hari, waktu, mata_kuliah)
        else:
            print("Format input tidak valid. Masukkan dengan format: hari, waktu, mata kuliah")
    return jadwal

    def main() -> None:
    # Fungsi utama program
    print("Selamat datang di aplikasi penjadwalan.")
    print("Gunakan aplikasi ini untuk menyusun jadwal kuliah Anda.")
    print("Setelah selesai, Anda bisa melihat jadwal yang sudah dibuat.")
    print("Untuk keluar, cukup ketik 'selesai'.\n")

    jadwal_pengguna = dapatkan_jadwal_pengguna()

    print("\nJadwal yang telah Anda masukkan:")
    jadwal_pengguna.tampilkan_jadwal()

if __name__ == "__main__":
    main()

