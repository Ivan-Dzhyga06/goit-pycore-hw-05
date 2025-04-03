# ФУНКЦІЯ caching_fibonacci
def caching_fibonacci():
    # Створюємо порожній словник cache
    cache = {}
    # ФУНКЦІЯ fibonacci(n)
    def fibonacci(n):
        # Якщо n <= 0, повернути 0
        if n <= 0:
            return 0
        # Якщо n == 1, повернути 1
        elif n == 1:
            return 1
        # Якщо n у cache, повернути cache[n]
        if n in cache:
            return cache[n] 
        
        # Запис результатів в словник cache    
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        # Повертаємо словник cache
        return cache[n]
    # Повертаємо функцію fibonacci
    return fibonacci
# Кінець функції caching_fibonacci    
        
# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
