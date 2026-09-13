str = input('Enter a string: ').lower()
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
consonant_count = 0
for ch in str:
    if ch in vowels:
        vowel_count += 1
    elif ch.isalpha():
        consonant_count += 1
print('vowel count is : ', vowel_count)
print('Consonent count is : ', consonant_count)
