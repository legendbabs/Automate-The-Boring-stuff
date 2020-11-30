def main():
	tableData = [
	['apples', 'oranges', 'cherries', 'banana'],
	['Alice', 'Bob', 'Carol', 'David'],
	['dogs', 'cats', 'moose', 'goose']
	]

	printTable(tableData)


def printTable(tableList):
	index_list1 = []
	index_list2 = []
	index_list3 = []
	# Find the largest string in each of the inner lists
	for item in tableList[0]:
		index_list1.append(len(item))
	for item in tableList[1]:
		index_list2.append(len(item))
	for item in tableList[2]:
		index_list3.append(len(item))

	col1 = max(index_list1)
	col2 = max(index_list2)
	col3 = max(index_list3)
	maxWidths = []

	colWidths = [0] * len(tableList)
	print(tableList[0][0].rjust(col1) + tableList[1][0].rjust(col1) + tableList[2][0].rjust(col1))
	print(tableList[0][1].rjust(col1) + tableList[1][1].rjust(col1) + tableList[2][1].rjust(col1))
	print(tableList[0][2].rjust(col1) + tableList[1][2].rjust(col1) + tableList[2][2].rjust(col1))
	print(tableList[0][3].rjust(col1) + tableList[1][3].rjust(col1) + tableList[2][3].rjust(col1))


main()
