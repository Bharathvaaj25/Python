
votes = {
    "Bharathvaaj": 0,
    "Bala": 0,
    "Charan": 0
}


def add_vote(candidate):
    if candidate in votes:
        votes[candidate] += 1
        print(f"Vote added to {candidate}")
    else:
        print("Candidate not found!")


def display_results():
    print("\n--- Voting Results ---")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")


def find_winner():
    winner = max(votes, key=votes.get)
    print(f"\nWinner is: {winner}")




print("Voting Started...\n")

add_vote("Bharathvaaj")
add_vote("Bala")
add_vote("Bharathvaaj")
add_vote("Charan")
add_vote("Bharathvaaj")
add_vote("Bala")

display_results()
find_winner()