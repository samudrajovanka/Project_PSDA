
'''
Nama Kelompok:
- Marshall Anugrah Najmi    1910511034
- Brahma Aditama            1910511036
- Jovanka Samudra           1910511040
- Daffy Fayyadhya Ramzy     1910511044
- Muhammad Raffiza Azka     1910511062
'''

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
            print("=======Isi Queue=======")
            for i in range(self.last, (self.first-1), -1):
                print("="*10)
                print("Data ke ", i)
                print("NIK           :", self.data[i].nik)
                print("Nama          :", self.data[i].nama)
                print("Jenis Kelamin :", self.data[i].jenisKelamin)
                print("Alamat        :", self.data[i].alamat)
                print("Tanggal Lahir :", self.data[i].tglLahir)
                print("Usia          :", self.data[i].usia)
                print("Pekerjaan     :", self.data[i].pekerjaan)

                print("="*10)
        else:
            print("Queue Kosong")

# code struktur data BST
class Node:
    def __init__(self, nik, nama, jeniskelamin, alamat, usia, pekerjaan):
        self.nik = nik
        self.nama = nama
        self.jeniskelamin = jeniskelamin
        self.alamat = alamat
        # self.tgllahir = tgllahir
        self.usia = usia
        self.pekerjaan = pekerjaan
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, nik, nama, jeniskelamin, alamat, usia, pekerjaan):
        newNode = Node(nik, nama, jeniskelamin, alamat, usia, pekerjaan)
        if (self.root == None):
            self.root = newNode
            return
        current = self.root
        parent = None
        while(True):
            parent = current
            if (nik < current.nik):
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
            print("NIK :", root.nik, end="\n")
            print("Nama :", root.nama, end="\n")
            print("Kelamin :", root.jeniskelamin, end="\n")
            print("Alamat :", root.alamat, end="\n")
            print("Usia :", root.usia, end="\n")
            print("Pekerjaan :", root.pekerjaan, end="\n")
            print("===================")
            self.display(root.right)

    def find(self, nik):
        current = self.root
        while (current != None):
            if (current.nik == nik):
                return True
            elif (current.nik > nik):
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, nik):
        parent = self.root
        current = self.root
        isLeftChild = False

        while (current.nik != nik):
            parent = current
            if (current.nik > nik):
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

    def getSuccessor(self, deleleNode):
        successor = None
        successorParent = None
        current = deleleNode.right
        while (current != None):
            successorParent = successor
            successor = current
            current = current.left

        if (successor != deleleNode.right):
            successorParent.left = successor.right
            successor.right = deleleNode.right

        return successor
        # tgl lahir belom


# test :
b = BinarySearchTree()

b.insert(100, 'budi', 'l', 'jakarta', 20, 'kuli')
b.insert(110, 'seno', 'l', 'bekasi', 19, 'maling')
b.insert(200, 'udin', 'l', 'bandung', 16, 'pelajar')
b.insert(90, 'fatimah', 'p', 'padang', 17, 'pelajar')

# Main code
if __name__ == "__main__":
    import os

    # fungsi untuk clear screen
    def clsscr(): return os.system("cls")

    while True:
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
            pass
        elif menu == "2":
            # kode untuk melihat data yang sudah selesai diproses
            pass
        elif menu == "3":
            # kode mencari data yang sudah selesai diproses
            pass
        elif menu == "4":
            # kode menghapus data yang sudah diproses
            pass
        elif menu == "5":
            # kode untuk melihat data yang masih dalam proses
            pass
        elif menu == "6":
            # kode untuk keluar dari program
            clsscr()
            exit("Terima kasih...")
        else:
            # kode jika user memilih diluar jangkauan
            print("\nMaaf pilihan yang ada masukan tidak tersedia")
            print("Tekan ENTER untuk kembali...", end="")
            input()
