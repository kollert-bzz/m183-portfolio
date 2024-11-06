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
    return render_template('task.html', title="A1G", result=f'Ein Kreis mit einem Radius von: '
                                                            f'{round(math.sqrt(area/math.pi), 2)},'
                                                            f'\ngibt es eine Fläche von: {round(area, 2)}')

@app.route('/A1F', methods=['GET'])
def immutable_example():
    my_tuple = (1, 2, 3)
    return {'tuple': my_tuple}

@app.route('/A1E', methods=['GET'])
def compare_concepts():
    return {
        'OO': 'Objektorientierte Programmierung',
        'Functional': 'Funktionale Programmierung',
        'Procedural': 'Prozedurale Programmierung'
    }

@app.route('/B1G', methods=['GET'])
def algorithm_explanation():
    return {'explanation': 'Ein Algorithmus zur Berechnung der Fibonacci-Zahlen.'}

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
