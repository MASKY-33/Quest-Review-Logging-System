from quest_management.logic import write_review

while True:
    name_request = input("Give your name here: ").lower()

    if name_request == "stop":
        print("Thankyou, Bye!")
        break

    short_mssg_request = input("Give your review here: ").lower()

    review_result = write_review(name_request, short_mssg_request)
    print(review_result)