
print(f"NUMBER-COMMONATOR\n")
numbers_to_commanate = {}

# GET THE numbers_to_commanate
with open("original/text.txt", "r") as file:
    for line in file:

        i_start = -1
        for index, char in enumerate(line):
            if char.isdigit():
                if i_start == -1:
                    # start new number
                    i_start = index
            else:
                if i_start != -1:

                    # end new number
                    number = line[i_start:index]
                    i_start = -1

                    # add commas
                    print(f"====> FOUND: {number}")
                    numberfixed_backwards = ""
                    d_counter = 0
                    for d in range(len(number)-1, -1, -1):
                        numberfixed_backwards += number[d]
                        d_counter += 1
                        if d_counter >= 3 and d != 0:
                            numberfixed_backwards += ","
                            d_counter = 0
                    numberfixed = "".join(reversed(numberfixed_backwards))
                    numbers_to_commanate[number] = numberfixed
                    print(numberfixed)

# USE THE numbers_to_commanate
filecontent = ""
with open("original/text.txt", "r") as file:
    filecontent = file.read()
text = ""
for item in filecontent.split(" "):
    if item in numbers_to_commanate:
        item = numbers_to_commanate[item]
    text += f"{item} "
with open("edited/text.txt", "w") as file:
    file.write(text)
print("\nREPLACED TEXT!")