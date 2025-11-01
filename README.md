# ЛР1

## Задание 1
```python
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age+1}.")
```
![Task 1](../python_labs/images/lab01/01.png)

## Задание 2
```python
a = input("a: ")
b = input("b: ")
a = a.replace(',','.')
b = b.replace(',','.')
a = float(a)
b = float(b)
sum = a+b
avg = (a+b)/2
print(f"sum={sum:.2f}; avg={avg:.2f}")
```
![Task 2](../python_labs/images/lab01/02.png)

## Задание 3
```python
price = int(input("Исходная цена: "))
discount = int(input("Скидка: "))
vat = int(input("НДС: "))

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(f"База после скидки: {base:.2f} ₽")
print(f"НДС: {vat_amount:.2f} ₽")
print(f"Итого к оплате: {total:.2f} ₽")
```
![Task 3](../python_labs/images/lab01/03.png)

## Задание 4
```python
m = int(input("Минуты: "))
hours = m // 60
minutes = m % 60
print(f"{hours}:{minutes:02d}")
```
![Task 4](../python_labs/images/lab01/04.png)

## Задание 5
```python
fio = input("ФИО: ")
nospaces = " ".join(fio.strip().split())
length = len(nospaces)
words = fio.strip().split()
initials = "".join(word[0].upper() for word in words)
print(f"Инициалы: {initials}.")
print(f"Длина (символов): {length}")
```
![Task 5](../python_labs/images/lab01/05.png)


# ЛР2

## Задание 1
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError
    return (min(nums), max(nums))

print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
try:
    min_max([])
except ValueError:
    print("ValueError")
print(min_max([1.5, 2, 2.0, -3.1]))
```
![Task 1.1](../python_labs/images/lab02/01_1.png)

```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
```
![Task 1.2](../python_labs/images/lab02/01_2.png)

```python
def flatten(mat: list[list | tuple]) -> list:
    result = []
    for row in mat:
        if isinstance(row, (list, tuple)):
            result.extend(row)
        else:
            raise TypeError
    return result

print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
try:
    flatten([[1, 2], "ab"])
except TypeError:
    print("TypeError")
```
![Task 1.3](../python_labs/images/lab02/01_3.png)

## Задание B
```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    if not all(len(row) == len(mat[0]) for row in mat):
        raise ValueError
    num_rows = len(mat)
    num_cols = len(mat[0])
    return [[mat[r][c] for r in range(num_rows)] for c in range(num_cols)]

print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
try:
    print(transpose([[1, 2], [3]]))
except ValueError:
    print("ValueError")
print()
```

![Task 2.1](../python_labs/images/lab02/02_1.png)

```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not all(len(row) == len(mat[0]) for row in mat if mat):
        raise ValueError
    return [sum(row) for row in mat]

print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
try:
    print(row_sums([[1, 2], [3]]))
except ValueError:
    print("ValueError")
print()
```

![Task 2.2](../python_labs/images/lab02/02_2.png)

```python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat or not all(len(row) == len(mat[0]) for row in mat):
        raise ValueError
    num_cols = len(mat[0])
    return [sum(mat[r][c] for r in range(len(mat))) for c in range(num_cols)]

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
try:
    print(col_sums([[1, 2], [3]]))
except ValueError:
    print("ValueError")
```

![Task 2.3](../python_labs/images/lab02/02_3.png)

## Задание C
```python
def format_record(rec: tuple[str, str, float]) -> str:
    if len(rec) != 3:
        raise TypeError
    fio, group, gpa = rec
    if not isinstance(gpa, float):
        raise TypeError
    fio = fio.strip()
    group = group.strip()
    if not fio:
        raise ValueError
    if not group:
        raise ValueError

    name_parts = [part.strip() for part in fio.split() if part.strip()]
    if len(name_parts) < 2:
        raise ValueError
    surname = name_parts[0].title()
    initials = '.'.join(part[0].upper() for part in name_parts[1:]) + '.'
    formatted_fio = f"{surname} {initials}"

    gpa_formatted = f"{gpa:.2f}"
    return f"{formatted_fio}, гр. {group}, GPA {gpa_formatted}"

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
try:
    print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
except ValueError:
    print("ValueError")
```

![Task 3.1](../python_labs/images/lab02/03_1.png)


# ЛР3

## Задание A
```python
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = re.sub(r'[\t\r\n]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка",yo2e=True))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
```

![Task 1.1](../python_labs/images/lab03/01_1.png)

```python
import re

def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*', text)

print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
```

![Task 1.2](../python_labs/images/lab03/01_2.png)

```python
import re

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] = 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = list(freq.items())
    items.sort(key=lambda x: (-x[1], x[0]))
    return items[:n]

print(count_freq(["a","b","a","c","b","a"]))
print(top_n(count_freq(["a","b","a","c","b","a"]), 2))
print(count_freq(["bb","aa","bb","aa","cc"]))
print(top_n(count_freq(["bb","aa","bb","aa","cc"]), 2))
```

![Task 1.3](../python_labs/images/lab03/01_3.png)

## Задание B

```python
from python_labs.src.lib.text import normalize, tokenize, count_freq, top_n

text = ''
try:
    while True:
        text += input() + ' '
except EOFError:
    pass

normalized = normalize(text)
tokens = tokenize(normalized)
freq = count_freq(tokens)

total = len(tokens)
unique = len(freq)

print(f"Всего слов: {total}")
print(f"Уникальных слов: {unique}")
print("Топ-5:")
for word, count in top_n(freq, 5):
    print(f"{word}:{count}")
```

![Task 2.1](../python_labs/images/lab03/02_1.png)
