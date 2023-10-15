while True: 
    try:
        Nim = int(input("Masukkan Nim : "))
        Nama = str(input("Masukan Nama : "))
        Password = int(input("Silahkan Masukkan Password : "))

        if Nama == "Fajar" and Nim == 2309116060 and Password == 11111:
            print("Anda telah berhasil login")

            print(35*"-") 
            print("Selamat datang di Konversi Kilogram")
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