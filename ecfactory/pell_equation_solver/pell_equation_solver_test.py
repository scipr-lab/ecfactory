"""
Test the Pell Equation Solver

    Contains a set of test vectors for pell equation solver
"""

from ecfactory.pell_equation_solver import pell_solve


def test_pell_equation(d, m):
    gen, sols = pell_solve(d, m)

    assert gen[0]**2 - d*gen[1]**2 == 1
    for sol in sols:
        assert sol[0]**2 - d*sol[1]**2 == m


def test_vectors_pell_equation():
    test_pell_equation(34, 4)
    test_pell_equation(2, 2)
    test_pell_equation(3, 5)
    test_pell_equation(5, 234)
    test_pell_equation(6, 1253)
    test_pell_equation(1325, 2)
    test_pell_equation(15251, 34)

    test_pell_equation(34, -4)
    test_pell_equation(2, -2)
    test_pell_equation(3, -5)
    test_pell_equation(5, -234)
    test_pell_equation(6, -1253)
    test_pell_equation(1325, -2)
    test_pell_equation(15251, -34)

    test_pell_equation(63*103, -180)
    test_pell_equation(63 * 103, -80)


if __name__ == '__main__':
    print("Running test vectors")
    test_vectors_pell_equation()
    print("Tests finished")
