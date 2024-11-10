import math
from flask import Flask, render_template
from functools import reduce

app = Flask(__name__, template_folder='html')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/A1G', methods=['GET'])
def pure_function():
    def calculate_area(radius):
        return math.pi * radius * radius

    area = calculate_area(3)
    return render_template('task.html', title='A1G', result=f'Ein Kreis mit einem Radius von: '
                                                            f'{round(math.sqrt(area / math.pi), 2)},'
                                                            f'\ngibt es eine Fläche von: {round(area, 2)}')


@app.route('/A1F', methods=['GET'])
def immutable_example():
    student_info = [
        ('Alice', 20, 1),
        ('Bob', 22, 2),
        ('Charlie', 19, 3)
    ]
    result = 'Studenten Informationen:\n'
    for student in student_info:
        name, age, student_id = student
        result += f'Name: {name}, Alter: {age}, ID: {student_id}\n'

    return render_template('task.html', title='A1F', result=result)


@app.route('/A1E', methods=['GET'])
def compare_concepts():
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

    def procedural_factorial(number):
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result

    def functional_factorial(number):
        return 1 if number == 0 else number * functional_factorial(number - 1)

    oo_result = oo_factorial(5)
    procedural_result = procedural_factorial(5)
    functional_result = functional_factorial(5)

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

    return render_template('task.html', title='A1E - Fibonacci Algorithmus', result=result)


@app.route('/B1G', methods=['GET'])
def fibonacci_algorithm():
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    n = 5
    fibonacci_result = fibonacci(n)
    result = f'Die {n}. Fibonacci-Zahl ist: {fibonacci_result}'

    return render_template('task.html', title='B1G - Fibonacci Algorithmus', result=result)


@app.route('/B1F', methods=['GET'])
def split_algorithm():
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    n = 7
    fibonacci_result = fibonacci(n)
    result = f'Die {n}. Fibonacci-Zahl ist: {fibonacci_result}'

    return render_template('task.html', title='B1G - Fibonacci Algorithmus', result=result)


@app.route('/B1E', methods=['GET'])
def combined_algorithm():
    def total_calories(exercises):
        return sum(exercises)

    result = f'Total Kalorien: {total_calories([200, 300, 150])}'
    return render_template('task.html', title='B1E - Calorie Counter', result=result)


@app.route('/B2G', methods=['GET'])
def function_as_object():
    def greet(name):
        return f'Hallo, {name}!'

    greeting_function = greet
    result = f'{greeting_function("Timo")}'
    return render_template('task.html', title='B2G - Function as an Object', result=result)


@app.route('/B2F', methods=['GET'])
def higher_order_function():
    def apply_function(func, value):
        return func(value)

    result = f'Resultat: {apply_function(lambda x: x * 2, 187)}'
    return render_template('task.html', title='B2F - Higher Function', result=result)


@app.route('/B2E', methods=['GET'])
def closure_example():
    def outer_function(x):
        def inner_function(y):
            return x + y

        return inner_function

    closure = outer_function(10)
    result = f'Resultat: {closure(5)}'
    return render_template('task.html', title='B2E - Closure Function', result=result)


@app.route('/B3G', methods=['GET'])
def lambda_example():
    square = lambda x: x * x
    squared = square(13.7)
    result = f'{math.sqrt(squared)}² = {round(squared, 2)}'
    return render_template('task.html', title='B3G - Lambda', result=result)


@app.route('/B3F', methods=['GET'])
def multi_arg_lambda():
    add = lambda x, y: x + y
    a = 3
    b = 4
    result = f'{a} + {b} = {add(a, b)}'
    return render_template('task.html', title='B3F - Lambda 2', result=result)


@app.route('/B3E', methods=['GET'])
def sort_example():
    numbers = [5, 3, 9, 1]
    sorted_numbers = sorted(numbers, key=lambda x: x)
    result = f'{numbers} sortiert = {sorted_numbers}'
    return render_template('task.html', title='B3E - Lambda 3', result=result)


@app.route('/B4G', methods=['GET'])
def map_example():
    numbers = [1, 2, 3, 4]
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    sum_of_numbers = reduce(lambda x, y: x + y, numbers)
    result = (f'Zahlen: {numbers}\nQuadratzahlen: {squared_numbers}\n'
              f'Gerade Zahlen: {even_numbers}\nSumme: {sum_of_numbers}')
    return render_template('task.html', title='B4G - Map, Filter, Reduce', result=result)


@app.route('/B4F', methods=['GET'])
def combine_map_filter_reduce():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    combined = reduce(
        lambda x, y: x + y,
        filter(
            lambda x: x % 2 == 0,
            map(lambda x: x ** 2, numbers)
        )
    )
    result = f'{numbers} quadriert nur die geraden Zahlen zusammengezählt = {combined}'
    return render_template('task.html', title='B4F - Map & Filter & Reduce', result=result)


@app.route('/B4E', methods=['GET'])
def complex_data_processing():
    from functools import reduce
    data = [{'value': 10}, {'value': 20}, {'value': 30}, {'value': 40}, {'value': 50}]
    filtered_data = list(filter(lambda item: item['value'] > 20, data))
    mapped_data = list(map(lambda item: {'value': item['value'] * 2}, filtered_data))
    total_value = reduce(lambda acc, item: acc + item['value'], mapped_data, 0)
    result = (f'Daten: {data}\nDaten > 20: {filtered_data}\nNeue Daten * 2: {mapped_data}'
              f'\nNeue Daten Summiert: {total_value}')
    return render_template('task.html', title='B4E - Map & Filter & Reduce 2', result=result)


@app.route('/C1G', methods=['GET'])
def refactoring_example():
    numbers = [1, 2, 7, 3]

    def calculate_sum(numbers):
        return sum(numbers)

    total_sum = calculate_sum(numbers)
    result = f'Summe von {numbers} = {total_sum}'
    return render_template('task.html', title='C1G - Refactoring', result=result)


@app.route('/C1F', methods=['GET'])
def get_average():
    numbers1 = [10, 20, 30, 40, 50]
    numbers2 = [10, 50, 60, 700]
    def calculate_average(numbers):
        return sum(numbers) / len(numbers) if numbers else 0
    average1 = calculate_average(numbers1)
    average2 = calculate_average(numbers2)
    result = f'Durchschnitt von {numbers1} = {average1}\nDurchschnitt von {numbers2} = {average2}'
    return render_template('task.html', title='C1F - Refactoring 2', result=result)


@app.route('/C1E', methods=['GET'])
def refactoring_impact():
    numbers = [10, 20, 30, 40, 50]
    def calculate_total(numbers):
        return sum(numbers)
    def calculate_average(numbers):
        return sum(numbers) / len(numbers) if numbers else 0
    total_sum = calculate_total(numbers)
    average = calculate_average(numbers)
    result = (f'Summe von {numbers} = {total_sum}\nDurchschnitt von {numbers} = {average:.2f}')
    return render_template('task.html', title='C1E - Refactoring Impact', result=result)


if __name__ == '__main__':
    app.run(debug=True)
