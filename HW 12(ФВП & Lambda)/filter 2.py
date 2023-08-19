a = ["world", "hello", "3243", "potato", "carrot", "hi"]
b = list(filter(lambda x: len(x) > 4, a))
print(b)

# ['world', 'hello', 'potato', 'carrot'] - Только слова где ДЛИНА больше 4 символов

# ----------------------------------------------------------------------------------------

a = "432jfdsHFDS343f"
b = list(filter(str.isupper, a))

print(b)
# ['H', 'F', 'D', 'S']

# ----------------------------------------------------------------------------------------

a = "432jfdsHFDS343f"
b = list(filter(str.isdigit, a))

print(b)
# ['4', '3', '2', '3', '4', '3']

# ISDIGIT - только ЦИФРЫ

# ----------------------------------------------------------------------------------------

a = "432jfdsHFDS343f"
b = list(filter(str.isalpha, a))

print(b)
# ['j', 'f', 'd', 's', 'H', 'F', 'D', 'S', 'f'] 

# ISAPHA - только БУКВЫ


d = {
    "moscow": 800,
    "boston": 700,
    "LA": 400,
    "SF": 900,
    "Chicago": 650,
    "SP": 600,
}

b = list(filter(lambda x: d[x] > 700, d))

print(b)
# ['moscow', 'SF']
