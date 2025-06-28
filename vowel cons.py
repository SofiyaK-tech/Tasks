def count_vowels_consonants(s):
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    vowels = consonants = 0

    for ch in s:
        if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
            lower = ch.lower()
            is_vowel = False
            for v in vowels_list:
                if lower == v:
                    vowels += 1
                    is_vowel = True
                    break
            if not is_vowel:
                consonants += 1
    return f"Vowels: {vowels}, Consonants: {consonants}"

print(count_vowels_consonants("Hello World"))
