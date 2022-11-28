logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
d = dict()
risposta = True
while risposta == True:
    name = input("What s your name:")
    price = int(input("Place your bid?"))
    d[name] = price
    others = input("Are the any others?")
    if others == "no":
        risposta = False
n = 0
winner = ""

for x in d:
    if n < d[x]:
        n = d[x]
        winner = x

print(f"The winner is {winner} with {n} !!")
print(logo)


