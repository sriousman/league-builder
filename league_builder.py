###  PROJECT 1: LEAGUE BUILDER  ##############################################
#    AUTHOR: srious                                                          #
#    DESCRIPTION:                                                            #
#        Program requires a file, 'soccer_players.csv', to read player       #
#        profiles, build a league for three teams, and generate letters to   #
#        each player's guardian(s) with league instructions in a separate    #
#        file.                                                               #
##############################################################################

import csv # Module for reading and writing to .csv files

# VARIABLES #
sharks = [{'TeamName':'Sharks','First Practice':'3:00pm, Thursday March 9th.'}]
dragons =[{'TeamName':'Dragons','First Practice':'3:00pm, Wednesday March 8th.'}]
raptors =[{'TeamName':'Raptors','First Practice':'3:00pm, Wednesday March 8th.'}]
teams = [sharks,dragons,raptors]
letter_text = "Dear {},\n Congratulations!\n\n Your child, {}, has been drafted to the {}.\n\nWe will be having our first practice at {}\n\n Thanks, Greg"

# Loop through each player of the team passed.
# Create a player_name.txt file and write the
# generate string for letter
def write_letters(team):
    team_name = team[0]['TeamName']
    first_practice = team[0]['First Practice']

    for player in team[1:]:
        filename = '_'.join(player['Name'].lower().split())

        file = open(filename + '.txt','a')
        file.write(letter_text.format(player['Guardian Name(s)'],
                                        player['Name'],
                                        team_name,
                                        first_practice))

# Prevent from running when loaded. Won't run unless main execution thread
if __name__ == "__main__":

    # Open and Read from .csv file
    # Separate players with xp
    # Assign each player to a team
    with open('soccer_players.csv', newline='') as csvfile:
        playerreader = csv.DictReader(csvfile, delimiter=',')
        players = list(playerreader)

        xp_players = [player for player in players if player['Soccer Experience'] =='YES' ]
        no_xp_players = [player for player in players if player['Soccer Experience'] =='NO' ]

        while xp_players:
            for team in teams:
                team.append(xp_players.pop())

        while no_xp_players:
            for team in teams:
                team.append(no_xp_players.pop())

    # Create a file teams.txt
    # Loop through each team writing player assignments to team.txt
    # Call write_letters
    with open('teams.txt', 'a') as teamfile:
        for team in teams:
            write_letters(team)
            teamfile.write("\n"+team[0]['TeamName'])
            for player in team[1:]:
                teamfile.write('{}, {}, {}\n'.format(player['Name'],
                                        player['Soccer Experience'],
                                        player['Guardian Name(s)'])
                                        )
