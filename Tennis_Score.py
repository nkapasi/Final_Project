Player1 = raw_input("Who starts Serving?")

Player2 = raw_input("Name the other Player?")

set_number_games = raw_input("How many Games per Set?")

Game_score_list = [0,15,30,40,45]

Set_Score_List = [0,1,2,3,4,5,6,7,8]

Match_Score_List = [0,1,2,3]

def Game_Score(Game_score_list):
    player1Match = 0
    player2Match = 0
    for w in range(0,len(Match_Score_List)):
        Player1Set = 0
        Player2Set = 0
        for j in range(0,2*len(Set_Score_List)):
            Player1Game = 0
            Player2Game = 0
            print"Enter 1 if %s won the point"%(Player1)
            print"Enter 2 if %s won the point"%(Player2)
            for i in range(0,10*len(Game_score_list)):
                Score = raw_input()

                if Score == "1" and Game_score_list[Player1Game] in [40,45] and Game_score_list[Player2Game] in [40,45]:
                    if Game_score_list[Player2Game] == 40 and Game_score_list[Player1Game] == 40:
                        print "Advantage %s"%(Player1)
                        Player1Game = Player1Game + 1
                    elif Game_score_list[Player2Game] == 45:
                        Player2Game = Player2Game - 1
                        print "deuce"
                    elif Game_score_list[Player1Game] == 45:
                        print "%s won the game"%(Player1)
                        break
                    continue
                elif Score == "2" and Game_score_list[Player1Game] in [40,45] and Game_score_list[Player2Game] in [40,45]:
                    if Game_score_list[Player1Game] == 40 and Game_score_list[Player2Game] == 40:
                        print "Advantage %s"%(Player2)
                        Player2Game = Player2Game + 1
                    elif Game_score_list[Player2Game] == 45:
                        print "%s won the game"%(Player2)
                        break
                    elif Game_score_list[Player1Game] == 45:
                        Player1Game = Player1Game - 1
                        print "deuce"
                    continue 
                elif Score == "1":
                    Player1Game = Player1Game + 1
                    if Game_score_list[Player1Game] == 45:
                        print "%s won the game"%(Player1)
                        break
                    elif Game_score_list[Player2Game] == 45:
                        print "%s won the game"%(Player2)
                        break
                elif Score == "2":
                    Player2Game = Player2Game+1
                    if Game_score_list[Player1Game] == 45:
                        print "%s won the game"%(Player1)
                        break
                    if Game_score_list[Player2Game] == 45:
                        print "%s won the game"%(Player2)
                        break
                print "%s:%s"%(Player1,Game_score_list[Player1Game])
                print "%s:%s"%(Player2,Game_score_list[Player2Game])
            if Set_Score_List[Player1Set] in [int(set_number_games)-1, int(set_number_games)] and Set_Score_List[Player2Set] in [int(set_number_games)-1, int(set_number_games)]:
                if Game_score_list[Player1Game] == 45 and Set_Score_List[Player1Set] == int(set_number_games):
                    print "%s won the set"%(Player1)
                    break
                elif Game_score_list[Player2Game] == 45 and Set_Score_List[Player2Set] == int(set_number_games):
                    print "%s won the set"%(Player2)
                    break
                elif Game_score_list[Player1Game] == 45:
                    Player1Set = Player1Set + 1
                elif Game_score_list[Player2Game] == 45:
                    Player2Set = Player2Set + 1
            elif Game_score_list[Player1Game] == 45:
                Player1Set = Player1Set +1
                if Set_Score_List[Player1Set] == int(set_number_games):
                    print "%s won the set"%(Player1)
                    break
                elif Set_Score_List[Player2Set] == int(set_number_games):
                    print "%s won the set"%(Player2)
                    break
            elif Game_score_list[Player2Game] == 45:
                Player2Set = Player2Set + 1
                if Set_Score_List[Player1Set] == int(set_number_games):
                    print "%s won the set"%(Player1)
                    break
                elif Set_Score_List[Player2Set] == int(set_number_games):
                    print "%s won the set"%(Player2)
                    break
            print "%s:%s"%(Player1,Set_Score_List[Player1Set])
            print "%s:%s"%(Player2,Set_Score_List[Player2Set])
        if Set_Score_List[Player1Set] == int(set_number_games):
            player1Match = player1Match + 1
            if Match_Score_List[player1Match] == 2:
                print "%s won the match"%(Player1)
                break
            elif Match_Score_List[player2Match] == 2:
                print "%s won the game"%(Player2)
                break
        elif Set_Score_List[Player2Set] == int(set_number_games):
            player2Match = player2Match + 1
            if Match_Score_List[player1Match] == 3:
                print "%s won the match"%(Player1)
                break
            elif Match_Score_List[player2Match] == 3:
                print "%s won the match"%(Player2)
                break
        print "%s:%s"%(Player1,Match_Score_List[player1Match])
        print "%s:%s"%(Player2, Match_Score_List[player2Match])



print Game_Score(Game_score_list)