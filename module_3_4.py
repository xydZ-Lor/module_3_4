def single_root_words(root_word, *other_words):
    same_words = []
    rwu = root_word.upper()

    for i in other_words:
        owu = i.upper()
        if rwu in owu or owu in rwu:
            same_words.append(i)

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)