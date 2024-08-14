text = "Thank you everyone for being so kind, I am very happy to appear for this interview." 
first_occurrence = text.find("ery") 
second_occurrence = text.find("ery", first_occurrence + 1) 
word = text[second_occurrence-1:text.find(" ", second_occurrence)] 
output = (word, second_occurrence) 
print(output)