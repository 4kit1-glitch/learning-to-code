def reverse_sentence(sentence):
    word_list = sentence.split()
    reversed_list = list(reversed(word_list))
    reversed_sentence = ' '.join(reversed_list).capitalize()
    return reversed_sentence

print(reverse_sentence("Reverse this sentence"))