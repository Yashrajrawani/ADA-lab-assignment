import time
import random
import matplotlib.pyplot as plt
import itertools

print("===== Q1: Merge Sort =====")

def merge_sort(input_arr):
    if len(input_arr) <= 1:
        return input_arr
    
    mid = len(input_arr) // 2
    left = merge_sort(input_arr[:mid])
    right = merge_sort(input_arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Timing Merge Sort
input_arr = [random.randint(1, 1000) for _ in range(1000)]
start = time.time()
merge_sort(input_arr)
end = time.time()

print("Merge Sort Time:", end - start)


print("\n===== Q2: Sorting Comparison =====")

def bubble_sort(input_arr):
    n = len(input_arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if input_arr[j] > input_arr[j+1]:
                input_arr[j], input_arr[j+1] = input_arr[j+1], input_arr[j]

sizes = [100, 200, 500, 1000]

bubble_times = []
merge_times = []
builtin_times = []

for size in sizes:
    input_arr = [random.randint(1, 1000) for _ in range(size)]
    
    # Bubble Sort
    temp = input_arr.copy()
    start = time.time()
    bubble_sort(temp)
    bubble_times.append(time.time() - start)
    
    # Merge Sort
    temp = input_arr.copy()
    start = time.time()
    merge_sort(temp)
    merge_times.append(time.time() - start)
    
    # Built-in Sort
    temp = input_arr.copy()
    start = time.time()
    sorted(temp)
    builtin_times.append(time.time() - start)

plt.plot(sizes, bubble_times, label="Bubble Sort")
plt.plot(sizes, merge_times, label="Merge Sort")
plt.plot(sizes, builtin_times, label="Built-in Sort")
plt.xlabel("Input Size")
plt.ylabel("Time")
plt.legend()
plt.show()


print("\n===== Q3: Activity Selection =====")

def activity_selection(start, end):
    activities = list(zip(start, end))
    activities.sort(key=lambda x: x[1])  # sort by finish time
    
    selected = [activities[0]]
    
    for i in range(1, len(activities)):
        if activities[i][0] >= selected[-1][1]:
            selected.append(activities[i])
    
    return selected

start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]

print("Selected Activities:", activity_selection(start, end))


print("\n===== Q4: 0/1 Knapsack =====")

def knapsack(W, wt, val, n):
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]],
                               dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][W]

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50

print("Maximum Profit:", knapsack(W, wt, val, len(val)))


print("\n===== Q5: Traveling Salesman Problem (TSP) =====")

def tsp(graph):
    n = len(graph)
    cities = list(range(n))
    min_path = float('inf')
    
    for perm in itertools.permutations(cities[1:]):
        cost = 0
        k = 0
        
        for j in perm:
            cost += graph[k][j]
            k = j
        
        cost += graph[k][0]
        min_path = min(min_path, cost)
    
    return min_path

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print("Minimum TSP Cost:", tsp(graph))


print("\n===== END OF ASSIGNMENT =====")