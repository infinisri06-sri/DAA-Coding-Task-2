def knapsack_brute_force(value, weight, max_weight):
    n = len(value)
    max_value = 0
    best_combination = []

   
    for comb in range(2 ** n):
        temp_weight = 0
        temp_value = 0

        
        combination = [int(bit) for bit in bin(comb)[2:].zfill(n)]

        
        for i in range(n):
            if combination[i] == 1:
                temp_weight += weight[i]
                temp_value += values[i]


        if temp_weight <= max_weight and temp_value > max_value:
            max_value = temp_value
            best_combination = combination.copy()

    return best_combination, max_value


values = [3, 4, 8, 8, 10, 6]
weight= [2, 3, 4, 5, 9, 7]
max_weight = 15


best_combo, max_val = knapsack_brute_force(values, weight, max_weight)


print("Best Combination (0 = exclude, 1 = include):", best_combo)
print("Maximum Value it can reach :",max_val)
