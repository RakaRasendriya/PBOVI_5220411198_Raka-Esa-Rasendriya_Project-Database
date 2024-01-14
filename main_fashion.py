import mysql.connector
from mysql.connector import Error
import os

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='5220411198',
            user='root',
            password=''
        )
        print("Koneksi ke database berhasil")
    except Error as e:
        print(f"Error: {e}")
    return connection

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Query berhasil dijalankan")
    except Error as e:
        print(f"Error: {e}")

class Pakaian:
    def __init__(self, nama, umur, jenis_kelamin):
        self.nama = nama
        self._umur = umur
        self.__jenis_kelamin = jenis_kelamin

    def display_info(self):
        print(f"\nInformasi Pengguna:")
        print(f"Nama            : {self.nama}")
        print(f"Umur            : {self._umur} tahun")
        print(f"Jenis Kelamin   : {self.__jenis_kelamin}")

class Laki(Pakaian):
    casual = {
        'atasan': ['T-shirt ', 'Sweater', 'Hoodie'],
        'bawahan': ['Jeans', 'Chino shorts', 'Joggers'],
        'alas_kaki': ['Shoes', 'Sneakers', 'Sandals']
    }

    formal = {
        'atasan': ['Suit Jacket', 'Tuxedo shirt', 'Polo shirt'],
        'bawahan': ['Suit trousers', 'Chinos', 'Tuxedo pants'],
        'alas_kaki': ['Oxford shoes', 'Loafers', 'Brogues']
    }

    def __init__(self, nama, umur):
        super().__init__(nama, umur, "Laki-laki")
        self.top = None
        self.bottom = None
        self.alas_kaki = None
        self.tipe_pakaian = None

    def show_menu(self, kategori, clothes):
        print(f"Pilihan {kategori}:")
        for idx, item in enumerate(clothes[kategori], start=1):
            print(f"{idx}. {item}")
        choice = int(input(f"Pilih nomor {kategori}: "))
        return clothes[kategori][choice - 1]

    def pilih_pakaian(self, kategori, clothes):
        print(f"\nMemilih Pakaian untuk {self.nama} ({kategori}):")
        selected_item = self.show_menu(kategori, clothes)
        return selected_item

    def set_tipe_pakaian(self, tipe):
        print(f"\nMemilih Tipe Pakaian {tipe} untuk {self.nama}:")
        if tipe == 'casual':
            self.top = self.pilih_pakaian('atasan', self.casual)
            self.bottom = self.pilih_pakaian('bawahan', self.casual)
            self.alas_kaki = self.pilih_pakaian('alas_kaki', self.casual)
        elif tipe == 'formal':
            self.top = self.pilih_pakaian('atasan', self.formal)
            self.bottom = self.pilih_pakaian('bawahan', self.formal)
            self.alas_kaki = self.pilih_pakaian('alas_kaki', self.formal)
        self.tipe_pakaian = tipe

    def display_pakaianL(self):
        super().display_info()
        print(f"\nDetail Pakaian untuk {self.nama}:")
        print(f"Tipe Pakaian    : {self.tipe_pakaian if self.tipe_pakaian else 'Belum dipilih'}")
        print(f"Atasan          : {self.top if self.top else 'Belum dipilih'}")
        print(f"Bawahan         : {self.bottom if self.bottom else 'Belum dipilih'}")
        print(f"Alas Kaki       : {self.alas_kaki if self.alas_kaki else 'Belum dipilih'}")

class Perempuan(Pakaian):
    casual = {
        'dalam': ['Blouse', 'Sweater', 'T-Shirt'],
        'luar': ['Vest', 'Cardigan', 'Denim Jacket'],
        'bawahan': ['Skirt', 'Pants', 'Shorts'],
        'alas_kaki': ['Shoes', 'Sneakers', 'Sandals']
    }

    formal = {
        'dalam': ['Dress shirt', 'Blouse', 'Kemeja Putih'],
        'luar': ['Long Cardigan', 'Blazer', 'Vest'],
        'bawahan': ['Dress pants', 'Pencil skirt', 'Trousers'],
        'alas_kaki': ['Heels', 'Pumps', 'Slingbacks']
    }

    def __init__(self, nama, umur):
        super().__init__(nama, umur, "Perempuan")
        self.inner = None
        self.outer = None
        self.bottom = None
        self.alas_kaki = None
        self.tipe_pakaian = None

    def show_menu(self, kategori, clothes):
        print(f"Pilihan {kategori}:")
        for idx, item in enumerate(clothes[kategori], start=1):
            print(f"{idx}. {item}")
        choice = int(input(f"Pilih nomor {kategori}: "))
        return clothes[kategori][choice - 1]

    def pilih_pakaian(self, kategori, clothes):
        print(f"\nMemilih Pakaian untuk {self.nama} ({kategori}):")
        selected_item = self.show_menu(kategori, clothes)
        return selected_item

    def set_tipe_pakaian(self, tipe):
        print(f"\nMemilih Tipe Pakaian {tipe} untuk {self.nama}:")
        if tipe == 'casual':
            self.inner = self.pilih_pakaian('dalam', self.casual)
            self.outer = self.pilih_pakaian('luar', self.casual)
            self.bottom = self.pilih_pakaian('bawahan', self.casual)
            self.alas_kaki = self.pilih_pakaian('alas_kaki', self.casual)
        elif tipe == 'formal':
            self.inner = self.pilih_pakaian('dalam', self.formal)
            self.outer = self.pilih_pakaian('luar', self.formal)
            self.bottom = self.pilih_pakaian('bawahan', self.formal)
            self.alas_kaki = self.pilih_pakaian('alas_kaki', self.formal)
        self.tipe_pakaian = tipe

    def display_pakaianP(self):
        super().display_info()
        print(f"\nDetail Pakaian untuk {self.nama}:")
        print(f"Tipe Pakaian    : {self.tipe_pakaian if self.tipe_pakaian else 'Belum dipilih'}")
        print(f"Inner           : {self.inner if self.inner else 'Belum dipilih'}")
        print(f"Outer           : {self.outer if self.outer else 'Belum dipilih'}")
        print(f"Bawahan         : {self.bottom if self.bottom else 'Belum dipilih'}")
        print(f"Alas Kaki       : {self.alas_kaki if self.alas_kaki else 'Belum dipilih'}")

class Tampilan(Perempuan):
    pilihan = {
        'aksesoris': ['Anting', 'Kalung', 'Gelang', 'Cincin'],
        'makeup': ['Base', 'Eye', 'Lip', 'Cheek', 'Brow', 'Setting Spray', 'Body', 'Mineral', 'Skincare-Infused']
    }

    def __init__(self, nama, umur):
        super().__init__(nama, umur)
        self.aksesoris = []
        self.makeup = []

    def tambah_aksesoris(self):
        selected_tampilan = self.show_menu('aksesoris', self.pilihan)

        if selected_tampilan not in self.aksesoris:
            self.aksesoris.append(selected_tampilan)
            print(f"Aksesoris {selected_tampilan} dipilih.")
        
    def tambah_makeup(self):
        selected_tampilan = self.show_menu('makeup', self.pilihan)

        if selected_tampilan not in self.makeup:
            self.makeup.append(selected_tampilan)
            print(f"Make Up {selected_tampilan} dipilih.")
        
    def display_tampilan(self):
        super().display_pakaianP()
        print(f"Make Up         : {', '.join(self.makeup) if self.makeup else 'Belum dipilih'}")
        print(f"Aksesoris       : {', '.join(self.aksesoris) if self.aksesoris else 'Belum dipilih'}")


#Penerapan CRUD, INSERT, SELECT dan lainnya yang dibutuhkan untuk mengelola database
def list_pengguna(connection):
    connection = create_connection()
    if connection.is_connected():
        try:
            cursor = connection.cursor(dictionary=True)

            query = "SELECT * FROM users"
            cursor.execute(query)
            users = cursor.fetchall()

            while True:
                print("\n==============================")
                print("\nList Pengguna:")
                for idx, user in enumerate(users, start=1):
                    print(f"{idx}. {user['nama']} ({user['jenis_kelamin']})")
                choice_detail = input("\nPilih nomor pengguna untuk melihat atau tambah detail (0 untuk kembali): ")
                if choice_detail.isdigit():
                    choice_detail = int(choice_detail)
                    if 0 < choice_detail <= len(users):
                        pengguna_terpilih = users[choice_detail - 1]

                        while True:
                            os.system("cls")
                            print("\n==============================")
                            print(f"Detail Pengguna {pengguna_terpilih['nama']} ({pengguna_terpilih['jenis_kelamin']}):")
                            print("1. Tampilkan Pakaian")
                            print("2. Tambah Pakaian")
                            print("3. Hapus Pengguna")
                            print("4. Update Data Pengguna")
                            print("0. Kembali")
                            choice_detail_menu = input("\nPilih Menu : ")

                            if choice_detail_menu == "1":
                                display_pakaian_pengguna(connection, pengguna_terpilih)
                            elif choice_detail_menu == "2":
                                tambah_pakaian_pengguna(connection, pengguna_terpilih)
                            elif choice_detail_menu == "3":
                                hapus_pengguna(connection, pengguna_terpilih)
                            elif choice_detail_menu == "4":
                                update_data_pengguna(connection, pengguna_terpilih)
                            elif choice_detail_menu == "0":
                                break
                            else:
                                print("Pilihan tidak valid. Silakan pilih antara 0-4.")
                            os.system("pause")

                    elif choice_detail == 0:
                        break
                    else:
                        print("Nomor pengguna tidak valid.")
                else:
                    print("Masukkan angka yang valid.")
                os.system("pause")

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            connection.close()
    else:
        print("Tidak dapat terhubung ke database.")


def display_pakaian_pengguna(connection, pengguna_terpilih):
    cursor = connection.cursor(dictionary=True)

    if pengguna_terpilih['jenis_kelamin'] == 'L':
        pengguna = Laki(pengguna_terpilih['nama'], pengguna_terpilih['umur'])
        query_pakaian = f"SELECT * FROM laki WHERE user_id = {pengguna_terpilih['id']}"
        cursor.execute(query_pakaian)
        pakaian = cursor.fetchone()

        if pakaian:
            pengguna.top = pakaian['top']
            pengguna.bottom = pakaian['bottom']
            pengguna.alas_kaki = pakaian['alas_kaki']
            pengguna.tipe_pakaian = pakaian['tipe_pakaian']

        pengguna.display_pakaianL()

    elif pengguna_terpilih['jenis_kelamin'] == 'P':
        pengguna = Tampilan(pengguna_terpilih['nama'], pengguna_terpilih['umur'])
        query_pakaian = f"SELECT * FROM perempuan WHERE user_id = {pengguna_terpilih['id']}"
        cursor.execute(query_pakaian)
        pakaian = cursor.fetchone()

        if pakaian:
            pengguna.inner = pakaian['inner_clothes']
            pengguna.outer = pakaian['outer_clothes']
            pengguna.bottom = pakaian['bottom']
            pengguna.alas_kaki = pakaian['alas_kaki']
            pengguna.tipe_pakaian = pakaian['tipe_pakaian']

        query_tampilan = f"SELECT * FROM tampilan WHERE user_id = {pengguna_terpilih['id']}"
        cursor.execute(query_tampilan)
        tampilan = cursor.fetchone()

        if tampilan:
            pengguna.aksesoris = tampilan['aksesoris'].split(', ') if tampilan['aksesoris'] else []
            pengguna.makeup = tampilan['makeup'].split(', ') if tampilan['makeup'] else []

        pengguna.display_tampilan()


def hapus_pengguna(connection, pengguna_terpilih):
    user_id = pengguna_terpilih['id']
    jenis_kelamin = pengguna_terpilih['jenis_kelamin']
    confirm_delete = input(f"Apakah Anda yakin ingin menghapus pengguna {pengguna_terpilih['nama']}? (Y/N): ")

    if confirm_delete.upper() == 'Y':
        try:
            cursor = connection.cursor()

            if jenis_kelamin == 'L':
                query_delete_pakaian = f"DELETE FROM laki WHERE user_id = {user_id}"
                execute_query(connection, query_delete_pakaian)
            elif jenis_kelamin == 'P':
                query_delete_pakaian_perempuan = f"DELETE FROM perempuan WHERE user_id = {user_id}"
                query_delete_tampilan = f"DELETE FROM tampilan WHERE user_id = {user_id}"
                execute_query(connection, query_delete_pakaian_perempuan)
                execute_query(connection, query_delete_tampilan)

            query_delete_user = f"DELETE FROM users WHERE id = {user_id}"
            execute_query(connection, query_delete_user)

            print(f"Pengguna dengan ID {user_id} berhasil dihapus.")
            os.system("pause")

        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            tampil()
    else:
        print(f"Pengguna dengan ID {user_id} tidak dihapus.")


def update_data_pengguna(connection, pengguna_terpilih):
    user_id = pengguna_terpilih['id']
    try:
        cursor = connection.cursor(dictionary=True)
        query_get_user = f"SELECT * FROM users WHERE id = {user_id}"
        cursor.execute(query_get_user)
        user_data = cursor.fetchone()

        if user_data:
            print(f"\nData Pengguna yang akan diupdate:")
            print(f"Nama          : {user_data['nama']}")
            print(f"Umur          : {user_data['umur']}")
            print(f"Jenis Kelamin : {user_data['jenis_kelamin']}")

            baru_nama = input("\nMasukkan Nama Baru: ")
            baru_umur = int(input("Masukkan Umur Baru: "))
            baru_jk = input("Masukkan Jenis Kelamin Baru (L/P): ")

            if baru_jk.upper() in ['L', 'P']:
                query_update_user = f"UPDATE users SET nama = '{baru_nama}', umur = {baru_umur}, jenis_kelamin = '{baru_jk}' WHERE id = {user_id}"
                execute_query(connection, query_update_user)
                print("Data pengguna berhasil diupdate.")
                os.system("pause")
                tampil()
            else:
                print("Jenis kelamin tidak valid.")
                os.system("pause")
        else:
            print(f"Pengguna dengan ID {user_id} tidak ditemukan.")
            os.system("pause")

    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

    os.system("pause")


def tambah_pakaian_pengguna(connection, pengguna_terpilih):
    cursor = connection.cursor()

    if pengguna_terpilih['jenis_kelamin'] == 'L':
        pengguna = Laki(pengguna_terpilih['nama'], pengguna_terpilih['umur'])
        query_pakaian = f"SELECT * FROM laki WHERE user_id = {pengguna_terpilih['id']}"
        cursor.execute(query_pakaian)
        pakaian = cursor.fetchone()

        if pakaian:
            pengguna.top = pakaian[1]
            pengguna.bottom = pakaian[2]
            pengguna.alas_kaki = pakaian[3]
            pengguna.tipe_pakaian = pakaian[4]

        pengguna.display_pakaianL()

        while True:
            os.system("cls")
            print("\n==============================")
            print("\nTambah Pakaian:")
            print("1. Casual")
            print("2. Formal")
            print("0. Kembali")
            choice_tambah_pakaian = input("\nPilih Tipe Pakaian (0-2): ")

            if choice_tambah_pakaian == "1":
                pengguna.set_tipe_pakaian('casual')
                update_query = f"""
                UPDATE laki
                SET top = '{pengguna.top}', bottom = '{pengguna.bottom}', alas_kaki = '{pengguna.alas_kaki}', tipe_pakaian = 'casual'
                WHERE user_id = {pengguna_terpilih['id']}
                """
                execute_query(connection, update_query)
                print("Pakaian casual berhasil ditambahkan.")

            elif choice_tambah_pakaian == "2":
                pengguna.set_tipe_pakaian('formal')
                update_query = f"""
                UPDATE laki
                SET top = '{pengguna.top}', bottom = '{pengguna.bottom}', alas_kaki = '{pengguna.alas_kaki}', tipe_pakaian = 'formal'
                WHERE user_id = {pengguna_terpilih['id']}
                """
                execute_query(connection, update_query)
                print("Pakaian formal berhasil ditambahkan.")

            elif choice_tambah_pakaian == "0":
                break

            else:
                print("Pilihan tidak valid. Silakan pilih antara 0-2.")
            os.system("pause")

    elif pengguna_terpilih['jenis_kelamin'] == 'P':
        pengguna = Tampilan(pengguna_terpilih['nama'], pengguna_terpilih['umur'])
        query_pakaian = f"SELECT * FROM perempuan WHERE user_id = {pengguna_terpilih['id']}"
        cursor.execute(query_pakaian)
        pakaian = cursor.fetchone()

        if pakaian:
            pengguna.inner = pakaian[1]
            pengguna.outer = pakaian[2]
            pengguna.bottom = pakaian[3]
            pengguna.alas_kaki = pakaian[4]
            pengguna.tipe_pakaian = pakaian[5]

        pengguna.display_tampilan()

        while True:
            os.system("cls")
            print("\n==============================")
            print("\nTambah Pakaian:")
            print("1. Casual")
            print("2. Formal")
            print("3. Tambah Aksesoris")
            print("4. Tambah MakeUp")
            print("0. Kembali")
            choice_tambah_pakaian = input("\nPilih Tipe Pakaian (0-3): ")

            if choice_tambah_pakaian == "1":
                pengguna.set_tipe_pakaian('casual')
                update_query = f"""
                UPDATE perempuan
                SET inner_clothes = '{pengguna.inner}', outer_clothes = '{pengguna.outer}',
                bottom = '{pengguna.bottom}', alas_kaki = '{pengguna.alas_kaki}', tipe_pakaian = 'casual'
                WHERE user_id = {pengguna_terpilih['id']}
                """
                execute_query(connection, update_query)
                print("Pakaian casual berhasil ditambahkan.")
            elif choice_tambah_pakaian == "2":
                pengguna.set_tipe_pakaian('formal')
                update_query = f"""
                UPDATE perempuan
                SET inner_clothes = '{pengguna.inner}', outer_clothes = '{pengguna.outer}',
                bottom = '{pengguna.bottom}', alas_kaki = '{pengguna.alas_kaki}', tipe_pakaian = 'formal'
                WHERE user_id = {pengguna_terpilih['id']}
                """
                execute_query(connection, update_query)
                print("Pakaian formal berhasil ditambahkan.")
                
            elif choice_tambah_pakaian == "3":
                pengguna.tambah_aksesoris()
                update_query = f"""
                UPDATE tampilan
                SET aksesoris = '{', '.join(pengguna.aksesoris)}'
                WHERE user_id = {pengguna_terpilih['id']}
                """
                execute_query(connection, update_query)
                print("Aksesoris berhasil ditambahkan.")

            elif choice_tambah_pakaian == "4":
                pengguna.tambah_makeup()
                update_query = f"""
                UPDATE tampilan
                SET makeup = '{', '.join(pengguna.makeup)}'
                WHERE user_id = {pengguna_terpilih['id']}
                """
                execute_query(connection, update_query)
                print("MakeUp berhasil ditambahkan.")

            elif choice_tambah_pakaian == "0":
                break
            else:
                print("Pilihan tidak valid. Silakan pilih antara 0-3.")
            os.system("pause")
    else:
        print("Jenis kelamin tidak valid.")


#Main Program
def tampil():
    connection = create_connection()
    while True:
        os.system("cls")
        print("\n==============================")
        print("Menu Utama :")
        print("1. Tambah Pengguna")
        print("2. List Pengguna")
        print("3. Keluar")
        choice_menu = input("\nPilih Menu : ")

        if choice_menu == "1":
            while True:
                nama = input("\nMasukkan Nama Pengguna: ")
                umur = int(input("Masukkan Umur Pengguna: "))
                jenis_kelamin = input("Masukkan Jenis Kelamin Pengguna (L/P): ")

                if jenis_kelamin.upper() in ['L', 'P']:
                    break
                else:
                    print("Jenis kelamin tidak valid. Silahkan isi ulang data diri Anda.")
                os.system("pause")

            if jenis_kelamin.upper() == 'L':
                pengguna = Laki(nama, umur)
                query_insert = f"INSERT INTO users (nama, umur, jenis_kelamin) VALUES ('{nama}', {umur}, 'L')"
                execute_query(connection, query_insert)

                query_get_id = f"SELECT id FROM users WHERE nama = '{nama}'"
                cursor = connection.cursor()
                cursor.execute(query_get_id)
                user_id = cursor.fetchone()[0]

                query_insert_laki = f"INSERT INTO laki (user_id, top, bottom, alas_kaki, tipe_pakaian) VALUES ({user_id}, '', '', '', '')"
                execute_query(connection, query_insert_laki)

            elif jenis_kelamin.upper() == 'P':
                pengguna = Tampilan(nama, umur)
                query_insert = f"INSERT INTO users (nama, umur, jenis_kelamin) VALUES ('{nama}', {umur}, 'P')"
                execute_query(connection, query_insert)

                query_get_id = f"SELECT id FROM users WHERE nama = '{nama}'"
                cursor = connection.cursor()
                cursor.execute(query_get_id)
                user_id = cursor.fetchone()[0]

                query_insert_perempuan = f"INSERT INTO perempuan (user_id, inner_clothes, outer_clothes, bottom, alas_kaki, tipe_pakaian) VALUES ({user_id}, '', '', '', '', '')"
                execute_query(connection, query_insert_perempuan)

                query_insert_tampilan = f"INSERT INTO tampilan (user_id, aksesoris, makeup) VALUES ({user_id}, '', '')"
                execute_query(connection, query_insert_tampilan)

        elif choice_menu == "2":
            list_pengguna(connection)

        elif choice_menu == "3":
            print("Program selesai. Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-4.")
        os.system("pause")

if __name__ == "__main__":
    # create_connection()
    tampil()