"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	time = 0
	bs = 0
	return helper(n, time, bs)


def helper(n, time, bs):
	if 0 <= n <= 10:
		return n
	else:
		if n < 10 ** (time+1):
			if n < 0:
				return helper(-n, time, bs)
			else:
				first = n // (10 ** time)
				if first > bs:
					return first
				else:
					return bs
		else:
			sq = n//(10 ** time) - (n//(10 ** (time + 1))) * 10
			if sq > bs:
				bs = sq
			time += 1
			return helper(n, time, bs)


if __name__ == '__main__':
	main()
