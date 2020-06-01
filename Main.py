'''
Nama Kelompok:
- Marshall Anugrah Najmi    1910511034
- Brahma Aditama            1910511036
- Jovanka Samudra           1910511040
- Daffy Fayyadhya Ramzy     1910511044
- Muhammad Raffiza Azka     1910511062
'''

import os
import time


class DataPenduduk:
    nik: str
    nama: str
    jenisKelamin: chr
    alamat: str
    tglLahir: list
    usia: int
    pekerjaan: str

# code struktur data Queue


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.data = []

    def createEmpty(self):
        self.first = -1
        self.last = -1

    def isEmpty(self):
        hasil = False
        if(self.first == -1):
            hasil = True
        return hasil

    def add(self, nik, nama, jenisKelamin, alamat, tglLahir, usia, pekerjaan):
        if(self.isEmpty() == True):
            self.last = 0
            self.first = 0

            self.data.append([])
            self.data[self.last] = DataPenduduk()
            self.data[0].nik = nik
            self.data[0].nama = nama
            self.data[0].jenisKelamin = jenisKelamin
            self.data[0].alamat = alamat
            self.data[0].tglLahir = tglLahir
            self.data[0].usia = usia
            self.data[0].pekerjaan = pekerjaan
        else:
            self.last = self.last + 1

            self.data.append([])
            self.data[self.last] = DataPenduduk()
            self.data[self.last].nik = nik
            self.data[self.last].nama = nama
            self.data[self.last].jenisKelamin = jenisKelamin
            self.data[self.last].alamat = alamat
            self.data[self.last].tglLahir = tglLahir
            self.data[self.last].usia = usia
            self.data[self.last].pekerjaan = pekerjaan

    def getFirst(self):
        return self.data[self.first]

    def delete(self):
        if(self.last == 0):
            self.first = -1
            self.last = -1

        else:
            for i in range(self.first+1, self.last+1):
                self.data[i-1].nik = self.data[i].nik
                self.data[i-1].nama = self.data[i].nama
                self.data[i-1].jenisKelamin = self.data[i].jenisKelamin
                self.data[i-1].alamat = self.data[i].alamat
                self.data[i-1].usia = self.data[i].usia
                self.data[i-1].pekerjaan = self.data[i].pekerjaan

            self.last = self.last - 1

    def printQueue(self):
        if(self.first != 1):
            for i in range(self.first, self.last+1):
                print(self.data[i].nik + "\t" + self.data[i].nama)
        else:
            print("Tidak ada data")

# code struktur data BST


class Node:
    def __init__(self, nik, nama, jenisKelamin, alamat, tglLahir, usia, pekerjaan):
        self.nik = nik
        self.nama = nama
        self.jenisKelamin = jenisKelamin
        self.alamat = alamat
        self.tglLahir = tglLahir
        self.usia = usia
        self.pekerjaan = pekerjaan
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, nik, nama, jenisKelamin, alamat, tglLahir, usia, pekerjaan):
        newNode = Node(nik, nama, jenisKelamin, alamat,
                       tglLahir, usia, pekerjaan)
        if (self.root == None):
            self.root = newNode
            return
        current = self.root
        parent = None
        while(True):
            parent = current
            if (int(nik) < int(current.nik)):
                current = current.left
                if (current == None):
                    parent.left = newNode
                    return
            else:
                current = current.right
                if (current == None):
                    parent.right = newNode
                    return

    def display(self, root):
        if (root != None):
            self.display(root.left)
            print("NIK              :", root.nik)
            print("Nama             :", root.nama)
            print("Kelamin          :", root.jenisKelamin)
            print("Alamat           :", root.alamat)
            print("Tanggal Lahir    :", "/".join(root.tglLahir))
            print("Usia             :", root.usia)
            print("Pekerjaan        :", root.pekerjaan)
            print("===============================")
            self.display(root.right)

    def find(self, nik):
        current = self.root
        while (current != None):
            if (int(current.nik) == int(nik)):
                return True
            elif (int(current.nik) > int(nik)):
                current = current.left
            else:
                current = current.right
        return False

    def printNode(self, nik):
        current = self.root
        while (current != None):
            if (int(current.nik) == int(nik)):
                print("NIK              :", current.nik)
                print("Nama             :", current.nama)
                print("Kelamin          :", current.jenisKelamin)
                print("Alamat           :", current.alamat)
                print("Tanggal Lahir    :", "/".join(current.tglLahir))
                print("Usia             :", current.usia)
                print("Pekerjaan        :", current.pekerjaan)
                print("===============================")
                return 0
            elif (int(current.nik) > int(nik)):
                current = current.left
            else:
                current = current.right

    def delete(self, nik):
        parent = self.root
        current = self.root
        isLeftChild = False

        while (int(current.nik) != int(nik)):
            parent = current
            if (int(current.nik) > int(nik)):
                isLeftChild = True
                current = current.left
            else:
                isLeftChild = False
                current = current.right
            if (current == None):
                return False

        # case 1 (Node has no children)
        if (current.left == None and current.right == None):
            if (current == self.root):
                self.root = None
            if (isLeftChild == True):
                parent.left = None
            else:
                parent.right = None

        # case 2 (node has 1 child)
        elif (current.right == None):
            if (current == self.root):
                self.root = current.left
            elif (isLeftChild):
                parent.left = current.left
            else:
                parent.right = current.left

        elif (current.left == None):
            if (current == self.root):
                self.root = current.right
            elif (isLeftChild):
                parent.left = current.right
            else:
                parent.right = current.right

        elif(current.left != None and current.right != None):
            successor = self.getSuccessor(current)
            if (current == self.root):
                self.root = successor
            elif (isLeftChild):
                parent.left = successor
            else:
                parent.right = successor
            successor.left = current.left
        return True

    def getSuccessor(self, deleteNode):
        successor = None
        successorParent = None
        current = deleteNode.right
        while (current != None):
            successorParent = successor
            successor = current
            current = current.left

        if (successor != deleteNode.right):
            successorParent.left = successor.right
            successor.right = deleteNode.right

        return successor


# fungsi untuk menghitung usia dilihat dari tanggal lahir
def hitungUsia(tglLahir):
    waktu = time.localtime()
    usia = (waktu.tm_year-1) - int(tglLahir[2])

    if waktu.tm_mon == int(tglLahir[1]):
        if waktu.tm_mday <= int(tglLahir[0]):
            usia = waktu.tm_year - int(tglLahir[2])
    elif waktu.tm_mon > int(tglLahir[1]):
        usia = waktu.tm_year - int(tglLahir[2])

    return usia


# Main code
if __name__ == "__main__":

    # fungsi untuk clear screen
    def clsscr(): return os.system("cls")

    # inisialisasi objek
    queue = Queue()
    BST = BinarySearchTree()
    queue.createEmpty()

    while True:

        # Main menu
        clsscr()
        print("===========================")
        print("            Menu")
        print("===========================")
        print("[1] Masukan Data Baru")
        print("[2] Lihat Data")
        print("[3] Cari Data")
        print("[4] Hapus Data")
        print("[5] Lihat Data Dalam Proses")
        print("[6] Keluar")
        print("---------------------------")
        menu = input("Pilih menu > ")

        if menu == "1":

            # kode memasukan data baru
            while True:
                clsscr()
                print("=========================")
                print("        Buat Data")
                print("=========================")
                NIK = input("NIK              : ")
                nama = input("Nama             : ")
                jenisKelamin = input("Jenis Kelamin    : ")
                alamat = input("Alamat           : ")
                print("- Format (DD/MM/YYYY)")
                tglLahir = input("Tanggal Lahir    : ").split("/")
                pekerjaan = input("Pekerjaan        : ")

                # menghitung usia berdasarkan tanggal lahir
                usia = hitungUsia(tglLahir)

                tanya = input("\nApakah anda sudah yakin [y/t] > ")

                if tanya.lower() == "y":

                    # memasukan data yang telah diinput ke dalam queue
                    queue.add(NIK, nama, jenisKelamin, alamat,
                              tglLahir, usia, pekerjaan)
                    print("\nData anda sedang diproses, mohon tunggu...")
                    input("Tekan ENTER untuk kembali...")
                    break
                elif tanya.lower() == "t":
                    tanya = input("Apakah anda ingin mengisi ulang [y/t] > ")

                    # mengisi data ulang
                    if tanya.lower() == "y":
                        pass
                    elif tanya.lower() == "t":
                        break
                    else:
                        print("\nMaaf pilihan yang anda pilih tidak tersedia")
                        print("Data tidak tersimpan!!!")
                        input("Tekan ENTER untuk kembali...")
                        break
                else:
                    print("\nMaaf pilihan yang anda pilih tidak tersedia")
                    print("Data tidak tersimpan!!!")
                    input("Tekan ENTER untuk kembali...")
                    break

        elif menu == "2":
            # kode untuk melihat data yang sudah selesai diproses
            pass
        elif menu == "3":
            # kode mencari data yang sudah selesai diproses
            pass
        elif menu == "4":
            # kode menghapus data yang sudah diproses
            while True:
                clsscr()
                print("=========================")
                print("        Hapus Data")
                print("=========================")
                NIK = input("Masukkan NIK dari data yang ingin dihapus: ")

                # mengecek apakah data ada
                check = BST.find(NIK)
                if check == True:
                    BST.printNode(NIK)
                    tanya = input("Hapus Data? [y/t] > ")
                    if tanya.lower() == "y":
                        clsscr()

                        # menghapus data pada BST
                        BST.delete(NIK)
                        print("Data berhasil dihapus!!!")
                        input("Tekan ENTER untuk kembali...")
                        break
                    elif tanya.lower() == 't':
                        clsscr()
                        print("Data tidak jadi dihapus")
                        tanya = input("Masukkan ulang NIK? [y/t] > ")
                        if tanya.lower() == 'y':
                            pass
                        elif tanya.lower() == 't':
                            break
                        else:
                            print("\nMaaf pilihan yang anda pilih tidak tersedia")
                            input("Tekan ENTER untuk kembali...")
                            break
                    else:
                        print("\nMaaf pilihan yang anda pilih tidak tersedia")
                        input("Tekan ENTER untuk kembali...")
                        break
                elif check == False:
                    print("\nData dengan NIK tersebut tidak ditemukan")
                    tanya = input("Masukkan ulang NIK? [y/t] > ")
                    if tanya.lower() == 'y':
                        pass
                    elif tanya.lower() == 't':
                        break
                    else:
                        print("\nMaaf pilihan yang anda pilih tidak tersedia")
                        input("Tekan ENTER untuk kembali...")
                        break

        elif menu == "5":
            # kode untuk melihat data yang masih dalam proses
            clsscr()
            print("====================================")
            print("             Dalam Proses")
            print("====================================")
            print("NIK\t\tNama")
            print("------------------------------------")

            # mencetak isi dalam antrian proses
            queue.printQueue()

            # mengambil data yang ada pada antrian pertama
            dataPertama = queue.getFirst()
            tanya = input("\nApakah data " + dataPertama.nik +
                          " sudah selesai dikerjakan [y/t] > ")

            # memasukan data pertama pada antrian kedalam data yang sudah selesai dikerjakan
            if tanya.lower() == "y":
                BST.insert(dataPertama.nik, dataPertama.nama, dataPertama.jenisKelamin,
                           dataPertama.alamat, dataPertama.tglLahir, dataPertama.usia, dataPertama.pekerjaan)
                print("\nData", dataPertama.nik, "telah selesai dikerjakan")
                input("Tekan ENTER untuk kembali...")
                queue.delete()
            elif tanya.lower() == "t":
                input("Tekan ENTER untuk kembali...")
            else:
                print("\nMaaf pilihan yang anda pilih tidak tersedia")
                input("Tekan ENTER untuk kembali...")

        elif menu == "6":
            # kode untuk keluar dari program
            clsscr()
            exit("Terima kasih...")
        else:
            # kode jika user memilih diluar jangkauan pilihan menu
            print("\nMaaf pilihan yang ada masukan tidak tersedia")
            input("Tekan ENTER untuk kembali...")
