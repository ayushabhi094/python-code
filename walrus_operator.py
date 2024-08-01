# walrus operator allows you to assign a value within expression

# The walrus operator allows us to assign a value to a variable and return that value, all in the same expression

all_words = ['hello', 'hi', 'welcome', 'world', 'oh', 'common']

for one_word in all_words:
    if(word_len := len(one_word) <4 ):
        print(f"the {one_word} has length {word_len}")