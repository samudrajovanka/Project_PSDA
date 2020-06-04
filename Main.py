'''
Nama Kelompok:
- Marshall Anugrah Najmi    1910511034
- Brahma Aditama            1910511036
- Jovanka Samudra           1910511040
- Daffy Fayyadhya Ramzy     1910511044
- Muhammad Raffiza Azka     1910511062
'''

# import module
from os import system
from time import localtime
from getpass import getpass

# code struktur data Queue
class DataPenduduk:
    NIK: str
    nama: str
    kelamin: chr
    alamat: str
    tglLahir: list
    usia: int
    pekerjaan: str

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

    def add(self, NIK, nama, kelamin, alamat, tglLahir, usia, pekerjaan):
        if(self.isEmpty() == True):
            self.last = 0
            self.first = 0

            self.data.append([])
            self.data[self.last] = DataPenduduk()
            self.data[0].NIK = NIK
            self.data[0].nama = nama
            self.data[0].kelamin = kelamin
            self.data[0].alamat = alamat
            self.data[0].tglLahir = tglLahir
            self.data[0].usia = usia
            self.data[0].pekerjaan = pekerjaan
        else:
            self.last = self.last + 1

            self.data.append([])
            self.data[self.last] = DataPenduduk()
            self.data[self.last].NIK = NIK
            self.data[self.last].nama = nama
            self.data[self.last].kelamin = kelamin
            self.data[self.last].alamat = alamat
            self.data[self.last].tglLahir = tglLahir
            self.data[self.last].usia = usia
            self.data[self.last].pekerjaan = pekerjaan

    def getFirst(self):
        return self.data[0]

    def delete(self):
        if(self.last == 0):
            self.first = -1
            self.last = -1

        else:
            for i in range(self.first+1, self.last+1):
                self.data[i-1].NIK = self.data[i].NIK
                self.data[i-1].nama = self.data[i].nama
                self.data[i-1].kelamin = self.data[i].kelamin
                self.data[i-1].alamat = self.data[i].alamat
                self.data[i-1].usia = self.data[i].usia
                self.data[i-1].pekerjaan = self.data[i].pekerjaan

            self.last = self.last - 1

    def printQueue(self):
        if(self.first != -1):
            for i in range(self.first, self.last+1):
                print(self.data[i].NIK + "\t" + self.data[i].nama)
        else:
            print("Tidak ada data")

# code struktur data BST
class Node:
    def __init__(self, NIK, nama, kelamin, alamat, tglLahir, usia, pekerjaan):
        self.NIK = NIK
        self.nama = nama
        self.kelamin = kelamin
        self.alamat = alamat
        self.tglLahir = tglLahir
        self.usia = usia
        self.pekerjaan = pekerjaan
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, NIK, nama, kelamin, alamat, tglLahir, usia, pekerjaan):
        newNode = Node(NIK, nama, kelamin, alamat, tglLahir, usia, pekerjaan)
        if (self.root == None):
            self.root = newNode
            return
        current = self.root
        parent = None
        while(True):
            parent = current
            if (int(NIK) < int(current.NIK)):
                current = current.left
                if (current == None):
                    parent.left = newNode
                    return
            else:
                current = current.right
                if (current == None):
                    parent.right = newNode
                    return
    def isEmpty(self):
        hasil=False
        if(self.root==None):
            hasil=True
        return hasil

    def display(self, root):
        if(self.isEmpty()):
            print("Data kosong")
        elif (root != None):
            self.display(root.left)
            print(root.NIK + "\t" + root.nama)
            self.display(root.right)

    def find(self, NIK):
        current = self.root
        while (current != None):
            if (int(current.NIK) == int(NIK)):
                return True
            elif (int(current.NIK) > int(NIK)):
                current = current.left
            else:
                current = current.right
        return False

    def printNode(self, NIK):
        current = self.root
        while (current != None):
            if (int(current.NIK) == int(NIK)):
                print("NIK              :", current.NIK)
                print("Nama             :", current.nama)
                print("Kelamin          :", current.kelamin)
                print("Alamat           :", current.alamat)
                print("Tanggal Lahir    :", "/".join(current.tglLahir))
                print("Usia             :", current.usia)
                print("Pekerjaan        :", current.pekerjaan)
                print("======================================")
                break
            elif (int(current.NIK) > int(NIK)):
                current = current.left
            else:
                current = current.right

    def delete(self, NIK):
        parent = self.root
        current = self.root
        isLeftChild = False

        while (int(current.NIK) != int(NIK)):
            parent = current
            if (int(current.NIK) > int(NIK)):
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
    
# code struktur data linked list
class Akun:
    nama = None
    username = None
    password = None

class Elemen:
    def __init__(self):
        self.kontainer = Akun()
        self.next = None

    def getKontainer(self):
        return self.kontainer

    def setNext(self, nextt):
        self.next = nextt

    def getNext(self):
        return self.next

class List:
    def __init__(self):
        self.first = None
        self.data = []
        self.data.append(Elemen())

    def setFirst(self, first):
        self.first = first

    def getFirst(self):
        return self.first

    def createList(self):
        self.first = -1
        for i in range(0, len(self.data)):
            self.data[i].setNext(-2)

    def countElemen(self):
        hasil = 0
        if(self.first != -1):
            bantu = self.first

            while bantu != -1:
                hasil = hasil + 1
                bantu = self.data[bantu].getNext()
        return hasil

    def emptyElemen(self):
        hasil = -1

        if(self.countElemen() < len(self.data)):
            ketemu = False
            i = 0

            while(ketemu == False) and (i < len(self.data)):
                if(self.data[i].getNext() == -2):
                    hasil = i
                    ketemu = True
                else:
                    i = i+1
        return hasil

    def addFirst(self, nama, username, password):
        baru = self.emptyElemen()
        self.data[baru].getKontainer().username = username
        self.data[baru].getKontainer().password = password
        self.data[baru].getKontainer().nama = nama
        
        if(self.first == -1):
            self.data[baru].setNext(-1)
        else:
            self.data[baru].setNext(self.first)
        self.first = baru
        
        self.data.append(Elemen())
        self.data[-1].setNext(-2)

    def addAfter(self, prev, nama, username, password):
        if prev != -1:
            baru = self.emptyElemen()
            self.data[baru].getKontainer().username = username
            self.data[baru].getKontainer().password = password
            self.data[baru].getKontainer().nama = nama

            if(self.data[prev].getNext() == -1):
                self.data[baru].setNext(-1)
            else:
                self.data[baru].setNext(self.data[prev].getNext())

            self.data[prev].setNext(baru)
            self.data.append(Elemen())
            self.data[-1].setNext(-2)
            

    def addLast(self, nama, username, password):
        if(self.first == -1):
            self.addFirst(nama, username, password)
        else:
            last = self.first
            while self.data[last].getNext() != -1:
                last = self.data[last].getNext()
            self.addAfter(last, nama, username, password)

    def delFirst(self):
        if(self.first != -1):
            hapus = self.first

            if(self.countElemen() == 1):
                self.first = -1
            else:
                self.first = self.data[self.first].getNext()
            self.data[hapus].setNext(-2)
        else:
            print("List Kosong")

    def delAfter(self, prev):
        if(prev != -1):
            hapus = self.data[prev].getNext()
            if(hapus != -1):
                if(self.data[hapus].getNext() == -1):
                    self.data[prev].setNext(-1)
                else:
                    self.data[prev].setNext(self.data[hapus].getNext())

                self.data[hapus].setNext(-2)

    def delLast(self):
        if(self.first != -1):
            if(self.countElemen() == 1):
                self.delFirst()
            else:
                last = self.first
                before_last = -1

                while self.data[last].getNext() != -1:
                    before_last = last 
                    last = self.data[last].getNext()
                self.delAfter(before_last)
        else:
            print("List Kosong")

    def printElement(self):
        if(self.first != -1):
            bantu = self.first
            i = 1

            while bantu != -1:
                print("Elemen ke : ", i)
                print("Nim : ", self.data[bantu].getKontainer().username)
                print("Nama : ", self.data[bantu].getKontainer().password)
                print("Nama : ", self.data[bantu].getKontainer().nama)
                print("Next : ", self.data[bantu].getNext())
                print("----------------------------")
                bantu = self.data[bantu].getNext()
                i = i+1
        else:
            print("List Kosong")

    def delAll(self):
        for i in range(self.countElemen(),-1,-1):
            self.delLast()

# code untuk login atau daftar slot
class Login:
    def __init__(self):
        self.slot = []
        
        # membuat 10 slot untuk menyimpan data akun
        for i in range(0, 10):
            self.slot.append(List())
            self.slot[i].createList()
    
    def login(self, username, password):
        index = len(password) - 8
        if self.slot[index].countElemen() != 0:
            bantu = self.slot[index].getFirst()
            while bantu != -1:
                if (username == self.slot[index].data[bantu].getKontainer().username and
                    password == self.slot[index].data[bantu].getKontainer().password):
                        return True
                else:
                    bantu = self.slot[index].data[bantu].getNext()
            
        return False
        
    def cekValidasiAkun(self, username, password, retryPassword):
        try:
            valid = True
            pesanError = ""
            
            for i in range(0, 10):
                if self.slot[i].countElemen() != 0:
                    bantu = self.slot[i].getFirst()
                    while bantu != -1:
                        if username.lower() == self.slot[i].data[bantu].getKontainer().username.lower():
                            raise ValueError("Maaf username sudah terdaftar")
                        else:
                            bantu = self.slot[i].data[bantu].getNext()
            
            if len(password) < 8 or len(password) > 17:
                raise ValueError("Panjang password antara 8-17")
            
            if password != retryPassword:
                raise ValueError("Password yang anda masukan berbeda")                
        except ValueError as VE:
            valid = False
            pesanError = VE
        finally:
            return valid, pesanError  
    
    def daftar(self, nama, username, password):
        index = len(password) - 8
        if self.slot[index].countElemen() == 0:
            self.slot[index].addFirst(nama, username, password)
        else:
            prev = self.count[index].countElemen() - 1
            self.slot[index].addAfter(prev, nama, username, password)
        
    
# fungsi untuk menghitung usia dilihat dari tanggal lahir
def hitungUsia(tglLahir):
    waktu = localtime() # mengambil waktu lokal saat ini
    usia = (waktu.tm_year-1) - int(tglLahir[2])

    if waktu.tm_mon == int(tglLahir[1]):
        if waktu.tm_mday <= int(tglLahir[0]):
            usia = waktu.tm_year - int(tglLahir[2])
    elif waktu.tm_mon > int(tglLahir[1]):
        usia = waktu.tm_year - int(tglLahir[2])

    return usia

# mengecek apakah data sudah ada atau belum
def cekData(NIK, objekQueue, objekBST):
    exist = False
    # mengecek pada objek queue, apakah sudah ada atau belum
    if not objekQueue.isEmpty():
        for i in range(objekQueue.first, objekQueue.last+1):
            if NIK == objekQueue.data[i].NIK:
                exist = True
                break
        else:
            exist = False
        
    # mengecek pada objek BST, apakah sudah ada atau belum
    if not exist:
        exist = objekBST.find(NIK)
        
    return exist

# untuk mengecek kevalidasian data
def validasiData(NIK, kelamin, tglLahir):
    try:
        hasil = True
        pesanError = ""
        
        # mengecek validasi NIK
        if NIK.isalpha():
            raise ValueError("NIK yang anda masukan tidak valid")
        elif len(NIK) < 10 or len(NIK) > 10:
            raise ValueError("NIK harus terdiri dari 10 angka")
        
        # mengecek validasi jenis kelamin
        if kelamin.lower() != "l" and kelamin.lower() != "p":
            raise ValueError("Jenis kelamin yang anda masukan tidak valid")
        
        # mengecek validasi tanggal lahir
        if len(tglLahir) != 3:
            raise ValueError("Format tanggal yang anda masukan salah")
        elif len(tglLahir) == 3:
            if tglLahir[0].isalpha() or tglLahir[1].isalpha() or tglLahir[2].isalpha():
                raise ValueError("Format tanggal yang anda masukan salah")
            elif int(tglLahir[0]) < 1 or int(tglLahir[0]) > 31:
                raise ValueError("Tanggal lahir yang anda masukan tidak valid")
            elif int(tglLahir[1]) < 1 or int(tglLahir[1]) > 12:
                raise ValueError("Bulan lahir yang anda masukan tidak valid")
            elif int(tglLahir[2]) < 1800 or int(tglLahir[2]) > localtime().tm_year:
                raise ValueError("Tahun lahir yang anda masukan di luar jangkauan")

    # masuk jika ada error
    except ValueError as VE:
        hasil = False
        pesanError = VE
    finally:
        return hasil, pesanError

# Main code program
if __name__ == "__main__":

    # fungsi untuk clear screen
    clear = lambda: system("cls")

    # inisialisasi objek
    queue = Queue()
    BST = BinarySearchTree()
    login = Login()

    # membuat queue kosong
    queue.createEmpty()
    
    # login terlebihi dahulu sebelum masuk kedalam menu utama
    while True:
        clear()
        print(" Selamat datang di Pendataan Penduduk")
        print("======================================")
        print("[1] Masuk")
        print("[2] Daftar")
        print("======================================")
        menu = input("Pilih menu > ")

        if menu == "1":
            clear()
            username = input("Username = ")
            password = getpass("Password = ")
            masuk = login.login(username, password)
            
            if masuk:
                break
            else:
                clear()
                print("\aUsername atau password yang anda masukan salah")
                input("Tekan ENTER untuk kembali")
        elif menu == "2":
            masuk = True
            while masuk:
                clear()
                print("======================================")
                print("             DAFTAR AKUN")
                print("======================================")
                nama        = input("Nama           = ")
                username    = input("Username       = ")
                password    = getpass("Password       = ")
                retPass     = getpass("Ulang Password = ")
                print("======================================")
                
                valid, pesanError = login.cekValidasiAkun(username, password, retPass)
                if valid:
                    while True:
                        tanya = input("Apakah anda sudah yakin [y/t] > ")
                        if tanya.lower() == "y":
                            clear()
                            login.daftar(nama, username, password)
                            print("Selamat akun anda telah terdaftar")
                            input("Tekan ENTER untuk kembali")
                            masuk = False
                            break
                        elif tanya == "t":
                            while True:
                                tanya = input("Apakah anda ingin mengisi ulang [y/t] > ")
                                # mengisi data ulang
                                if tanya.lower() == "y":
                                    break
                                elif tanya.lower() == "t":
                                    masuk = False
                                    break
                            break
                else:
                    print("\n--------------------------------------")
                    print("\aPERINGATAN")
                    print(pesanError)
                    print("--------------------------------------\n")
                    
                    while True:
                        tanya = input("Daftar ulang [y/t] > ")
                        
                        if tanya.lower() == "y":
                            break
                        elif tanya.lower() == "t":
                            masuk = False
                            break
                
        else:
            clear()
            print("\aMaaf pilihan yang ada masukan tidak tersedia")
            input("Tekan ENTER untuk kembali ke Menu")

    while masuk:

        # Menu utama
        clear()
        print("===========================")
        print("            MENU")
        print("===========================")
        print("[1] Masukan Data Baru")
        print("[2] Lihat Data")
        print("[3] Cari Data")
        print("[4] Hapus Data")
        print("[5] Data Dalam Proses")
        print("[6] Keluar")
        print("---------------------------")
        menu = input("Pilih menu > ")

        if menu == "1":
            # kode memasukan data baru
            masuk = True
            while masuk:
                clear()
                print("======================================")
                print("             BUAT DATA")
                print("======================================")
                NIK         = input("NIK                 : ")
                nama        = input("Nama                : ")
                kelamin     = input("Jenis Kelamin [L/P] : ")
                alamat      = input("Alamat              : ")
                print("- Format DD/MM/YYYY")
                tglLahir    = input("Tanggal Lahir       : ").split("/")
                pekerjaan   = input("Pekerjaan           : ")
                print("======================================\n")

                # mengecek kevalidasian data
                valid, pesanError = validasiData(NIK, kelamin, tglLahir)
                
                # jika data sudah valid data dapat diproses
                if valid:
                    # pengecekean data apakah sudah ada atau belum (berdasarkan NIK)
                    exist = cekData(NIK, queue, BST)
                    if exist:
                        # Data tidak berhasil ditambahkan karena NIK sudah ada
                        print("--------------------------------------")
                        print("\aPERHATIAN!!!")
                        print("Data yang anda masukan sudah ada")
                        print("--------------------------------------\n")

                        while True:
                            tanya = input("Apakah anda ingin mengisi ulang [y/t] > ")
                            # mengisi data ulang
                            if tanya.lower() == "y":
                                break
                            elif tanya.lower() == "t":
                                masuk = False
                                break
                    else:
                        while True:
                            tanya = input("Apakah anda sudah yakin [y/t] > ")
                            # data akan disimpan lalu akan diproses
                            if tanya.lower() == "y":
                                # menghitung usia berdasarkan tanggal lahir
                                usia = hitungUsia(tglLahir)
                                
                                # memasukan data yang telah diinput ke dalam queue
                                queue.add(NIK, nama, kelamin.upper(), alamat,
                                        tglLahir, usia, pekerjaan)
                                
                                clear()
                                print("Data anda sedang diproses, mohon tunggu...")
                                input("Tekan ENTER untuk kembali ke Menu")
                                
                                masuk = False
                                break
                            elif tanya.lower() == "t":
                                while True:
                                    tanya = input("Apakah anda ingin mengisi ulang [y/t] > ")
                                    # mengisi data ulang
                                    if tanya.lower() == "y":
                                        break
                                    elif tanya.lower() == "t":
                                        masuk = False
                                        break
                                break
                else:
                    print("--------------------------------------")
                    print("\aPERHATIAN!!!")
                    print(pesanError)
                    print("--------------------------------------\n")
                    
                    while True:
                        tanya = input("Apakah anda ingin mengisi ulang [y/t] > ")
                        # mengisi data ulang
                        if tanya.lower() == "y":
                            break
                        elif tanya.lower() == "t":
                            masuk = False
                            break

        elif menu == "2":
            # kode untuk melihat data yang sudah selesai diproses
            while True:
                clear()
                print("======================================")
                print("             DATA PENDUDUK")
                print("======================================")
                print("NIK\t\tNama")
                print("--------------------------------------")
                BST.display(BST.root)
                
                # jika pada BST tidak kosong maka akan menampilkan menu tambahan
                if not BST.isEmpty():
                    print("\n\n[1] Lihat Detail Data")
                    print("[2] Kembali ke menu")
                    print("======================================")
                    tanya = input("Pilih menu > ")
                    
                    if tanya == "1":
                        NIK = input("\nMasukkan NIK untuk lihat detail data = ")
                        exist = BST.find(NIK)
                        
                        if exist:
                            clear()                        
                            print("======================================")
                            print("             DATA PENDUDUK")
                            print("======================================")
                            BST.printNode(NIK)                        
                        else:
                            clear()
                            print("\aData yang anda cari tidak ditemukan.")
                            
                        input("\nTekan ENTER untuk kembali")
                        
                    elif tanya == "2":
                        break
                    else:
                        clear()
                        print("\aMaaf pilihan yang ada masukan tidak tersedia")
                        input("Tekan ENTER untuk kembali")
                
                # Jika data pada BST kosong maka hanya akan menampilkan sebagai berikut
                else:
                    input("\nTekan ENTER untuk kembali ke Menu")
                    break

        elif menu == "3":
            # kode mencari data yang sudah selesai diproses
            masuk = True
            while masuk:
                clear()
                NIK = input("Masukkan NIK untuk dicari = ")
                
                # cek datanya ada apa tidak
                exist = BST.find(NIK)
                
                clear()
                # Jika data ditemukan maka akan menampilkan data sesuai NIK yang dicari
                if exist == True:
                    print("====================================")
                    print("             DATA PENDUDUK")
                    print("====================================")
                    BST.printNode(NIK)
                elif exist == False:
                    print("\aData yang anda cari tidak ditemukan")
                
                print(end= "\n")
                while True:
                    tanya = input("Apakah anda ingin mencari ulang [y/t] > ")
                    if tanya.lower() == "y":
                        break
                    elif tanya.lower() == "t":
                        masuk = False
                        break

        elif menu == "4":
            # kode menghapus data yang sudah diproses
            masuk = True
            while masuk:
                clear()
                NIK = input("Masukkan NIK dari data yang ingin dihapus = ")

                # mengecek apakah data ada
                exist = BST.find(NIK)
                
                clear()
                # Jika data ditemukan maka akan menampilkan datanya terlebih dahulu sebelum dihapus
                if exist == True:
                    clear()                    
                    print("======================================")
                    print("             HAPUS DATA")
                    print("======================================")
                    BST.printNode(NIK)
                    
                    print(end= "\n")
                    while True:
                        tanya = input("Apakah anda yakin ingin menghapus data ini [y/t] > ")
                        
                        if tanya.lower() == "y":
                            clear()
                            # menghapus data pada BST
                            BST.delete(NIK)
                            print("Data berhasil dihapus!!!")
                            input("Tekan ENTER untuk kembali ke Menu")
                            
                            masuk = False
                            break
                        elif tanya.lower() == 't':
                            clear()
                            # Data tidak jadi dihapus
                            print("Data tidak jadi dihapus")
                            while True:
                                tanya = input("Apakah anda ingin menghapus data lagi [y/t] > ")
                                if tanya.lower() == 'y':
                                    break
                                elif tanya.lower() == 't':
                                    masuk = False
                                    break
                            break
                                
                elif exist == False:
                    print("\aData dengan NIK tersebut tidak ditemukan\n")
                    
                    while True:
                        tanya = input("Apakah anda ingin mencari ulang [y/t] > ")
                        if tanya.lower() == 'y':
                            break
                        elif tanya.lower() == 't':
                            masuk = False
                            break

        elif menu == "5":
            # kode untuk melihat data yang masih dalam proses
            clear()
            print("======================================")
            print("             DALAM PROSES")
            print("======================================")
            print("NIK\t\tNama")
            print("--------------------------------------")

            # mencetak isi dalam antrian proses
            queue.printQueue()

            if not queue.isEmpty():    
                # mengambil data yang ada pada antrian pertama
                dataPertama = queue.getFirst()
                
                print(end= "\n")
                while True:
                    tanya = input("Apakah data dengan NIK " + dataPertama.NIK + " sudah selesai dikerjakan [y/t] > ")

                    # memasukan data pertama pada antrian kedalam data yang sudah selesai dikerjakan
                    if tanya.lower() == "y":
                        clear()
                        BST.insert(dataPertama.NIK, dataPertama.nama, dataPertama.kelamin,
                                dataPertama.alamat, dataPertama.tglLahir, dataPertama.usia, dataPertama.pekerjaan)
                        print("Data dengan NIK ", dataPertama.NIK, "telah selesai dikerjakan")
                        input("Tekan ENTER untuk kembali ke Menu")
                        queue.delete()
                        break
                    elif tanya.lower() == "t":
                        input("\nTekan ENTER untuk kembali ke Menu")
                        break
            else:
                input("\nTekan ENTER untuk kembali ke Menu")

        elif menu == "6":
            # kode untuk keluar dari program
            clear()
            exit("Terima kasih...")
        else:
            # kode jika user memilih diluar jangkauan pilihan menu
            clear()
            print("\aMaaf pilihan yang ada masukan tidak tersedia")
            input("Tekan ENTER untuk kembali ke Menu")
