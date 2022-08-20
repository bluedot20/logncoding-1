### Review on double list ### 


# colors = ["red", "green", "yellow"]
# numbers = [ 4, 5, 10 ]
# fruits = ["banana", "apple", "grape"]

# myList = [["red", "green", "yellow"],[ 4, 5, 10 ],["banana", "apple", "grape"]]

# # for i in (myList): 
# # 	print(i)

# # for i in range(0, len(myList)): 
# # 	# print(myList[i])
# # 	for j in range(0, len(myList[i])): 
# # 		print(myList[i][j])






# ## Median ##   1, 3, 7, 9
# myList2 = [[1, 91, 3],[ 4, 5, 6, 10 ],[4, 8, 11]]

# maxNum = 0 
# newList = []
# for i in range(0, len(myList2)): 
# 	for j in range(0, len(myList2[i])): 
# 		# print(myList2[i][j])
# # 		if myList2[i][j] > maxNum: 
# # 			maxNum = myList2[i][j]
# # print(maxNum)
# 		newList.append(myList2[i][j])		# creating a entirely new list 
# newList.sort()			# in increasing order 
# print(newList[-1])			# getting the last element 
# length = len(newList)
# print(newList[length - 1])		# another way to get the last element 


# print(newList)
# middleIndex = len(newList) // 2
# # print(middleIndex)
# print(newList[middleIndex]) 			# 6 
# print(newList[middleIndex - 1]) 			# 5

# median = ( newList[middleIndex] + newList[middleIndex - 1] )  /  2
# print(median)




### Creating Tetris Blocks ### 

# block numbers 
# 1 -> J shape   # 2 -> L shape   # 3 -> S shape    # 4 -> Z shape 
# 5 -> I shape 	 # 6 -> T shape   # 7 -> O shape 

# printing blocks 
# print(". # .")
# print(". # .")
# print(". # #")

def make_block(block_num): 
	if block_num == 1:  # J 
		block = [[False, True, False], [False, True, False], [True, True, False]]
	elif block_num == 2:  # L 
		block = [[False, True, False], [False, True, False], [False, True, True]]
	elif block_num == 3:  # S 
		block = [[False,False,False], [False,True,True], [True,True,False]]
	elif block_num == 4:  # Z
		block = [[False,False,False], [True,True,False], [False,True,True]] 
	elif block_num == 5:  # I 
		block = [[False, False, False, False], [True, True, True, True], 
		[False, False, False, False], [False, False, False, False]]
	elif block_num == 6: # T
		block = [[False,False,False], [True,True,True], [False,True,False]]
	elif block_num == 7: # O
		block = [[False,False,False], [False,True,True], [False,True,True]]	

	return block 

import random 
def show_block(): 
	block_num = random.randint(1, 7)
	block = make_block(block_num)
	for i in block: 
		for j in i: 
			if j == True: 
				print("#", end = " ")
			else: 
				print(".", end = " ")
		print()

show_block()
# generating random numbers from 1 ~ 7 for the tetris shapes 
# block_number = random.randint(1, 7)


