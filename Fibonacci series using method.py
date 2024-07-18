def fibonacci(n):
    a, b = 0, 1
    fib_series = []
    
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b

    return fib_series

if __name__ == "__main__":
    num = int(input("Enter the number of Fibonacci numbers to generate: "))

    fib_series = fibonacci(num)

    print(f"The first {num} numbers in the Fibonacci series are:")
    print(", ".join(map(str, fib_series)))
