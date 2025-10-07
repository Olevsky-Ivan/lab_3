def percent_func(ls: list):
    if not ls:
        return 0
    count_percent = 0
    for number in ls:
        str_num = str(number)
        sum_ = sum(int(i) for i in str_num)
        if sum_ > 10:
            count_percent += 1
    return (count_percent / len(ls)) * 100


numbers = []
while True:
    n = int(input("Введіть число (0 для завершення): "))
    if n == 0:
        break
    numbers.append(n)

print(f"Відсоток чисел з сумою цифр > 10: {percent_func(numbers)}%")

def percent_func_digit():
    total = 0
    count = 0
    while True:
        n = input("Введіть число (0 для завершення): ")
        if n == "0":
            break
        total += 1
        s = sum(int(i) for i in n if i.isdigit())
        if s > 10:
            count += 1
    if total > 0:
        percent = (count / total) * 100
        print(f"Відсоток чисел з сумою цифр більшою за 10: {percent}%")
    else:
        print("Жодного числа не було введено.")
