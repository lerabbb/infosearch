def check(str):
    counter = 0
    for c in str:
        if c=="(":
            counter+=1
        else:
            counter-=1    
    return counter==0


input_str = input("Введите скобочную последовательность: ")

if check(input_str):
    print("Правильная последовательность")
else:
    print("Неправильная последовательность")