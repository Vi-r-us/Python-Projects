# Create a dictionary and take input from the user and return the meaning of the word from the dictionary
apni_dict = { "barista":"a person whose job involves preparing and serving different types of coffee" ,
"butthurt": "inappropriately strong negative emotional response from a perceived personal insult strong feelings of shame" ,
"clickbait" : "online content to attract more visitors to a particular website" ,
"awesomesauce" : "extremely good; excellent" ,
"catastrophize" : "present a situation as worse than it is"
}

#To get a specific meaning
print("Enter the word you want the meaning of ")
key = input()
print("You have entered ",key,"which means-\n",apni_dict[key])
print("Enter a key ")

#to add a key-value pair
key1 = input()
print("Enter the value")
value1 = input()
apni_dict.update( {key1:value1} )
print(apni_dict)

#to remove a specific key 
print("Enter the key you want to remove ")
rem_key = input()
apni_dict.pop(rem_key)
print(apni_dict)
