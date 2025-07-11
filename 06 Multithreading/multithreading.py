# %% [markdown]
"""
# Multithreading
Multiple threads can execute multiple functions simultaneously
"""
# %%
import time
time.sleep(5)
print("Hello!")
# %%
# Write a decorator to measuer time required by a function
def time_dec(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        print(f"Results : {res}")
        stop = time.perf_counter()
        elapsed = stop - start
        print(f"Time Elapsed : {elapsed:.4f} sec")
        return res
    return wrapper
# %% [markdown]
"""
Create two functions
1. simple interest
2. hypotenuse
"""
# %%
@time_dec
def simple_interest(p, n, r):
    print("Simple Intrest function Started")
    time.sleep(2)
    i = (p * n * r) / 100
    a = p + i
    return i, a 
# %%
import math

@time_dec
def hypotenuse(a, b):
    print("Hypotenuse function started")
    time.sleep(3)
    h = math.sqrt(a**2 + b**2)
    return h
# %%
i1, a1 = simple_interest(p=10_000, n=5, r=6.5)
# %%
h1 = hypotenuse(4, 5)
# %%
# Single Thread execution
start = time.perf_counter()
i2, a2 = simple_interest(p=50_000, n=3, r=7.1) # 2 sec
h2 = hypotenuse(3, 4) # 3 sec
stop = time.perf_counter()
elapsed = stop - start
print(f"Total Time required : {elapsed:.4f} sec")
# %%
# Mutli-threading
from threading import Thread

start = time.perf_counter()
# Create the threads
th1 = Thread(target=hypotenuse, args=(3, 4))
th2 = Thread(target=simple_interest, args=(12_000, 4, 6.8))
# Start the threads
th1.start()
th2.start()
# Wait for all threads to finish
th1.join()
th2.join()
stop = time.perf_counter()
elapsed = stop - start
print(f"Total Time Multithreading : {elapsed:.4f} sec")
# %% [markdown]
"""
Multithreading on multiple values
"""
# %%
@time_dec
def square_list(nums: list[int]):
    for i in nums:
        time.sleep(1)
        print(f"Square of {i} is {i**2}")

# %%
a = [3, 4, 11, 12, 34, 25]
square_list(a)
# %%
b = [23, 24, 101]
square_list(b)
# %%
def square(n: int):
    time.sleep(1)
    print(f"Square of {n} is {n**2}")

# %%
square(11)
# %%
# Multithreading

@time_dec
def multithreading_squares(nums: list[int]):
    # Create threads and start
    threads = []
    for i in nums:
        th = Thread(target=square, args=(i,))
        th.start()
        threads.append(th)

    # Wait for all threads to finish
    for th in threads:
        th.join()
# %%
multithreading_squares(a)
# %%
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
square_list(c)
# %%
multithreading_squares(c)
# %% [markdown]
"""
# Downloading multiple files via single threading vs multithreading
"""
# %%
url1 = "https://raw.githubusercontent.com/utkarshg1/mlproject_regression/main/artifacts/data.csv"
print(url1)

# %%
url1.split("/")

# %%
url1.split("/")[-1]
# %%
from urllib.request import urlretrieve

def download_file(url: str):
    filename = url.split("/")[-1]
    print(f"Downloading {filename} ...")
    urlretrieve(url, filename)
    print(f"{filename} download complete!")
# %%
download_file(url1)
# %%
# Single threaded download multiple files

@time_dec
def download_many_files(urls: list[str]):
    for url in urls:
        download_file(url)
# %%
urls = [
    "https://raw.githubusercontent.com/utkarshg1/mlproject_regression/main/artifacts/data.csv",
    "https://raw.githubusercontent.com/utkarshg1/mlproject_regression/main/artifacts/test.csv",
    "https://raw.githubusercontent.com/utkarshg1/mlproject_regression/main/artifacts/train.csv"
]
print(urls)
# %%
download_many_files(urls)
# %%
# Write function to download files simultaneously with multithreading
@time_dec
def multithreaded_download(urls: list[str]):
    # Create and start threads
    threads = []
    for url in urls:
        th = Thread(target=download_file, args=(url,))
        th.start()
        threads.append(th)
    # Wait for all threads to finish
    for th in threads:
        th.join()
# %%
multithreaded_download(urls)
# %% [markdown]
"""
# Multithreading can be used to execute code parallely and takes less time
"""
# %%
