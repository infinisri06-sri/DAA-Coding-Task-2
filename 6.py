def knapsack_brute_force(value, weight, max_weight):
    n = len(value)
    max_value = 0
    best_combination = []

 
    for comb in range(2 ** n):
        temp_weight = 0
        temp_value = 0
        combination = [int(x) for x in bin(comb)[2:].zfill(n)]  # binary array

     
        for i in range(n):
            if combination[i] == 1:
                temp_weight += weight[i]
                temp_value += value[i]

        
        if temp_weight <= max_weight and temp_value > max_value:
            max_value = temp_value
            best_combination = combination.copy()

    return best_combination, max_value


values = [4, 5, 7, 8, 10, 6]
weights = [2, 3, 6, 5, 8, 7]
max_weight = 15

result = knapsack_brute_force(values, weights, max_weight)
print("Best combination:", result[0])
print("Maximum value:",result[1])
