from math import floor

def to_binary() -> str:
    decimal = int(input("Napiste cislo v desitkove soustave: "))
    limit = floor(decimal/2)
    binary = []

    for i in range(limit, -1, -1):
        if 2**i <= decimal:
            binary.append(1)
            decimal -= 2**i
        elif 2**i > decimal:
            if sum(binary) != 0:
                binary.append(0)

    binary_str = "".join(str(bit) for bit in binary)
    return binary_str

def to_decimal() -> int: 
    binary = input("Napiste cislo v binarni soustave: ")
    decimal = 0
    for i in reversed(range(len(binary))):
        print(f"Iterace je {i} a hodnota v bin. je {binary[-i-1]}")
        if int(binary[-i-1]) == 1:
            decimal += 2**i
    return decimal
 
        



choice = input("Pro převod do decimální soustavy zadejte \"dec\", pro převod do binární zadejte \"bin\" (and \"z\" for exit): ")

match choice:
    case "dec":
        print(to_decimal())
    case "bin":
        print(to_binary())
    case "z":
        pass