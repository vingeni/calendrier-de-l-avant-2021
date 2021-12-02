#!/usr/bin/awk -f

{
	positions[$1] += $2
	if ($1 == "forward") {
		aim = positions["down"] - positions["up"];
		positions["depth"] +=  aim * $2
	}
}

END {
	for(p in positions) {
		print p, positions[p]
	}
	print "multiply:", (positions["depth"]) * positions["forward"]
}

