def cipher(step, text):
    result = ''
    lower_letter = ord('a')
    upper_letter = ord('A')
    for char in text:
        if char.isalpha():
            if char.islower():
                start_letter = lower_letter
            else:
                start_letter = upper_letter
            result += chr(
                (ord(char) + step - start_letter) % 26 + start_letter
            )
        else:
            result += char
    return result


def main(text):
    punctuation = '.,?!"=()'
    result = []
    for word in text.split():
        length = len(word)
        if word[0] in punctuation:
            length -= 1
        if word[-1] in punctuation:
            length -= 1
        result.append(cipher(length, word))
    print(' '.join(result))


text = input()

main(text)
