import numpy as np

def solve_quadratic(a, b, c):
    """
    Solves a quadratic equation of the form: ax^2 + bx + c = 0
    Returns a list containing the roots.
    """
    roots = np.roots([a, b, c])
    return roots.tolist()

def solve_cubic(a, b, c, d):
    """
    Solves a cubic equation of the form: ax^3 + bx^2 + cx + d = 0
    Returns a list containing the roots.
    """
    roots = np.roots([a, b, c, d])
    return roots.tolist()

def solve_quartic(a, b, c, d, e):
    """
    Solves a quartic equation of the form: ax^4 + bx^3 + cx^2 + dx + e = 0
    Returns a list containing the roots.
    """
    roots = np.roots([a, b, c, d, e])
    return roots.tolist()

def main():
    print("Choose an operation:")
    print("1. Solve Quadratic Equation")
    print("2. Solve Cubic Equation")
    print("3. Solve Quartic Equation")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        a = float(input("Enter the coefficient of x^2: "))
        b = float(input("Enter the coefficient of x: "))
        c = float(input("Enter the constant: "))
        roots = solve_quadratic(a, b, c)
        print("The roots of the quadratic equation are:", roots)
    elif choice == '2':
        a = float(input("Enter the coefficient of x^3: "))
        b = float(input("Enter the coefficient of x^2: "))
        c = float(input("Enter the coefficient of x: "))
        d = float(input("Enter the constant: "))
        roots = solve_cubic(a, b, c, d)
        print("The roots of the cubic equation are:", roots)
    elif choice == '3':
        a = float(input("Enter the coefficient of x^4: "))
        b = float(input("Enter the coefficient of x^3: "))
        c = float(input("Enter the coefficient of x^2: "))
        d = float(input("Enter the coefficient of x: "))
        e = float(input("Enter the constant: "))
        roots = solve_quartic(a, b, c, d, e)
        print("The roots of the quartic equation are:", roots)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()