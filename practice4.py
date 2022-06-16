#5. Write a Python Program to Remove Punctuation From a String?
import string
str = "Hello! My name is - Prateek. My Father's name is Dinesh Singh.(Mother's name - 'Shakuntla Devi')"
for i in str:
    if i in string.punctuation:
        str = str.replace(i,'')
print(str)
