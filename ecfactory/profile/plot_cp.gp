set terminal svg
f = "cp"
set output 'plots/'.f.'/'.f.'.svg'
set xlabel "Number of bits in r"
set ylabel "Time in seconds"
kmax = 19
kmin = 5
color(k) = (k-kmin)*16777215/(1.5*(kmax-kmin))
set title ""
set key font ",10"
set label font ",14"
set xlabel font ",14"
set ylabel font ",14"
plot for [i=kmin:kmax] 'logs/'.f.'/k'.i.'.csv' every ::1 with lines lw 2 lt rgb color(i) title "k=".i
