# Anime Vote Solver
This code generates a sorted list of anime according to the sorting scheme described below.

# Voting Scheme

Every couple of months our social anime watchgroup has to decide which anime to watch, which leads to the dilemma of how to decide which anime to watch.
For this purpose, everyone suggests some anime and then a voting mechanism is set up to decide which of the suggested anime should be watched. The voting mechanism 
works as follows.

Each participant gets n positive votes, ranging from [1, ... , n], each of these positive votes can be used once, in addition everyone gets m 
many -1 votes and any number of 0 votes. After each participant has assigned their votes to each anime, the votes are collected. 

First the votes are summed up and sorted, where the positive votes are reduced to 1.
For example: 1 + 1 + 1 - 1 + 0 = 3, and 1337 + 69 + 42 - 1 + 0 = 3.

Then, to break ties for the animes that have similar scores in the previous step, we use the full score without the reduction.
For example: 1 + 1 + 1 - 1 + 0 = 3 and 1337 + 69 + 42 - 1 + 0 = 1447

# How to use the solver
Call main.py with the following arguments

```--path: Path to the folder containing ONLY the txt files with the respective votes.```

```--pos: Number of legal positive votes, for 1-9 give 9```

```--neg: number of legal negative votes, for 5x -1 return 5```

```--animes: Path to the file containing the names of the animes in terms of how they are listed for voting.```


The output is a sorted list of animes.

# Example
There is already an example in the repo which can be executed as follows:

```python3 main.py --path votes/ --neg 2 --pos 6 --animes animes.txt```

Result:
```
Cowboy Bebop, Relative Score: 3, Total Points: 15
Toradora!, Relative Score: 3, Overall Points: 7
Steins;Gate, Relative Score: 2, Overall Points: 7
Attack on Titan, Relative Score: 1, Overall Points: 8
My Neighbour Totoro, Relative Score: 1, Overall Points: 5
Psycho-Pass, Relative Score: 1, Overall Points: 5
Paranoia Agent, Relative Score: 1, Overall Points: 4
Demon Slayer: Kimetsu no Yaiba, Relative Score: 1, Overall Points: 3
One Punch Man, Relative Score: 0, Overall Points: 0
Your Lie in April, Relative Score: -1, Overall Points: 3
```
