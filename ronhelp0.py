
def word_in_string_list(words: str, word: list[str]) -> bool:
    index = 0
    while index < len(words):
        if words[index] == word:
            return True
        index += 1
    return False # we only get here if the if in the loop is never reached


print(word_in_string_list(["no", "Yes", "yesnt", "silvivivibea", "test"], "test"))
