def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        total_legs = (num_chickens * 2) + (num_rabbits * 4)
        if total_legs == numlegs:
            return num_chickens, num_rabbits
    return None, None

numheads = int(input())
numlegs = int(input())

chickens, rabbits = solve(numheads, numlegs)

if chickens is not None:
    print(f"Number of chicens: {chickens}")
    print(f"Number of rabbits: {rabbits}")
else:
    print("No solution found.")