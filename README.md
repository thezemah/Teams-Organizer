
# Soccer Team Organizer

## Overview
This project is a Python-based tool designed to calculate player scores and organize players into balanced soccer teams. The tool processes player data stored in a JSON file, calculates scores for each player based on their attributes, and divides them into evenly matched teams.

## Features
- **Calculate Player Scores**:
  - Scores are calculated based on attributes in three categories: `mental`, `physical`, and `technical`.
  - Weighted scoring:
    - Technical: 50%
    - Mental: 25%
    - Physical: 25%
  - Each category is averaged, and a final weighted score is calculated.
- **Organize Teams**:
  - Evenly distributes players into a specified number of teams based on their scores.
  - Ensures balance by sorting players by their scores and distributing them cyclically.

## File Structure
```
soccer_team_organizer/
├── players.json        # JSON file containing player data
├── script.py           # Main Python script for calculating scores and organizing teams
└── README.md           # Documentation
```

## Prerequisites
- Python 3.7 or higher
- Libraries: No external libraries are required (uses Python standard libraries).

## Usage
The script provides two main functionalities: **calculating scores** and **organizing teams**. These are handled using command-line arguments.

### 1. Calculating Scores
This functionality calculates player scores and updates the `players.json` file.

#### Command:
```bash
python script.py calculate <path_to_json>
```

#### Example:
```bash
python script.py calculate players.json
```

#### Output:
- The script reads the `players.json` file, calculates scores, and updates the file with the scores.

#### Updated JSON Example:
```json
{
    "name": "Player1",
    "attributes": {
        "mental": {"determination": 80, "discipline": 77, "knowledge": 79},
        "physical": {"power": 75, "speed": 88},
        "technical": {"ball_control": 92, "defense": 71, "shooting": 85}
    },
    "score": {
        "general": 81,
        "physical": 82,
        "technical": 83,
        "mental": 79
    }
}
```

### 2. Organizing Teams
This functionality organizes players into a specified number of teams based on their scores.

#### Command:
```bash
python script.py organize <path_to_json> <num_teams>
```

#### Example:
```bash
python script.py organize players.json 3
```

#### Output:
- Displays the organized teams in the terminal.

#### Example Output:
```
Teams organized:
Team 1:
  - Player3 (Score: 83)
  - Player7 (Score: 76)
Team 2:
  - Player1 (Score: 81)
  - Player8 (Score: 75)
Team 3:
  - Player4 (Score: 80)
  - Player6 (Score: 74)
```

## JSON Input Format
The `players.json` file should contain player data structured as follows:
```json
[
    {
        "name": "Player1",
        "attributes": {
            "mental": {"determination": 80, "discipline": 77, "knowledge": 79},
            "physical": {"power": 75, "speed": 88},
            "technical": {"ball_control": 92, "defense": 71, "shooting": 85}
        }
    },
    {
        "name": "Player2",
        "attributes": {
            "mental": {"determination": 70, "discipline": 65, "knowledge": 60},
            "physical": {"power": 60, "speed": 70},
            "technical": {"ball_control": 75, "defense": 80, "shooting": 85}
        }
    }
]
```

## Output Example
- After running the `calculate` command, the `players.json` file will include scores in a `score` field.
- The `organize` command outputs the organized teams to the terminal.

## Notes
- **Reusability**: Scores are calculated once and saved in the JSON file. You don’t need to recalculate scores every time you organize teams.
- **Scalability**: The script can handle any number of players and teams as long as the input JSON file is formatted correctly.

## Future Improvements
- Add an option to export organized teams to a file (e.g., CSV, JSON).
- Support for more flexible weighting of attributes.
- Add a GUI for easier use by non-technical users.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

---

Enjoy organizing your soccer games! ⚽
