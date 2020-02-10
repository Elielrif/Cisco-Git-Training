# this function checks whether a list passed as an argument contains
# nine digits from '1' to '9'
def checkset(digs):
	return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]



# this will be a list of rows representing the sudoku
rows = [ ]
for r in range(9):
	ok = False
	while not ok:
		row = input("Enter row #" + str(r + 1) + ": ")
		ok = len(row) == 9 or row.isdigit()
		if not ok:
			print("Incorrect row data - 9 digits required")
	rows.append(row)

ok = True

# check if all rows are good
for r in range(9):
	if not checkset(rows[r]):
		ok = False
		break

# check if all columns are good
if ok:
	for c in range(9):
		col = []
		for r in range(9):
			col.append(rows[r][c])
		if not checkset(col):
			ok = False
			break

# check if all sub-squares (3x3) are good
if ok:
	for r in range(0, 9, 3):
		for c in range(0, 9, 3):
			sqr = ''
			# make a string containing all digits from a sub-square
			for i in range(3):
				sqr += rows[r+i][c:c+3]
			if not checkset(list(sqr)):
				ok = False
				break

# print the final verdict
if ok:
	print("Yes")
else:
	print("No")


#295743861
#Enter row #2: 431865927
#Enter row #3: 876192543
#Enter row #4: 387459216
#Enter row #5: 612387495
#Enter row #6: 549216738
#Enter row #7: 763524189
#Enter row #8: 928671354
#Enter row #9: 154938672
#