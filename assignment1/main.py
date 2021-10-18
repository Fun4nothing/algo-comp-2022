#!usr/bin/env python3
import json
import sys
import os

INPUT_FILE = 'testdata.json'  # Constant variables are usually in ALL CAPS


class User:
    def __init__(self, name, gender, preferences, grad_year, responses):
        self.name = name
        self.gender = gender
        self.preferences = preferences
        self.grad_year = grad_year
        self.responses = responses


# Takes in two user objects and outputs a float denoting compatibility
def compute_score(user1, user2):
    # Immediately check to see whether gender preferences match with user genders
    # Todo later implement this with an iterable solution if preferences is greater than length 1
    if not (user1.gender == user2.preferences[0] and user2.gender == user1.preferences[0]):
        return 0.0

    total_score = 0.0

    """
    Grad year comparison
    A greater difference in grad years yields a lower total score 4 - difference
    This is significantly lower weight than the responses section (1/6 of compatibility)
    """
    total_score += 4 - abs(user1.grad_year - user2.grad_year)

    """
    Look at responses here to differentiate differences
    This is the most important part of defining total score
    """
    # Basic comparing function to check if responses to questions are the same
    for i in range():
        if user1.responses[i] == user2.responses[i]:
            total_score += 1

    # Normalize score between 0 - 1 given 24 possible points
    return total_score / 24.0


if __name__ == '__main__':
    # Make sure input file is valid
    if not os.path.exists(INPUT_FILE):
        print('Input file not found')
        sys.exit(0)

    users = []
    with open(INPUT_FILE) as json_file:
        data = json.load(json_file)
        for user_obj in data['users']:
            new_user = User(user_obj['name'], user_obj['gender'],
                            user_obj['preferences'], user_obj['gradYear'],
                            user_obj['responses'])
            users.append(new_user)

    for i in range(len(users) - 1):
        for j in range(i + 1, len(users)):
            user1 = users[i]
            user2 = users[j]
            score = compute_score(user1, user2)
            print('Compatibility between {} and {}: {}'.format(user1.name, user2.name, score))
