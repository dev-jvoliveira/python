def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n = int(input("Digite um número para gerar os primeiros n números da sequência de Fibonacci: "))

if n <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    fibonacci_sequence = fibonacci(n)
    print(f"Os primeiros {n} números da sequência de Fibonacci são: {fibonacci_sequence}")
