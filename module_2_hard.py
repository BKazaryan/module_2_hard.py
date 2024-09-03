def code(numbers):
    result = []
    for i in range(1, numbers + 1):
        for j in range(i + 1, numbers + 1):
            sum_ = i + j
            if numbers % sum_ == 0:
                result.append(i)
                result.append(j)
    return result

n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    result = code(n)
    print("Нужный пароль:",*result)
else:
    print("Число должно быть в диапазоне от 3 до 20.")