import time

def fibonacci_normal(n):
    if n <= 1:
        return n
    else:
        return fibonacci_normal(n-1) + fibonacci_normal(n-2)

# Measure time for the non-cached version
print()
print("NON-CACHED : ")

start_time = time.time()
result_normal = fibonacci_normal(30)
end_time = time.time()
print(f"Result (Non-cached): {result_normal}")
print(f"Time taken (Non-cached): {end_time - start_time} seconds")



import functools
import time

@functools.lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n <= 1:
        return n
    else:
        return fibonacci_cached(n-1) + fibonacci_cached(n-2)

# Measure time for the cached version
print()
print("CACHED : ")

start_time = time.time()
result_cached = fibonacci_cached(30)
end_time = time.time()
print(f"Result (Cached): {result_cached}")
print(f"Time taken (Cached): {end_time - start_time} seconds")