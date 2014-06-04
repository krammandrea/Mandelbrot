from django.test import TestCase


# Create your tests here.

class TestAlgorithm(TestCase):
    def test_basics(self):
        import algorithmWithNumPy
        algorithmWithNumPy.calculate_mandelbrot()
