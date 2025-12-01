total_zeros = 0


dial_pos = 50

with open('input') as f:
    while f:
        input_line = f.readline()
        if input_line != "":
            input_line = input_line.rstrip("\n")
            amount  = int(input_line[1:])


            if input_line[0] == "L": 
                if (dial_pos - amount) < 0:
                    total_zeros += abs((100 + dial_pos - amount) // 100)
                    if dial_pos != 0:
                        total_zeros += 1

                dial_pos += 100
                dial_pos = (dial_pos - amount) % 100
                
                if dial_pos == 0:
                    total_zeros += 1

            elif input_line[0] == "R":
                total_zeros += (dial_pos + amount) // 100
                dial_pos = (dial_pos + amount) % 100


        else:
            break

print(total_zeros)


