def solution(skill, skill_trees):
    result = 0
    for skill_tree in skill_trees:
        skills = list(skill)
        for spell in skill_tree:
            if spell in skills:
                if skills[0] == spell:
                    skills.pop(0)
                else:
                    break
        else:
            result += 1
    return result