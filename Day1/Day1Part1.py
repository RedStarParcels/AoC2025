total_zeros = 0


dial_pos = 50

with open('input') as f:
    while f:
        input_line = f.readline()
        if input_line != "":
            input_line = input_line.rstrip("\n")
            
            if input_line[0] == "L":
                dial_pos = dial_pos + 100
                dial_pos = (dial_pos - int(input_line[1:])) % 100

            elif input_line[0] == "R":
                dial_pos = (dial_pos + int(input_line[1:])) % 100

            if dial_pos == 0:
                total_zeros += 1

        else:
            break

print(total_zeros)


