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


# ЛР4

## Задание A
```python
from pathlib import Path
import csv


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    path = Path(path)
    with open(path, "r", encoding=encoding) as file:
        return file.read()


def write_csv(
    rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    path = Path(path)
    ensure_parent_dir(path)
    if rows:
        first_row_length = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_row_length:
                raise ValueError(
                    f"Строка {i} имеет длину {len(row)}, ожидается {first_row_length}"
                )

    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)


def ensure_parent_dir(path: str | Path) -> None:
    path = Path(path)
    parent_dir = path.parent
    parent_dir.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":

    from io_txt_csv import read_text, write_csv

    write_csv([("word", "count"), ("test", 3)], "data/check.csv")
    try:
        txt = read_text("test_input.txt")
        print("Файл успешно прочитан")
    except FileNotFoundError:
        print("Файл test_input.txt не найден")
    except UnicodeDecodeError:
        print("Ошибка кодировки при чтении файла")
```

![Task 1.1](../python_labs/images/lab04/01_1.png)
![Task 1.2](../python_labs/images/lab04/01_2.png)

## Задание B
```python
import sys
import argparse
from pathlib import Path

from io_txt_csv import read_text, write_csv
from python_labs.src.lib.text import normalize, tokenize, count_freq, top_n


def generate_report(input_path: str, output_path: str, encoding: str = "utf-8") -> None:

    try:
        text = read_text(input_path, encoding)
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_path}' не найден")
        sys.exit(1)
    except UnicodeDecodeError as e:
        print(f"Ошибка кодировки: {e}")
        print("Попробуйте указать другую кодировку с помощью --encoding")
        sys.exit(1)

    normalized_text = normalize(text, casefold=True, yo2e=True)
    tokens = tokenize(normalized_text)
    frequencies = count_freq(tokens)
    sorted_words = sorted(frequencies.items(), key=lambda x: (-x[1], x[0]))

    header = ("word", "count")
    write_csv(sorted_words, output_path, header)
    total_words = len(tokens)
    unique_words = len(frequencies)

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")

    if unique_words > 0:
        top_5_words = top_n(frequencies, 5)
        print("Топ-5:")
        for i, (word, count) in enumerate(top_5_words, 1):
            print(f"  {i}. '{word}' - {count}")
    else:
        print("Топ-5: нет данных")

    print(f"Отчет сохранен в: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Генератор отчета по частотности слов в тексте"
    )
    parser.add_argument(
        "--in",
        dest="input_file",
        default="test_input.txt",
    )
    parser.add_argument(
        "--out",
        dest="output_file",
        default="data/report.csv",
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
    )

    args = parser.parse_args()
    generate_report(args.input_file, args.output_file, args.encoding)


if __name__ == "__main__":
    main()
```

![Task 2.1](../python_labs/images/lab04/02_1.png)
![Task 2.2](../python_labs/images/lab04/02_2.png)


# ЛР5

## Задание A
```python
import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8.
    Порядок колонок — как в первом объекте, дополнительные — в алфавитном порядке.
    """
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if not json_file.is_file():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")

    with json_file.open("r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Ошибка чтения JSON: {e}")

    if not data or not isinstance(data, list):
        raise ValueError(
            "Пустой JSON или неподдерживаемая структура: ожидается список словарей."
        )
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями.")

    first_keys = list(data[0].keys())
    all_keys = set(first_keys)
    for item in data[1:]:
        all_keys.update(item.keys())
    additional_keys = sorted(all_keys - set(first_keys))
    fieldnames = first_keys + additional_keys

    with csv_file.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            row = {key: item.get(key, "") for key in fieldnames}
            writer.writerow(row)


json_to_csv(f"C:/Users/arpik/PycharmProjects/PythonProject18/python_labs/data/lab05/samples/people.json", f"C:/Users/arpik/PycharmProjects/PythonProject18/python_labs/data/lab05/out/people_from_json.csv")


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    csv_file = Path(csv_path)
    json_file = Path(json_path)

    if not csv_file.is_file():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")

    with csv_file.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV файл не содержит заголовка.")
        data = list(reader)

    if not data:
        raise ValueError("CSV файл пуст.")

    with json_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


csv_to_json(f"C:/Users/arpik/PycharmProjects/PythonProject18/python_labs/data/lab05/samples/people.csv", f"C:/Users/arpik/PycharmProjects/PythonProject18/python_labs/data/lab05/out/people_from_csv.json")
```

![Task 1.1](../python_labs/images/lab05/01_1_1.png)
![Task 1.2](../python_labs/images/lab05/01_1_2.png)

![Task 1.3](../python_labs/images/lab05/01_2_1.png)
![Task 1.4](../python_labs/images/lab05/01_2_2.png)

## Задание B
```python
from openpyxl import Workbook
import csv
from pathlib import Path


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использует openpyxl.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    csv_file = Path(csv_path)
    xlsx_file = Path(xlsx_path)

    if not csv_file.is_file():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    with csv_file.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        raise ValueError("CSV файл пустой")

    for row in rows:
        ws.append(row)

    for col_idx, col_cells in enumerate(ws.columns, start=1):
        max_length = max(
            len(str(cell.value)) if cell.value is not None else 0 for cell in col_cells
        )
        adjusted_width = max(max_length, 8)
        col_letter = ws.cell(row=1, column=col_idx).column_letter
        ws.column_dimensions[col_letter].width = adjusted_width

    wb.save(xlsx_file)


csv_to_xlsx('C:/Users/arpik/PycharmProjects/PythonProject18/python_labs/data/lab05/samples/people.csv', 'C:/Users/arpik/PycharmProjects/PythonProject18/python_labs/data/lab05/out/people.xlsx')
```

![Task 2.1](../python_labs/images/lab05/01_2_1.png)
![Task 2.2](../python_labs/images/lab05/02_2.png)


# ЛР6

## Задание 1
```python
import  argparse
from python_labs.src.lib.text import *

def cat(text, n):
    f = open(text, "r").readlines()
    if not n:
        for i in f:
            print(i.replace("\n", ""))
    else:
        f = enumerate(f)
        for i in f:
            print(i[0],i[1].replace("\n", ""))


def stats(txt,n):
    f = open(txt, "r").read()
    txt = top_n(count_freq(tokenize(normalize(f))),n)
    for a in txt:
        print(a[1],a[0])



# def main():
parser = argparse.ArgumentParser("CLI‑утилиты лабораторной №6")
subparsers = parser.add_subparsers(dest="command")

# подкоманда cat
cat_parser = subparsers.add_parser("cat",help = "Вывести содержимое файла")
cat_parser.add_argument("--input",required = True)
cat_parser.add_argument("-n", action="store_true",help = "Нумировать строки")

# подкоманда stats
stats_parser = subparsers.add_parser("stats",help = "Частоты слез")
stats_parser.add_argument("--input",required = True)
stats_parser.add_argument("--top",type = int, default = 5)

args = parser.parse_args()
# print("DEBUG:", args)

if args.command == "cat":
    cat(args.input,args.n)

if args.command == "stats":
    stats(args.input,args.top)
```

![Task 1.1](../python_labs/images/lab06/01.png)


## Задание 2
```python
import argparse
from python_labs.src.lab05.csv_xlsx import csv_to_xlsx
from python_labs.src.lab05.json_csv import json_to_csv, csv_to_json



parser = argparse.ArgumentParser("CLI‑утилиты лабораторной №6")
subparsers = parser.add_subparsers(dest="command")

json2csv_parser = subparsers.add_parser("json2csv",help = "Первевести json в csv")
json2csv_parser.add_argument("--in",required=True,dest='input')
json2csv_parser.add_argument("--out",required=True)

csv2json_parser = subparsers.add_parser("csv2json", help = "Перевести csv в json")
csv2json_parser.add_argument("--in",required=True,dest='input')
csv2json_parser.add_argument("--out",required=True)

csv2xlsx_parser = subparsers.add_parser("csv2xlsx",help = "Первевести csv в xlsx")
csv2xlsx_parser.add_argument("--in",required=True,dest='input')
csv2xlsx_parser.add_argument("--out",required=True)

args = parser.parse_args()

if args.command == "json2csv":
    json_to_csv(args.input,args.out)
if args.command == "csv2json":
    csv_to_json(args.input,args.out)
if args.command == "csv2xlsx":
    csv_to_xlsx(args.input,args.out)

```

```python
python -m python_labs.src.lab06.cli_convert csv2xlsx --in "python_labs/data/lab05/samples/people.csv" --out "python_labs/data/lab06/out/people.xlsx"
```
![Task 2.1](../python_labs/images/lab06/02_1.png)

```python
python -m python_labs.src.lab06.cli_convert csv2json --in "python_labs/data/lab05/samples/people.csv" --out "python_labs/data/lab06/out/people_from_csv.json"
```
![Task 2.2](../python_labs/images/lab06/02_2.png)

```python
python -m python_labs.src.lab06.cli_convert json2csv --in "python_labs/data/lab05/samples/people.json" --out "python_labs/data/lab06/out/people.csv"
```
![Task 2.3](../python_labs/images/lab06/02_3.png)


# ЛР7

## Задание 1
```python
import pytest

from python_labs.src.lib.text import normalize, tokenize, count_freq, top_n


class TestText:

    @pytest.mark.parametrize(
        "input_text, expected",
        [
            ("Hello world", "hello world"),
            (" PYTHON  Programming  ", "python programming"),
            ("Test123", "test123"),
            ("", ""),
            ("  ", ""),
            ("Hello!!??", "hello!!??"),
            ("Привет Мир", "привет мир"),
            ("café", "café"),
        ],
    )
    def test_normalize(self, input_text, expected):
        assert normalize(input_text) == expected

    @pytest.mark.parametrize(
        "input_text, expected",
        [
            ("Hello world", ["Hello", "world"]),
            ("", []),
            ("hello, world!", ["hello", "world"]),
            ("Привет мир", ["Привет", "мир"]),
        ],
    )
    def test_tokenize(self, input_text, expected):
        assert tokenize(input_text) == expected

    @pytest.mark.parametrize(
        "tokens, expected",
        [
            (["hello", "world", "hello"], {"hello": 2, "world": 1}),
            ([], {}),
            (["a", "b", "a", "c", "c"], {"a": 2, "b": 1, "c": 2}),
        ],
    )
    def test_count_freq(self, tokens, expected):
        assert count_freq(tokens) == expected

    @pytest.mark.parametrize(
        "freq, n, expected",
        [
            ({"hello": 2, "world": 1}, 1, [("hello", 2)]),
            ({"a": 2, "b": 2, "c": 1}, 2, [("a", 2), ("b", 2)]),
            ({"x": 3, "y": 3, "z": 3}, 3, [("x", 3), ("y", 3), ("z", 3)]),
            ({}, 1, []),
        ],
    )
    def test_top_n(self, freq, n, expected):
        assert top_n(freq, n) == expected
```

![Task 1.1](../python_labs/images/lab07/01.png)


## Задание 2
```python
import json
import csv

from pathlib import Path
import pytest

from python_labs.src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == len(data)
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people_out.json"
    rows = [
        {"name": "Alice", "age": "22"},
        {"name": "Bob", "age": "25"},
    ]
    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(rows)

    csv_to_json(str(src), str(dst))

    data_out = json.loads(dst.read_text(encoding="utf-8"))

    assert len(data_out) == len(rows)
    assert all("name" in rec and "age" in rec for rec in data_out)


@pytest.mark.parametrize(
    "func, input_file, error",
    [
        ("json_to_csv", "invalid.json", ValueError),
        ("csv_to_json", "invalid.csv", ValueError),
    ],
)
def test_invalid_content_raises(func, input_file, error, tmp_path: Path):
    # Создаем файл с некорректным содержимым
    fpath = tmp_path / input_file
    fpath.write_text("this is not valid json or csv", encoding="utf-8")

    # Подготавливаем путь назначения
    dst = tmp_path / "out.file"

    # Выбираем функцию для теста
    f = json_to_csv if func == "json_to_csv" else csv_to_json

    with pytest.raises(error):
        f(str(fpath), str(dst))


@pytest.mark.parametrize("func", [json_to_csv, csv_to_json])
def test_file_not_found_raises(func, tmp_path: Path):
    non_existent_path = tmp_path / "no_such_file.non"
    dst = tmp_path / "out.file"
    with pytest.raises(FileNotFoundError):
        func(str(non_existent_path), str(dst))
```

![Task 2.1](../python_labs/images/lab07/02.png)


# ЛР8

## Задание 1
```python
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any


@dataclass
class Student:
    fio: str
    birthdate: str  # формат YYYY-MM-DD
    group: str
    gpa: float

    def __post_init__(self):
        # Валидация формата даты
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Некорректный формат даты рождения. Ожидается YYYY-MM-DD.")

        # Валидация диапазона GPA
        if not (0.0 <= self.gpa <= 5.0):
            raise ValueError("GPA должен быть в диапазоне от 0.0 до 5.0.")

    def age(self) -> int:
        """Возвращает количество полных лет."""
        today = datetime.today()
        birth = datetime.strptime(self.birthdate, "%Y-%m-%d")
        age = today.year - birth.year
        if (today.month, today.day) < (birth.month, birth.day):
            age -= 1
        return age

    def to_dict(self) -> Dict[str, Any]:
        """Сериализация объекта в словарь."""
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Student":
        """Десериализация: создаёт объект из словаря."""
        return cls(**data)

    def __str__(self) -> str:
        return f"Студент: {self.fio}, Группа: {self.group}, Возраст: {self.age()}, GPA: {self.gpa:.2f}"
```



## Задание 2
```python
import json
from pathlib import Path
from typing import List
from python_labs.src.lab08.models import Student


def students_to_json(students: List[Student], path: str) -> None:
    """Сохраняет список студентов в JSON-файл."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump([s.to_dict() for s in students], f, ensure_ascii=False, indent=4)


def students_from_json(path: str) -> List[Student]:
    """Читает JSON-файл и возвращает список объектов Student."""
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")

    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Ошибка при разборе JSON: {e}")

    if not isinstance(data, list):
        raise ValueError("Ожидался JSON-массив.")

    students = []
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Каждый элемент массива должен быть объектом.")
        students.append(Student.from_dict(item))

    return students


students = students_from_json("C:/Users/arpik/PycharmProjects/PythonProject18/python_labs/data/lab08/samples/students_input.json")


for s in students:
    print(s)

students_to_json(students, "C:/Users/arpik/PycharmProjects/PythonProject18/python_labs/data/lab08/out/students_output.json")
print("Файл students_output.json успешно создан!")
```

![Task 2.1](../python_labs/images/lab08/01.png)
![Task 2.2](../python_labs/images/lab08/02.png)
![Task 2.3](../python_labs/images/lab08/03.png)





