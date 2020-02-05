text1 = input("enter :")
text2 = input('enter :')

if len(text1) < 1 or len(text2) < 1:
    print('not anagrams')

text1 = text1.upper()
text2 = text2.upper()

text1Adj = text1.replace(' ', '')
text2Adj = text2.replace(' ', '')
counter = 0
if len(text1Adj) == len(text2Adj):

    for i in text1Adj:
        for j in text2Adj:
            if i == j:
                counter += 1
                break

if counter == len(text1Adj):
    print("anagrams")
else:
    print("not anagrams")


#------------------------------------------------------
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# this is what we're going to do with both strings:
# - remove spaces
# - change all letters to upper case
# - convert into list
# - sort the list
# - join list's elements into string
# and finally, compare both strings
# Let's do it!

strx1 = ''.join(sorted(list(str1.upper().replace(' ', ''))))
strx2 = ''.join(sorted(list(str2.upper().replace(' ', ''))))
if len(strx1) > 0 and strx1 == strx2:
    print("Anagrams")
else:
    print("Not anagrams")

print(strx1)
print(strx2)