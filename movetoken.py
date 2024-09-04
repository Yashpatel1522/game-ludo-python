from potions import (
    main_list,
    maindict,
    player_1_path,
    player_2_path,
    player_3_path,
    player_4_path,
    safe_zone,
)


def move_token(id, num, token_moving, new_lst):
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

                if (
                    main_list[player_1_path[index][0]][player_1_path[index][1]].strip()
                    == ""
                ):
                    main_list[player_1_path[index][0]][
                        player_1_path[index][1]
                    ] = token_moving.upper()
                elif player_1_path[index] == player_1_path[len(player_1_path) - 1]:
                    maindict[id][f"{token_moving}_is_completed"] = True
                    if (
                        main_list[player_1_path[index][0]][
                            player_1_path[index][1]
                        ].strip()
                        == "-"
                    ):

                        main_list[player_1_path[index][0]][
                            player_1_path[index][1]
                        ] = token_moving.upper()
                    else:
                        main_list[player_1_path[index][0]][player_1_path[index][1]] = (
                            main_list[player_1_path[index][0]][player_1_path[index][1]]
                            + ","
                            + token_moving.upper()
                        )

                    if (
                        maindict[1]["r1_is_completed"]
                        and maindict[1]["r2_is_completed"]
                        and maindict[1]["r3_is_completed"]
                        and maindict[1]["r4_is_completed"]
                    ):
                        maindict[1]["is_completed"] = True
                else:
                    safe_or_not = [player_1_path[index][0], player_1_path[index][1]]
                    if safe_or_not in safe_zone:

                        main_list[player_1_path[index][0]][player_1_path[index][1]] = (
                            main_list[player_1_path[index][0]][player_1_path[index][1]]
                            + ","
                            + token_moving.upper()
                        )
                    elif (
                        token_moving[0]
                        == main_list[player_1_path[index][0]][player_1_path[index][1]][
                            0
                        ].lower()
                    ):
                        main_list[player_1_path[index][0]][player_1_path[index][1]] = (
                            main_list[player_1_path[index][0]][player_1_path[index][1]]
                            + ","
                            + token_moving.upper()
                        )
                    else:
                        token = main_list[player_1_path[index][0]][
                            player_1_path[index][1]
                        ].lower()
                        kill_token(token, token_moving)

            if id == 2:
                index = (
                    player_2_path.index(
                        maindict[id][f"{token_moving}_current_postition"]
                    )
                    + num
                )
                maindict[id][f"{token_moving}_current_postition"] = player_2_path[index]
                if (
                    main_list[player_2_path[index][0]][player_2_path[index][1]].strip()
                    == ""
                ):
                    main_list[player_2_path[index][0]][
                        player_2_path[index][1]
                    ] = token_moving.upper()
                elif player_2_path[index] == player_2_path[len(player_2_path) - 1]:
                    maindict[id][f"{token_moving}_is_completed"] = True
                    if (
                        main_list[player_2_path[index][0]][
                            player_2_path[index][1]
                        ].strip()
                        == "-"
                    ):

                        main_list[player_2_path[index][0]][
                            player_2_path[index][1]
                        ] = token_moving.upper()
                    else:
                        main_list[player_2_path[index][0]][player_2_path[index][1]] = (
                            main_list[player_2_path[index][0]][player_2_path[index][1]]
                            + ","
                            + token_moving.upper()
                        )

                    if (
                        maindict[2]["b1_is_completed"]
                        and maindict[2]["b2_is_completed"]
                        and maindict[2]["b3_is_completed"]
                        and maindict[2]["b4_is_completed"]
                    ):
                        maindict[2]["is_completed"] = True
                else:
                    safe_or_not = [player_2_path[index][0], player_2_path[index][1]]
                    if safe_or_not in safe_zone:

                        main_list[player_2_path[index][0]][player_2_path[index][1]] = (
                            main_list[player_2_path[index][0]][player_2_path[index][1]]
                            + ","
                            + token_moving.upper()
                        )
                    elif (
                        token_moving[0]
                        == main_list[player_2_path[index][0]][player_2_path[index][1]][
                            0
                        ].lower()
                    ):
                        main_list[player_2_path[index][0]][player_2_path[index][1]] = (
                            main_list[player_2_path[index][0]][player_2_path[index][1]]
                            + ","
                            + token_moving.upper()
                        )
                    else:
                        token = main_list[player_2_path[index][0]][
                            player_2_path[index][1]
                        ].lower()
                        kill_token(token, token_moving)
                    # main_list[player_2_path[index][0]][player_2_path[index][1]] = (
                    #     main_list[player_2_path[index][0]][player_2_path[index][1]]
                    #     + ","
                    #     + token_moving.upper()
                    # )

                # main_list[pos[0]][pos[1]] = "   "
            if id == 3:
                index = (
                    player_3_path.index(
                        maindict[id][f"{token_moving}_current_postition"]
                    )
                    + num
                )
                maindict[id][f"{token_moving}_current_postition"] = player_3_path[index]

                if (
                    main_list[player_3_path[index][0]][player_3_path[index][1]].strip()
                    == ""
                ):
                    main_list[player_3_path[index][0]][
                        player_3_path[index][1]
                    ] = token_moving.upper()
                elif player_3_path[index] == player_3_path[len(player_3_path) - 1]:
                    maindict[id][f"{token_moving}_is_completed"] = True
                    if (
                        main_list[player_3_path[index][0]][
                            player_3_path[index][1]
                        ].strip()
                        == "-"
                    ):

                        main_list[player_3_path[index][0]][
                            player_3_path[index][1]
                        ] = token_moving.upper()
                    else:
                        main_list[player_3_path[index][0]][player_3_path[index][1]] = (
                            main_list[player_3_path[index][0]][player_3_path[index][1]]
                            + ","
                            + token_moving.upper()
                        )

                    if (
                        maindict[3]["g1_is_completed"]
                        and maindict[3]["g2_is_completed"]
                        and maindict[3]["g3_is_completed"]
                        and maindict[3]["g4_is_completed"]
                    ):
                        maindict[3]["is_completed"] = True
                else:
                    # main_list[player_3_path[index][0]][player_3_path[index][1]] = (
                    #     main_list[player_3_path[index][0]][player_3_path[index][1]]
                    #     + ","
                    #     + token_moving.upper()
                    # )
                    safe_or_not = [player_3_path[index][0], player_3_path[index][1]]
                    if safe_or_not in safe_zone:

                        main_list[player_3_path[index][0]][player_3_path[index][1]] = (
                            main_list[player_3_path[index][0]][player_3_path[index][1]]
                            + ","
                            + token_moving.upper()
                        )
                    elif (
                        token_moving[0]
                        == main_list[player_3_path[index][0]][player_3_path[index][1]][
                            0
                        ].lower()
                    ):
                        main_list[player_3_path[index][0]][player_3_path[index][1]] = (
                            main_list[player_3_path[index][0]][player_3_path[index][1]]
                            + ","
                            + token_moving.upper()
                        )
                    else:
                        token = main_list[player_3_path[index][0]][
                            player_3_path[index][1]
                        ].lower()
                        kill_token(token, token_moving)
                # main_list[pos[0]][pos[1]] = "   "
            if id == 4:
                index = (
                    player_4_path.index(
                        maindict[id][f"{token_moving}_current_postition"]
                    )
                    + num
                )
                maindict[id][f"{token_moving}_current_postition"] = player_4_path[index]

                if (
                    main_list[player_4_path[index][0]][player_4_path[index][1]].strip()
                    == ""
                ):
                    main_list[player_4_path[index][0]][
                        player_4_path[index][1]
                    ] = token_moving.upper()
                elif player_4_path[index] == player_4_path[len(player_4_path) - 1]:
                    maindict[id][f"{token_moving}_is_completed"] = True
                    if (
                        main_list[player_4_path[index][0]][
                            player_4_path[index][1]
                        ].strip()
                        == "-"
                    ):

                        main_list[player_4_path[index][0]][
                            player_4_path[index][1]
                        ] = token_moving.upper()
                    else:
                        main_list[player_4_path[index][0]][player_4_path[index][1]] = (
                            main_list[player_4_path[index][0]][player_4_path[index][1]]
                            + ","
                            + token_moving.upper()
                        )

                    if (
                        maindict[4]["y1_is_completed"]
                        and maindict[4]["y2_is_completed"]
                        and maindict[4]["y3_is_completed"]
                        and maindict[4]["y4_is_completed"]
                    ):
                        maindict[4]["is_completed"] = True
                else:
                    safe_or_not = [player_4_path[index][0], player_4_path[index][1]]
                    if safe_or_not in safe_zone:

                        main_list[player_4_path[index][0]][player_4_path[index][1]] = (
                            main_list[player_4_path[index][0]][player_4_path[index][1]]
                            + ","
                            + token_moving.upper()
                        )
                    elif (
                        token_moving[0]
                        == main_list[player_4_path[index][0]][player_4_path[index][1]][
                            0
                        ].lower()
                    ):
                        main_list[player_4_path[index][0]][player_4_path[index][1]] = (
                            main_list[player_4_path[index][0]][player_4_path[index][1]]
                            + ","
                            + token_moving.upper()
                        )
                    else:
                        token = main_list[player_4_path[index][0]][
                            player_4_path[index][1]
                        ].lower()
                        kill_token(token, token_moving)
                    # main_list[player_4_path[index][0]][player_4_path[index][1]] = (
                    #     main_list[player_4_path[index][0]][player_4_path[index][1]]
                    #     + ","
                    #     + token_moving.upper()
                    # )
                # main_list[pos[0]][pos[1]] = "   "
            if len(main_list[pos[0]][pos[1]].split(",")) == 1:
                main_list[pos[0]][pos[1]] = "   "
            else:
                lst = main_list[pos[0]][pos[1]].split(",")
                new_lst = []
                for i in lst:
                    new_lst.append(i.lower())

                index = new_lst.index(token_moving)
                new_lst.remove(new_lst[index])
                lst = []
                for i in new_lst:
                    lst.append(i.upper())
                main_list[pos[0]][pos[1]] = (",").join(lst)
        else:
            print("no token avilable...")
    else:
        move_token(id, num)
