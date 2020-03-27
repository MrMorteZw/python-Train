stop = 1
print("Choose your language..")
print("زبان مورد نظر خود را انتخاب کنيد...")
print("1-Farsi")
print("2-English")
lang = input("")
if lang =="2":
    while  stop==1:
        a = input("""
        '<'Please select an option'>'
        1-Add contacts

        2-contacts Search

        3-View contacts

        4-Delete contacts

        5-Finish


        """)

        if a == "1":
            b = input("Enter the contact name: ")
            c = input("Enter the contact number: ")
            f = open("Contacts-List.txt","a") 
            f.write("|_"+"Name: "+b+" | "+"Number: "+c+"_|"+"\n")
            f.close()

        elif a=="2":
            shsh=input("Send the contact's name to find: ")
            print("|Your result: ")
            f = open("Contacts-List.txt", "r")
            for line in f:
                 if shsh in line: print (line)
            f.close()
    
        elif a=="3":
            print("<<Full contact list>>: ")
            f = open('Contacts-List.txt', 'r')
            for i, line in enumerate(f, start=0):
                print('{} = {}'.format(i, line.strip()))

        elif a=="4":
            print("Send the contact's row for deletion")
            print("Refer to the 2-contacts Search to see the number rows")
            f = open("Contacts-List.txt", "r")
            mokhatab = f.readlines()
            f.close()
            radif = int(input(": "))
            mokhatab.pop(radif) 
            f = open("Contacts-List.txt", "w")
            mokhatab = "".join(mokhatab)
            f.write(mokhatab)
            f.close()

        elif a=="5":
           stop=2
           print("App closed!")
if lang == "1":
        while  stop==1:
            a = input("""
            '<'Please select an option'>'
            1-افزودن مخاطبین

            2-جستجوی  مخاطب

            3-نمایش مخاطبین

            4-حذف مخاطبین

            5-پایان


            """)

            if a == "1":
                b = input("نام مخاطب را وارد کنید: ")
                c = input("شماره تماس را وارد کنید: ")
                f = open("Contacts-List.txt","a")
                f.write("|_"+"Name: "+b+" | "+"Number: "+c+"_|"+"\n")
                f.close()

            elif a=="2":
                shsh=input("برای پیدا کردن نام مخاطب را ارسال کنید: ")
                print("|نتیجه شما: ")
                f = open("Contacts-List.txt", "r")
                for line in f:
                     if shsh in line: print (line)
                f.close()
    
            elif a=="3":
                print("<<ليست کامل مخاطب ها>>: ")
                f = open('Contacts-List.txt', 'r')
                for i, line in enumerate(f, start=0):
                    print('{} = {}'.format(i, line.strip()))

            elif a=="4":
                print("رديف مخاطب را جهت حذف آن ارسالکنيد")
                print("براي ديدن شماره رديف مخاطب ها به نمایش مخاطب ها مراجعه کنيد!")
                f = open("Contacts-List.txt", "r")
                mokhatab = f.readlines()
                f.close()
                radif = int(input(": "))
                mokhatab.pop(radif) 
                f = open("Contacts-List.txt", "w")
                mokhatab = "".join(mokhatab)
                f.write(mokhatab)
                f.close()

            elif a=="5":
               stop=2
               print("برنامه بسته شده است!")
