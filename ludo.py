from itertools import count
from potions import (
    main_list,
    maindict,
    player_1_path,
    player_2_path,
    player_3_path,
    player_4_path,
)
from movetoken import move_token
import random


counter = 0


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


def keep_token_outside(id, token_for_out_side, inside_lst):
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
        keep_token_outside(id)


def random_number():
    return random.randint(1, 6)


def kill_token(token, token_moving):
    if token[0] == "r":
        current_index = maindict[1][f"{token}_current_postition"]
        maindict[1][f"{token}_current_postition"] = maindict[1][
            f"{token}_actual_postition"
        ]

        actual_index = maindict[1][f"{token}_actual_postition"]

        main_list[actual_index[0]][actual_index[1]] = token.upper()
        main_list[current_index[0]][current_index[1]] = token_moving.upper()
    elif token[0] == "b":

        current_index = maindict[2][f"{token}_current_postition"]
        maindict[2][f"{token}_current_postition"] = maindict[2][
            f"{token}_actual_postition"
        ]

        actual_index = maindict[2][f"{token}_actual_postition"]

        main_list[actual_index[0]][actual_index[1]] = token.upper()
        main_list[current_index[0]][current_index[1]] = token_moving.upper()

    elif token[0] == "g":
        current_index = maindict[3][f"{token}_current_postition"]
        maindict[3][f"{token}_current_postition"] = maindict[3][
            f"{token}_actual_postition"
        ]

        actual_index = maindict[3][f"{token}_actual_postition"]

        main_list[actual_index[0]][actual_index[1]] = token.upper()
        main_list[current_index[0]][current_index[1]] = token_moving.upper()
    else:
        current_index = maindict[4][f"{token}_current_postition"]
        maindict[4][f"{token}_current_postition"] = maindict[4][
            f"{token}_actual_postition"
        ]

        actual_index = maindict[4][f"{token}_actual_postition"]

        main_list[actual_index[0]][actual_index[1]] = token.upper()
        main_list[current_index[0]][current_index[1]] = token_moving.upper()


def check_user(id, num):
    lst = check_token_outside(id)

    if len(lst) == 0 and num != 6:
        return
    elif len(lst) == 0 and num == 6:
        final_lst = []
        for i in range(1, 5):
            ele = f"{maindict[id]['color'].lower()}{i}"
            if ele not in lst:
                final_lst.append(ele)
        print(final_lst)
        token_for_out_side = input("get token out of house :")
        keep_token_outside(id, token_for_out_side, final_lst)
    elif len(lst) > 0 and num == 6:
        token_out_and_in_both(id, num)
    elif num != 6 and len(lst) > 0:
        lst = check_token_outside(id)
        new_lst = []
        for i in lst:
            if id == 1:
                if (
                    player_1_path.index(maindict[id][f"{i}_current_postition"])
                    + 1
                    + num
                ) <= len(player_1_path):
                    new_lst.append(i)
            if id == 2:
                if (
                    player_2_path.index(maindict[id][f"{i}_current_postition"])
                    + 1
                    + num
                ) <= len(player_2_path):
                    new_lst.append(i)
            if id == 3:
                if (
                    player_3_path.index(maindict[id][f"{i}_current_postition"])
                    + 1
                    + num
                ) <= len(player_3_path):
                    new_lst.append(i)
            if id == 4:
                if (
                    player_4_path.index(maindict[id][f"{i}_current_postition"])
                    + 1
                    + num
                ) <= len(player_4_path):
                    new_lst.append(i)

        if len(new_lst) > 0:
            print(new_lst)
            token_moving = input("token name for move :")
            move_token(id, num, token_moving, new_lst)


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


def token_out_and_in_both(id, num):
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

    # print(new_lst)
    # inside_lst=[]
    if len(new_lst) > 0:
        print(new_lst, "this token out side of house")

    inside_lst = check_token_inside_house(id)
    print(inside_lst, "this token in side of house")
    token_for_out_side = input("enter token for move : ")

    if token_for_out_side in lst:
        # new_lst = []
        # token_moving = input("token name for move :")
        move_token(id, num, token_for_out_side, new_lst)

    elif token_for_out_side in inside_lst:

        keep_token_outside(id, token_for_out_side, inside_lst)

    else:
        token_out_and_in_both(id)
    # else:
    #     token_out_and_in_both(id)


def play_ludo_pleyer(length):
    print_ludo()
    for i in count(0):

        for id in range(1, length + 1):
            counter = 0
            for i in count(0):
                if maindict[id]["is_completed"] == False:
                    print(f"Turn of pleyer {id} : ")
                    num = int(input("enter digit : "))
                    # input(f"press any key : ")
                    # num = random_number()

                    if counter == 2 and num == 6:
                        continue
                    elif num == 6:
                        print("\nyou got :", num, "\n")
                        check_user(id, num)
                        print_ludo()
                        counter = counter + 1
                    else:
                        print("\nyou got :", num, "\n")
                        check_user(id, num)
                        print_ludo()
                        break
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
