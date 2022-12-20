# leetcode 125
import re

s = input()

# remove non-alphanumeric characters
# strs = ''.join(i for i in s if i.isalnum()).lower()

strs = s.lower()
strs = re.sub('[^a-z0-9]', '', strs)

# check palindrome (using slicing)
print(strs == strs[::-1])
