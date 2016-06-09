kmin=5
kmax=19
do for [k=kmin:kmax] {
	set terminal svg
	set output 'plots/cp_vs_dem/k'.k.'.svg'
	set xlabel "Number of bits in r"
	set ylabel "Time in seconds"
	set key font ",14"
	set label font ",14"
	set xlabel font ",14"
	set ylabel font ",14"
	set label "k=".k at screen 0.54,0.92 center front font ",14"
	plot 'logs/dem/k'.k.'.csv' every ::1 with lines lw 2 lt rgb "blue" title "dem:", 'logs/cp/k'.k.'.csv' every ::1 with lines lw 2 lt rgb "red" title "cp:"
	unset label
	unset xlabel
	unset ylabel
	unset output
	unset terminal
	unset key
}
