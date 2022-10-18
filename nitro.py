import requests
import random
import string
import time
num = int(input('Input How Many Codes to Generate: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")
with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")
        print(f"{nitro} ")
    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")
    input("Press Enter to continue.")