#!/usr/bin/awk -f

BEGIN {
	last = -1
	increased = 0
}

{
	if (last >= 0 && last < $0) {
	        increased = increased + 1
	}
	last = $0
}


END {
	print(increased)
}
