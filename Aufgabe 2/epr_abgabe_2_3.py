__author__ = "Chris"


def streichholzspiel():
    streichhoelzer = 13
    spieler = 0 # welcher spieler dran ist (spieler 1 = spieler 0, spieler 2 = spieler 1)
    while streichhoelzer > 0: 
        visualisierung(streichhoelzer)
        a = 0     
        # Spieler 1 ist dran   
        if spieler == 0:  
            while a < 1 or a > 3: 
                a = int(input("Spieler 1 ist dran, wie viele Streichhölzer sollen genommen werden? (1-3): "))
                if (a < 1 or a > 3):
                    print("ungültige Eingabe")
        # Spieler 2 ist dran            
        else: 
            while a < 1 or a > 3: 
                a = int(input("Spieler 2 ist dran, wie viele Streichhölzer sollen genommen werden? (1-3): "))
                if (a < 1 or a > 3):
                    print("ungültige Eingabe")
        streichhoelzer -= a
        # Gewinner am Ende vom Spiel
        if streichhoelzer <= 0: 
            print("Spieler", spieler + 1 ,"hat gewonnen")
            visualisierung(0)
        if spieler == 0:
            spieler += 1
        else:
            spieler -= 1


def visualisierung(n): # Visualisierung der Streichhölzer in der Konsole
    vis = "==================================================\nEs verbleiben noch " + str(n) + " Streichhölzer:\n"
    for _ in range(n): 
        vis += "()  "
    for _ in range(3):
        vis += "\n"
        for _ in range(n):
            vis += "||  "
    vis += "\n=================================================="
    print(vis)

streichholzspiel()

##TESTCASES##
#   1. Versucht der User mehr als 3 oder weniger als 1 Streichholz zu ziehen,
#      dann erscheint "ungültige Eingabe" und User wird erneut aufgefordert,
#      eine Zahl zu wählen.
#   2. Versucht der User einen Buchstaben anstatt einer Zahl zu schreiben,
#      dann erscheint und ValueError und man muss das Programm
#      von neu laufen lassen.
#   3. Geben die User die Zahlen zwischen 1-3 an, dann spielen sie das Spiel,
#      bis der letzte Spieler die letzten Streichhölzer zieht.