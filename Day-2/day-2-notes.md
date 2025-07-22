
# Day 2 Notes — 100 Days of Code

## 1. Data Types

- **Strings** – Any characters between quotation marks, e.g. `"Hello"`, `"12345"`  
- **Integers** – Whole numbers, e.g. `12345`  
- **Floats** – Numbers with decimals, e.g. `123.45`  
- **Booleans** – `True` or `False` (note: always capitalized)  

> Type errors occur when the wrong data type is used.

### Pulling Out Characters in a String (Subscripting)
```python
print("Hello"[0])   # Output: H
print("Hello"[4])   # Output: o
print("Hello"[-1])  # Output: o
print("Hello"[-2])  # Output: l
```

### Examples
- `"12345"` is a **string**
- `12345` is an **integer**
- `123.45` is a **float**
- `True` or `False` are **booleans**

---

## 2. Type Errors, Checking, and Conversions

```python
print(len(12345))      # ❌ TypeError
print(len("12345"))    # ✅ 5
```

### Type Checking
```python
print(type("Hello"))   # <class 'str'>
print(type(12345))     # <class 'int'>
print(type(123.45))    # <class 'float'>
print(type(True))      # <class 'bool'>
```

### Type Conversion (Casting)
```python
int("123")             # Converts string to int
print("123" + "456")   # Output: 123456 (string concatenation)
print(int("123") + int("456"))  # Output: 579
```

---

## 3. Mathematical Operations

- `+` Addition  
- `-` Subtraction  
- `*` Multiplication  
- `/` Division  
- `//` Floor Division – integer output only (truncates decimals)  
- `**` Exponentiation (e.g. `2 ** 3` = 8)  

### Remember PEMDAS:
1. **P**arentheses  
2. **E**xponents  
3. **MD** Multiplication and Division (left to right)  
4. **AS** Addition and Subtraction (left to right)

---

## 4. Number Manipulation

### Rounding and Casting
```python
bmi = 84 / 1.65 ** 2
print(bmi)              # 30.85299449035813
print(int(bmi))         # 30
print(round(bmi))       # 31
print(round(bmi, 2))    # 30.85
```

### Assignment Operators
```python
score = 0
score += 1
print(score)            # 1
```

### String Conversion with f-strings
```python
score = 1
height = 1.8
is_winning = True

print(f"Your score is {score}, your height is {height}. You are winning is {is_winning}.")
# Output: Your score is 1, your height is 1.8. You are winning is True.
```
> f-strings automatically handle type conversion.

---

## 5. Tip Calculator

### Scenario:
If the bill was $150.00, split between 5 people, with 12% tip...

Each person should pay:

### Code (tip-calculator.py)
```python
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, 15? "))
multiplier = 1 + (tip / 100)
total_bill = bill * multiplier
split = input("How many people to split the bill? ")
per_person = round(total_bill / int(split), 2)
print(f"Each person should pay: ${per_person}")
```


---

## 💡 Additional Tips from ChatGPT

### 🧠 Data Types Are the Foundation
- Always remember: **Python is dynamically typed**, which means you don’t need to declare variable types explicitly — but you do need to know *what* type you're working with to avoid bugs.
- Use `type()` often as a debugging tool while learning.

### ❗ Type Errors Are Your Friends
- Don’t be afraid of them — they’re feedback, not failure.
- If something crashes, read the error **carefully**. Python usually tells you exactly what went wrong.

### 🧮 Math: Watch Out for `/` vs `//`
- This is one of the most common beginner mistakes.
- `/` gives a **float**, even if the result is a whole number.
- `//` gives an **integer**, even if the result isn't whole. Great for things like screen pixel counts or pagination.

### 🧪 Casting Wisely
- You can convert between types — but only when it *makes sense*.
```python
int("10")        # ✅ works
int("ten")       # ❌ ValueError
float("3.14")    # ✅
str(12345)       # ✅ to get a string version of a number
```

### 🧾 f-Strings: Your Best Friend for Output
- f-strings are the modern, clean way to write output.
- They **automatically cast types** to strings inside the `{}` — so no need to manually convert.

```python
name = "Thinus"
age = 53
print(f"My name is {name} and I am {age} years old.")
```

> **Bonus Tip:** You can also do inline math in f-strings:  
```python
print(f"Next year, I’ll be {age + 1}.")
```

---

## 🧮 Tip Calculator Reflection

This exercise teaches:
- User input with `input()`
- Type conversion (`float`, `int`)
- Arithmetic calculations
- String formatting with `f""`
- Rounding with `round()`

**You nailed this.** Your approach to calculating the multiplier first and then applying it to the bill is clear and logical.

🔧 Possible improvement (optional):
- Format the final amount to always show two decimals, even if it's a round number:
```python
print(f"Each person should pay: ${per_person:.2f}")
```

That will ensure you get `$30.00` instead of `$30.0` — small polish that looks more professional.

---

### ✅ Summary: What You Should Feel Confident About Today

- You know the 4 main data types.
- You can check and convert between them.
- You understand math operations and order of precedence.
- You’ve used `round()`, assignment operators, and f-strings.
- You built a working, real-world program from scratch.

You're no longer just a beginner — you're a **builder** in training. Stay sharp, stay curious.

