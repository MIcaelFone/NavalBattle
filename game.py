umberRows = 20
numberColumns = 20
global Counternumberofaircraftcarrier
global counternumberofcruiser
global counternumberofFrigate
global positions_agreed
global positions_tried
global hits_positions_aircraft_carrier
global hits_positions_cruiser
global hits_positions_frigate

matrix = ["#"] * numberRows
legenda_vertical = ["01", "02", "03", "04", "05", "06", "07", "08", "09","10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
legenda_horizontal = "          1      2      3      4      5      6      7      8      9     10      11     12     13     14     15     16     17     18     19     20"
positions_tried = []
positions_tried_defense = []
positions_agreed = []

contador = 0


def createArray():
    matrix = [" 0 "] * numberRows
    for line in range(numberRows):
        matrix[line] = ["  0  "] * numberColumns
    return matrix

def printarray(tabuleiro):
    print(legenda_horizontal)
    for row in range(numberRows):
        Matrix_row = "   "
        Matrix_row += legenda_vertical[row] + "   "
        for column in range(numberColumns):
            Matrix_row += tabuleiro[row][column] + "  "
        print(Matrix_row)
    print(legenda_horizontal)


def Defensematrix(matrix):
    counternumberofAircraftCarrier = 3
    counternumberofCruise = 3
    counternumberofFrigate = 3

    while counternumberofAircraftCarrier > 0 or counternumberofCruise > 0 or counternumberofFrigate > 0:
        print("1-Aircraft carrier")
        print("2-Cruizer")
        print("3-Frigate")
        option = int(input("Type an option:"))
        if option == 1 and counternumberofAircraftCarrier == 0 or option == 2 and counternumberofCruise == 0 or option == 3 and counternumberofFrigate == 0:
            print("You can not insert more of this vessel")
            Defensematrix(matrix)
        row = int(input("Type a row:"))-1
        column = int(input("Type a column:"))-1
        if [row, column] not in positions_tried_defense:
            positions_tried_defense.append([row, column])

            if row < len(matrix) and column < len(matrix[0]):
                if option == 1 and column < 17:
                    matrix[row][column] = "  A  "
                    matrix[row][column + 1] = "  A  "
                    matrix[row][column + 2] = "  A  "
                    matrix[row][column + 3] = "  A  "
                    counternumberofAircraftCarrier -= 1
                    printarray(matrix)
                    print("Insertion an Aircraft carrier")
                    print(f'AircraftCarrier :{counternumberofAircraftCarrier}')
                    print("------------------------------------------------------------------------------------------------------------------------------")
                elif option == 2 and column < 17:
                    matrix[row][column] = "  C  "
                    matrix[row][column + 1] = "  C  "
                    matrix[row][column + 2] = "  C  "
                    counternumberofCruise -= 1
                    printarray(matrix)
                    print("Insertion a Cruiser")
                    print(f'Cruiser:{+counternumberofCruise}')
                    print("------------------------------------------------------------------------------------------------------------------------------")
                elif option == 3 and column < 19:
                    matrix[row][column] = "  F  "
                    matrix[row][column + 1] = "  F  "
                    counternumberofFrigate -= 1
                    printarray(matrix)
                    print("Insertion a Frigate")
                    print(f'Frigate:{counternumberofFrigate}')
                    print("------------------------------------------------------------------------------------------------------------------------------")

            else:
                print("Invalid row or column. Please try again.")
        else:
            print("These coordinates already have used")

points=0
attempts_aircraft_carrier=0
attempts_frigate=0
attempts_cruiser=0
def attackingMatrix(Defensematrix, Attackmatriz):
    total_of_vessel_parts=9
    attempts_total=0
    global points
    global attempts_aircraft_carrier
    global attempts_cruiser
    global attempts_frigate

    for cont in range(100):
        print()
    while (total_of_vessel_parts > 0):
        print("Its the time of attack.")
        row = int(input("Type the row of a coordinates attack:"))-1
        column = int(input("Type the column of a coordinates attack:"))-1
        if row < len(Attackmatriz) and column < len(Attackmatriz[0]):
            if [row, column] not in positions_tried:
                positions_tried.append([row, column])
                if Defensematrix[row][column] == "  A  ":
                    hit_aircraft_carrier(row,column,Attackmatriz)
                    total_of_vessel_parts -= 1
                    attempts_total+=1
                    attempts_aircraft_carrier+=1
                    if attempts_aircraft_carrier / 4 != 0:
                        points = points + 30
                        print(f'Score:{points}')

                elif Defensematrix[row][column] == "  C  ":
                    total_of_vessel_parts -= 1
                    hit_cruiser(row,column,Attackmatriz)
                    attempts_total += 1
                    attempts_cruiser+=1

                    if attempts_cruiser / 3 != 0:
                        points = points + 40
                        print(f'Score:{points}')


                elif Defensematrix[row][column] == "  F  ":
                    total_of_vessel_parts -= 1
                    hit_frigate(row,column,Attackmatriz)
                    attempts_total += 1
                    attempts_frigate+=1
                    if attempts_frigate / 2 != 0:
                        points = points + 50
                        print(f'Score:{points}')
                else:
                    print("Missed the target!!")
                    Attackmatriz[row][column] = "  E  "
                    printarray(Attackmatriz)

                    attempts_total += 1
                    print(f'Score:{points}')


            else:
                print("This coordinates already have used!")
        else:
            print("Invalid row or column. Please try again.")

        if(attempts_total==40):
            print("GAME OVER!!!")
            break


def hit_aircraft_carrier(row,column,attackmatriz):
    global attempts_aircraft_carrier
    global points
    print("You hit a part of a vessel!!")
    attackmatriz[row][column] = "  A  "
    printarray(attackmatriz)
    attempts_aircraft_carrier += 1

def hit_cruiser(row,column,attackmatriz):
    global points
    global attempts_cruiser
    global attempts_frigate
    global attempts_aircraft_carrier
    print("You hit a part of a vessel!!")
    attackmatriz[row][column] = "  C  "
    printarray(attackmatriz)
    attempts_cruiser = +1

def hit_frigate(row,column,attackmatriz):
    global points
    global attempts_frigate
    global attempts_aircraft_carrier
    global attempts_cruiser
    print("You hit a part of a vessel!!")
    attackmatriz[row][column] = "  F  "
    printarray(attackmatriz)
    attempts_frigate = +1


Defense= createArray()
printarray(Defense)
Defensematrix(Defense)
Attack = createArray()
attackingMatrix(Defense, Attack)