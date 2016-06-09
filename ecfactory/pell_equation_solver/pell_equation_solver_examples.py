from pell_equation_solver import pell_solve

# Example: finding solutions to x^2 - D*y^2 = m
m = -8
D = 33
sols = pell_solve(D,m)
print('Minimal solution to x^2 - D*y^ = 1 is (' + str(sols[0][0]) + ', ' + str(sols[0][1]) + ')')
print('Printing primitive solutions to x^2 - D*y^2 = m...')
for x,y in sols[1]:
    print('\t(' + str(x) + ', ' + str(y) + ')')