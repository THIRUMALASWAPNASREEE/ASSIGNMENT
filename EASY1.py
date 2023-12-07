Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal 
substring consisting of non-space characters only.
def length_of_last_word(s):
    words = s.split()
    if not words:
        return 0
    return len(words[-1])

while True:
    s = input()
    if 1 <= len(s) <= 104 and all(ch.isalpha() or ch.isspace() for ch in s):
        break
   
result = length_of_last_word(s)
print(result)
