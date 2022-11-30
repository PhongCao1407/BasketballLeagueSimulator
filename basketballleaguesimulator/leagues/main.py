'''
This file is for drafting purpose only. It is to be replace with the front end later
'''
# Database
from .models import Leagues, Teams, Players

# Package
from faker import Faker
fake = Faker()

# Utilities
from .utils.utils import print_list, generate_random_letter, generate_random_jersey_number


def main():
    # Constants
    INPUT_TEXT = """\nPlease choose an option:\n
    1) Create new league\n
    2) Add team to league\n
    3) Add player to team\n
    4) Simulate season\n
    Choose anything else to exit\n
    """
    OPTIONS = set([1, 2, 3, 4])

    option = int(input(INPUT_TEXT))
    
    while option in OPTIONS:
        if option == 1:
            create_league()
        elif option == 2:
            add_team_to_league()
        elif option == 3:
            add_player_to_team()
        elif option == 4:
            simulate_season()
        else:
            break

        option = input(INPUT_TEXT)



'''
CREATE Operations
'''

def create_league():
    # Get league name
    league_name = input('\nPlease provide a league name: ') 

    # Add new sport to db
    try:
        new_league = Leagues(name=league_name)
        new_league.save()
        print('\nCreate league successful\n')
    except: # Need to add the error here
        print('There was an error.')


    # Generating teams
    num_of_teams = int(input('\nPlease choose the number of teams for the league: '))
    create_teams_random(new_league, num_of_teams)
    print('\nGenerating teams successful\n--------------------------------------')


def create_team(team_name, team_league, team_city):
    team = Teams(name=team_name, location=team_city, league=team_league)
    team.save()
    return team


def create_teams_random(team_league, num_of_teams):
    # TODO
    print('\nGenerating teams...\n')

    num_of_players = int(input('\nHow many players do you want in a team? '))

    # To keep track of used team name
    team_names = set()

    for _ in range(num_of_teams):
        # Generate team name
        random_letter = generate_random_letter()
        while random_letter in team_names:
            random_letter = generate_random_letter()

        team_name = random_letter
        team_names.add(team_name)

        # Generate random city
        team_city = fake.city()

        # Create team
        team = create_team(team_name, team_league, team_city)

        # Create players for team
        print('\nCreated team', team_name)
        print('\nGenerating players...\n')
        create_players_random(team, num_of_players)


def create_player(player_first_name, player_last_name, player_jersey_number, player_team):
    player = Players(first_name=player_first_name, last_name=player_last_name, jersey_number=player_jersey_number, team=player_team)
    player.save()
    return player


def create_players_random(player_team, num_of_players):
    player_jersey_numbers = set()
    for _ in range(num_of_players):
        # Get player details
        player_first_name = fake.first_name_male()
        player_last_name = fake.last_name_male()

        jersey_number = generate_random_jersey_number()
        while jersey_number in player_jersey_numbers:
            jersey_number = generate_random_jersey_number()
        player_jersey_number = jersey_number
        player_jersey_numbers.add(jersey_number)
        
        
        # Create players
        player = create_player(player_first_name, player_last_name, player_jersey_number, player_team)
        


        






    