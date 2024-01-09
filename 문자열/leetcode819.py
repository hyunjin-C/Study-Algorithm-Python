# 금지된 단어를 제외한 가장 흔하게 등장하는 단어
# 대소문자 구분X, 구두점(마침표, 쉼표) 무시
import re
import collections


def mostCommonWord(paragraph, banned):
    paragraph = paragraph.lower()
    paragraph = re.sub('[^a-z]', ' ', paragraph).split()

    paragraph = [value for value in paragraph if value not in banned]

    counter = collections.Counter(paragraph).most_common(1)
    return counter[0][0]


print(mostCommonWord(
    "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))

print(mostCommonWord("a.", []))

print(mostCommonWord("Bob. hIt, baLl", ["bob", "hit"]))
