import sympy as sp

def find_initial_x0(function_str):
    x = sp.symbols('x')
    f = sp.sympify(function_str)
    x0 = None
    i = 0
    while True:
        try:
            f_prev = f.subs(x, i)
            f_curr = f.subs(x, i + 1)
        except (sp.ZeroDivisionError, ValueError, TypeError):
            i += 1
            continue
        if f_prev.is_real and f_curr.is_real:
            if f_prev * f_curr < 0:
                x0 = i
                break
        i += 1
    return x0

def newton_raphson(function_str, x0, precision=5):
    x = sp.symbols('x')
    f = sp.sympify(function_str)
    df = sp.diff(f, x)
    f_func = sp.lambdify(x, f)
    df_func = sp.lambdify(x, df)
    x_old = x0
    x_new = x_old - f_func(x_old) / df_func(x_old)
    while round(abs(x_new - x_old), precision) != 0:
        x_old = x_new
        x_new = x_old - f_func(x_old) / df_func(x_old)
    return round(x_new, precision)

function_str = input("Enter the simplified function in terms of x (Ex: x**3 + x - 5): ")

x0 = find_initial_x0(function_str)

if x0 is not None:
    print(f"Initial value x0 found: {x0}")
    precision = 5
    root = newton_raphson(function_str, x0, precision)
    print(f"The root of the function {function_str} is approximately: {root}")
else:
    print("Unable to determine initial value x0. Consider trying a different function.")
