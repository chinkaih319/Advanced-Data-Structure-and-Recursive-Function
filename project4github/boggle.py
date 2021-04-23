"""
File: boggle.py
Name: Justin Huang
----------------------------------------
TODO: Boggle Mission
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dic_list = []
time = 0


def main():
	"""
	TODO:
	"""
	boggle = []
	read_dictionary()
	for i in range(4):
		print((i+1), end='')
		cha = input(' row of letters: ').strip()
		if len(cha) != 7:
			print('illegal input')
			break
		elif cha[1] != ' ' or cha[3] != ' ' or cha[5] != ' ':
			print('illegal input')
			break
		elif cha[0].isalpha() is False or cha[2].isalpha() is False or cha[4].isalpha() is False or cha[6].isalpha() is False:
			print('illegal input')
			break
		else:
			low_cha = cha.lower().split(' ')
			boggle.append(low_cha)
	word_collection = []
	for i in range(len(boggle[0])):
		for j in range(len(boggle)):
			center_word = boggle[i][j]
			current_center = (i, j)
			boggle_make(
						boggle, [current_center], len(boggle), word_collection, len(boggle[0]), current_center, center_word,
						)
	print(f'There are {time} words in total.')


def boggle_make(boggle, cur_position_list, row, word_collection, column, center, start_word):
	global time
	if has_prefix(start_word) is False:
		return
	else:
		for x in range(-1, 2, 1):
			for y in range(-1, 2, 1):
				current_index = (center[0]+x, center[1]+y)
				if x == 0 and y == 0:
					pass
				else:
					if 0 <= current_index[0] < column:
						if 0 <= current_index[1] < row:
							if current_index not in cur_position_list:
								cur = start_word + boggle[current_index[0]][current_index[1]]
								cur_position_list.append(current_index)
								if len(cur) >= column and cur not in word_collection:
									if cur in dic_list:
										word_collection.append(cur)
										time += 1
										print(f'Found "{cur}"')
										boggle_make(boggle, cur_position_list, row, word_collection, column, current_index, cur)
								else:
									boggle_make(boggle, cur_position_list, row, word_collection, column, current_index, cur)
								cur_position_list.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			sp_l = line.strip()
			dic_list.append(sp_l)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for i in range(len(dic_list)):
		if dic_list[i].startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
