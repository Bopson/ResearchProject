# Define a Player class to represent football players
class Player:
    def __init__(self, name, position, skill_level):
        self.name = name
        self.position = position
        self.skill_level = skill_level

# Define a function to select the best team based on player positions and skill levels
def select_best_team(players, positions_needed):
    best_team = {}  # Create an empty dictionary to store the best team
    players.sort(key=lambda player: -player.skill_level)  # Sort players by skill level in descending order

    for player in players:
        position = player.position  # Get the player's position
        if position in positions_needed and positions_needed[position] > 0:
            # If there are available slots for this position, add the player to the best team
            best_team.setdefault(position, []).append(player)
            positions_needed[position] -= 1

    return best_team  # Return the selected best team

# Define a function to print the best team with the specified number of players for each position
def print_best_team(best_team):
    for position, players in best_team.items():
        print(f"{position} (Count: {len(players)}):")
        for player in players:
            print(f"  {player.name} ({player.skill_level})")

# Create player objects with name, position, and skill level
players = [
    Player("Player1", "Goalkeeper", 90),
    Player("Player2", "Goalkeeper", 85),
    Player("Player3", "Defender", 92),
    Player("Player4", "Defender", 89),
    Player("Player5", "Defender", 87),
    Player("Player6", "Midfielder", 95),
    Player("Player7", "Midfielder", 93),
    Player("Player8", "Forward", 97),
    Player("Player9", "Forward", 94),
]

# Define the number of players needed for each position
positions_needed = {
    "Goalkeeper": 1,
    "Defender": 3,
    "Midfielder": 2,
    "Forward": 2,
}

# Select the best team based on the number of players needed for each position
best_team = select_best_team(players, positions_needed)

# Print the best team
print_best_team(best_team)
