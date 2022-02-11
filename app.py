def fizz_buzz(input):
    output = ""
    if input % 3 == 0:
        output += "Fizz"
    if input % 5 == 0:
        output += "Buzz"
    if not output:
        output = f"{input}"
    return output


for i in range(0, 100):
    print(fizz_buzz(i))
