from sage.all import QuadraticField, is_prime, kronecker, fundamental_discriminant, log, sqrt, is_square, power_mod, Integer
import time
from ecfactory.pell_equation_solver import pell_solve
from ecfactory.utils import is_valid_curve

def make_curve(k,D):
    """
    Description:
    
        Find all MNT curves with embedding degree k and fundamental discriminant D
    
    Input:
    
        k - embedding degree
        D - (negative) fundamental discriminant
    
    Output:
    
        curves - list of the aforementioned elliptic curves;
                 each curve is represented as a tuple (q,t,r,k,D)
    
    """
    assert k == 3 or k== 4 or k == 6, 'Invalid embedding degree'
    assert fundamental_discriminant(D) == D, 'Invalid discriminant'
    if k == 3:
        curves = _mnt_subcall(k,D, 24,lambda x: ((x % 24 == 19) and kronecker(6,x) == 1), 6, 3, -3, lambda x: (x -3 )//6, lambda x: (x+3)//6, lambda l: 6*l - 1, lambda l: -6*l - 1, lambda l: 12*l*l - 1)
    if k == 4:
        curves = _mnt_subcall(k,D,-8, lambda x: ( (x % 8 == 3) and kronecker(-2, x) ==1) or (x == 2) or (x == 8), 3, 2, 1, lambda x: (x-2)//3, lambda x: (x-1)//3, lambda l: -l, lambda l: l+1, lambda l: l*l + l + 1)
    if k == 6:
        curves = _mnt_subcall(k,D,-8, lambda x: (x % 8 == 3) and kronecker(-2, x) == 1, 6, 5, 1, lambda x: (x+1)//6, lambda x: (x-1)//6, lambda l: 2*l + 1, lambda l: -2*l + 1, lambda l: 4*l*l + 1)
    for c in curves:
        assert is_valid_curve(c[0],c[1],c[2],c[3],c[4]), 'Invalid output'
        assert k == c[3], 'Bug in code'
        assert D == c[4], 'Bug in code'
    return curves
   
def _mnt_subcall(k,D, m, condition, modulus, c1, c2, l1, l2, t1, t2, q0):
    D2 = -3*D
    D2 = Integer(D2)
    assert condition(-D), 'No curve exists'
    pell_sols = pell_solve(D2, m) # solve the Pell equation
    curves = []
    curves2 = []
    if len(pell_sols[1])== 0: # no solutions found, so abort
        return curves
    sols = [(Integer(i[0]), Integer(i[1])) for i in pell_sols[1]]
    gen = (Integer(pell_sols[0][0]), Integer(pell_sols[0][1]))
    q = 0
    t = 0
    for i in range(0, len(sols)):
        if sols[i][0] < 0:
            sols[i] = (sols[i][0]*gen[0] + D2*sols[i][1]*gen[1], sols[i][1]*gen[0] + sols[i][0]*gen[1])
    for sol in sols:
        check = False
        x = sol[0]
        l = 0
        t = 0
        q = 0
        if x % modulus == c1:
            l = l1(x)
            t = t1(l)
            check = True
        elif x % modulus == c2:
            l = l2(x)
            t = t2(l)
            check = True
        if check:
            q = q0(l)
            if is_prime(q) and is_prime(q+1-t):
                if ((q,t) not in curves2):
                    curves.append((q,t,q+1-t,k,D))
                    curves2.append((q,t)) 
    return curves