import os

def hakemistojen_luonti():

    parent = "./testidata/"

    print("--------------------------------------------")
    print("|                                          |")
    print("| Nykyisen kansion hakemistot ja tiedostot |")
    print("|                                          |")
    print("--------------------------------------------")
    for asia in os.listdir(parent):
            print(asia)

    try:
        kansio = "./testidata/kuvat/"
        if (os.path.exists(kansio)):
            print("Kuvat kansio on jo olemassa!")
        else:
            os.mkdir(kansio)
            print("Kuvat kansio luotu.")
    except FileExistsError:
        print("Kansio on jo olemassa, et voi luoda sitä uudestaan!")

    try:
        kansio = "./testidata/videot/"
        if (os.path.exists(kansio)):
            print("Videot kansio on jo olemassa!")
        else:
            os.mkdir(kansio)
            print("Videot kansio luotu.")
    except FileExistsError:
        print("Kansio on jo olemassa, et voi luoda sitä uudestaan!")

    try:
        kansio = "./testidata/gifs/"
        if (os.path.exists(kansio)):
            print("Gifi kansio on jo olemassa!")
        else:
            os.mkdir(kansio)
            print("Gifi kansio luotu.")
    except FileExistsError:
        print("Kansio on jo olemassa, et voi luoda sitä uudestaan!")


def listaus():

    parent = "./testidata/"

    print("KANSIOT:")
    for tiedosto in os.listdir(parent):
        if os.path.isdir(parent + tiedosto):
            print("\t- " + tiedosto)
    print("TIEDOSTOT:")
    for tiedosto in os.listdir(parent):
        if os.path.isfile(parent + tiedosto):
            print("\t- " + tiedosto)


def lajittelu():

    parent = "./testidata/"

    for tiedosto in os.listdir(parent):
        if os.path.isfile(parent + tiedosto):
            print("\t- " + tiedosto)
            jako = tiedosto.split(".")
            paate = jako[1]
            print("Pääte on : " + paate)
            # if(paate == "txt"):


def main():

    isRunning = True

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
                print("Aloitetaan lajittelu...")
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