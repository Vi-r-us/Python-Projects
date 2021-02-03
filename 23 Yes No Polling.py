print("Welcome to the Yes or No Issue Polling App.")

votes = {}
issue = input("\nWhat is the yes or no issue  you will be voting on today: ").capitalize().strip()
no_of_votes = int(input("What are the number of voters you will allow on the issue: "))
yes = 0
no = 0

for i in range(no_of_votes):
    name = input("\nEnter your full name: ").title().strip()
    if name not in votes.keys():
        print(f"Here's the issue: {issue}")
        vote = input("What do you think?....yes or no: ").lower()
        if vote == 'yes':
            yes += 1
        elif vote == 'no':
            no += 1
        else:
            print("That is not a yes or no answer, but okay...")
        print(f"Thank you {name}! Your vote of {vote} has been recorded.")
        votes[name] = vote
    else:
        print("Sorry, it seems that you someone with that name has already voted.")

print(f"\nThe following {len(votes)} people voted:")
for key in votes.keys():
    print(key)

print(f"\nOn the following issue: {issue.lower()}")
if yes > no:
    print(f"Yes Wins! {yes} votes to {no}.")
elif no > yes:
    print(f"No Wins! {no} votes to {yes}.")
else:
    print(f"It was a tie! {yes} votes to {no}.")

ch = input("\nDo you want to see the voting results (yes/no): ").lower().strip()
if ch == 'yes':
    for key, value in votes.items():
        print(f"Voter: {key}\t\t\t\tVote: {value}")

print("Thank You for using Yes or No Issue Polling App.")
