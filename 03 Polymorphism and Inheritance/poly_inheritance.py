# %% [markdown]
"""
# Part 1 - Polymorphism
"""

# %% [markdown]

"""
In order to convert .py to .ipynb
you need to install below

```cmd
uv add pip notebook
```

1. Ctrl + Shift + P 
2. Export as ipynb with output
3. Restart VS Code

"""

# %%
# Ignore non harmful warnings
from warnings import filterwarnings
filterwarnings("ignore")

# %% [markdown]
"""
# Polymorphism in function

You have multiple datatypes or classes but same
function can be applied on them
"""

# %%
a = "ETLHive"
print(a, type(a), len(a))

# %%
b = [11, 12, 13, 14, 15]
print(b, type(b), len(b))

# %%
c = {
    "name": "Abhijeet",
    "age": 28,
    "marks": 78.5
}
print(c, type(c), len(c))
# %% [markdown]
"""
# Polymorphism in operators
Same operator but multiple datatypes
"""

# %%
a = 23
b = 34
print(a + b)
# %%
a = 11.5
b = 12.3
print(a + b)
# %%
a = "Rahul"
b = "More"
print(a + " " + b)
# %%
a = [3, 4, 5]
b = [6, 7, 8]
print(a + b)
# %%
a = [1, 2]
b = [4, 5, 6, 7]
print(a + b)

# %% [markdown]
"""
# Polymorphism in classes
"""

# %%
class India:

    def capital(self):
        print("New Delhi is captial of India")

    def language(self):
        print("Hindi is widely spoken in India")
        
# %%
class USA:

    def capital(self):
        print("Washington D.C. is capital of USA")
    
    def language(self):
        print("English is widely spoken in USA")

# %%
class France:

    def capital(self):
        print("Paris is capital of France")

    def language(self):
        print("French is Widely spoken in France")

# %%
c1 = India()
print(type(c1))
c1.capital()
c1.language()

# %%
c2 = USA()
print(type(c2))
c2.capital()
c2.language()

# %%
c3 = France()
print(type(c3))
c3.capital()
c3.language()

# %%
countries = [c1, c2, c3]

for country in countries:
    print(type(country))
    country.capital()
    country.language()
    print("\n" + "="*50 + "\n")

# %% [markdown]
"""
# Three shapes Square, Rectangle and Circle
Apply polymorphism to calculate perimeter and area
"""

# %% 
from dataclasses import dataclass
# %%
@dataclass
class Square:

    side: int | float
    
    def perimeter(self) -> int | float:
        return 4 * self.side
    
    def area(self) -> int | float:
        return self.side ** 2
    
# %%
@dataclass
class Rectangle:

    width: int | float 
    height: int | float

    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def area(self):
        return self.width * self.height

# %%
import math 
print(math.pi)

# %%
@dataclass
class Circle:

    radius: int | float   

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def area(self) -> float:
        return math.pi * (self.radius ** 2 )
    
# %%
s1 = Circle(radius = 7)
s2 = Rectangle(width=20, height=10)
s3 = Square(side = 5)
s4 = Rectangle(width=10.5, height=8)
s5 = Circle(radius = 12)
# %%
shapes = [s1, s2, s3, s4, s5]

for shape in shapes:
    print(type(shape))
    print(shape)
    print(f"Perimeter : {shape.perimeter():.2f}")
    print(f"Area : {shape.area():.2f}")
    print("\n" + "="*50 + "\n")
# %% [markdown]
"""
# Inheritance
1. Single
2. Multilevel
3. Hierarchical
"""

# %% [markdown]

"""
## Single Inheritance
"""

# %%
class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")

# %%
class Employee(Person):

    def __init__(self, name: str, age: int, company: str):
        super().__init__(name, age)
        self.company = company
    
    def work(self):
        print(f"I work at {self.company}")
    
# %%
p1 = Person(name="Raman", age=28)
print(type(p1))
# %%
p1.name
# %%
p1.age
# %%
p1.introduce()
# %%
e2 = Employee(name="Aditi", age=32, company="Infosys")
print(type(e2))
# %%
e2.name
# %%
e2.age
# %%
e2.company
# %%
e2.work()
# %%
e2.introduce()
# %%
e2.introduce()
e2.work()
# %% [markdown]

"""
## 2. Multilevel Inehritance
Class A -> Class B -> Class C
"""
# %%
class Employee2:

    def __init__(self, emp_id: int, name: str):
        self.emp_id = emp_id
        self.name = name

    def get_details(self):
        print(f"Employee Id : {self.emp_id}")
        print(f"Employee name : {self.name}")
    
# %%
class Manager(Employee2):

    def __init__(self, emp_id: int, name: str, dept: str):
        super().__init__(emp_id, name)
        self.dept = dept

    def get_department(self):
        print(f"Department : {self.dept}")

# %%
class Director(Manager):

    def __init__(
            self, 
            emp_id: int, 
            name: str, 
            dept: str,
            region: str):
        super().__init__(emp_id, name, dept)
        self.region = region

    def get_all_info(self):
        self.get_details()
        self.get_department()
        print(f"Region : {self.region}")
    
# %%

emp = Employee2(emp_id=105, name="Sarthak")
print(type(emp))

# %%
emp.emp_id

# %%
emp.name
# %%
emp.get_details()
# %%
manager = Manager(emp_id=103, name="Aditi", dept="Engg.")
print(type(manager))
# %%
manager.emp_id
# %%
manager.name
# %%
manager.dept
# %%
manager.get_department()
# %%
manager.get_details()
# %%
manager.get_details()
manager.get_department()
# %%
director = Director(
    emp_id=102, name="John", dept="Sales", region="Asia"
)
print(type(director))
# %%
director.emp_id
# %%
director.name
# %%
director.dept
# %%
director.region
# %%
director.get_details()
# %%
director.get_department()
# %%
director.get_all_info()
# %% [markdown]
"""
## 3. Hierarchical Inheritance
"""
# %%
from abc import ABC, abstractmethod
# %%
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        print(f"Perimeter : {self.perimeter():.2f}")
        print(f"Area : {self.area():.2f}") 

# %%
class Rectangle2(Shape):

    def __init__(self, width: int|float, height: int|float):
        super().__init__()
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def area(self):
        return self.width * self.height

# %%
class Circle2(Shape):

    def __init__(self, radius: int | float):
        super().__init__()
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
        
# %%
shapes2: list[Shape] = [
    Rectangle2(width= 20, height=15),
    Circle2(radius=20),
    Circle2(radius=14),
    Rectangle2(width=5, height=3),
    Circle2(radius=15)
]
print(shapes2)
# %%
for shape in shapes2:
    print(type(shape))
    shape.describe()
# %%
r1 = Rectangle2(width=5, height=3)
r1.describe()
# %%
c1 = Circle2(radius=11.5)
c1.describe()

# %%
