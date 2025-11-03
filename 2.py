def combination(data, start, k, current=""):
    if len(current) == k:
        print(current)
        return

    for i in range(start, len(data)):
        combination(data, i + 1, k, current + data[i])


t = input("Enter any random  string for combination: ")
s = int(input("Enter length for this  combination: "))
print(f"All combinations of length {s} are:")
combination(t,0,s)