file = open("read.py")

operators = {'igual': 'Asignacion', 'sumar': 'Suma'}
operators_key = operators.keys()

numbers = {'1': 'uno', '2': 'dos'}
numbers_key = numbers.keys()

a = file.read()

programa = a.split("/n")
for line in programa:
    tokens = line.split(' ')
    print("Los tokens son ", tokens)
    for token in tokens:
        if token in operators_key:
            print(token, "Operador", operators[token])
        if token in numbers_key:
            print(token, "numero", numbers[token])