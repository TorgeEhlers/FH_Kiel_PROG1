
kontakte = {"Torge": 2004,
            "Ove": 2002,
            "Tilo": 2005}

print(kontakte["Ove"])
print(kontakte["Torge"])
kontakte.update({"Mika": 2003})
print(kontakte["Mika"])
kontakte.pop("Tilo")
print(f"Das Dictionary beinhaltet {len(kontakte)} Einträge!")
kontakte.update({"Torge": 2003})
print(kontakte)
