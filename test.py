import unittest
import tempfile

from main import analyze_sales_data


# Тест функции analyze_sales_data
class TestAnalyzeSalesData(unittest.TestCase):
    def test_analyze_sales_data(self):
        data = """2023-09-19,10:15:32,Electronics,Laptop,1200.00
2023-09-19,10:16:45,Clothing,T-shirt,25.50
2023-09-19,10:17:01,Food,Pizza,15.99"""


        with tempfile.NamedTemporaryFile(delete=False, mode='w') as tmpfile:
            tmpfile.write(data)

        expected_result = {
            'date': '2023-09-19',
            'time': '10:15:32',
            'category': 'Electronics',
            'name': 'Laptop',
            'price': 1200.00
        }

        result = analyze_sales_data(tmpfile.name)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
