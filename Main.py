'''
Nama Kelompok:
- Marshall Anugrah Najmi    1910511034
- Brahma Aditama            1910511036
- Jovanka Samudra           1910511040
- Daffy Fayyadhya Ramzy     1910511044
- Muhammad Raffiza Azka     1910511062
'''

# code struktur data queue
class DataPndk:
    nik: str
    nama: str 
    jenisKelamin: chr
    alamat: str
    tglLahir : list
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
    
    def add(self, nik, nama, jenisKelamin, alamat, tglLahir, usia, pekerjaan):
        if(self.isEmpty()==True):
            self.last = 0
            self.first = 0
            
            self.data.append([])
            self.data[self.last] = DataPndk()
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
            self.data[self.last] = DataPndk()
            self.data[self.last].nik = nik
            self.data[self.last].nama = nama
            self.data[self.last].jenisKelamin = jenisKelamin
            self.data[self.last].alamat = alamat
            self.data[self.last].tglLahir = tglLahir
            self.data[self.last].usia = usia
            self.data[self.last].pekerjaan = pekerjaan
            
    def delete(self):
        if(self.last==0):
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
        if(self.first!=1):
            print("=======Isi Queue=======")
            for i in range(self.last,(self.first-1),-1):
                print("="*10)
                print("Data ke ",i)
                print("NIK           : ", self.data[i].nik)
                print("Nama          : ", self.data[i].nama)
                print("Jenis Kelamin : ", self.data[i].jenisKelamin)
                print("Alamat        : ", self.data[i].alamat)
                print("Tanggal Lahir : ", self.data[i].tglLahir)
                print("Usia          : ", self.data[i].usia)
                print("Pekerjaan     : ", self.data[i].pekerjaan)
                
                print("="*10)
        else:
            print("Queue Kosong")

# code struktur data BST


