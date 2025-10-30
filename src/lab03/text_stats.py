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