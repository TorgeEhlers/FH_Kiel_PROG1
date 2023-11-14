
# Liste erzeugen
todo = []

# Element dazu
todo.append("Python lernen")
todo.append("Einkaufen gehen")
todo.append("Python lernen")
todo.insert(0,"Geld abheben")
todo.remove("Python lernen")


for i, elem in enumerate(todo):
    print(f"An der Stelle {i} ist {elem}")

