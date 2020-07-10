# 函数练习 2

"""
    统计考试成绩,包括：平均分，对所有人按成绩从高到低排队，谁成绩最好，谁成绩最差。
"""


def average_score(scores):
    """
    Calculating the average score.
    """
    return float(sum(scores.values())) / len(scores.values())


def descending_score(scores):
    """
    Sort the input list from largest to smallest.
    """
    scores_list = [(scores[x], x) for x in scores]
    descending_list = sorted(scores_list, reverse=True)
    return [(x[1], x[0]) for x in descending_list]


def highest_score(scores):
    """
    Find the highest grade and the corresponding name.
    """
    descending_list = descending_score(scores)
    highest_score = descending_list[0][1]
    return [(x[0], x[1]) for x in descending_list if x[1] == highest_score]


def lowest_score(scores):
    """
    Find the lowest grade and the corresponding name.
    """
    descending_list = descending_score(scores)
    lowest_score = descending_list[-1][1]
    return [(x[0], x[1]) for x in descending_list if x[1] == lowest_score]


if __name__ == "__main__":
    examine_scores = {
        "google": 98,
        "facebook": 99,
        "baidu": 52,
        "alibaba": 80,
        "yahoo": 49,
        "github": 49,
        "IBM": 70,
        "android": 76,
        "apple": 99,
        "amazon": 99,
    }

    average_score = average_score(examine_scores)  # 平均分
    print("The average grade is: " + str(average_score))

    descending_score_name = descending_score(examine_scores)  # 降序排列
    print(
        "The results in descending order of performance are: "
        + str(descending_score_name)
    )

    highest_score_name = highest_score(examine_scores)  # 最好成绩
    print("The highest grades and corresponding names are: " + str(highest_score_name))

    lowest_score_name = lowest_score(examine_scores)  # 最差成绩
    print("The lowest grades and corresponding names are: " + str(lowest_score_name))
