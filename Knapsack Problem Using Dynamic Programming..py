def knapsack_01(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
for i in range(1, n + 1):
        current_weight = weights[i - 1]
        current_value = values[i - 1]
        
        for w in range(1, capacity + 1):
            if current_weight <= w:
                dp[i][w] = max(current_value + dp[i - 1][w - current_weight], 
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
                
    max_value = dp[n][capacity]
    
    selected_indices = []
    w = capacity
    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:
            selected_indices.append(i - 1)  
            w -= weights[i - 1]             
            
    selected_indices.reverse()
    
    return max_value, selected_indices

if __name__ == "__main__":
    item_values = [60, 100, 120]
    item_weights = [10, 20, 30]
    knapsack_capacity = 50

    max_val, items = knapsack_01(item_weights, item_values, knapsack_capacity)
    
    print("Maximum Value : {max_val}")
    print("Selected Item in Indices: {items}")
