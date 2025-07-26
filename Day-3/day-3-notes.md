
# 🧠 Day 3 – Conditional Logic in Python

## ✅ 1. Conditional Statements (`if` / `else`)

Conditional statements allow your program to **make decisions** and **execute different code blocks based on conditions**.

```python
if condition:
    do_this
else:
    do_that
```

- Indentation is **critical** in Python. It defines what code belongs to which block.
- Example:

```python
if height > 120:
    print("You can ride the rollercoaster.")
else:
    print("Sorry, you need to grow taller.")
```

---

## 🔁 2. Comparison Operators

These operators are used to compare values in conditions:

| Operator | Meaning               |
|----------|------------------------|
| `>`      | Greater than           |
| `<`      | Less than              |
| `>=`     | Greater than or equal  |
| `<=`     | Less than or equal     |
| `==`     | Equal to               |
| `!=`     | Not equal to           |

---

## ➗ 3. The Modulo Operator (`%`)

- The **modulo operator** returns the **remainder** after division.
- Examples:

```python
10 % 5  # Returns 0 → 10 is evenly divisible by 5
10 % 3  # Returns 1 → 3 goes into 10 three times with 1 leftover
```

Great for checking things like **even/odd numbers**, or if something is divisible by a number.

---

## 🧱 4. Nesting and `elif`

### Nesting `if` inside another `if`:

```python
if condition:
    if another_condition:
        do_this
    else:
        do_that
else:
    do_something_else
```

### `if` / `elif` / `else` structure:

```python
if condition1:
    do_this
elif condition2:
    do_that
else:
    do_something_else
```

- `elif` stands for **"else if"**.
- Python evaluates conditions **in order**, and **only the first true condition runs**.

---

## 🔗 5. Logical Operators

Used to combine multiple conditions:

| Operator | Meaning                       |
|----------|-------------------------------|
| `and`    | Both conditions must be true  |
| `or`     | At least one must be true     |
| `not`    | Inverts the condition (i.e., "not true" means false) |

### Example:

```python
if age >= 18 and height >= 120:
    print("You can ride!")
```

---


