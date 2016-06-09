import ecfactory.mnt_curves as mnt
from ecfactory.utils import print_curve

# Example (MNT curve with k = 6 and D = -19)
curves = mnt.make_curve(6,-19)
q,t,r,k,D = curves[0]
print_curve(q,t,r,k,D)

# Example (MNT curve with k = 3 and D = -19)
curves = mnt.make_curve(3, -19)
q,t,r,k,D = curves[0]
print_curve(q,t,r,k,D)

# Enumerate through all MNT curves with k = 6 and -D < 200000
f = open("mnt6_enumeration.csv", 'w')
f.write('q,t,r,k,D\n')
D = -11
while -D < 200000:
    try:
        curves = mnt.make_curve(6,D)
        if (len(curves) > 0):
            for c in curves:
                for i in range(0, len(c)):
                    if i != len(c) - 1:
                        f.write(str(c[i]) + ',')
                    else:
                        f.write(str(c[i]) + '\n')
    except AssertionError as e:
        pass
    D -= 8
f.close()
