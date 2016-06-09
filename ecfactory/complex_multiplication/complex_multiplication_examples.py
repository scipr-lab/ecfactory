from sage.all import EllipticCurve
import ecfactory.complex_multiplication as cm
from ecfactory.utils import print_curve

# Example
q,t,r,k,D = (9118668363579256702502724196290077470606883146523450654874350215381, 650645402122989554764568571081790, 1188650876978797236509935829939, 11, -84)
E = cm.make_curve(q,t,r,k,D) # takes a few seconds
print(E)
print_curve(q,t,r,k,D)