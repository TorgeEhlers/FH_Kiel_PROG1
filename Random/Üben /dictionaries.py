# liste = ["Torge", 19, True]

kontakte = {"Torge": 1721231, 
            "Ove": 1248613794,
            "Tilo": 9021748364}


print(kontakte["Torge"])
print(f"Die Telefeonnummer von Ove lautet", kontakte["Ove"])
print(kontakte.keys())
print(kontakte.values())
print(kontakte.items())
print(kontakte.keys("Torge"))