list_npm = []
list_nama = []
list_studi = []
list_ipk = []
class dataMahasiswa :
    def __init__(self,npm,nama,studi,ipk):
        self.npm = npm
        list_npm.append(self.npm)
        self.nama = nama
        list_nama.append(self.nama)
        self.studi = studi
        list_studi.append(self.studi)
        self.ipk = ipk
        list_ipk.append(self.ipk)

    def tampil_data (self):
        n = 0
        print("\nJumlah Mahasiswa Yang Sudah Terinput : ",x)
        for i in range(x):
            n+=1
            if list_ipk[i] >= 3.50 :
                print("\n----------- Mahasiswa ke -",n,"-----------")
                print("NPM Mahasiswa : ",list_npm[i])
                print("Nama Mahasiswa : ",list_nama[i])
                print("Program Studi Mahasiswa : ",list_studi[i])
                print("IPK Mahasiswa : ",list_ipk[i])
                print("--------------------------------------------")
            else:
                i+=1
        print("Catatan : Apabila Mahasiswa Yang Tidak Tampil Dikarenakan IPK")

stop = False
x = 0
while(not stop):
    inputNpm = input("Masukkan NPM : ")
    inputNama = input("Masukkan Nama : ")
    inputStudi = input("Masukkan Program Studi : ")
    inputIPK = float(input("Masukkan IPK : "))
    mahasiswa = dataMahasiswa(inputNpm,inputNama,inputStudi,inputIPK)
    x+=1
    ulang = input("Apakah ingin input ulang (y/t) ? : ")
    if ulang == "t":
        stop = True

mahasiswa.tampil_data()