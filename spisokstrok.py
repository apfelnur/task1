def common_chars(words):
    result = []
    for char in set(words[0]):
        if all(word.count(char) > 0 for word in words):
            result.append(char)
    return result


print("common_chars(['bella', 'label', 'roller'])")
