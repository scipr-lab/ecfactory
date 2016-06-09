from sage.all import is_square, sqrt, Integer, floor, ceil

def pell_solve(D, m):
    """
    Description:
        
        Solves the Pell equation x^2 - D*y^2 = m
    
    Input:
    
        D - nonsquare integer
        m - integer
    
    Output:
    
        (x0, y0) - minimal solution to x^2 - D*y^2 = 1
        prim_sols - list of primitive solutions for each solution class to x^2 - D*y^2 = m
    
    """
    assert not is_square(D), 'D cannot be a perfect square'
    if m*m >= D:
        return _pell_solve_2(D,m)
    else:
        return _pell_solve_1(D,m)


def _pell_solve_1(D,m): # m^2 < D
    root_d = Integer(floor(sqrt(D)))
    a = Integer(floor(root_d))
    P = Integer(0)
    Q = Integer(1)
    p = [Integer(1),Integer(a)]
    q = [Integer(0),Integer(1)]
    i = Integer(1)
    x0 = Integer(0)
    y0 = Integer(0)
    prim_sols = []
    test = Integer(0)
    while not (Q == 1 and i%2 == 1) or i == 1:
        test = p[i]**2 - D* (q[i]**2)
        if test == 1:
            x0 = p[i]
            y0 = q[i]
        test = (m/test)
        if is_square(test) and test >= 1:
            test = Integer(test)
            prim_sols.append((test*p[i],test*q[i]))
        i+=1
        P = a*Q - P
        Q = (D-P**2)/Q
        a = Integer(floor((P+root_d)/Q))
        p.append(a*p[i-1]+p[i-2])
        q.append(a*q[i-1]+q[i-2])
    return (x0,y0), prim_sols
    
   
def _pell_solve_2(D,m): # m^2 >= D
    prim_sols = []
    t,u = _pell_solve_1(D,1)[0]
    if m > 0:
        L = Integer(0)
        U = Integer(floor(sqrt(m*(t-1)/(2*D))))
    else:
        L = Integer(ceil(sqrt(-m/D)))
        U = Integer(floor(sqrt(-m*(t+1)/(2*D))))
    for y in range(L,U+1):
        y = Integer(y)
        x = (m + D*(y**2))
        if is_square(x):
            x = Integer(sqrt(x))
            prim_sols.append((x,y))
            if not ((-x*x - y*y*D) % m == 0 and (2*y*x) % m == 0): # (x,y) and (-x,y) are in different solution classes, so add both
                prim_sols.append((-x,y))
    return (t,u),prim_sols