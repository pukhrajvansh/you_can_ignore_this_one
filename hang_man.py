
import random
anymore = False
while not anymore:
    words = ["apple", "cake", "play", "easy", "gate", "day", "use", "make", "year", "game", 
            "bay", "fun", "cute", "run", "key", "lay", "bake", "blue", "happy", "stay"]

    ran_word = random.choice(words)
    length_word = len(ran_word)
    ran_list = list(ran_word)
    blanks = ("_" * length_word)
    list_bl = list(blanks)
    wrong_guess = 0
    stages = {
        "1": """
        -----
        |   |
            |
            |
            |
            |
        =========
        """,
        "2": """
        -----
        |   |
        O   |
            |
            |
            |
        =========
        """,
        "3": """
        -----
        |   |
        O   |
        |   |
            |
            |
        =========
        """,
        "4": """
        -----
        |   |
        O   |
       /|   |
            |
            |
        =========
        """,
        "5": """
        -----
        |   |
        O   |
       /|\  |
            |
            |
        =========
        """,
        "6": """
        -----
        |   |
        O   |
       /|\  |
       /    |
            |
        =========
        """,
        "7": """
        -----
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========
        """
    }
    


    





    goal = False
    
    while not goal:
        stages_no = str(wrong_guess + 1)
        askii = stages[stages_no]
        print("\n" * 100)
        print(askii)
        print(f"you can guess the range of letter by these blanks underscore \n{''.join(list_bl)}")
        use = input("guess the letters").lower()
        listt = list(use)
        for index, element in enumerate(ran_list):
            for user in listt:

                if user == element:
                    list_bl[index] = user
                
                    if "_" not in list_bl:
                    
                        goal = True
                        print(f"{''.join(list_bl)} \nyou won the game\n")
        if user not in ran_list:
            wrong_guess += 1    
            
        if wrong_guess == 7:
            goal = True
            ac_word = ran_word        
            print(f"{''.join(list_bl)} /ngame over\nthe actual word was '{ac_word}'")                
        
        
                    
    
    ask = input("press enter for play it again or press n for over the game").lower()
    if ask == "n":
        anymore = True