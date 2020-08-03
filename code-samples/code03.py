def Is_Magic_Square(Array):

    Magic_Chek = 0
    Magic_Sum = 0

    for i in range(len(Array)):
        Magic_Chek += Array[0][i]

    for i in range(len(Array)):
        Magic_Sum += Array[i][0]

    if Magic_Sum != Magic_Chek:
        return "\nyour cube is not magic\n"
    else:
        Magic_Sum = 0

    for i in range(len(Array)):
                Magic_Sum += Array[i][i]

    if Magic_Sum != Magic_Chek:
        return "\nyour cube is not magic\n"
    else:
        Magic_Sum = 0

    j = len(Array)
    for i in range(len(Array)):

                Magic_Sum += Array[i][j - 1]

    if Magic_Sum != Magic_Chek:
        return "\nyour cube is not magic\n"
    else:
        Magic_Sum = 0

    j = len(Array) - 1
    for i in range(len(Array)):
        Magic_Sum += Array[i][j - i]

    if Magic_Sum != Magic_Chek:
        return "\nyour cube is not magic\n"
    else:
        return "\nyour cube is magic\n"


def MagicSquare(ONumber):

    i, j = 0, 0
    if ONumber % 2 == 0:

        print("\nplease enter a odd number\n")
    else:
        col = ONumber
        row = ONumber
        arr = [[0 for i in range(col)] for j in range(row)]
        arr[0][ONumber // 2] = 1

        j = (ONumber - 1) // 2

        for key in range(2, (ONumber * ONumber) + 1):
            if i >= 1:
                k = i - 1
            else:
                k = ONumber - 1
            if j >= 1:
                l = j - 1
            else:
                l = ONumber - 1
            if arr[k][l] >= 1:
                i = (i + 1) % ONumber
            else:
                i = k
                j = l
            arr[i][j] = key

        return arr
                        

def Magic_square(Enumber):

    col = Enumber
    row = Enumber
    arr = [[0 for i in range(col)] for j in range(row)]

    for i in range(0, n):
        for j in range(0, n):
            arr[i][j] = (n * i) + j + 1

    for i in range(0, int(n / 4)):
        for j in range(0, int(n / 4)):
            arr[i][j] = (n * n + 1) - arr[i][j]

    for i in range(0, int(n / 4)):
        for j in range(3 * int((n / 4)), n):
            arr[i][j] = (n * n + 1) - arr[i][j]

    for i in range(3 * int((n / 4)), n):
        for j in range(0, int(n / 4)):
            arr[i][j] = (n * n + 1) - arr[i][j]

    for i in range(3 * int((n / 4)), n):
        for j in range(3 * int((n / 4)), n):
            arr[i][j] = (n * n + 1) - arr[i][j]

    for i in range(int(n / 4), 3 * int((n / 4))):
        for j in range(int(n / 4), 3 * int((n / 4))):
            arr[i][j] = (n * n + 1) - arr[i][j]
    return arr


while True:
    x = int(
        input(
            "if you wanna create a magic cube enter '1' else if you wanna test your cube that is magic or nor enter '2' :"
        )
    )

    print("")
    if x == 1:
        n = int(
            input(
                "enter a odd number or even number (the even number you enter, must be devisible by 4): "
            )
        )

        if n % 2 != 0:
            for i in range(n):
                print("")
                print(MagicSquare(n)[i])
            print("")
            break

        elif n % 4 == 0:
            for i in range(n):
                print("")
                print(Magic_square(n)[i])
            print("")
            break

        elif n % 2 == 0:
            print("your even number should be factor of 4")
            break

    else:
        if x == 2:
            NumberOfSquare = int(
                input("enter a number for rows and columns of your cube: ")
            )

            print("")

            Arr = [[0 for i in range(NumberOfSquare)] for j in range(NumberOfSquare)]

            for i in range(0, NumberOfSquare):
                for j in range(0, NumberOfSquare):
                    print("enter row of ", i + 1, "column of ", j + 1)
                    Arr[i][j] = int(input())

                        print(Is_Magic_Square(Arr))
            break
