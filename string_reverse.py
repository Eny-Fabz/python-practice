# This is the practice to try and have the word I supply, written backwards
def string_reverse(text):
    text_reversed = '' # So for this to work without [::-1], I found out we need to first initialize a variable with an empty string
    for char in text:
        text_reversed = char + text_reversed # This will take the first character and place it 1st. Then it will successively add the 2nd char to the front of the 1st. It continues in this manner till the last char
    return text_reversed # In this way the text has been reversed
# So using my name as an example word, it will display...
print(string_reverse('Eniola'))