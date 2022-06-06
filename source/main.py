from interpolation import calculateInterpolation

x = []
f = []
val = []


def readGameStateFromFile(pathToFile):
    file = open(pathToFile, "r")
    for s in file:
        r = s.split(";")
        if len(r) == 2:
            x.append(float(r[0]))
            f.append(float(r[1]))
        else:
            val.append(float(r[0]))


if __name__ == '__main__':
    readGameStateFromFile(input("Insert file path:\n"))
    print("Result:")
    for i in val:
        print("f(" + str(i) + ") = " + str(calculateInterpolation(x, f, i)))
    input("Insert any key")
