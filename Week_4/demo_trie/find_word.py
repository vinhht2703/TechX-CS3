arrChar = ["cat", "banana", "obama", "batman", "car", "cow", "alibaba"]

# ca => cat, car
# ba => banana, batman

getChar = input("Input keyword to search: ")

# O(N)
matchingWords = [word for word in arrChar if word.startswith(getChar)]

# Print result
if matchingWords:
    print("Matching words:", ", ".join(matchingWords))
else:
    print("No matching words found.")
