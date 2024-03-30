import math
import cmath

def solve_quadratic(a, b, c):
    """
    Solves a quadratic equation of the form: ax^2 + bx + c = 0
    Returns a tuple containing the roots.
    """
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return (root, root)
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return (complex(real_part, imaginary_part), complex(real_part, -imaginary_part))

def solve_cubic(a, b, c, d):
    """
    Solves a cubic equation of the form: ax^3 + bx^2 + cx + d = 0
    Returns a list containing the roots.
    """
    q = (3*c - b**2) / (9*a)
    r = (2*b**3 - 9*a*b*c + 27*a**2*d) / (54*a**2)
    discriminant = q**3 + r**2
    if discriminant > 0:
        # Three distinct real roots
        s = cmath.cbrt(r + math.sqrt(discriminant))
        t = cmath.cbrt(r - math.sqrt(discriminant))
        root1 = -b / (3*a) + s + t
        root2 = -b / (3*a) - (s + t)/2 + (s - t)*cmath.sqrt(3)/2
        root3 = -b / (3*a) - (s + t)/2 - (s - t)*cmath.sqrt(3)/2
        return [root1, root2, root3]
    elif discriminant == 0:
        # Three real roots, at least two are equal
        r13 = -2*q/3
        root1 = root2 = root3 = r13
        return [root1, root2, root3]
    else:
        # One real root and two complex conjugate roots
        theta = math.acos(r / math.sqrt(-q**3))
        root1 = 2 * math.sqrt(-q) * math.cos(theta / 3) - b / (3*a)
        root2 = 2 * math.sqrt(-q) * math.cos((theta + 2*math.pi) / 3) - b / (3*a)
        root3 = 2 * math.sqrt(-q) * math.cos((theta - 2*math.pi) / 3) - b / (3*a)
        return [root1, root2, root3]

def solve_quartic(a, b, c, d, e):
    """
    Solves a quartic equation of the form: ax^4 + bx^3 + cx^2 + dx + e = 0
    Returns a list containing the roots.
    """
    # Implement a method to solve the quartic equation here
    # This could involve using the Ferrari's method or other techniques
    # Return the roots as a list
    pass

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