def printMe(text, times):
    printAmount = int(times)
    printAmount += printAmount
    i = 1
    while i <= printAmount:
        print(text)
        i += i

printMe(input("Syötä nimi\n"),4)