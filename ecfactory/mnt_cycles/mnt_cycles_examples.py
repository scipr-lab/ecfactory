import ecfactory.mnt_cycles as mnt_cycles

# Example (find an MNT cycle with D = -19)
cycles = mnt_cycles.make_cycle(-19)
print('Found a cycle: ' + str(cycles[0][0]) + ', ' + str(cycles[0][1]))