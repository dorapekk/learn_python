SHOTS = [
    "gin",
    "palinka",
    "vodka",
    "whiskey",
    "tequila",
    ]

j = 0
while j < len(SHOTS):
    print(SHOTS[j])
    j = j + 1

PEOPLE = [
{
    "first_name": "Bubu",
    "last_name": "Szigethy",
    "favourite": "whiskey",
 },
{   
    "first_name": "Tasi",
    "last_name": "Tasnadi",
    "favourite": "tequila",
},
{   
    "first_name": "Balazs",
    "last_name": "Bellanyi",
    "favourite": "palinka",
},
{   
    "first_name": "Dora",
    "last_name": "Pekk-Juhasz",
    "favourite": "vodka",
},
{   
    "first_name": "Erika",
    "last_name": "Juhasz",
    "favourite": "gin",
}
]



i = 0
while i < len(PEOPLE):
    first_name = PEOPLE[i]["first_name"]
    last_name = PEOPLE[i]["last_name"]
    print(f"{first_name} {last_name} ")
    i = i + 1

