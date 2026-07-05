def write_review(name, message):

    try:
        with open("quest_book.txt", "a") as file:
            
            file.write(f"Quest : {name} | Message : {message} \n")
            return "Your review is successfully saved. Thankyou!"
        
    except IOError:
        return "System error: Message could not be saved!"