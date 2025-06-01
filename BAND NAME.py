# This is a band name generator

print("\nHello! Welcome to the Band Name Generator!")
print("Ready to get the name of the next big internet sensation?")
print("Just answer a few question and you'll be all set.\n")

pet = input("What was your pet's name growing up? ").strip().title()
toy = input("What was your favourite toy growing up? ").strip().title()
city = input("What was the city you grew up in? ").strip().title()
celebrity = input("Who was your favourite celebrity growing up? ").strip().title()
if not pet or not toy or not city or not celebrity:
    print("Oops! Looks like you skipped a question. Please try again.")
    exit()  # or quit()

import random
names1 = (pet, toy)
names2 = (city, celebrity)
suffixes = ("Sucide", "Rebellion", "Imperial Empire", "Jack Sparrows")

# The f string makes the code look cleaner and { is a replacement for +
print(f"Your band name could be {random.choice(names1)} {random.choice(names2)} {random.choice(suffixes)}")