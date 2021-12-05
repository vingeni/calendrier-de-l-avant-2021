#!/usr/bin/awk -f

BEGIN {
	FS=""
}

{
	for(p=1; p <= NF; p++) {
		counter[p-1] += ($p == "1") # count the number of one per position p
	}
}

END {
	for(p in counter) {
		# most common bit
		gammabit = (counter[p] > (NR/2))
		gamma = lshift(gamma, 1) + gammabit

		epsilonbit = 1 - gammabit
		epsilon = lshift(epsilon, 1) + epsilonbit
	}
	print "gamma:" gamma, "epsilon:" epsilon, "result:" (gamma * epsilon)
}

