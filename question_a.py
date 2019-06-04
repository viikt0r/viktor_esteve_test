def isOverlap(line1, line2):
	x1, x2 = line1
	x3, x4 = line2


	if ((x1 >= x3 and x1 <= x4) or (x3 >= x1 and x3 <= x2)):
		return True

	return False


