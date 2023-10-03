num1 = 42    #tipo de datos 
num2 = 2.3   #primitivo = number
boolean = True  #primitivo = boleano
string = 'Hello World' #primitivo = string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana') #stings
print(type(fruit))
print(pizza_toppings[1])#'sausage'
pizza_toppings.append('Mushrooms')#['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives','Mushrooms']
print(person['name'])#'John'
person['name'] = 'George'#cambia el name a 'George'
person['eye_color'] = 'blue' #agrega eye_color='blue'
print(fruit[2])#'banana'

"""
Condicionales
"""
if num1 > 45:                          
    print("It's greater")# no sucede porque num1 es menor a 45
else:
    print("It's lower") #entonces imprime I´ts lower

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!") #imprime just right ya que no se cumplen las condiciones anteriores

"""
For loop
"""
for x in range(5):
    print(x) #0,1,2,3,4
for x in range(2,5):
    print(x) #2,3,4
for x in range(2,10,3):
    print(x) #2,5,8 
    """
    Este bucle for itera sobre los valores generados por range(2, 10, 3), 
    que produce una secuencia de números desde 2 hasta 9, 
    pero con un paso de 3 en cada iteración. En cada iteración, 
    la variable x toma uno de estos valores y se imprime en la consola.
    """
x = 0 #se le asigna a x el valor de 0

"""
While loop
"""
while(x < 5): #stop si se incrementa hasta 5 
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)#name: 'George', location: 'Salt Lake', age: '37', is_balding: 'false' eye_color: 'blue'
person.pop('eye_color')#elimina 'eye_color'
print(person)#name: 'George', location: 'Salt Lake', age: '37', is_balding: 'false'

for topping in pizza_toppings: 
    if topping == 'Pepperoni': #start
        continue 
    """
    Esta declaración continue se utiliza para saltar al siguiente ciclo de iteración 
    inmediato, sin ejecutar el código restante dentro del bucle en esta iteración 
    en particular. En otras palabras, si topping es igual a 'Pepperoni', 
    se omitirá todo lo que sigue en esta iteración del bucle y pasará a la 
    siguiente iteración.
    """
    print('After 1st if statement') 
    """
    print('After 1st if statement'): Si topping no es igual a 'Pepperoni', 
    se imprimirá la cadena 'After 1st if statement'.
    """
    if topping == 'Olives': 
        break 
    """
    La declaración break se utiliza para salir inmediatamente del bucle en el 
    que se encuentra. 
    Si topping es igual a 'Olives', el bucle for se detendrá inmediatamente 
    y no continuará iterando sobre los elementos restantes en pizza_toppings.
    """

#acá comienza una función def= def se ocupa para combinar funciones y bucles for en python 
def print_hello_ten_times():
    for num in range(10):
        print('Hello')
"""
imprime la cadena 'Hello' 10 veces. El bucle for se ejecuta 10 veces, 
comenzando desde 0 hasta 9, y en cada iteración, 
imprime 'Hello' en la consola. Como resultado, verás la palabra 'Hello' 
impresa 10 veces cuando llames a esta función.
"""
print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
"""
Esta función toma un argumento x, que debe ser un número entero. 
Luego, utiliza un bucle for para imprimir la cadena 'Hello' x veces. 
Por ejemplo, si llamas a print_hello_x_times(4), verás 'Hello' impreso 4 veces 
en la consola.
"""
print_hello_x_times(4) 

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello') 
"""
Esta función es similar a la segunda, pero tiene un valor predeterminado para el 
argumento x, que es 10. Si no proporcionas un valor para x cuando llamas 
a la función, imprimirá 'Hello' 10 veces. Sin embargo, si proporcionas un valor 
diferente, como print_hello_x_or_ten_times(4), imprimirá 'Hello' 4 veces 
en lugar de 10.
"""

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

num3 = 72
print(num3)

fruit[0] = 'cranberry'
print(person['favorite_team'])
print(pizza_toppings[7])
print(boolean) 
fruit.append('raspberry') #agrega raspberry a la lista
fruit.pop(1) #elimina el elemento x1 de la lista
#al final quedaría fruit= [cranberry,banana,raspberry]