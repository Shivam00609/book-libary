print("Welcome to my library")
x = input("Enter your name : ")
print("Welcome to", x)

def run():
    print("press 1 to continue")
    print("press 2 to exit")
    a = int(input("Enter no. continue or exit : "))
    if a == 1:
        book()
    elif a == 2:
        print("Thanks for visit")
    else:
        print("Invalid input no.")
        run()

def book():
    print("press 1 to MAHABHARAT")
    print("press 2 to RAMAYANA")
    print("press 3 to SHIV")
    print("press 4 to BHAGVATGITA")
    print("press 5 to HANUMAN")

    b = int(input("Enter book no. : "))

    if b == 1:
        print("""
MAHABHARAT: 
The Mahabharat is a major Sanskrit epic describing the struggle between 
Pandavas and Kauravas, leading to the great Kurukshetra war.
""")
        run()

    elif b == 2:
        print("""
RAMAYAN:
The Ramayana tells the story of Lord Rama’s journey to rescue Sita 
from the demon king Ravana.
""")
        run()

    elif b == 3:
        print("""
SHIV TANDAV:
Shiv Tandav is the cosmic dance of Lord Shiva symbolizing creation, 
preservation, and destruction. It represents infinite divine energy.
""")
        run()

    elif b == 4:
        print("""
BHAGAVAT GITA:
The Bhagavad Gita is a dialogue between Krishna and Arjuna, explaining 
duty (dharma), devotion, and the path to liberation.
""")
        run()

    elif b == 5:
        print("""
HANUMAN:
Hanuman is the mighty devotee of Lord Rama. He gives courage, removes 
fear, and brings strength, peace, and victory in life.
""")
        run()

    else:
        print("Invalid Input")
        run()
book()
