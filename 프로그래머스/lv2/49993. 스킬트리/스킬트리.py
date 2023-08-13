def solution(skill, skill_trees):
    result = 0
    for skill_tree in skill_trees:
        skills = list(skill)
        for spell in skill_tree:
            if skills and skills[0] == spell:
                skills.pop(0)
            elif spell in skills:
                break
        else:
            result += 1
    return result