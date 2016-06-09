import ecfactory.mnt_curves as mnt

def make_cycle(D):
    """
    Description:
    
        Find all MNT cycles with fundamental discriminant D
        
    Input:
    
        D - (negative) fundamental discriminant
    
    Output:
    
        cycles - list of the aforementioned cycles;
                 each cycle is a list containing the curves on the cycle;
                 each curve is represented as a tuple (q,t,r,k,D)
    
    """
    curves4 = mnt.make_curve(4,D)
    curves6 = mnt.make_curve(6,D)
    cycles = []
    for c in curves4:
        for c2 in curves6:
            if (c[0] == c2[2] and c[2] == c2[0]):
                cycles.append([c,c2])
    return cycles