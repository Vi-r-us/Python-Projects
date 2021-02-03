print("Welcome to the Frequency Analysis App.")


def string_with_letters(x):
    val = list([val for val in x if val.isalpha()])
    result = "".join(val)
    return result


counter = 1
while True:
    content = input("\n\nEnter a word/phrase to count the occurrence of each letter: ").lower().strip()
    content = string_with_letters(content)
    alpha = []
    occurrence = []

    for i in range(len(content)):
        if content[i] not in alpha:
            alpha.append(content[i])

    for i in alpha:
        occurrence.append(int(content.count(i)))

    print(f"\nHere is the frequency analysis from key phrase {counter}")
    print("\t Letter \t Occurrence \t Percentage ")
    for i in range(len(alpha)):
        print(f"\t {alpha[i]} \t\t\t {occurrence[i]} \t\t\t\t{round( 100*occurrence[i]/len(content), 2)}%")

    sorted_alpha = []
    occurrence2 = occurrence.copy()
    occurrence.sort()
    occurrence.reverse()

    for i in range(len(alpha)):
        j = occurrence2.index(occurrence[i])
        occurrence2.remove(occurrence2[j])
        sorted_alpha.append(alpha[j])
        alpha.remove(alpha[j])

    print("\nLetters Ordered from Highest to Lowest:")
    for ele in sorted_alpha:
        print(ele, end='')

    ch = input("\n\nWant to try this again? (yes/no)").lower()
    if ch == 'yes':
        continue
    else:
        break
