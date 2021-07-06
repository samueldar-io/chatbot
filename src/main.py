import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty= 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words = []):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    #Response ----------------------------------------------------------------------
    response('Hola!', ['hola', 'hey', 'buenos dias', 'buenas tardes', 'buenas noches'], single_response=True)
    response('Estoy bien y tu?', ['como','estas'], required_words=['como','estas'])
    response('Gracias', ['me','gusta','krowdfund.me'], required_words=['gusta'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    print (highest_prob_list)
    return best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

while True:
    print('Bot: ' + get_response(input('Tu: ')))