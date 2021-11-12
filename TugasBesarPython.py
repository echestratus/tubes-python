def dataCleansing(filename): #fungsi untuk melakukan data cleansing/data preprocessing
    #Bagian buka file dan deklarasi variable
    f = open(filename,'r',encoding='utf-8-sig') # " encoding='utf-8-sig' " berfungsi untuk menghilangkan characters "ï»¿"
    lst = [] #Variable untuk menyimpan data dari file yang belum diperbaiki
    newLst = [] #Variable untuk menyimpan data dari variable list lst yang telah diperbaiki
    save = [] #Variable untuk mengumpulkan data yang akan dihapus pada tahap memperbaiki data yang double
    x = 0 #x sebagai counter dalam perulangan jika diperlukan
    c = f.read(4) #Variable untuk assign beberapa character dari file agar bisa memilah apakah delimiter dalam file itu coma atau semicolon
    f.seek(0) #Mengembalikan pointer file ke semula
    print("\nBefore fixed\n")
    if c[3] == ',': #Jika delimiter dalam file csv nya berbentuk coma maka nanti isi dari fungsi split adalah coma
        for i in f:
            a = i.split(',') #Proses assign data dari file yang sudah di split berdasarkan delimiternya ke variable a
            print(a)
            lst.append(a) #Proses menambahkan data dari variable a ke variable list lst
    elif c[3] == ';': #Jika delimiter dalam file csv berbentuk semicolon maka isi dari fungsi split adalah semicolon
        for i in f: #Untuk proses yang ini sama dengan yang atas
            a = i.split(';')
            print(a)
            lst.append(a)
    else:
        pass
    for i in lst: #Proses ini bertujuan untuk menghilangkan '\n' di akhir data
        newLst.append([])
        for j in i:
            newLst[x].append(j.strip()) #berikut fungsi untuk menghilangkan '\n' di akhir data adalah strip()
        x+=1
    newLst.pop(0)
    print('\nAfter Fixed\n')
    #Bagian untuk fix kolom nim dan nilai yang tertukar
    x = 0
    lstForDelete = []
    for i in newLst: #Untuk menukar nim yang letaknya tidak sesuai dengan fieldnya pada proses ini di check apakah digit kolom nim kurang dari 10 dan digit di kolom-kolom berikutnya lebih dari 5 digit
        if (len(newLst[x][0]) < 10) and (len(newLst[x][1]) > 5): #Pada proses ini ditetapkan untuk yang digitnya kurang dari 6 digit maka tidak bisa diasumsikan sebagai NIM
            temp = newLst[x][0]
            newLst[x][0] = newLst[x][1]
            newLst[x][1] = temp
        elif (len(newLst[x][0]) < 10) and (len(newLst[x][2]) > 5):
            temp = newLst[x][0]
            newLst[x][0] = newLst[x][2]
            newLst[x][2] = temp
        elif (len(newLst[x][0]) < 10) and (len(newLst[x][3]) > 5):
            temp = newLst[x][0]
            newLst[x][0] = newLst[x][3]
            newLst[x][3] = temp
        elif (len(newLst[x][0]) < 10) and (len(newLst[x][5]) > 5):
            temp = newLst[x][0]
            newLst[x][0] = newLst[x][5]
            newLst[x][5] = temp
        elif (len(newLst[x][0]) < 10) and (len(newLst[x][6]) > 5):
            temp = newLst[x][0]
            newLst[x][0] = newLst[x][6]
            newLst[x][6] = temp
        elif (len(newLst[x][0]) < 6):
            lstForDelete.append(newLst[x]) #Pada proses di line ini jika ternyata seluruh kondisi telah dicheck dan di kolom NIM ternyata masih kurang dari 6 digit
        x += 1 #maka data dari baris tersebut akan disimpan di variable list lstForDelete lalu akan diremove data didalamnya pada variable newLst
    for i in lstForDelete:
        newLst.remove(i) #disini bagian remove data yang ada di dalam lstForDelete pada newLst
    lstForDelete.clear()

    #Bagian untuk ubah huruf di nim menjadi angka terdekat
    lstForConvert = []
    for i in range(len(newLst)):
        for j in range(len(newLst[i])):
            indicator = 0
            string = newLst[i][j]
            for k in string:
                lstForConvert.append(k)
            for l in range(len(lstForConvert)):
                if lstForConvert[l] == 'B':
                    lstForConvert[l] = '8'
                    indicator = 1
                elif lstForConvert[l] == 'T':
                    lstForConvert[l] = '7'
                    indicator = 1
                elif lstForConvert[l] == 'S':
                    lstForConvert[l] = '5'
                    indicator = 1
                elif lstForConvert[l] == 'E':
                    lstForConvert[l] = '3'
                    indicator = 1
                elif lstForConvert[l] == 'I':
                    lstForConvert[l] = '1'
                    indicator = 1
                elif lstForConvert[l] == 'A':
                    lstForConvert[l] = '4'
                    indicator = 1
                elif lstForConvert[l] == 'b':
                    lstForConvert[l] = '6'
                    indicator = 1
                elif lstForConvert[l] == 'g':
                    lstForConvert[l] = '9'
                    indicator = 1
                elif lstForConvert[l] == 'O':
                    lstForConvert[l] = '0'
                    indicator = 1
                else:
                    continue

            if indicator == 1:
                string = ''.join(lstForConvert)
                newLst[i][j] = string
            lstForConvert.clear()
    #Bagian untuk fix jika ada yang kelebihan field
    x = 0
    for i in newLst:
        if len(i)>7:
            for j in range(len(i)-1,6,-1):
                temp = newLst[x][j]
                newLst[x].remove(newLst[x][j])
                if temp == '':
                    continue
                elif int(temp) % 2 == 0:
                    newLst[x][5] = temp
                else:
                    newLst[x][6] = temp
        x += 1

    #Bagian untuk menambahkan nilai yang kosong
    x = 0
    for i in newLst:
        for j in range(len(i)):
            if newLst[x][j] == '':
                newLst[x][j] = '50'
        x += 1
    #Bagian untuk pengecekan anomali nilai
    for i in range(len(newLst)):
        for j in range(1,7):
            try:
                if float(newLst[i][j]) > 100:
                    newLst[i][j] = '80'
                elif float(newLst[i][j]) < 0:
                    newLst[i][j] = '20'
            except:
                continue
    #Bagian untuk pengecekan panjang NIM
    dltLst = []
    for i in range(len(newLst)):
        if len(newLst[i][0]) > 10:
            dlt = newLst[i][0]
            for j in dlt:
                dltLst.append(j)
            for k in range(len(newLst[i][0])-1,9,-1):
                dltLst.pop(k)
            dlt = ''.join(dltLst)
            newLst[i][0] = dlt
            dltLst.clear()
        elif len(newLst[i][0]) < 10:
            dlt = newLst[i][0]
            for j in dlt:
                dltLst.append(j)
            for k in range(len(newLst[i][0]),10):
                dltLst.append('0')
            dlt = ''.join(dltLst)
            newLst[i][0] = dlt
            dltLst.clear()
    #Bagian untuk fix data yang double
    for i in range(0,len(newLst)):
        for j in range(i,len(newLst)):
            if i == j:
                continue
            elif newLst[i][0] == newLst[i-1][0]:
                continue
            elif newLst[i][0] == newLst[j][0]:
                save.append(newLst[j])
    for i in save:
        newLst.remove(i)
    #Menghapus data yang sangat tidak sesuai
    x = 0
    delete = []
    for i in newLst:
        try:
            int(newLst[x][0])
            float(newLst[x][1])
            float(newLst[x][2])
            float(newLst[x][3])
            float(newLst[x][4])
            float(newLst[x][5])
            float(newLst[x][6])
        except:
            delete.append(newLst[x])
        x += 1
    for i in range(len(delete)):
        newLst.remove(delete[i])

    #Bagian untuk check isi listnya
    newLst.insert(0, ['NIM', 'TUGAS1', 'TUGAS2', 'QUIZ1', 'QUIZ2', 'UTS', 'UAS'])
    for i in newLst:
        print(i)
    f.close()
    #Bagian ini untuk save data file csv ke file csv baru
    f1 = open('coba.csv','w')
    x = 0
    for i in newLst:
        f1.write(i[0]+','+i[1]+','+i[2]+','+i[3]+','+i[4]+','+i[5]+','+i[6]+"\n")
        x += 1
    f1.close()
    dataProcessing('coba.csv')
def dataProcessing(fixedfilename): #Fungsi untuk menghitung mean, median dan standard deviation
    print('\nData Processing\n')
    f = open(fixedfilename,'r')
    #Bagian untuk append data file ke list
    lst = []
    newLst = []
    for i in f:
        a = i.split(',')
        lst.append(a)
    for i in range(len(lst)):
        newLst.append([])
        for j in range(len(lst[i])):
            newLst[i].append(lst[i][j].strip())
    newLst.remove(newLst[0])
    for i in newLst:
        print(i)
    #Bagian untuk append data nilai ke variable list khusus nilai
    process = []
    for i in range(len(newLst)):
        for j in range(1,len(newLst[i])):
            process.append(float(newLst[i][j]))
    print(process)
    #Bagian menghiitung mean
    sumMean = sum(process)
    mean = sumMean/len(process)
    print("Mean : ",mean)
    #Bagian menghitung median
    process.sort()
    print(process)
    mid = (len(process)-1)/2
    if (int(mid)+1) % 2 == 0:
        median = (process[int(mid)] + process[int(mid+1)])/2
        print("Median : ",median)
    else:
        median = process[int(mid)]
        print('Median : ',median)

dataCleansing('dataset11.csv')
