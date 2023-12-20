import logging

def next_row(row):
    row = [1] + row
    for i in range(1, len(row)-1):
        row[i] += row[i+1]
    return row

try:
    input_str = input("Введите целое число n: ")
    n = int(input_str)

    if n<=0:
        raise ValueError(f"Expeceted n>0. Actual n<0: {n}")
    
    arr=[]
    for i in range(n):
        arr = next_row(arr)
        print(arr)

except ValueError as err:
    logging.error(err)