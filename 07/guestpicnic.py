import pprint

all_guests = {
    "Alice": {"apples": 5, "pretzels": 12},
    "Bob": {"ham sandwiches": 3, "apples": 2},
    "Carol": {"cups": 3, "apple pies": 1},
}


def total_brought(guests, item):
    """Articles apportés"""
    num_brought = 0
    for v in guests.values():
        num_brought = num_brought + v.get(item, 0)
    return num_brought


print("\nNumber of things being brought:")
print(f" - Apples         {total_brought(all_guests, 'apples')}")
print(f" - Cups           {total_brought(all_guests, 'cups')}")
print(f" - Cakes          {total_brought(all_guests, 'cakes')}")
print(f" - Ham Sandwiches {total_brought(all_guests, 'ham sandwiches')}")
print(f" - Apple Pies     {total_brought(all_guests, 'apple pies')}")

print()
print(all_guests)
print()
pprint.pprint(all_guests)
