liste = []
with open("öğrenciler.txt","r+",encoding="utf-8") as file :
    while True :
        x = input("ekle1, sil2, gör3, çık4: ")
        if x == "1" :
            ad = input("öğr adı: ")
            soyad = input("öğr. soyadı: ")
            no = input("öğr no: ")
            ogrenci = ad +"\t"+ soyad +"\t"+ no +"\n"
            liste.append(ogrenci)
        elif  x == "2" :
            ad = input("öğr adı: ")
            soyad = input("öğr. soyadı: ")
            no = input("öğr no: ")
            ogrenci = ad + "\t" + soyad + "\t" + no + "\n"

            if liste.count(ogrenci) == 0 :
                print("böyle bir öğrenci kayıtlı değil")
            for i in liste :
                if i == ogrenci :
                    liste.remove(ogrenci)

        elif x == "3" :
            print(liste)
        elif x == "4" :
            break
        else :
            print("geçerli rakam gir")
    file.writelines(liste)


#görüntülemede \t ve \n lerin de çıkması sourunu var
#döngüden çıkmadıkça (4e basmadıkça) liste dosyaya yazılmıyor ama 3e basınca dosyaya yazılmamış olsa da görüntüleyebiliyorsun