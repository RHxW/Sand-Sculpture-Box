import random


def gen_doors():
    # 用于生成随机列表，表示三扇门，[0,0,1] 表示第三扇门后面有奖品，或选手第一次选择，[1,0,0] 表示选手选择第一扇门。
    a = [0, 0, 0]
    a[random.randint(1, 3) - 1] = 1
    return a


def check(problem, answer):
    # 用于核对选手结果和正确答案，对1错0
    return 1 if 2 in [i + j for i, j in zip(problem, answer)] else 0


def reveal(problem: list, answer: list):
    # 主持人打开一扇门，置为-1.
    c = [i + j for i, j in zip(problem, answer)]
    new_problem = problem.copy()
    new_problem[c.index(0)] = -1
    return new_problem


def re_choose(problem: list, answer: list):
    # 选手在主持人打开一扇空门后选择另一扇门。
    setall = set([0, 1, 2])
    used_set = set([problem.index(-1), answer.index(1)])
    new_answer = [0, 0, 0]
    new_answer[setall.difference(used_set).pop()] = 1
    return new_answer


def game_on(times=10):
    origin_answer_count = 0
    new_answer_count = 0
    for i in range(times):
        doors = gen_doors()
        answer = gen_doors()
        new_problem = reveal(doors, answer)
        new_answer = re_choose(new_problem, answer)
        if check(new_problem, answer):
            origin_answer_count += 1
        if check(new_problem, new_answer):
            new_answer_count += 1

    print("origin answer: %.2f" % ((origin_answer_count/times)*100))
    print("change answer: %.2f" % ((new_answer_count/times)*100))

if __name__ == "__main__":
    game_on(10000)