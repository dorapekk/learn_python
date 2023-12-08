from person import Person
import random 

PEOPLE = [
    Person(first_name="Dora", last_name="Pekk-Juhasz", sex="female"),
    Person(first_name="Zsolt", last_name="Tasnadi", sex="male"),
    Person(first_name="Balazs", last_name="Bellanyi", sex="male"),
    Person(first_name="Blanka", last_name="Szigethy", sex="female"),
]

def drawed_example():
    tasi = PEOPLE[1]
    manci = PEOPLE[0]
    manci.set_drawed(tasi)
    print(manci.drawed.get_full_name())

drawed_example()

def main():
    random.shuffle(PEOPLE)
    i = 0
    while i < len(PEOPLE):
        person = PEOPLE[i]
        print(person.get_full_name())
        i = i + 1

main()
