# %% [markdown]
"""
# Exception Handling
## Different exeptions in python
"""
# %%
# ZeroDivision Error -> any number divided by 0
a = 12
b = 0
print(a / b)
# %%
# TypeError -> different datatypes divided togethor
c = "test"
d = c / 2
print(c, d)
# %%
a = "23"
b = int(a)
print(a, type(a))
print(b, type(b))
# %%
a = "abc"
b = int(a)
print(b, type(b))
# %% [markdown]
"""
# Handling the exceptions
try: Whatever code you want to execute
except: If code gets exception exception block will be triggered
"""

# %%
def division(num: int | float, den: int | float) -> float:
    return num / den    
# %%
division(3, 4)
# %%
division(11.5, 2.8)
# %%
division(10, 0)
# %%
division("abc", 3)
# %%
division(11, 0)
print("Code complete")
# %%
# Generic Exception handling
def division2(num: int|float, den: int|float) -> float:
    try:
        return num / den
    except Exception as e:
        print(f"Exception Occured : {e}")

# %%
r1 = division2(12, 4)
print(r1)
print("division complete")
# %%
r2 = division2(10, 0)
print(r2)
print("Division Complete")
# %%
r3 = division2(3)
print(r3)
# %%
# Custom exception handling
def division3(num: int|float, den: int|float) -> float:
    try:
        return num / den
    except ZeroDivisionError:
        print("Denominator of division cannot be 0")
    except TypeError:
        print("Only integer and float can do division")
# %%
r4 = division3(10, 7)
print(r4)
print("Division Complete")
# %%
r5 = division3(15, 0)
print(r5)
print("Complete")
# %%
r6 = division3(3, "a")
print(r6)
print("Complete")
# %% [markdown]
"""
## Exception handling blocks
1. try - any code to be executed
2. except - excutes if try block fails
3. else - executes if try block is successful
4. finally - always executes not matter what
"""

# %%
import math
def hypotenuse(a: int|float, b: int|float) -> float:
    return math.sqrt(a**2 + b**2)

# %%
hypotenuse(3, 4)
# %%
hypotenuse("a", 2)
# %%
def hypotenuse2(a: int|float, b: int|float) -> float:
    try:
        h = math.sqrt(a**2 + b**2)
    except Exception as e:
        print(f"Exception occured : {e}")
    else:
        print(f"Hypotenuse of sides {a} and {b} is {h:.4f}")
        return h
    finally:
        print("Finally Block will always be executed")

# %%
h1 = hypotenuse2(3, 4)
# %%
print(h1)

# %%
h2 = hypotenuse2("a", "b")
# %%
h4 = hypotenuse2(3, "")
# %% [markdown]
"""
# Raising custom exceptions
"""
# %%
# Age cannot be 0 or negative 
# Age upper limit should be 110
def validate_age(age: int):
    if type(age) != int:
        raise ValueError("Age Should be an Integer")
    
    if age <= 0 or age >= 110:
        raise ValueError("Age must be between 1 to 110")

    print(f"Valid age entered : {age} years")
    return age

# %%
try:
    age = validate_age(23)
except Exception as e:
    print(f"Exception occured : {e}")

# %%
def validate_age_exc(age: int):
    try:
        return validate_age(age)
    except Exception as e:
        print(f"Exception Occured : {e}")

# %%
a1 = validate_age_exc(23)
print(a1)
# %%
a2 = validate_age_exc("Twenty Three")
print(a2)
# %%
a3 = validate_age_exc(False)
print(a3)
# %%
a4 = validate_age_exc(10.8)
print(a4)
# %%
a5 = validate_age_exc(-3)
print(a5)
# %%
a6 = validate_age_exc(150)
print(a6)
# %%
import pandas as pd 
def analyze_data(file_path: str, cat: str, con: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
        print(df.head())
        a = (
            df.groupby(cat)
            .agg({con: "sum"})
            .sort_values(by = con, ascending=False)
        )
        print(a)
        a.plot(kind="bar", figsize=(10, 4))
        return a
    except Exception as e:
        print(f"Exception occured : {e}")

# %%
b1 = analyze_data(
    file_path="./50_Startups.csv",
    cat = "STATE",
    con = "PROFIT"
)
# %%
b2 = analyze_data(
    file_path="./50_Startups.csv",
    cat = "STATE",
    con = "MKT"
)
# %%
b3 = analyze_data(
    file_path="Startups.csv",
    cat = "STATE",
    con = "ADMIN"
)
# %%
b3 = analyze_data(
    file_path="./50_Startups.csv",
    cat = "STATE",
    con = "Sales"
)
# %%
