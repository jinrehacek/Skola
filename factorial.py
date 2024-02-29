array = []
number = int(input("cislo: "))

def factorial(n):
    if n == 0:
        return 1
    array.append(n)
    if n == 1:
        return 1
    return factorial(int(n-1))

factorial(number)

sum = 1
for num in array:
    sum = sum * num

print(array)
print(sum)
