from itertools import count
import random

main_list = [
    ["R", "R", "R ", "R ", "R", "R", " ", " ", " ", "G", "G", "G ", "G ", "G", "G"],
    ["R", " ", "  ", "  ", " ", "R", " ", " ", " ", "G", " ", "  ", "  ", " ", "G"],
    ["R", " ", "*", "*", " ", "R", " ", " ", " ", "G", " ", "* ", "* ", " ", "G"],
    ["R", " ", "*", "*", " ", "R", " ", " ", " ", "G", " ", "* ", "* ", " ", "G"],
    ["R", " ", "  ", "  ", " ", "R", " ", " ", " ", "G", " ", "  ", "  ", " ", "G"],
    ["R", "R", "R ", "R ", "R", "R", " ", " ", " ", "G", "G", "G ", "G ", "G", "G"],
    [" ", " ", "  ", "  ", " ", " ", "-", "-", "-", " ", " ", "  ", "  ", " ", " "],
    [" ", " ", "  ", "  ", " ", " ", "-", "-", "-", " ", " ", "  ", "  ", " ", " "],
    [" ", " ", "  ", "  ", " ", " ", "-", "-", "-", " ", " ", "  ", "  ", " ", " "],
    ["B", "B", "B ", "B ", "B", "B", " ", " ", " ", "Y", "Y", "Y ", "Y ", "Y", "Y"],
    ["B", " ", "  ", "  ", " ", "B", " ", " ", " ", "Y", " ", "  ", "  ", " ", "Y"],
    ["B", " ", "*", "*", " ", "B", " ", " ", " ", "Y", " ", "* ", "* ", " ", "Y"],
    ["B", " ", "*", "*", " ", "B", " ", " ", " ", "Y", " ", "* ", "* ", " ", "Y"],
    ["B", " ", "  ", "  ", " ", "B", " ", " ", " ", "Y", " ", "  ", "  ", " ", "Y"],
    ["B", "B", "B ", "B ", "B", "B", " ", " ", " ", "Y", "Y", "Y ", "Y ", "Y", "Y"],
]

maindict = {
    1: {
        "color": "R",
        "r1_actual_postition": [2, 2],
        "r2_actual_postition": [2, 3],
        "r3_actual_postition": [3, 2],
        "r4_actual_postition": [3, 3],
        "r1_current_postition": [2, 2],
        "r2_current_postition": [2, 3],
        "r3_current_postition": [3, 2],
        "r4_current_postition": [3, 3],
        "is_started": False,
        "is_completed": False,
    },
    2: {
        "color": "B",
        "b1_actual_postition": [11, 2],
        "b2_actual_postition": [11, 3],
        "b3_actual_postition": [12, 2],
        "b4_actual_postition": [12, 3],
        "b1_current_postition": [11, 2],
        "b2_current_postition": [11, 3],
        "b3_current_postition": [12, 2],
        "b4_current_postition": [12, 3],
        "is_started": False,
        "is_completed": False,
    },
    3: {
        "color": "G",
        "g1_actual_postition": [2, 11],
        "g2_actual_postition": [2, 12],
        "g3_actual_postition": [3, 11],
        "g4_actual_postition": [3, 12],
        "g1_current_postition": [2, 11],
        "g2_current_postition": [2, 12],
        "g3_current_postition": [3, 11],
        "g4_current_postition": [3, 12],
        "is_started": False,
        "is_completed": False,
    },
    4: {
        "color": "Y",
        "y1_actual_postition": [11, 11],
        "y2_actual_postition": [11, 12],
        "y3_actual_postition": [12, 11],
        "y4_actual_postition": [12, 12],
        "y1_current_postition": [11, 11],
        "y2_current_postition": [11, 12],
        "y3_current_postition": [12, 11],
        "y4_current_postition": [12, 12],
        "is_started": False,
        "is_completed": False,
    },
}
player_2_path = [
    [13, 6],
    [12, 6],
    [11, 6],
    [10, 6],
    [9, 6],
    [8, 5],
    [8, 4],
    [8, 3],
    [8, 2],
    [8, 1],
    [8, 0],
    [7, 0],
    [6, 0],
    [6, 1],
    [6, 2],
    [6, 3],
    [6, 4],
    [6, 5],
    [5, 6],
    [4, 6],
    [3, 6],
    [2, 6],
    [1, 6],
    [0, 6],
    [0, 7],
    [0, 8],
    [1, 8],
    [2, 8],
    [3, 8],
    [4, 8],
    [5, 8],
    [6, 9],
    [6, 10],
    [6, 11],
    [6, 12],
    [6, 13],
    [6, 14],
    [7, 14],
    [8, 14],
    [8, 13],
    [8, 12],
    [8, 11],
    [8, 10],
    [8, 9],
    [9, 8],
    [10, 8],
    [11, 8],
    [12, 8],
    [13, 8],
    [14, 8],
    [14, 7],
    [13, 7],
    [12, 7],
    [11, 7],
    [10, 7],
    [9, 7],
    [8, 7],
]
player_3_path = [
    [1, 8],
    [2, 8],
    [3, 8],
    [4, 8],
    [5, 8],
    [6, 9],
    [6, 10],
    [6, 11],
    [6, 12],
    [6, 13],
    [6, 14],
    [7, 14],
    [8, 14],
    [8, 13],
    [8, 12],
    [8, 11],
    [8, 10],
    [8, 9],
    [9, 8],
    [10, 8],
    [11, 8],
    [12, 8],
    [13, 8],
    [14, 8],
    [14, 7],
    [14, 6],
    [13, 6],
    [12, 6],
    [11, 6],
    [10, 6],
    [9, 6],
    [8, 5],
    [8, 4],
    [8, 3],
    [8, 2],
    [8, 1],
    [8, 0],
    [7, 0],
    [6, 0],
    [6, 1],
    [6, 2],
    [6, 3],
    [6, 4],
    [6, 5],
    [5, 6],
    [4, 6],
    [3, 6],
    [2, 6],
    [1, 6],
    [0, 6],
    [0, 7],
    [1, 7],
    [2, 7],
    [3, 7],
    [4, 7],
    [5, 7],
    [6, 7],
]
player_4_path = [
    [8, 13],
    [8, 12],
    [8, 11],
    [8, 10],
    [8, 9],
    [9, 8],
    [10, 8],
    [11, 8],
    [12, 8],
    [13, 8],
    [14, 8],
    [14, 7],
    [14, 6],
    [13, 6],
    [12, 6],
    [11, 6],
    [10, 6],
    [9, 6],
    [8, 5],
    [8, 4],
    [8, 3],
    [8, 2],
    [8, 1],
    [8, 0],
    [7, 0],
    [6, 0],
    [6, 1],
    [6, 2],
    [6, 3],
    [6, 4],
    [6, 5],
    [5, 6],
    [4, 6],
    [3, 6],
    [2, 6],
    [1, 6],
    [0, 6],
    [0, 7],
    [0, 8],
    [1, 8],
    [2, 8],
    [3, 8],
    [4, 8],
    [5, 8],
    [6, 9],
    [6, 10],
    [6, 11],
    [6, 12],
    [6, 13],
    [6, 14],
    [7, 14],
    [7, 13],
    [7, 12],
    [7, 11],
    [7, 10],
    [7, 9],
    [7, 8],
]
player_1_path = [
    [6, 1],
    [6, 2],
    [6, 3],
    [6, 4],
    [6, 5],
    [5, 6],
    [4, 6],
    [3, 6],
    [2, 6],
    [1, 6],
    [0, 6],
    [0, 7],
    [0, 8],
    [1, 8],
    [2, 8],
    [3, 8],
    [4, 8],
    [5, 8],
    [6, 9],
    [6, 10],
    [6, 11],
    [6, 12],
    [6, 13],
    [6, 14],
    [7, 14],
    [8, 14],
    [8, 13],
    [8, 12],
    [8, 11],
    [8, 10],
    [8, 9],
    [9, 8],
    [10, 8],
    [11, 8],
    [12, 8],
    [13, 8],
    [14, 8],
    [14, 7],
    [14, 6],
    [13, 6],
    [12, 6],
    [11, 6],
    [10, 6],
    [9, 6],
    [8, 5],
    [8, 4],
    [8, 3],
    [8, 2],
    [8, 1],
    [8, 0],
    [7, 0],
    [7, 1],
    [7, 2],
    [7, 3],
    [7, 4],
    [7, 5],
    [7, 6],
]


def check_token_outside(id):
    lst = []
    maindict[id]["is_started"] = True
    search_actual_1 = f"{maindict[id]['color'].lower()}1_actual_postition"
    search_actual_2 = f"{maindict[id]['color'].lower()}2_actual_postition"
    search_actual_3 = f"{maindict[id]['color'].lower()}3_actual_postition"
    search_actual_4 = f"{maindict[id]['color'].lower()}4_actual_postition"

    search_current_1 = f"{maindict[id]['color'].lower()}1_current_postition"
    search_current_2 = f"{maindict[id]['color'].lower()}2_current_postition"
    search_current_3 = f"{maindict[id]['color'].lower()}3_current_postition"
    search_current_4 = f"{maindict[id]['color'].lower()}4_current_postition"

    if maindict[id][search_actual_1] != maindict[id][search_current_1]:
        lst.append(f"{maindict[id]['color'].lower()}1")
    if maindict[id][search_actual_2] != maindict[id][search_current_2]:
        lst.append(f"{maindict[id]['color'].lower()}2")
    if maindict[id][search_actual_3] != maindict[id][search_current_3]:
        lst.append(f"{maindict[id]['color'].lower()}3")
    if maindict[id][search_actual_4] != maindict[id][search_current_4]:
        lst.append(f"{maindict[id]['color'].lower()}4")
    return lst


def check_token_inside_house(id):
    lst = []
    maindict[id]["is_started"] = True
    search_actual_1 = f"{maindict[id]['color'].lower()}1_actual_postition"
    search_actual_2 = f"{maindict[id]['color'].lower()}2_actual_postition"
    search_actual_3 = f"{maindict[id]['color'].lower()}3_actual_postition"
    search_actual_4 = f"{maindict[id]['color'].lower()}4_actual_postition"

    search_current_1 = f"{maindict[id]['color'].lower()}1_current_postition"
    search_current_2 = f"{maindict[id]['color'].lower()}2_current_postition"
    search_current_3 = f"{maindict[id]['color'].lower()}3_current_postition"
    search_current_4 = f"{maindict[id]['color'].lower()}4_current_postition"

    if maindict[id][search_actual_1] == maindict[id][search_current_1]:
        lst.append(f"{maindict[id]['color'].lower()}1")
    if maindict[id][search_actual_2] == maindict[id][search_current_2]:
        lst.append(f"{maindict[id]['color'].lower()}2")
    if maindict[id][search_actual_3] == maindict[id][search_current_3]:
        lst.append(f"{maindict[id]['color'].lower()}3")
    if maindict[id][search_actual_4] == maindict[id][search_current_4]:
        lst.append(f"{maindict[id]['color'].lower()}4")
    return lst


def keep_token_outside(id):
    lst = check_token_outside(id)
    final_lst = []
    for i in range(1, 5):
        ele = f"{maindict[id]['color'].lower()}{i}"
        if ele not in lst:
            final_lst.append(ele)
    print(final_lst)
    token_for_out_side = input("get token out of house :")
    if token_for_out_side in final_lst:
        pos_change = f"{token_for_out_side}_current_postition"
        pos = maindict[id][pos_change]

        if id == 1:
            maindict[id][pos_change] = player_1_path[0]
            main_list[player_1_path[0][0]][
                player_1_path[0][1]
            ] = token_for_out_side.upper()
            main_list[pos[0]][pos[1]] = "   "
        elif id == 2:
            maindict[id][pos_change] = player_2_path[0]
            main_list[player_2_path[0][0]][
                player_2_path[0][1]
            ] = token_for_out_side.upper()
            main_list[pos[0]][pos[1]] = "   "

        elif id == 3:
            maindict[id][pos_change] = player_3_path[0]
            main_list[player_3_path[0][0]][
                player_3_path[0][1]
            ] = token_for_out_side.upper()
            main_list[pos[0]][pos[1]] = "   "

        elif id == 4:
            maindict[id][pos_change] = player_4_path[0]
            main_list[player_4_path[0][0]][
                player_4_path[0][1]
            ] = token_for_out_side.upper()
            main_list[pos[0]][pos[1]] = "   "

    else:
        keep_token_outside(id)


def random_number():
    return random.randint(1, 6)


def move_token(id, num,token_moving,new_lst):
    # lst = check_token_outside(id)
    # new_lst = []
    # for i in lst:
    #     if id == 1:
    #         if (
    #             player_1_path.index(maindict[id][f"{i}_current_postition"]) + 1 + num
    #         ) <= len(player_1_path):
    #             new_lst.append(i)
    #     if id == 2:
    #         if (
    #             player_2_path.index(maindict[id][f"{i}_current_postition"]) + 1 + num
    #         ) <= len(player_2_path):
    #             new_lst.append(i)
    #     if id == 3:
    #         if (
    #             player_3_path.index(maindict[id][f"{i}_current_postition"]) + 1 + num
    #         ) <= len(player_3_path):
    #             new_lst.append(i)
    #     if id == 4:
    #         if (
    #             player_4_path.index(maindict[id][f"{i}_current_postition"]) + 1 + num
    #         ) <= len(player_4_path):
    #             new_lst.append(i)

    # print(new_lst)
    # token_moving = input("token name for move :")
    if token_moving in new_lst:
        if len(new_lst) != 0:
            pos = maindict[id][f"{token_moving}_current_postition"]
            if id == 1:
                index = (
                    player_1_path.index(
                        maindict[id][f"{token_moving}_current_postition"]
                    )
                    + num
                )
                maindict[id][f"{token_moving}_current_postition"] = player_1_path[index]

                main_list[player_1_path[index][0]][
                    player_1_path[index][1]
                ] = token_moving.upper()
                main_list[pos[0]][pos[1]] = "   "
            if id == 2:
                index = (
                    player_2_path.index(
                        maindict[id][f"{token_moving}_current_postition"]
                    )
                    + num
                )
                maindict[id][f"{token_moving}_current_postition"] = player_2_path[index]

                main_list[player_2_path[index][0]][
                    player_2_path[index][1]
                ] = token_moving.upper()
                main_list[pos[0]][pos[1]] = "   "
            if id == 3:
                index = (
                    player_3_path.index(
                        maindict[id][f"{token_moving}_current_postition"]
                    )
                    + num
                )
                maindict[id][f"{token_moving}_current_postition"] = player_3_path[index]

                main_list[player_3_path[index][0]][
                    player_3_path[index][1]
                ] = token_moving.upper()
                main_list[pos[0]][pos[1]] = "   "
            if id == 4:
                index = (
                    player_4_path.index(
                        maindict[id][f"{token_moving}_current_postition"]
                    )
                    + num
                )
                maindict[id][f"{token_moving}_current_postition"] = player_4_path[index]

                main_list[player_4_path[index][0]][
                    player_4_path[index][1]
                ] = token_moving.upper()
                main_list[pos[0]][pos[1]] = "   "
        else:
            print("no token avilable...")
    else:
        move_token(id, num)


def check_user(id, num):
    lst = check_token_outside(id)

    if len(lst) == 0 and num != 6:
        return
    elif len(lst) == 0 and num == 6:
        keep_token_outside(id)
    elif len(lst) > 0 and num == 6:
        token_out_and_in_both(id)
    elif num != 6 and len(lst) > 0:
        lst = check_token_outside(id)
        new_lst = []
        for i in lst:
            if id == 1:
                if (
                    player_1_path.index(maindict[id][f"{i}_current_postition"]) + 1 + num
                ) <= len(player_1_path):
                    new_lst.append(i)
            if id == 2:
                if (
                    player_2_path.index(maindict[id][f"{i}_current_postition"]) + 1 + num
                ) <= len(player_2_path):
                    new_lst.append(i)
            if id == 3:
                if (
                    player_3_path.index(maindict[id][f"{i}_current_postition"]) + 1 + num
                ) <= len(player_3_path):
                    new_lst.append(i)
            if id == 4:
                if (
                    player_4_path.index(maindict[id][f"{i}_current_postition"]) + 1 + num
                ) <= len(player_4_path):
                    new_lst.append(i)

        print(new_lst)
        token_moving = input("token name for move :")
        move_token(id, num,token_moving,new_lst)


def print_ludo():
    for i in main_list:
        count = 0
        for j in i:

            if j:
                print(f"| {j} |", end=" ")
                count = count + 1
            else:
                print(f"| {j} |", end=" ")
                count = count + 1
        print("\n")

    # for i in range(1, pleyers + 1):
    #     color = maindict[i]["color"].lower()
    #     for j in range(1, 5):
    #         searching = f"{color}{j}_current_postition"
    #         pos = maindict[i][searching]
    #         main_list[pos[0]][pos[1]] = maindict[i]["color"] + str(j)


def token_out_and_in_both(id):
    lst = check_token_outside(id)
    print(lst, "this token out side of house")
    inside_lst = check_token_inside_house(id)
    print(inside_lst, "this token in side of house")

    token_for_out_side = input("enter token for move : ")

    if token_for_out_side in lst:
        move_token()
    elif token_for_out_side in inside_lst:
        if token_for_out_side in inside_lst:
            pos_change = f"{token_for_out_side}_current_postition"
            pos = maindict[id][pos_change]

        if id == 1:
            maindict[id][pos_change] = player_1_path[0]
            if main_list[player_1_path[0][0]][player_1_path[0][1]].strip() == "":
                main_list[player_1_path[0][0]][
                    player_1_path[0][1]
                ] = token_for_out_side.upper()
            else:
                main_list[player_1_path[0][0]][player_1_path[0][1]] = (
                    main_list[player_1_path[0][0]][player_1_path[0][1]]
                    + ","
                    + token_for_out_side.upper()
                )
            main_list[pos[0]][pos[1]] = "   "
        elif id == 2:
            maindict[id][pos_change] = player_2_path[0]
            if main_list[player_2_path[0][0]][player_2_path[0][1]].strip() == "":
                main_list[player_2_path[0][0]][
                    player_2_path[0][1]
                ] = token_for_out_side.upper()
            else:
                main_list[player_2_path[0][0]][player_2_path[0][1]] = (
                    main_list[player_2_path[0][0]][player_2_path[0][1]]
                    + ","
                    + token_for_out_side.upper()
                )
            main_list[pos[0]][pos[1]] = "   "

        elif id == 3:
            maindict[id][pos_change] = player_3_path[0]
            if main_list[player_3_path[0][0]][player_3_path[0][1]].strip() == "":
                main_list[player_3_path[0][0]][
                    player_3_path[0][1]
                ] = token_for_out_side.upper()
            else:
                main_list[player_3_path[0][0]][player_3_path[0][1]] = (
                    main_list[player_3_path[0][0]][player_3_path[0][1]]
                    + ","
                    + token_for_out_side.upper()
                )
            main_list[pos[0]][pos[1]] = "   "

        elif id == 4:
            maindict[id][pos_change] = player_4_path[0]
            if main_list[player_4_path[0][0]][player_4_path[0][1]].strip() == "":
                main_list[player_4_path[0][0]][
                    player_4_path[0][1]
                ] = token_for_out_side.upper()
            else:
                main_list[player_4_path[0][0]][player_4_path[0][1]] = (
                    main_list[player_4_path[0][0]][player_4_path[0][1]]
                    + ","
                    + token_for_out_side.upper()
                )
            main_list[pos[0]][pos[1]] = "   "

        else:
            token_out_and_in_both(id)
    else:
        token_out_and_in_both(id)


def play_ludo_pleyer(length):
    print_ludo()
    for i in count(0):

        for id in range(1, length + 1):
            if maindict[id]["is_completed"] == False:
                print(f"Turn of pleyer {id} : ")
                num = int(input("enter digit : "))
                # input(f"press any key : ")
                # num = random_number()
                print("\nyou got :", num, "\n")
                check_user(id, num)
                print_ludo()

            else:
                continue


def start_ludo(pleyers):

    for i in range(1, pleyers + 1):
        color = maindict[i]["color"].lower()
        for j in range(1, 5):
            searching = f"{color}{j}_current_postition"
            pos = maindict[i][searching]
            main_list[pos[0]][pos[1]] = maindict[i]["color"] + str(j)

    play_ludo_pleyer(pleyers)


def display_menu():
    for i in count(0):
        try:
            print(
                "============================select pleyers============================"
            )
            print("1:   2 player")
            print("2 :  3 player")
            print("3 :  4 player")
            print("4 :    exit")
            print(
                "========================================================================================"
            )
            operations = int(input("Select any one option from upper list :").strip())

            if operations == 1:
                start_ludo(2)
            elif operations == 2:
                start_ludo(3)
            elif operations == 3:
                start_ludo(4)

            elif operations == 4:
                print("Thank You For Visiting ludo game.....")
                break
            else:
                print("ERORR : Choice is Invalid....................")
        except Exception as err:
            print(err)
            continue


for i in count(0):
    try:
        print(
            "============================Welcome To Ludo Game============================"
        )
        print("1:   start game")
        print("2 :  Exit")
        print(
            "========================================================================================"
        )
        operations = int(input("Select any one option from upper list :").strip())

        if operations == 1:
            display_menu()

        elif operations == 2:
            print("Thank You For Visiting ludo game.....")
            break
        else:
            print("ERORR : Choice is Invalid....................")
    except Exception as err:
        print(err)
        continue
