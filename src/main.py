
print(f"NUMBER-COMMONATOR")

text_commanated = ""
with open("original/text.txt", "r") as file:

    text = f"{file.read()} "

    digit_indexend = -1
    for (index, char) in enumerate(text):
        if not char.isdigit():
            text_commanated += char # ADD CHAR
        else:
            # build entire digitword w/ commas
            if digit_indexend == -1 or digit_indexend < index:
                # get digitword
                digitword = ""
                digit_index = index
                digit_char = char
                while digit_char.isdigit() and digit_index+1 <= (len(text)-1):
                    digitword += digit_char
                    digit_index += 1
                    digit_char = text[digit_index]
                digit_indexend = digit_index
                # commonate digitword
                digitword_backwards = ""
                i_counter = 0
                for i in range(len(digitword)-1, -1, -1):
                    digitword_backwards += f"{digitword[i]}" # the char
                    i_counter += 1
                    if i_counter >= 3 and i != 0:
                        digitword_backwards += "," # the comma
                        i_counter = 0
                digitword = "".join(reversed(digitword_backwards))
                text_commanated += digitword # ADD DIGITWORD
                print(f"✓ found {digitword}")

with open("edited/text.txt", "w") as file:
    file.write(text_commanated)
    print(f"SAVED TO: edited/text.txt")