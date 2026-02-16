def string_calculator(s):
    digit_map = {
        "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3",
        "FOU": "4", "FIV": "5", "SIX": "6",
        "SEV": "7", "EIG": "8", "NIN": "9"
    }

    reverse_map = {v: k for k, v in digit_map.items()}

    for op in "+-*":
        if op in s:
            left, right = s.split(op)
            operator = op
            break

    def decode(part):
        num = ""
        for i in range(0, len(part), 3):
            num += digit_map[part[i:i+3]]
        return int(num)

    num1 = decode(left)
    num2 = decode(right)

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    else:
        result = num1 * num2

    if result == 0:
        return "ZER"

    output = ""
    for digit in str(result):
        output += reverse_map[digit]

    return output


s = input()
print(string_calculator(s))