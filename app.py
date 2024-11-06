import math
from flask import Flask, render_template

app = Flask(__name__, template_folder='html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/A1G', methods=['GET'])
def pure_function():
    def calculate_area(radius):
        return math.pi * radius * radius
    area = calculate_area(3)
    return render_template('task.html', title="A1G", result=f'Ein Kreis mit einem Radius von: '
                                                            f'{round(math.sqrt(area/math.pi), 2)},'
                                                            f'\ngibt es eine Fläche von: {round(area, 2)}')

@app.route('/A1F', methods=['GET'])
def immutable_example():
    student_info = [
        ('Alice', 20, 1),
        ('Bob', 22, 2),
        ('Charlie', 19, 3)
    ]
    result = "Studenten Informationen:\n"
    for student in student_info:
        name, age, student_id = student
        result += f"Name: {name}, Alter: {age}, ID: {student_id}\n"

    return render_template('task.html', title="A1F", result=result)


import math
from cmath import sqrt
from flask import Flask, render_template

app = Flask(__name__, template_folder='html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/A1G', methods=['GET'])
def pure_function():
    def calculate_area(radius):
        return math.pi * radius * radius
    area = calculate_area(3)
    return render_template('task.html', title="A1G", result=f'Bei einem Kreis mit einem Radius von: '
                                                            f'{round(math.sqrt(area/math.pi), 2)},'
                                                            f'\ngibt es eine Fläche von: {round(area, 2)}')

@app.route('/A1F', methods=['GET'])
def immutable_example():
    student_info = [
        ('Alice', 20, 1),
        ('Bob', 22, 2),
        ('Charlie', 19, 3)
    ]
    result = "Studenten Informationen:\n"
    for student in student_info:
        name, age, student_id = student
        result += f"Name: {name}, Alter: {age}, ID: {student_id}\n"

    return render_template('task.html', title="A1F", result=result)


@app.route('/A1E', methods=['GET'])
def compare_concepts():
    # Objektorientierte Programmierung (OO)
    def oo_factorial(number):
        class FactorialCalculator:
            def __init__(self, number):
                self.number = number

            def calculate(self):
                result = 1
                for i in range(1, self.number + 1):
                    result *= i
                return result
        calculator = FactorialCalculator(number)
        return calculator.calculate()

    # Prozedurale Programmierung
    def procedural_factorial(number):
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result

    # Funktionale Programmierung
    def functional_factorial(number):
        return 1 if number == 0 else number * functional_factorial(number - 1)

    # Berechnungen mit den jeweiligen Funktionen
    oo_result = oo_factorial(5)  # Beispiel: 5! = 120
    procedural_result = procedural_factorial(5)  # Beispiel: 5! = 120
    functional_result = functional_factorial(5)  # Beispiel: 5! = 120

    # Erklärungen und Unterschiede im Return
    result = f'''
    def oo_factorial(number):
        class FactorialCalculator:
            def __init__(self, number):
                self.number = number

            def calculate(self):
                result = 1
                for i in range(1, self.number + 1):
                    result *= i
                return result


    def procedural_factorial(number):
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result


    def functional_factorial(number):
        return 1 if number == 0 else number * functional_factorial(number - 1)
        
        
    Ergebnis: {functional_result}
    '''

    return render_template('task.html', title="A1E - Fibonacci Algorithmus", result=result)


@app.route('/B1G', methods=['GET'])
def fibonacci_algorithm():
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    n = 5
    fibonacci_result = fibonacci(n)
    result = f"Das {n}. Fibonacci-Zahl ist: {fibonacci_result}"

    return render_template('task.html', title="B1G - Fibonacci Algorithmus", result=result)


@app.route('/B1F', methods=['GET'])
def split_algorithm():
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    return {'fibonacci': fibonacci(5)}

@app.route('/B1E', methods=['GET'])
def combined_algorithm():
    def total_calories(exercises):
        return sum(exercises)
    return {'total_calories': total_calories([200, 300, 150])}

@app.route('/B2G', methods=['GET'])
def function_as_object():
    def greet(name):
        return f'Hello, {name}!'
    greeting_function = greet
    return {'greeting': greeting_function('Alice')}

@app.route('/B2F', methods=['GET'])
def higher_order_function():
    def apply_function(func, value):
        return func(value)
    return {'result': apply_function(lambda x: x * 2, 10)}

@app.route('/B2E', methods=['GET'])
def closure_example():
    def outer_function(x):
        def inner_function(y):
            return x + y
        return inner_function
    closure = outer_function(10)
    return {'closure_result': closure(5)}

@app.route('/B3G', methods=['GET'])
def lambda_example():
    square = lambda x: x * x
    return {'square': square(4)}

@app.route('/B3F', methods=['GET'])
def multi_arg_lambda():
    add = lambda x, y: x + y
    return {'sum': add(3, 5)}

@app.route('/B3E', methods=['GET'])
def sort_example():
    numbers = [5, 3, 9, 1]
    sorted_numbers = sorted(numbers, key=lambda x: x)
    return {'sorted_numbers': sorted_numbers}

@app.route('/B4G', methods=['GET'])
def map_example():
    numbers = [1, 2, 3, 4]
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    return {'squared_numbers': squared_numbers}

@app.route('/B4F', methods=['GET'])
def combine_map_filter_reduce():
    numbers = [1, 2, 3, 4, 5]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    squared_evens = list(map(lambda x: x ** 2, evens))
    return {'squared_evens': squared_evens}

@app.route('/B4E', methods=['GET'])
def complex_data_processing():
    from functools import reduce
    data = [{'value': 10}, {'value': 20}, {'value': 30}]
    total_value = reduce(lambda acc, item: acc + item['value'], data, 0)
    return {'total_value': total_value}

@app.route('/C1G', methods=['GET'])
def refactoring_example():
    total = sum([1, 2, 3])
    def calculate_sum(numbers):
        return sum(numbers)
    return {'sum': calculate_sum([1, 2, 3])}

@app.route('/C1F', methods=['GET'])
def code_readability():
    data = [1, 2, 3]
    result = [x * 2 for x in data]
    def double_numbers(numbers):
        return [x * 2 for x in numbers]
    return {'doubled': double_numbers(data)}

@app.route('/C1E', methods=['GET'])
def refactoring_impact():
    original_code = "print('Hello World')"
    refactored_code = "def greet(): print('Hello World')"
    return {'original': original_code, 'refactored': refactored_code}

if __name__ == '__main__':
    app.run(debug=True)
