from validation import validation_positive_num, validation_text
def num_input(msg):
    user_num_input = ""
    while not validation_positive_num(user_num_input):
        user_num_input = input(msg)
    return int(user_num_input)

def text_input(msg):
    user_text_input = input(msg)
    return user_text_input