# There is no Block Scope in Python

# if 3 > 2:
#     a_variable = 10

game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

create_enemy()

# Prime Number Checker
def is_prime(num):
    judge = True
    limit = 2
    while num != 1 and limit < num:
        if num % limit == 0:
            judge = False
            break
        limit += 1
    return judge

is_prime(75)





