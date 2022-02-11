def fizz_buzz(input):
    output = ""
    if input % 3 == 0:
        output += "Fizz"
    if input % 5 == 0:
        output += "Buzz"
    else:
        output = f"{input}"
    return output


print(fizz_buzz(14))
