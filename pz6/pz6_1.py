def fibonacci_sequence(n):
    fibonacci = [1, 1]
    for i in range(2, n):
        next_fib = fibonacci[-2] + fibonacci[-1]
        fibonacci.append(next_fib)
    return fibonacci

fibonacci_list = fibonacci_sequence(10)
print(fibonacci_list)
