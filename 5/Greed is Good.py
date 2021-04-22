"""
Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point

A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)

In some languages, it is possible to mutate the input to the function. This is something that you should never do. If you mutate the input, you will not be able to pass all the tests.
"""
def score(dice):
    score = 0
    score_dict = {"1":1000, "2":200, "3":300, "4":400, "5":500, "6":600}
    dice_set = set(dice)
    for element in list(dice_set):
        if dice.count(element) >= 3 and element not in [1,5]:
            score += score_dict[str(element)]

        elif dice.count(element) >= 3 and element == 1:
            score += score_dict[str(element)] + ((dice.count(element) - 3)*100)
        elif dice.count(element) >= 3 and element == 5:
            score += score_dict[str(element)] + ((dice.count(element) - 3)*50)
            
        elif dice.count(element) < 3 and element == 1:
            score += dice.count(element) * 100
        elif dice.count(element) < 3 and element == 5:
            score += dice.count(element) * 50

    return score
    
print(score([2, 4, 4, 5, 4]))