import os


# Parent hakemistopolun tulee olla testauksen aikana jossain muussa kuin nykyisessä kansiossa!
#
# Esimerkiksi ./testidata
#
parent = "./"



def hakemistojen_luonti():

    print("--------------------------------------------")
    print("|                                          |")
    print("| Nykyisen kansion hakemistot ja tiedostot |")
    print("|                                          |")
    print("--------------------------------------------")
    for asia in os.listdir(parent):
            print(asia)

    try:
        kansio = parent + "/kuvat/"
        if (os.path.exists(kansio)):
            print("Kuvat kansio on jo olemassa!")
        else:
            os.mkdir(kansio)
            print("Kuvat kansio luotu.")
    except FileExistsError:
        print("Kansio on jo olemassa, et voi luoda sitä uudestaan!")

    try:
        kansio = parent + "/videot/"
        if (os.path.exists(kansio)):
            print("Videot kansio on jo olemassa!")
        else:
            os.mkdir(kansio)
            print("Videot kansio luotu.")
    except FileExistsError:
        print("Kansio on jo olemassa, et voi luoda sitä uudestaan!")

    try:
        kansio = parent + "/gifs/"
        if (os.path.exists(kansio)):
            print("Gifi kansio on jo olemassa!")
        else:
            os.mkdir(kansio)
            print("Gifi kansio luotu.")
    except FileExistsError:
        print("Kansio on jo olemassa, et voi luoda sitä uudestaan!")

    try:
        kansio = parent + "/tiedostot/"
        if (os.path.exists(kansio)):
            print("Tiedostot kansio on jo olemassa!")
        else:
            os.mkdir(kansio)
            print("Tiedostot kansio luotu.")
    except FileExistsError:
        print("Kansio on jo olemassa, et voi luoda sitä uudestaan!")

    try:
        kansio = parent + "/arkistot/"
        if (os.path.exists(kansio)):
            print("Arkistot kansio on jo olemassa!")
        else:
            os.mkdir(kansio)
            print("Arkistot kansio luotu.")
    except FileExistsError:
        print("Kansio on jo olemassa, et voi luoda sitä uudestaan!")

def listaus():

    print("KANSIOT:")
    for tiedosto in os.listdir(parent):
        if os.path.isdir(parent + "/" + tiedosto):
            print("\t- " + tiedosto)
    print("TIEDOSTOT:")
    for tiedosto in os.listdir(parent):
        if os.path.isfile(parent + "/" + tiedosto):
            print("\t- " + tiedosto)


def lajittelu():

    for tiedosto in os.listdir(parent):

        tiedoston_polku = parent + "/" + tiedosto

        if os.path.isfile(tiedoston_polku):
            print("\t- " + tiedosto)
            jako = tiedosto.split(".")
            paate = jako[1]
            print("Pääte on : " + paate)


            # Voisi lisätä koodin joka lowercasee tiedostopäätteet ja tutkii vasta sitten.
            # Tällä voitaisiin lyhentää if ehtoja
            if(paate == "txt" or paate == "pdf" or paate == "docx" or paate == "csv" or paate == "xlsx" or paate == "pptx"):
                os.replace(str(tiedoston_polku), str(parent + "/" + "tiedostot" + "/" + tiedosto))
            elif (paate == "png" or paate == "jpg" or paate == "jpeg" or paate == "PNG" or paate == "JPG" or paate == "JPEG"):
                os.replace(str(tiedoston_polku), str(parent + "/" + "kuvat" + "/" + tiedosto))
            elif (paate == "mp4" or paate == "MP4" or paate == "mov" or paate == "MOV" or paate == "" or paate == "JPEG"):
                os.replace(str(tiedoston_polku), str(parent + "/" + "videot" + "/" + tiedosto))
            elif (paate == "gif"):
                os.replace(str(tiedoston_polku), str(parent + "/" + "gifs" + "/" + tiedosto))
            elif (paate == "zip" or paate == "rar" or paate == "7z"):
                os.replace(str(tiedoston_polku), str(parent + "/" + "arkistot" + "/" + tiedosto))
            else:
                print("No mitä vihhua?")


def main():

    isRunning = True


    cur_dir = os.getcwd()
    list_dir = os.listdir()
    print("Current directory: ", cur_dir)

    while isRunning:
        print("\n")
        print("1) Listaa tiedostot")
        print("2) Luo kansiot")
        print("3) Lajittele tiedostot")
        print("0) Lopeta")
        toimi = input("Mitä haluat tehdä? : ")
        print("\n")


        try:
            if (int(toimi) == 1):
                print("Listataan tiedostot...")
                listaus()
            elif (int(toimi) == 2):
                print("Aloitetaan luomaan kansio...")
                hakemistojen_luonti()
            elif (int(toimi) == 3):
                print("Aloitetaan tiedotojen lajittelu...")
                lajittelu()
            elif (int(toimi) == 0):
                print("Lopetetaan")
                isRunning = False
            else:
                print("Annoit väärän laisen vastauksen!!!")
        except ValueError:
            print("Annoit väärän laisen vastauksen!!!")


if __name__ == '__main__':
    main()