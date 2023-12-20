file_path = input("Введите путь до файла: ")
offset = int(input("Введите сдвиг: "))
lang = input("Введите язык: ")

try:
    f_in = open(file_path, "r", encoding = "utf-8")
    f_out = open("python_labs\labs\output.txt", "w", encoding = "utf-8")
    full_text = f_in.read()

    if lang.lower() in ["en", "eng"]:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
    elif lang.lower() in ["ru", "rus"]:
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    for symb in full_text:
        if symb.lower() in alphabet:
            res = alphabet[(alphabet.index(symb.lower()) + offset) % len(alphabet)]
            if symb.isupper():
                res = res.upper()
        else:
            res = symb
        f_out.write(res)

    f_in.close()
    f_out.close()

except Exception as e:
    print(e)