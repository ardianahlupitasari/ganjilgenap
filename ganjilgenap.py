print("1.tampilkan semua data")
print("2.tampilkan data yang bernilai genap")
print("3.tampilkan data yang bernilai ganjil")
print("4.jumla dan rata-rata bil ganjil")
print("5.jumlah dan rata - rata bil genap")
print("6.keluar")
a=int(input('masukkan panjang list='))
a=a+1
temp=0
alpro=[]
count=0
total=0
for i in range (a-1):
    x=int(input('masukkan elemen='))
    alpro.append(x)
print (alpro)
b=int(input('masukkan pilihan:'))
while b!=6:
    if b==1:
        print('TAMPILKAN SEMUA DATA')
        for i in alpro :
            print (i)
    elif b==2:
        print ('TAMPILKAN DATA YANG BERNILAI GENAP')
        for i in alpro:
            if i%2==0:
                print (i)
    elif b==3:
        print('TAMPILKAN DATA YANG BERNILAI GANJIL')
        for i in alpro:
            if i%2!=0:
                print (i)
    elif b==4:
        print('JUMLAH DAN RATA RATA BILANGAN GANJIL')
        
        for i in alpro:
            if i%2!=0:
                count=count+1
                temp=temp+i
                i=i+1
        print('jumlah bilangan ganjil=',temp)
        print('nilai rata-rata =',temp/count)

    elif b==5:
        print('JUMLAH DAN RATA RATA BILANGAN GENAP')
        for i in alpro:
            if i%2==0:
                temp=i
                count=1
                i=i+1
        print('jumlah bilangan genap=',temp)
        print('nilai rata-rata =',temp/count)
    else:
        print ('selesai')
    b=int(input('masukkan pilihan='))




