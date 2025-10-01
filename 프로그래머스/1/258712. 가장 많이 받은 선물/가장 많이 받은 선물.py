def solution(friends, gifts):
    friend_dicts = {friend:[{receiver:0 for receiver in friends}, {sender:0 for sender in friends}] for friend in friends}    
    for gift in gifts:
        sender, receiver = gift.split()
        friend_dicts[sender][0][receiver] += 1
        friend_dicts[receiver][1][sender] += 1
    
    gift_scores = {friend: sum(friend_dicts[friend][0].values()) - sum(friend_dicts[friend][1].values()) for friend in friends}
    
    max_gift_count = 0
    for friend in friends:
        gift_count = 0
        for other_friend in friends:
            if (friend_dicts[friend][0][other_friend] > friend_dicts[friend][1][other_friend]) or (friend_dicts[friend][0][other_friend] == friend_dicts[friend][1][other_friend] and gift_scores[friend] > gift_scores[other_friend]):
                gift_count += 1
        max_gift_count = max(max_gift_count, gift_count)
    
    return max_gift_count