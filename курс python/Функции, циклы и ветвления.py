def main():
    n = int(input("Введите размер списка: "))
    numbers = []
    
    print("Введите числа:")
    for i in range(n):
        num = int(input(f"{i + 1}: "))
        numbers.append(num)
    
    max_num = max(numbers)  
    min_num = min(numbers)  
    total_sum = sum(numbers)  
    
    sorted_numbers = sorted(numbers)
    
    print("Самое большое число:", max_num)
    print("Самое маленькое число:", min_num)
    print("Сумма чисел в ряду:", total_sum)
    print("Отсортированный список):", sorted_numbers)

main()