
def funcion_lineal(x, m, b):
    """Calcula f(x) = m*x + b.

    Args:
        x: Valor de entrada.
        m: Pendiente de la recta.
        b: Ordenada al origen.

    Returns:
        El resultado numérico m*x + b.

    Raises:
        TypeError: Si los argumentos no son numéricos
            o son booleanos.
        ValueError: Si un argumento es infinito o NaN.
    """
    valores = (x, m, b)

    for valor in valores:
        if isinstance(valor, bool) or not isinstance(
            valor, (int, float)
        ):
            raise TypeError(
                "x, m y b deben ser números."
            )

        if not __import__("math").isfinite(valor):
            raise ValueError(
                "x, m y b deben ser números finitos."
            )

    return m * x + b
