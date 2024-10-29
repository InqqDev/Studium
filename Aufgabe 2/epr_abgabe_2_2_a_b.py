__author__ = "Chris"


def schachbrett(n): # Schachbrett wird in der Konsole angezeigt
    vis = ""
    for i in range(n):
        vis += "\n"
        for j in range(n):
            vis += chr(j + 65) + str(i + 1) + " "
    print(vis)

##TESTCASES##
#   1. Wenn User 8 als input wählt, dann erscheint ein 8 x 8 Feld mit A-H und 1-8.
#   2. Wählt der User einen Buchstaben, dann gibt es einen ValueError.


def schachbrett_koenigin():
    n = int(input("Wie groß soll das Schachbrett sein?: ")) # User sucht größe des Bretts aus (n x n)
    schachbrett(n)
    vis = ""
    pos_koengin = input("Wo soll die Königin positioniert sein?: ") # User gibt Position der Königin ein
    x, y = pos_koengin[0], int(pos_koengin[1:])
    x = ord(x)

    if y > n or x - 64 > n or y < 1 or x - 64 < 1: # Wenn Input außerhalb vom Brett, dann kann nicht positioniert werden
        print("Königin kann nicht auf dem Schachbrett positioniert werden!")
        return 

    for i in range(n): #Gibt Schachbrett aus
        vis += "\n"
        for j in range(n):
            if(x == j + 65 and y == i + 1): # Checkt, ob man bei den "♛" - Koordinaten angelangt ist
                vis += "♛  "
            else:
                vis += chr(j + 65) + str(i + 1) + " "
    print(vis)

schachbrett_koenigin()

##TESTCASES##
#   1. Wenn User 8 als input nimmt, dann erscheint ein 8 x 8 Feld mit A-H und 1-8. Setzt man die Queen z.B. auf das Feld
#      G3, dann wird G3 mit dem Königin-Symbol ausgetauscht und in der üblichen Brettform angezeigt.
#   2. Wenn der User beim input der Queen in lower case schreibt,
#      dann kommt der Text: "Königin kann nicht positioniert werden!"
#   3. Wenn der User Buchstaben bei der Abfrage der Brettgröße schreibt, kommt ein ValueError.
#   4. Wenn man die Königin außerhalb des angezeigten Brettes setzt:
#      (z.B. 8 x 8 Brett und Königin auf I3), dann kommt: "Königin kann nicht positioniert werden!".