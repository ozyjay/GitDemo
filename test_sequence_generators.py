from unittest import TestCase


class Test(TestCase):
    def test_fibonacci(self):
        from sequence_generators import fibonacci

        # the fib of 1 is 1
        result = fibonacci(1)
        self.assertEqual(result, 1)

        # the fib of 2 is 1
        result = fibonacci(2)
        self.assertEqual(result, 1)

        # the fib of 3 is 2
        result = fibonacci(3)
        self.assertEqual(result, 2)

    def test_factorial(self):
        from sequence_generators import factorial

        result = factorial(1)
        self.assertEqual(result, 1)

        result = factorial(2)
        self.assertEqual(result, 2)

        result = factorial(3)
        self.assertEqual(result, 6)
