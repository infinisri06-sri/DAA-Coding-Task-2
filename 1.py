

def permutation(list, current=""):
    if len(list) == 0:
        print(current)
        return

    for i in range(len(list)):
       
        remaining = list[:i] + list[i+1:]
        permutation(remaining, current + list[i])


text = input("Enter any random string for permutation: ")
print("All possible permutations are:")
permutation(text)