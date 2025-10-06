from itertools import combinations
from collections import Counter

def solution(dice):
    max_win_rate = 0
    dice_cases = list(combinations(range(len(dice)), len(dice)//2))
    for i in range(len(dice_cases)//2):
        first_results, second_results = [], []
        get_all_cases(dice, dice_cases[i], 0, 0, first_results)
        get_all_cases(dice, dice_cases[-(i+1)], 0, 0, second_results)
        first_score_counts, second_score_counts = Counter(first_results), Counter(second_results)
        first_acc, second_acc = [0]*501, [0]*501
        for score in first_score_counts.keys():
            first_acc[score] = first_score_counts[score]
        
        for score in second_score_counts.keys():
            second_acc[score] = second_score_counts[score]
        
        for score in range(1, 501):
            first_acc[score] += first_acc[score-1]
            second_acc[score] += second_acc[score-1]
            
        first_wins, second_wins = 0, 0
        for score in first_score_counts.keys():
            first_wins += second_acc[score-1]*first_score_counts[score]
        for score in second_score_counts.keys():
            second_wins += first_acc[score-1]*second_score_counts[score]
        
        if first_wins > second_wins and first_wins > max_win_rate:
            win_comb, max_win_rate = dice_cases[i], first_wins
        elif first_wins < second_wins and second_wins > max_win_rate:
            win_comb, max_win_rate = dice_cases[-(i+1)], second_wins
        print(dice_cases[i], first_wins)
        print(dice_cases[-(i+1)], second_wins)
    
    return [i+1 for i in win_comb]
    
def get_all_cases(dices, seq, index, dice_sum, result):
    if index == len(seq):
        result.append(dice_sum)
        return

    for i in range(6):
        get_all_cases(dices, seq, index+1, dice_sum + dices[seq[index]][i], result)