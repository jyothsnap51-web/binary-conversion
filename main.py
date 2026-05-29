
a = int(input("Enter a decimal number: "))
binary = ""

while a > 0:
    remainder = a % 2
    binary = str(remainder) + binary
    a = a // 2

print("Binary:", binary)
