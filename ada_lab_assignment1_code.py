import time
import matplotlib.pyplot as plt

print("===== TASK 1: Algorithm Growth Observation =====")

# O(1)
def constant_time(n):
    return n * 2

start = time.time()
constant_time(1000000)
print("O(1) Time:", time.time() - start)

# O(n)
def linear_time(n):
    total = 0
    for i in range(n):
        total += i
    return total

start = time.time()
linear_time(100000)
print("O(n) Time:", time.time() - start)

# O(n^2)
def quadratic_time(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

start = time.time()
quadratic_time(500)
print("O(n^2) Time:", time.time() - start)

# O(log n)
def logarithmic_time(n):
    while n > 1:
        n = n // 2

start = time.time()
logarithmic_time(1000000)
print("O(log n) Time:", time.time() - start)


# GRAPH
sizes = [10, 100, 500, 1000]
times = []

for n in sizes:
    start = time.time()
    linear_time(n)
    times.append(time.time() - start)

plt.plot(sizes, times, marker='o')
plt.title("Input Size vs Execution Time (O(n))")
plt.xlabel("Input Size")
plt.ylabel("Time")
plt.show()


print("\n===== TASK 2: Linear Search =====")

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = list(range(100000))

# Best Case
start = time.time()
linear_search(arr, 0)
best = time.time() - start
print("Best Case:", best)

# Average Case
start = time.time()
linear_search(arr, 50000)
avg = time.time() - start
print("Average Case:", avg)

# Worst Case
start = time.time()
linear_search(arr, 99999)
worst = time.time() - start
print("Worst Case:", worst)

# Comparison Plot
cases = ["Best", "Average", "Worst"]
times = [best, avg, worst]

plt.bar(cases, times)
plt.title("Linear Search Comparison")
plt.ylabel("Time")
plt.show()


print("\n===== TASK 3: Recursion =====")

# Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print("Factorial(5):", factorial(5))

# Fibonacci Recursive
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

print("Fibonacci Recursive(10):", fib_recursive(10))

# Fibonacci Iterative
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print("Fibonacci Iterative(10):", fib_iterative(10))


print("\n===== TASK 4: Recurrence =====")

# T(n) = T(n/2) + n
def recurrence1(n):
    if n <= 1:
        return 1
    return recurrence1(n//2) + n

print("T(n) = T(n/2) + n:", recurrence1(16))

# T(n) = 2T(n/2) + n
def recurrence2(n):
    if n <= 1:
        return 1
    return 2 * recurrence2(n//2) + n

print("T(n) = 2T(n/2) + n:", recurrence2(16))


print("\n===== END OF ASSIGNMENT =====")