# 100 Days of Code: Day 1 Notes

## 1. Print Statement

```python
print("Hello World!")
```

- `"Hello World!"` is a **string**.
- Check for **syntax highlighting** in your editor and be aware of **syntax errors**.
- PyCharm will point out errors as you code.
- Observe differences in colours and error messages.

---

## 2. String Manipulation

To move to a new line within a string, use `\n`.

Example:

```python
print("Hello World!\nHello World!\nHello World!")
```

Output:

```
Hello World!
Hello World!
Hello World!
```

> See: `string-manipulation.py`

### Concatenation (Joining Strings)

Combine two or more strings:

```python
print("Hello " + "Thinus")
# Output: Hello Thinus
```

Take note of the space in `"Hello "`.

This can also be achieved using:

```python
print("Hello" + " " + "Thinus")
```

or

```python
print("Hello" + " Thinus")
```

> See: `concatenation.py`

Be careful with **spaces** and **tabs** to avoid indentation errors.

---

## 3. Input Function

```python
print("Hello " + input("What is your name?") + "!")
```

If the input is `Thinus`, the output will be:

```
Hello Thinus!
```

> See: `input.py`

**Note:** Use [Stack Overflow](https://stackoverflow.com) and [W3Schools](https://www.w3schools.com) for reference.

---

## 4. Variables

Variables allow us to **store values** in containers for later use. A variable gives a **label** to a piece of data.

Example:

```python
name = input("What is your name?")
print("Hello " + name + "!")
print(len(name))
```

> See: `variables.py`

---

## 5. Variable Naming Rules

- Use **descriptive** variable names.
- **No spaces** between words.
- **Do not start** variable names with numbers.
- Avoid using **reserved words** like `print` or `input` as variable names.
- Choose **simple** words to minimize typos.
- Follow **company style guides** when working in a professional environment.

---

## ✅ Day 1 Best Practices & Reminders

### 🧠 Mindset Tips
- Learning to code is like learning a language — repetition matters.
- Don’t worry if you don’t understand everything at once. Each concept will build on the last.

### 🧹 Clean Code Habits Start Now
- Use consistent indentation (**4 spaces** is standard in Python).
- Use blank lines to separate sections of code to improve readability.

### 🔍 Debugging Early
- If something doesn’t work, **read the error message slowly** — it's usually telling you what went wrong.
- Try commenting out code with `#` to isolate problems.

### 📁 Organize Your Files

Keep your Day 1 folder structured like this for clarity and future reference:

```
Day-1/
├── bandname-generator.py
├── concatenation.py
├── hello-world.py
├── input.py
├── string-manipulation.py
├── variables.py
└── day1-notes.md
```
