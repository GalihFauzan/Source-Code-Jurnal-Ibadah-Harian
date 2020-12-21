#Program catatan amal ibadah harian
ibadah='x'
while ibadah=='x':
    print("\t\t\tJURNAL IBADAH HARIAN ")
    print("\t\t    Tahun Hijriyah: 1441 - 1442 H")
    print("\t\t             2020 Masehi")
    print("======================================================================")
    print("")
    nama=input("Masukkan Nama \t: ") 
    print("1. Shalat")
    print("2. Mengaji")
    print("3. Belum Berbuat baik")
    ibadah=input("Masukkan Pilihan :")
    
    if (ibadah=='1'):
       print("1. Shalat Subuh")
       print("2. Shalat Dhuhur")
       print("3. Shalat Ashar")
       print("4. Shalat Maghrib")
       print("5. Shalat Isya")
       print("6. Shalat Sunnah Tahajjud")
       print("7. Shalat Sunnah Dhuha")
       print("8. Shalat Sunnah Rawatib")
       shalat=input("Sudah Shalatkah Anda Hari ini ? [y/t] : ")
       if shalat=='y':
            print("---------------------------------------------")
            print("Anda Telah Menunaikan Kewajiban Anda Hari Ini")
            print("---------------------------------------------")
            print("")
            input("Sudah Sholat apa saja hari ini?: ")
            print("")
            print("--------------------------------------------------------")
            print(">>>>>>>Selamat Anda Telah Mengisi Jurnal Kebaikan<<<<<<<")
            print("--------------------------------------------------------")
       else:
        print("")
        print(" مَنْ حَافَظَ عَلَيْهَا كَانَتْ لَهُ نُورًا، وَبُرْهَانًا، وَنَجَاةً يَوْمَ الْقِيَامَةِ، وَمَنْ لَمْ يُحَافِظْ عَلَيْهَا لَمْ يَكُنْ لَهُ نُورٌ، وَلَا بُرْهَانٌ، وَلَا نَجَاةٌ ، وَكَانَ يَوْمَ الْقِيَامَةِ مَعَ قَارُونَ، وَفِرْعَوْنَ، وَهَامَانَ، وَأُبَيِّ بْنِ خَلَفٍ  Artinya: Siapa saja yang menjaga sholat maka dia akan mendapatkan cahaya, petunjuk dan keselamatan pada hari kiamat. Sedangkan, siapa saja yang tidak menjaga sholat, dia tidak akan mendapatkan cahaya, petunjuk dan keselamatan. Dan pada hari kiamat nanti, dia akan dikumpulkan bersama dengan Qarun, Firaun, Haman, dan Ubay bin Khalaf.")
     
    elif (ibadah=='2'):
       print("1. Tadarus Mingguan")
       print("2. Mengaji Yasinan")
       print("3. Khataman Quran")
       mengaji=input("Sudah Mengajikah Anda Hari Ini ? [y/t] : ")
       if mengaji=='y':
        print("---------------------------------------------")
        print("Anda Telah Menunaikan Kewajiban Anda Hari Ini")
        print("---------------------------------------------")
        print("")
        input("Sudah Mengaji apa saja hari ini?: ")
        print("")
        print("--------------------------------------------------------")
        print(">>>>>>>Selamat Anda Telah Mengisi Jurnal Kebaikan<<<<<<<")
        print("--------------------------------------------------------")
       
       else:
            print("")
            print("عن عَبْدَ اللَّهِ بْنَ مَسْعُودٍ، يَقُولُ: قَالَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ: مَنْ قَرَأَ حَرْفًا مِنْ كِتَابِ اللَّهِ فَلَهُ بِهِ حَسَنَةٌ، وَالحَسَنَةُ بِعَشْرِ أَمْثَالِهَا، لَا أَقُولُ الم حَرْفٌ، وَلَكِنْ أَلِفٌ حَرْفٌ وَلَامٌ حَرْفٌ وَمِيمٌ حَرْفٌ   Artinya: Kata ‘Abdullah ibn Mas‘ud, Rasulullah shallallahu ‘alaihi wasallam bersabda, “Siapa saja membaca satu huruf dari Kitabullah (Al-Qur’an), maka dia akan mendapat satu kebaikan. Sedangkan satu kebaikan dilipatkan kepada sepuluh semisalnya. Aku tidak mengatakan alif lâm mîm satu huruf. Akan tetapi, alif satu huruf, lâm satu huruf, dan mîm satu huruf,”(HR. At-Tirmidzi)")
    elif (ibadah=='3'):
           print("لِلَّذِينَ أَحْسَنُوا الْحُسْنَىٰ وَزِيَادَةٌ ۖ وَلَا يَرْهَقُ وُجُوهَهُمْ قَتَرٌ وَلَا ذِلَّةٌ ۚ أُولَٰئِكَ أَصْحَابُ الْجَنَّةِ ۖ هُمْ فِيهَا خَالِدُونَ Bagi orang-orang yang berbuat baik, ada pahala yang terbaik (surga) dan tambahannya. Dan muka mereka tidak ditutupi debu hitam dan tidak (pula) kehinaan. Mereka itulah penghuni surga, mereka kekal di dalamnya. [Yûnus/10:26]")
       
    else:
        print("Mohon Masukkan Sesuai Pilihan Diatas")
