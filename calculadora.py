
def sumar(a, b):
    """Suma dos números."""
    return a + b


def restar(a, b):
    """Resta dos números."""
    return a - b


def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b


def dividir(a, b):
    """Divide a entre b."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b


def funcion_lineal(x, m, b):
    """Calcula f(x) = m*x + b."""
    return m * x + b


def calculadora():
    """Muestra el menú de la calculadora."""
    while True:
        print("\n===== CALCULADORA =====")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Calcular f(x) = m*x + b")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "6":
            print("Calculadora finalizada.")
            break

        if opcion not in ("1", "2", "3", "4", "5"):
            print("Opción inválida.")
            continue

        try:
            if opcion == "5":
                x = float(input("Ingresa el valor de x: "))
                m = float(input("Ingresa la pendiente m: "))
                b = float(input("Ingresa el valor de b: "))

                resultado = funcion_lineal(x, m, b)
                print(f"f({x}) = {m}*{x} + {b} = {resultado}")

            else:
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))

                if opcion == "1":
                    resultado = sumar(a, b)
                elif opcion == "2":
                    resultado = restar(a, b)
                elif opcion == "3":
                    resultado = multiplicar(a, b)
                else:
                    resultado = dividir(a, b)

                print(f"Resultado: {resultado}")

        except ValueError:
            print("Error: ingresa números válidos.")
        except ZeroDivisionError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    calculadora()
