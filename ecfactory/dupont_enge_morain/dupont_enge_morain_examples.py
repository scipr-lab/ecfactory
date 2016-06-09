import ecfactory.dupont_enge_morain as dem
from ecfactory.utils import print_curve

# Example
k = 7 # embedding degree
q,t,r,k,D = dem.run(10,k) # find q,t,r,k,D using DEM method, where r is at least a 10-bit prime and k = 7
print_curve(q,t,r,k,D)