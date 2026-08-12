
print(f"number-commanator")
text = None
digitwords_to_replace = {}

# GET THE digitwords_to_replace
with open("original/text.txt", "r") as file:

    for line in file:
        for word in line.split(" "):
            if word.isdigit():
                if int(word) > 999:

                    # digitwords_to_replace
                    digitword_backwards = ""
                    index_counter = 0

                    for i in range(len(word)-1, -1, -1):

                        index_counter += 1

                        digitword_backwards += f"{word[i]}" # the number
                        if index_counter == 3 and i > 0:
                            digitword_backwards += f"," # the comma
                            index_counter = 0
                    
                    digitword = "".join(reversed(digitword_backwards))
                    digitwords_to_replace[word] = digitword # add the digitword
                    print(f"✓ found {word} vs. {digitword}")

# USE THE digitwords_to_replace
with open("original/text.txt", "r") as file:
    text = file.read() # get text

for digitword, replacement in digitwords_to_replace.items():
    text = text.replace(digitword, replacement) # replace the digitword in text

with open("edited/text.txt", "w") as file:
    file.write(text) # file with the edited text
    print("REPLACED TEXT!")