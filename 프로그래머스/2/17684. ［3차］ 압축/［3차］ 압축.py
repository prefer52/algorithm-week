def solution(msg):
    msg_dict = {chr(i):i - ord('A') + 1 for i in range(ord('A'), ord('Z') + 1)}
    result = []
    start, nxt = 0, 1
    while start < len(msg):
        new_msg = msg[start]
        while nxt < len(msg) and new_msg + msg[nxt] in msg_dict:
            new_msg += msg[nxt]
            nxt += 1
        result.append(msg_dict[new_msg])
                
        if nxt < len(msg):
            msg_dict[new_msg + msg[nxt]] = len(msg_dict) + 1
        start = nxt
        nxt += 1
    
    return result