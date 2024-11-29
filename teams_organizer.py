import json
import argparse
from itertools import cycle

# Function to calculate player scores and update JSON
def calculate_scores_and_update_json(players):
    for player in players:
        name = player["name"]
        attributes = player["attributes"]

        # Calculate category scores (average of values)
        physical_score = sum(attributes["physical"].values()) / len(attributes["physical"])
        technical_score = sum(attributes["technical"].values()) / len(attributes["technical"])
        mental_score = sum(attributes["mental"].values()) / len(attributes["mental"])

        # Weighted overall score
        overall_score = (technical_score * 0.5) + (mental_score * 0.25) + (physical_score * 0.25)

        # Save scores to the player's data
        player["score"] = {
            "general": round(overall_score),
            "physical": round(physical_score),
            "technical": round(technical_score),
            "mental": round(mental_score),
        }

    return players

# Function to organize players into teams
def organize_teams(player_data, num_teams):
    # Extract scores
    player_scores = {player["name"]: player["score"]["general"] for player in player_data}

    # Sort players by score in descending order
    sorted_players = sorted(player_scores.items(), key=lambda x: x[1], reverse=True)

    # Create teams
    teams = {f"Team {i+1}": [] for i in range(num_teams)}
    team_cycle = cycle(teams.keys())  # Cycle through teams to balance them

    for player, score in sorted_players:
        team = next(team_cycle)
        teams[team].append({"name": player, "score": score})

    return teams

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description="Organize soccer teams or calculate scores.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subparser for "calculate" command
    calculate_parser = subparsers.add_parser(
        "calculate", help="Calculate scores and update the JSON file."
    )
    calculate_parser.add_argument("json_path", help="Path to the players JSON file.")

    # Subparser for "organize" command
    organize_parser = subparsers.add_parser(
        "organize", help="Organize players into teams based on scores."
    )
    organize_parser.add_argument("json_path", help="Path to the players JSON file.")
    organize_parser.add_argument("num_teams", type=int, help="Number of teams to create.")

    # Parse the arguments
    args = parser.parse_args()

    # Handle "calculate" command
    if args.command == "calculate":
        with open(args.json_path, "r") as players_file:
            players = json.load(players_file)

        updated_players = calculate_scores_and_update_json(players)

        with open(args.json_path, "w") as players_file:
            json.dump(updated_players, players_file, indent=4)

        print("Scores calculated and updated in the JSON file.")

    # Handle "organize" command
    elif args.command == "organize":
        with open(args.json_path, "r") as players_file:
            players = json.load(players_file)

        teams = organize_teams(players, args.num_teams)

        print("Teams organized:")
        for team, members in teams.items():
            print(f"{team}:")
            for member in members:
                print(f"  - {member['name']} (Score: {member['score']})")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
