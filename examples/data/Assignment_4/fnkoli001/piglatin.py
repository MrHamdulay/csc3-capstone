def toPigLatin(s):
    words_from_str = str(s).split(" ")
    str_to_return = []
    for word in words_from_str:
        chars_to_move = ""
        cnt = 0
        prefix = "a"
        for char in word:
            if char.lower() in ['a', 'e', 'i', 'o', 'u']:
                if cnt == 0:
                    chars_to_move = "w"
                    prefix = ""
                    break
                else:
                    break
            else:
                chars_to_move += char
                cnt += 1
        str_to_return.append(word[cnt:] + prefix + chars_to_move + "ay")
    return " ".join(str_to_return)


def toEnglish(s):
    words_from_str = str(s).split(" ")
    str_to_return = []
    for word in words_from_str:
        if word[-3::1] == "way":
            str_to_return.append(word[:len(word) - 3:1])
        elif word[-2::1] == "ay":
            chars_to_move = ""
            cnt = 0
            for char in word[-3::-1]:
                if char == "a":
                    break
                else:
                    chars_to_move += char
                    cnt += 1
            str_to_return.append(chars_to_move[::-1] + word[:len(word) - cnt - 3:])
        else:
            return "NOT PIG LATIN!"
    return " ".join(str_to_return)