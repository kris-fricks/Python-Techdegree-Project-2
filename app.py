import constants 
import copy

teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)


def clean_player_data():
    for player in players:
        if player['experience'] == 'NO':
            player['experience'] = False
        else:
            player['experience'] = True
        player['guardians'] = player['guardians'].split(" and ")    
        player['height'] = int(player['height'][:2])    
            

def add_teams_to_players():
    experienced_players = [p for p in players if p['experience'] == True ]     
    inexperienced_players = [p for p in players if p['experience'] == False ]  
    players_with_teams = []
    team_index = 0
    for pair_index in range(len(players) // 2):    
        if team_index < 3:                     
            experienced_player = experienced_players[pair_index]
            experienced_player['team'] = teams[team_index]
            
            inexperienced_player = inexperienced_players[pair_index] 
            inexperienced_player['team'] = teams[team_index]
            
            players_with_teams.append(experienced_player)
            players_with_teams.append(inexperienced_player)
        
        if (pair_index + 1) % 3 == 0:
            team_index += 1
    return players_with_teams


def display_stats():
    print("""
--------------------------------
 THE BASKETBALL TEAM STATS TOOL
--------------------------------
""")
    while True:
        print("""--MENU---
           
Here are your choices:
  1) Display Team Stats
  2) Quit  
""")
        try:
            user_option = int(input("Enter an option -->  "))
        except ValueError:
            print("We ran into an error. Try again.\n") 
        else:   
            if user_option > 2:
                print("Only type one of the options listed. Try again.\n")
            elif user_option < 1:
                print("Only type one of the options listed. Try again.\n") 
            elif user_option == 1:
                print("""
1) Panthers
2) Bandits
3) Warriors
""")
                user_option = int(input("Enter an option -->  "))
                try:
                    chosen_team_name = teams[user_option - 1]
                    players = add_teams_to_players()
                    chosen_team = []
                    player_height = []
                    player_guardians = []
                    experienced_players = 3
                    inexperienced_players = 3
                    for player in players:
                        current_player_team = player['team']
                        current_player_height = player['height']  
                        currrent_player_guardians = player['guardians']
                        if chosen_team_name == current_player_team:
                            chosen_team.append(player['name'])
                            player_height.append(player['height']) 
                            player_guardians.append(player['guardians'])
                            player_height_total = sum(player_height)
                            average_player_height = player_height_total // 6
                    player_names = ', '.join(chosen_team)
                    player_guardians = [item for items in player_guardians for item in items]
                    all_guardians = ', '.join(player_guardians)
                    print("------STATS------\n")
                    print("TEAM: {}\n".format(chosen_team_name))
                    print("TOTAL PLAYERS: {}\n".format(len(chosen_team)))
                    print("PLAYERS: {}\n".format(player_names))
                    print("EXPERIENCED PLAYERS: {}\n".format(experienced_players))
                    print("INEXPERIENCED PLAYERS: {}\n".format(inexperienced_players))
                    print("AVERAGE TEAM HEIGHT: {}\n".format(average_player_height))
                    print("GUARDIANS OF PLAYERS: {}\n".format(all_guardians))
                except ValueError:
                    print("Error")
            else:
                print("Closing app, see you next time!")
                break
            
                
if __name__ == '__main__':
    
    clean_player_data()
    display_stats()
    
    
    
   

