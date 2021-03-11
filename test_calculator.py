import calculator as calc


class TestCalculator:

    def test_add(self):
        assert 6 == calc.add(1, 5)

    def test_subtract(self):
        assert 2 == calc.subtract(4, 2)
        