#!/usr/bin/awk -f

{
	positions[$1] += $2
}

END {
	for(p in positions) {
		print p, positions[p]
	}
	print "multiply:", (positions["down"] - positions["up"]) * positions["forward"]
}

