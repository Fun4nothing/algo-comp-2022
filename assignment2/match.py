import numpy as np
from typing import List, Tuple

def run_matching(scores: List[List], gender_id: List, gender_pref: List) -> List[Tuple]:

    """
    TODO: Implement Gale-Shapley stable matching!
    :param scores: raw N x N matrix of compatibility scores. Use this to derive a preference rankings.
    :param gender_id: list of N gender identities (Male, Female, Non-binary) corresponding to each user
    :param gender_pref: list of N gender preferences (Men, Women, Bisexual) corresponding to each user
    :return: `matches`, a List of (Proposer, Acceptor) Tuples representing monogamous matches

    Some Guiding Questions/Hints:
        - This is not the standard Men proposing & Women receiving scheme Gale-Shapley is introduced as
        - Instead, to account for various gender identity/preference combinations, it would be better to choose a random half of users to act as "Men" (proposers) and the other half as "Women" (receivers)
            - From there, you can construct your two preferences lists (as seen in the canonical Gale-Shapley algorithm; one for each half of users
        - Before doing so, it is worth addressing incompatible gender identity/preference combinations (e.g. gay men should not be matched with straight men).
            - One easy way of doing this is setting the scores of such combinations to be 0
            - Think carefully of all the various (Proposer-Preference:Receiver-Gender) combinations and whether they make sense as a match
        - How will you keep track of the Proposers who get "freed" up from matches?
        - We know that Receivers never become unmatched in the algorithm.
            - What data structure can you use to take advantage of this fact when forming your matches?
        - This is by no means an exhaustive list, feel free to reach out to us for more help!
    """
    matches = [()]

    halfListSize = int(len(scores)/2)

    emptyMatch = (0, 0)
    for i in range(halfListSize):
        matches.append(emptyMatch)

    proposers = scores[:halfListSize]
    receivers = scores[halfListSize:]

    taken = [False for i in range(len(proposers))]

    while not all(flag is True for (flag) in taken):
        for i in range(len(receivers)):
            compatibility = 0.0
            bestMatch = (0, 0)
            for j in range(len(proposers)):
                proposerIndex = halfListSize + j
                currCompatibility = 0.0

                if gender_pref[i] == "Men" or "Bisexual":
                    if gender_id[proposerIndex] == "Male":
                        currCompatibility = scores[i][proposerIndex]
                elif gender_pref[i] == "Women" or "Bisexual":
                    if gender_id[proposerIndex] == "Female":
                        currCompatibility = scores[i][proposerIndex]

                print(currCompatibility)

                if currCompatibility > compatibility and taken[j] is False:
                    compatibility = currCompatibility
                    bestMatch = (proposerIndex, i)

            taken[bestMatch[0] - halfListSize] = True
            matches[i] = bestMatch

    for i in range(5):
        print(matches[i])

    return matches

if __name__ == "__main__":
    raw_scores = np.loadtxt('raw_scores.txt').tolist()
    genders = []
    with open('genders.txt', 'r') as file:
        for line in file:
            curr = line[:-1]
            genders.append(curr)

    gender_preferences = []
    with open('gender_preferences.txt', 'r') as file:
        for line in file:
            curr = line[:-1]
            gender_preferences.append(curr)

    gs_matches = run_matching(raw_scores, genders, gender_preferences)
