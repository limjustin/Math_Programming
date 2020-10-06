import sys

intVar, floatVar, boolVar, listVar, tupVar, dictVar, setVar, strVar = [None]*8

if __name__ == "__main__" :
    intVar = 0
    floatVar = 0.0
    boolVar = True
    strVar = ""
    listVar = []
    tupVar = ()
    dictVar = {}
    setVar = set()

    print("int Size : ", sys.getsizeof(intVar))
    print("float Size : ", sys.getsizeof(floatVar))
    print("boolVar Size : ", sys.getsizeof(boolVar))
    print("strVar Size : ", sys.getsizeof(strVar))
    print("listVar Size : ", sys.getsizeof(listVar))
    print("tupVar Size : ", sys.getsizeof(tupVar))
    print("dictVar Size : ", sys.getsizeof(dictVar))
    print("setVar Size : ", sys.getsizeof(setVar))
