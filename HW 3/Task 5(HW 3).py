user_input = str(input("Введите текст: "))
text = user_input[1:-1]

change = "*" + text + "*"
# VN: наоборот, нужно зацензурить середину слова, а парвую и последнюю буквы оставить нетронутыми

print(change)
