def get_starting_number():
    while True:
        num_bottles = input("How many bottles of beer on the wall? ")
        if num_bottles.isdigit() and int(num_bottles) > 0:
            return int(num_bottles)
        else:
            continue

def sing(num_bottles):
    i = num_bottles
    for i in range(num_bottles, 0, -1):
        if i > 2:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down, pass it around, {i-1} bottles of beer on the wall.\n")
        if i == 2:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down, pass it around, {i-1} bottle of beer on the wall.\n")
        elif i == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.\nTake it down, pass it around, no more bottles of beer on the wall!")
            break