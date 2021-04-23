"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


dic_list = []


def main():
    read_dictionary(FILE)
    print('Welcome to stanCode "Anagram Generator" ( or -1 to quit)')
    while True:
        find = input('Find anagrams for: ')
        if find == EXIT:
            break
        find_anagrams(find)


def read_dictionary(file_name):
    global dic_list
    with open(file_name, 'r') as f:
        for line in f:
            word = line.strip()
            dic_list.append(word)


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    global dic_list
    empty = []
    helper(s, empty, len(s), [], [s], '', dic_list)
    print(len(empty), 'anagram: ', empty)


def helper(s, empty, s_length, ans_list, list_s, cur, dic):
    if len(cur) == s_length:
        if cur in dic:
            if cur not in empty:
                empty.append(cur)
                print('Searching...')
                print('Found: ', end='')
                print(cur)
    else:
        for cha in s:
            if cur.count(cha) < s.count(cha):
                cur += cha
                if has_prefix(cur):
                    helper(s, empty, s_length, ans_list, list_s, cur, dic)
                cur = cur[:-1]


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    for i in range(len(dic_list)):
        if dic_list[i].startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
