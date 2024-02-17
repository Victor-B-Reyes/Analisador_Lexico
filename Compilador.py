file = open("read.py")

operators = {'=': 'Asignación', '+': 'Suma', '-': 'Subtraction', '/': 'Division',
             '*': 'Multiplication', '<': 'Menos que', '>': 'Mas que'}
operators_key = operators.keys()

data_type = {'int': 'tipo entero', 'float': 'Punto flotante', 'char': 'Tipo de caracter', 'long': 'largo int'}
data_type_key = data_type.keys()

punctuation_symbol = {':': 'colon', ';': 'semi-colon', '.': 'dot', ',': 'comma'}
punctuation_symbol_key = punctuation_symbol.keys()

identifier = {'a': 'id', 'b': 'id', 'c': 'id', 'd': 'id', 'x': 'id', 'y': 'id', 'z': 'id'}
identifier_key = identifier.keys()

numbers = {'1': 'uno', '2': 'dos', '3': 'tres', '4': 'cuatro', '5': 'cinco'}
numbers_key = numbers.keys()


a = file.read()

count = 0
program = a.split("\n")
for line in program:
    count = count + 1
    print("line#", count, "\n", line)

    tokens = line.split(' ')
    print("Los Tokens son", tokens)
    print("Line#", count, "propiedades \n")
    for token in tokens:
        if token in operators_key:
            print(token, "Operador de ", operators[token])
        if token in data_type_key:
            print(token, "Tipo de dato es", data_type[token])
        if token in punctuation_symbol_key:
            print(token, "Simbolo de cierre", punctuation_symbol[token])
        if token in identifier_key:
            print(token, "Identificador", identifier[token])
        if token in numbers_key:
            print(token, "Es el numero", numbers[token])
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _") 