import os



def get_music_list():
    file_path = ""
    while(True):
        print("Wählen Sie:")
        print("[1] Neue Liste erstellen")
        print("[2] Bestehende Liste benutzen")
        choice = int(input(" > "))


        if(choice == 1):
            print('Bitte geben Sie die Stücke im Format [Nummer, Name] ein.')
            print('Wenn Sie fertig sind, scheiben Sie "Eingabe ende"')
            with open("musikliste.csv", 'w', encoding='utf-8') as f:
                
                while(True):
                    str_in = input(" > ")
                    if str_in.lower() == "eingabe ende":
                        break
                    f.write(str_in + "\n")

                file_path = f.name    
                f.close()
            return file_path

        elif(choice == 2):
            print('Bitte geben Sie den Pfad zur Datei ein: ')
            file_path = input(" > ")

            print('Möchten Sie die Datei erweitern [Ja/Nein]?')
            choice = input(" > ").lower()
            
            if(choice == "ja"):
                print('Bitte geben Sie die Stücke im Format [Nummer, Name] ein.')
                print('Wenn Sie fertig sind, scheiben Sie "Eingabe ende"')
                
                with open(file_path, 'a', encoding='utf-8') as f:
                    while(True):
                        str_in = input(" > ")
                        if str_in.lower() == "eingabe ende":
                            break
                        f.write(str_in + "\n")

                    f.close()
            return file_path


def get_sponsors_list(number_of_pieces):
    file_path = ""
    while(True):

        print("Wählen Sie:")
        print("[1] Neue Liste erstellen")
        print("[2] Bestehende Liste benutzen")
        choice = int(input(' > '))

        if choice == 1:
            
            sponsoren = input_sponsoren(number_of_pieces)

            with open("sponsorenliste.csv", "w", encoding="utf-8") as f:
                for x in sponsoren:
                    f.write(x + "\n")

                file_path = f.name
                f.close()

            return file_path
        
        if choice == 2:
            print('Bitte geben Sie den Pfad zur Datei ein: ')
            file_path = input(" > ")

            print('Möchten Sie die Datei erweitern [Ja/Nein]?')
            choice = input(" > ").lower()

            if choice == 'ja':
                sponsoren = input_sponsoren(number_of_pieces)

                with open(file_path, 'a', encoding='utf-8') as f:
                    for x in sponsoren:
                        f.write(x + '\n')
                
                return file_path


def input_sponsoren(number_of_pieces):
    print('Bitte geben Sie die Sponsoren im Format [Name, Betrag, Stücknummer] ein.')
    print('Wenn Sie fertig sind, scheiben Sie "Eingabe ende"')
    print('Sollte ein Sponsor schon einmal existieren, wird er nicht hinzugefügt (Alle Werte identisch)')
    sponsoren = set()
    while(True):
        str_in = input(" > ").lower()
        if str_in.lower() == "eingabe ende":
            break
        if int(str_in.split(',')[2]) < 0 or int(str_in.split(',')[2]) > number_of_pieces:
            print('Achtung! Eingabe ignoriert, Stückwunsch nicht verfügbar')
        else:
            sponsoren.add(str_in)
    return sponsoren

get_sponsors_list(6)