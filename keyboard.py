#Rewrite problem according to your needs
problem = ""
example_too_left = problem
example_too_right = problem

#Comment out these default examples after you entered problem above 
example_too_left = "ueuag rKJ AGIQ GIAR FEgN"
example_too_right = "YJR SMDERT YP YJOD [IXX;R OD YJR DOC VJSTSVYRT MS,R GPT YJR ,PDY VP,,PM LRUNPSTF ;SUPIY"

example_too_right = example_too_right
def main():
    print()
    print("Problem: ", example_too_right)
    print("Decoded: ", end="")

    for i in range(len(example_too_right)):
        if example_too_right[i].lower() in hand_is_too_right:
            print(hand_is_too_right[example_too_right[i].lower()], end="")
        else:
            print("1", end="")
    print()
    print("('1' means some error)")
    print()

    print("Problem: ", example_too_left)
    print("Decoded: ", end="")

    for i in range(len(example_too_left)):
        if i != len(example_too_left)-1:
            if (example_too_left[i] == " "):
                print(" ", end="")
            elif (example_too_left[i] in hand_is_too_left_lower) and (example_too_left[i+1] in hand_is_too_left_upper):
                print(hand_is_too_left_lower[example_too_left[i]], end="")
                print("a", end="")
            elif (example_too_left[i] in hand_is_too_left_upper) and (example_too_left[i+1] in hand_is_too_left_lower):
                print(hand_is_too_left_upper[example_too_left[i]], end="")
                print("a", end="")
            elif (example_too_left[i] in hand_is_too_left_lower):
                print(hand_is_too_left_lower[example_too_left[i]], end="")
            elif (example_too_left[i] in hand_is_too_left_upper):
                print(hand_is_too_left_upper[example_too_left[i]], end="")
            else:
                print("1")
        else:
            if (example_too_left[i] == " "):
                print(" ", end=" ")
            elif (example_too_left[i] in hand_is_too_left_lower):
                print(hand_is_too_left_lower[example_too_left[i]], end="")
            elif (example_too_left[i] in hand_is_too_left_upper):
                print(hand_is_too_left_upper[example_too_left[i]], end="")
            else:
                print("1")

    print()
    print("('1' means some error)")
    print()

hand_is_too_right = {
    "w":"q",
    "e":"w",
    "r":"e",
    "t":"r",
    "y":"t",
    "u":"y",
    "i":"u",
    "o":"i",
    "p":"o",
    "[":"p",
    "s":"a",
    "d":"s",
    "f":"d",
    "g":"f",
    "h":"g",
    "j":"h",
    "k":"j",
    "l":"k",
    ";":"l",
    "x":"z",
    "c":"x",
    "v":"c",
    "b":"v",
    "n":"b",
    "m":"n",
    ",":"m",
    " ":" "
}

hand_is_too_left_lower = {
    "   ":"q",
    "q":"w",
    "w":"e",
    "e":"r",
    "r":"t",
    "t":"y",
    "y":"u",
    "u":"i",
    "i":"o",
    "o":"p",
    "a":"s",
    "s":"d",
    "d":"f",
    "f":"g",
    "g":"h",
    "h":"j",
    "j":"k",
    "k":"l",
    "z":"x",
    "x":"c",
    "c":"v",
    "v":"b",
    "b":"n",
    "n":"m",
}

hand_is_too_left_upper = dict()

for item in hand_is_too_left_lower:
    hand_is_too_left_upper[item.upper()] = hand_is_too_left_lower[item]

main()