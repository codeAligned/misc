#!/usr/bin/python3

#	Program will use (kind of) Dijkstra's algorithm to find the
# 	maximum value-path across the int array s, printing out the 
#	final path and the total path value


s = [[0,5,0,8,1,8],
	[3,6,1,3,6,3],
	[9,5,7,9,1,1],
	[8,7,9,4,8,3],
	[7,8,7,6,2,5],
	[3,4,0,5,0,4]]



def main(s):
	track = list()
	track.append(list())

	# setting up the first row
	for i in range(len(s[0])):
		
		# start point
		if i == 0:
			track[0].append((s[0][i], False))
		
		# rest of first row
		else:					#previous sum + current s
			track[0].append( (track[0][i-1][0] + s[0][i], 'R') )

	# setting up the first column
	for j in range(1,len(s)):

		track.append(list())
								# previous sum + current s
		track[j].append( (track[j-1][0][0] + s[j][0], 'D') )


	# iterate through rest of s, filling in track
	for i in range(1, len(s[0])):
		for j in range(1, len(s)):

			top  = track[j-1][i][0]
			left = track[j][i-1][0]

			# move down
			if top > left:
				tupl = (top + s[j][i], 'D')

			# move right
			else: # ties doesn't matter
				tupl = (left + s[j][i], 'R')

			track[j].append(tupl)

	# now let's gather our path
	col = len(track[0]) - 1
	row = len(track)    - 1
	total = track[row][col][0]
	path = ""

	while track[row][col][1]: # first entry is false, strings return true
		
		curr = track[row][col][1]
		path += curr

		if curr == 'R':
			col -= 1

		elif curr == 'D':
			row -= 1

		else:
			print('Something weird is going on')
			break


	# for i in range(len(track)):
	# 	print(track[i])

	print(path[::-1], total)


main(s)