def flames_relationship(person1, person2):
    name1 = person1.replace(" ", "").lower()
    name2 = person2.replace(" ", "").lower()
    unique_characters = list(set(name1 + name2))
    common_count = 0
    for char in unique_characters:
        if char in name1 and char in name2:
            common_count += 1
    relationship_index = (len(name1) + len(name2)) - 2 * common_count
    flames_dict = {
        0: "Friends",
        1: "Lovers",
        2: "Admirers",
        3: "Married",
        4: "Enemies",
        5: "Siblings"
    }
    relationship = flames_dict[relationship_index % 6]
    return relationship
person1 = input("Enter the first person's name: ")
person2 = input("Enter the second person's name: ")
relationship = flames_relationship(person1, person2)
print("The relationship between", person1, "and", person2, "is:", relationship)
