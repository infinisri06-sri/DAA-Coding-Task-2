def int_to_binary(num):
    if num == 0:
        return "0"
    binary = ""
    while num > 0:
        r = num % 2 
        binary = str(r) + binary
        num = num // 2
    return binary

num = int(input("Enter an integer: "))
binary = int_to_binary(num)
print("Binary equivalent:", binary)

p= int(input("Enter a bit position to check (0 = rightmost): "))


if p < 0 or p >= len(binary):
    print("Invalid position!")
else:
    bit = binary[-(p + 1)]   
    print(f"Bit at position {p}is{bit}")