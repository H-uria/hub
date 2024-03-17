def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Initialize the Fibonacci sequence with the first two terms

    # Generate the Fibonacci sequence up to the nth term
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence

def main():
    while True:
        try:
            n = int(input("Enter the value of n: "))  # Ask the user to input the value of n
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            fibonacci_sequence = generate_fibonacci(n)  # Generate the Fibonacci sequence
            print("Fibonacci sequence up to term", n, ":", fibonacci_sequence)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
