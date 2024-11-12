def inquiry():
    answers={}
    answers['name']=input("What is your name?")
    answers['age']=input("How old are you?")
    answers['colour']=input("What color do you like?")
    answers['python']=input("Do you like python?")
    answers['flat']=input('World is flat.')
    if answers['python']=='True':
        python="do"
    else:
        python="do not"
    if answers['flat']=='True':
        flat="Congratulations! You are really clever!"
    else:
        flat="Congratulations! You are much more clever than I expected!"
    print(f"So your name is {answers['name']}, your age is {answers['age']}, your favourite colour is {answers['colour']}, you {python} like python. {flat}")

inquiry()