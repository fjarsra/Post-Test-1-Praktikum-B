# Post-Test-1-Praktikum-B
# NIM : 2309116060
# Nama : Fajar Syafatoni Raihanadif
while True: 
    try:
        Nim = int(input("Masukkan Nim : "))
        Nama = str(input("Masukan Nama : "))
        Password = int(input("Silahkan Masukkan Password : "))

        if Nama == "Fajar" and Nim == 2309116060 and Password == 11111:
            print("Anda telah berhasil login")

            print(35*"-") #untuk menampilkan garis, 20* berarti ouput garis yang muncul adalah 20
            print("Selamat datang di Konversi Kilogram") #menampilkan kata kata yang ditulis di dalam kurung
            print(35*"-")
            
            angka1 = float(input("Masukan Berat dalam KG : "))
            
            print("\nPilih operasi:")       
            print("1. Kilogram --> Pounds")
            print("2. Kilogram --> Ounces")
            print("3. Kilogram --> Gram")
            print("4. Keluar")

            pilihan = input("Masukkan nomor operasi (1/2/3/4) : ") 
            if pilihan == '4':
                break

        
            if pilihan == '1':
                angka1 *= float(2.204623) 
                print("Hasil perkalian : ", angka1, "Lbs") 
            if pilihan == '2':
                angka1 *= float(35.274) 
                print("Hasil perkalian : ", angka1, "Ounces") 
            if pilihan == '3':
                angka1 *= float(1000) 
                print("Hasil perkalian : ", angka1, "Gram") 

    except ValueError: 
        print("Masukkan harus berupa angka.")

    else :
        print("Passworrd Salah")

print("Terima kasih.") 

![DD3A93C1-7887-4C8B-8C6B-5ECC61D43481](https://github.com/fjarsra/Post-Test-1-Praktikum-B/assets/144713730/a26214cf-e775-4c9a-8195-d8edcb196e24)
![Untitled Diagram drawio (1)](https://github.com/fjarsra/Post-Test-1-Praktikum-B/assets/144713730/bb2e467a-0d09-4008-8279-878b7e153f5e)
jadi Output yang dikleuarkan itu berdasarkan apa operasi yang kita pilih, contohnya jika kita memilih pounds maka berat 
kilogram yang sudah kita input akan dikonversi ke pounds dengan cara mengalikan input kg dengan 2.204623 setelah operasi dilakukan makan hasil akan langsung muncul di terminal

![konversi kilogram](https://github.com/fjarsra/Post-Test-1-Praktikum-B/assets/144713730/5d5c63a6-ff82-4497-a3b9-ec0335ebe72e)

Ini adalah contoh output yang akan keluar
![Screenshot 2023-09-25 231111](https://github.com/fjarsra/Post-Test-1-Praktikum-B/assets/144713730/031b50d0-620a-4f53-828e-4ba2cf909e59)


Ini adalah Output yang akan keluar jika NIM, Nama, dan Password tidak sesuai
![Screenshot 2023-09-25 231313](https://github.com/fjarsra/Post-Test-1-Praktikum-B/assets/144713730/f93b1f03-48d1-4580-9d2c-42c895c76429)




Tampak Kode jika dimasukkan kedalam VSCode
![Screenshot (74)](https://github.com/fjarsra/Post-Test-1-Praktikum-B/assets/144713730/847062ca-9b4a-41c1-ab03-fb85788d2043)







