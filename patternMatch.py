#sample input (pattern,string): "xxyxxy", "gogopowerrangergogopowerranger"
#sample output (x,y): ["go", "powerranger"]


def patternMatcher(pattern, string):
	patSwap = False
	patDict = {}
	firstYIdx = 0
    	if pattern[0] == 'y':
		newPattern = ""
		for i in range(len(pattern)):
			if pattern[i] == 'x':
				newPattern += 'y'
				if 'y' not in patDict:
					firstYIdx = i
					patDict['y'] = 1
				else:
					patDict['y'] += 1
			else:
				newPattern += 'x'
				if 'x' not in patDict:
					patDict['x'] = 1
				else:
					patDict['x'] += 1	
		pattern = newPattern
		patSwap = True
	else:
		for i in range(len(pattern)):
			if pattern[i] not in patDict:
				patDict[pattern[i]] = 1
				if pattern[i] == 'y':
					firstYIdx = i
			else:
				patDict[pattern[i]] += 1
				
	if 'y' not in patDict:
		patDict['y'] = 0
	
	
	if patDict['y'] != 0:
		for lenOfX in range(1,len(string)):
			lenOfY = (len(string)-(lenOfX*patDict['x']))/ patDict['y']
			YIdx = firstYIdx * lenOfX
			if lenOfY <= 0 or lenOfY%1 != 0:
				continue
			lenOfY = int(lenOfY)
			x = string[:lenOfX]
			y = string[YIdx:YIdx + lenOfY]
			checkString = map(lambda char: x if char == "x" else y, pattern)
			if string == "".join(checkString):
				return [x, y] if not patSwap else [y, x]
	else:
		lenOfX = int(len(string) / patDict['x'])
		last = string[:lenOfX]
		for i in range(int(len(string)/lenOfX)):
			if string[i*lenOfX:(i*lenOfX)+lenOfX] == last:
				continue
			else: 
				return []
			last = string[i*lenOfX:(i*lenOfX)+lenOfX]
		return [last, ''] if not patSwap else ['', last]
	
	return []