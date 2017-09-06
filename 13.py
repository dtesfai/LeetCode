numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

s = ''[::-1]

if len(s) > 0:
	sum = numerals[s[0]]
else:
	return sum

for i in range(1, len(s)):
	val = numerals[s[i]]
	old_val = numerals[s[i - 1]]
	if val < old_val:
		sum -= val
	else:
		sum += val

return sum