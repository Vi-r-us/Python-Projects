import random

print("Welcome to the Thesaurus App.")

meanings = {'Hot': ['balmy', 'boiling', 'scorching', 'summery', 'tropical'],
            'Cold': ['chilly', 'cool', 'freezing', 'frigid', 'polar'],
            'Happy': ['cherry', 'content', 'jocular', 'jovial', 'merry'],
            'Sad': ['downcast', 'glum', 'melancholy', 'miserable', 'unhappy']}

print("\nChoose a word from thesaurus and I will give you a synonym.")
print("\nHere are the words in the thesaurus:")
for key in meanings.keys():
    print(f"\t\t-{key}")

word = input("\nWhat words would you like a synonym for: ").title().strip()
if word in meanings.keys():
    random_meaning = random.choice(meanings[word])
    print(f"A synonym for {word} is {random_meaning}.")
else:
    print("Please choose the word from thesaurus only.")

whole = input("\nWould you like to see the whole thesaurus (yes/no):").lower().strip()
if whole == 'yes':
    for key, value in meanings.items():
        print(f"\n{key} synonyms are:")
        for ele in value:
            print("\t\t-", ele)

elif whole == 'no':
    print("I hope you enjoyed the program. Thank You!")
