#modifying Global Scope

enemies=1

def increases_enemies(enemy):

    print(f"enemies inside function: {enemies}")
    return enemy+1

enemies=increases_enemies(enemies)
print(f"enemies outside function: {enemies}")