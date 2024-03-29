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

