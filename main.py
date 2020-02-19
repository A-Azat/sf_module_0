import numpy as np
count = 0                            # ������� �������
number = np.random.randint(1,100)    # �������� �����
def score_game(core):
    '''��������� ���� 1000 ���, ���� ������ ��� ������ ���� ��������� �����'''
    count_ls = []
    np.random.seed(1)  # ��������� RANDOM SEED, ����� ��� ����������� ��� �������������!
    random_array = np.random.randint(1, 100, size=(1000))
    for number in random_array:
        count_ls.append(core(number))
    score = int(np.mean(count_ls))
    print(f"��� �������� ��������� ����� � ������� �� {score} �������")
    return(score)

def game_core_v3(number):
           
    count = 0
    max_val = 100
    min_val = 0
    predict = np.random.randint(1,100)
    while number != predict:
        count+=1
        if number > predict:
            min_val = predict
            predict = int (min_val  + ((max_val - min_val)/2))
        elif number < predict:
            max_val = predict
            predict = int (max_val - ((max_val-min_val)/2))
    return(count) # ����� �� �����, ���� �������
# ���������
score_game(game_core_v3)
