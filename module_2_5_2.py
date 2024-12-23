def single_root_words(root_word, *other_words):
    root_word = root_word.lower()
    same_words = []
    for word in other_words:
        if root_word in word.lower() or word.lower() in root_word:
            same_words.append(word)
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichlcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)