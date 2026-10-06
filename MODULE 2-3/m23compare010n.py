import time

# Create a list with 1,000,000 elements
arr = list(range(1_000_000))

# O(1) Access
start = time.time()

x = arr[500_000]

end = time.time()

print("O(1) Access")
print("Element found:", x)
print("Access time:", end - start, "seconds")
print()

# O(n) Search
target = 999_999

start = time.time()

found = target in arr

end = time.time()

print("O(n) Search")
print("Target:", target)
print("Found:", found)
print("Search time:", end - start, "seconds")