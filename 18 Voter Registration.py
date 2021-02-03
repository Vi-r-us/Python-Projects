import pickle

print("Welcome to the Voter Registration App.")

name = input("Please enter your name: ").title().strip()
age = int(input("Please enter your age: "))

if age > 17:
    print(f"\nCongratulations {name}! You are old enough to register to vote."
          f"\nHere ia a list of political parties to join.")

    f = open('18_parties.pkl', 'rb')
    parties = pickle.load(f)
    # parties = {'Republican': [...], 'Democratic': [...], 'Independent': [...], 'Libertarian': [...], 'Green': [...]}

    for party in parties.keys():
        print(f"\t-{party}")
    chosen_party = input("\nWhat party would you like to join: ").title().strip()

    if chosen_party in parties.keys():
        if name not in parties[chosen_party]:
            print(f"\nCongratulations {name}! You have joined the {chosen_party} party!.")

            if chosen_party == 'Republican' or chosen_party == 'Democratic':
                print("This is a major party!")
            elif chosen_party == 'Independent':
                print("You are an independent person!")
            else:
                print("This is not a major party.")

            parties[chosen_party].append(name)

            f = open('18_parties.pkl', 'wb')
            pickle.dump(parties, f)
            f.close()
        else:
            print("You are already in this party.")
    else:
        print("That is not a given party.")
    f.close()
else:
    print("\nYou are not old enough to register to vote.")
