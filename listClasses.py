classList = []
classes = int(input("how many classes are you taking this semester? "))
i = 0
while i < len(range(classes)):
    name = input("Enter the name of the class ")
    classList.append(name)
    i+=1
for className in classList:
    print(className)


