word=input().lower()
vowel="aoueiy"
result =''
for cha in word:
    if cha not in vowel:
        result+='.'
        result+=cha
print(result)
