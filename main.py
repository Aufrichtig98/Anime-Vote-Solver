import os
from collections import defaultdict
from argparse import ArgumentParser
from functools import reduce

def get_argument_parser():
    p = ArgumentParser("Rank the Animes given by preference")
    p.add_argument("--path", required=True,
        help="Path to the folder containing ONLY the txt files with the respective votes")
    p.add_argument("--pos", required=True, type=int,
        help="Amount of legal positive votes, for 1-9 supply 9")
    p.add_argument("--neg", type=int, required=True,
        help="Amount of legal neg votes, for 5x -1 supply 5")
    p.add_argument("--animes", required=True,
        help="Path to the file containing the name of the animes in respect to how they are listed for the votes")
    return p

def validate_vote(vote, neg, pos, name):
    votes_done = defaultdict(int)
    for i in vote:
        votes_done[i] += 1
        if i > pos:
            print(f"Warning {name} used value {i} even though the highes vote you can give is {pos}")
            return False
    if votes_done[-1] > neg:
        print(f"Warning {name} used value -1 {votes_done[-1]} times")
        return False
    for i in range(1, pos + 1):
        if votes_done[i] > 1:
            print(f"Warning {name} used value {i} {votes_done[i]} times")
            return False
        elif votes_done[i] == 0:
            print(f"Vote for {i} was not used by {name}")
    return True

def main(args):
    # List of lists containing the votes of each person
    votes = list()
    # List of Names of all suggested Animes
    animes = list()
    anime_summed_points = defaultdict(int)
    # Iterating over all files to populate vots
    for file in os.listdir(args.path):
        name = file.split(".")[0].split("/")[-1]
        votes_file_handle = open(args.path + "/" + file, "rt")
        name_file_handle = open(args.animes, "rt")
        current_file_vote = list()
        for vote, anime in zip(votes_file_handle,name_file_handle):
            current_file_vote.append(int(vote.strip("\n")))
            animes.append(anime.strip("\n"))
            anime_summed_points[anime.strip("\n")] += int(vote.strip("\n"))
        # Validates if the vote is legal, returns -1 if not and prints a warning if votes besides 0 are unused
        if not validate_vote(current_file_vote, args.neg, args.pos, name):
            return -1
        votes.append(current_file_vote)

    # This if obviously not maintainable code and i just wanted to see if i can write it as a one line (Answer is yes)
    # First votes will be unpacked which feeds all len(votes) many lists to zip
    # Zip takes the value at position 0 of each list and constructs a tuple, we do this or each pos in list which
    # Have the same length. Each new tuple are all collected votes for that anime.
    # Now we feed these tuple into a reduce that calculates the relative sum by interpreting every pos value 1 > as 1.
    ranking = [reduce(lambda x,y: x+1 if y > 0 else x-1 if y == -1 else x+0, k, 0) for k in zip(*votes)]

    # Before we sort the animes we need to add the names to the list because currently the name is inmplied by the pos
    # in the list but this does not hold anymore after sorting
    ranking_with_names = [i for i in zip(ranking, animes)]
    ranking_with_names = sorted(ranking_with_names, key=lambda x: x[0], reverse=True)
    clustered_ranks = [[ranking_with_names[0]]]
    # After getting the relative order we still need to break ties between animes, for that we use the normal score
    # and cluster them by there score
    for i in range(1, len(ranking_with_names)):
        if ranking_with_names[i][0] == clustered_ranks[-1][-1][0]:
            clustered_ranks[-1].append(ranking_with_names[i])
        else:
            clustered_ranks.append([ranking_with_names[i]])
    final_sorted =list()
    # Last sort the break ties
    for i in clustered_ranks:
        final_sorted += sorted(i, key=lambda x: anime_summed_points[x[1]], reverse=True)

    for i in final_sorted:
        print(f"{i[1]}, Relative Score: {i[0]}, Overall Points: {anime_summed_points[i[1]]}")

if __name__ == "__main__":
    p = get_argument_parser()
    args = p.parse_args()
    main(args)