import unittest
import time, math
import itertools

def generate_permutations(elements):
    for permutation in itertools.permutations(elements):
        yield permutation

def countdown_timer(seconds):
    if seconds< 0:
        raise ValueError("Time should not be negative")
    seconds = math.floor(seconds)
    while seconds >= 0:
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        yield f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        time.sleep(1)
        seconds -= 1
        
def fibonacci_generator():
    # Initialize variables for the first two Fibonacci numbers
    a, b = 0, 1
    # Yield the first two Fibonacci numbers
    yield a
    yield b
    # Generate subsequent Fibonacci numbers indefinitely
    while True:
        # Compute the next Fibonacci number
        a, b = b, a + b
        yield b
        
class TestCountdownTimer(unittest.TestCase):
    def test_output_format(self):
        # Test whether the output format of the countdown timer matches the expected format
        for time_str in countdown_timer(12):  # Run for a short sequence
            self.assertRegex(time_str, r"\d{2}:\d{2}:\d{2}", msg="Output format should be HH:MM:SS")

    def test_basic_functionality(self):
        # Test the basic functionality of the countdown timer for a short sequence from 12 seconds
        expected_output = [
            "00:00:12", "00:00:11", "00:00:10",
            "00:00:09", "00:00:08", "00:00:07",
            "00:00:06", "00:00:05", "00:00:04",
            "00:00:03", "00:00:02", "00:00:01", "00:00:00"
        ]
        actual_output = [time_str for time_str in countdown_timer(12)]
        self.assertEqual(actual_output, expected_output)

    def test_edge_cases(self):
        # Test edge cases such as zero seconds, non integer seconds, and negative seconds
        expected_output = ["00:00:00"]
        actual_output = [time_str for time_str in countdown_timer(0)]
        self.assertEqual(actual_output, expected_output)
        
        expected_output = ["00:00:01", "00:00:00"]
        actual_output = [time_str for time_str in countdown_timer(1.49)]
        self.assertEqual(actual_output, expected_output)
        edge_cases = [-5, -3.5]
        for seconds in edge_cases:
            with self.assertRaises(ValueError):
                for _ in countdown_timer(seconds):
                    pass

class TestFibonacciGenerator(unittest.TestCase):
    def test_first_20_fibonacci_numbers(self):
        # Generate the first 20 Fibonacci numbers
        expected_fibonacci_numbers = []
        fibonacci_gen = fibonacci_generator()
        for _ in range(20):  # Generate 20 Fibonacci numbers
            expected_fibonacci_numbers.append(next(fibonacci_gen))
        
        # Expected first 20 Fibonacci numbers
        known_fibonacci_numbers = [
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
            55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181
        ]
        
        # Compare generated Fibonacci numbers with known Fibonacci numbers
        self.assertEqual(expected_fibonacci_numbers, known_fibonacci_numbers)

    def test_next_10_fibonacci_numbers_21_to_30(self):
        # Generate the next 10 Fibonacci numbers (21-30)
        expected_fibonacci_numbers = []
        fibonacci_gen = fibonacci_generator()
        for _ in range(20):  # Generate 20 Fibonacci numbers to reach the 21st number
            next(fibonacci_gen)
        for _ in range(10):  # Generate 10 more Fibonacci numbers
            expected_fibonacci_numbers.append(next(fibonacci_gen))
        
        # Expected next 10 Fibonacci numbers (21-30)
        known_fibonacci_numbers = [
            6765, 10946, 17711, 28657, 46368,
            75025, 121393, 196418, 317811, 514229
        ]
        
        # Compare generated Fibonacci numbers with known Fibonacci numbers
        self.assertEqual(expected_fibonacci_numbers, known_fibonacci_numbers)

    def test_next_10_fibonacci_numbers_31_to_40(self):
        # Generate the next 10 Fibonacci numbers (31-40)
        expected_fibonacci_numbers = []
        fibonacci_gen = fibonacci_generator()
        for _ in range(30):  # Generate 30 Fibonacci numbers to reach the 31st number
            next(fibonacci_gen)
        for _ in range(10):  # Generate 10 more Fibonacci numbers
            expected_fibonacci_numbers.append(next(fibonacci_gen))
        
        # Expected next 10 Fibonacci numbers (31-40)
        known_fibonacci_numbers = [
            832040, 1346269, 2178309, 3524578, 5702887,
            9227465, 14930352, 24157817, 39088169, 63245986
        ]
        
        # Compare generated Fibonacci numbers with known Fibonacci numbers
        self.assertEqual(expected_fibonacci_numbers, known_fibonacci_numbers)
        
if __name__ == "__main__":
    unittest.main()
    
    # example of using Fibonacci number generator
    fibonacci_numbers = []
    fibonacci_gen = fibonacci_generator()
    for _ in range(100):
        fibonacci_numbers.append(next(fibonacci_gen))
    print ("The list of first 100 Fibonacci numbers:")
    print(fibonacci_numbers)
    
    # example of how the countdown timer works
    print("Countdown timer demo")
    for time_str in countdown_timer(9):
        print(time_str)
    print("Wake up!")
        
    # example of using permutation generator
    elements = ['a', 'b', 'c', 'd'] # or use: elements = 'abcd'
    permutation_generator = generate_permutations(elements)
    print("Permutation generator demo")
    counter = 0
    for permutation in permutation_generator:
        print(permutation)
        counter += 1
    print("The number of permutations is %s" %counter)