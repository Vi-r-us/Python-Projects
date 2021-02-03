name = input("\nWhat's your name? : ")
print(f"\nHello {name} !!\nI will count the number of times a specific letter or "
      f"special character occurs in a message.")
message = input("\nPlease Enter a message : ")
letter = input("Which Letter you want to count the occurrences of : ")
message = message.lower()
letter = letter.lower()
print(f"{name}, your message has {message.count(letter)}'s in it.")
