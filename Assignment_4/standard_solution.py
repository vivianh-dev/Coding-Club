def calculate_total_score(scores):
    return sum(scores)

def calculate_average_score(scores):
    return sum(scores) / len(scores)

def find_lowest_score(frames) -> tuple[int, int]:
    lowest_score = frames[0]
    lowest_frame = 1
    for idx, score in enumerate(frames[1:]):
        if score < lowest_score:
            lowest_score = score
            lowest_frame = idx + 2 # Offset by 1 due to 1 shift, second offset by 1 to account for 0 index
    return lowest_score, lowest_frame

def earned_free_game(scores) -> bool:
    seven_count = 0
    for score in scores:
        if score == 7:
            seven_count += 1
    return seven_count == 3

def had_turkey(scores):
    for i in range(len(scores) - 2):
        if scores[i] == 10 and scores[i+1] == 10 and scores[i+2] == 10:
            return True
    return False

def main():
    scores = [7, 9, 6, 10, 10, 10, 7, 5, 8, 7]
    total_score = calculate_total_score(scores)
    average_score = calculate_average_score(scores)
    lowest_score, lowest_frame = find_lowest_score(scores)
    free_game = earned_free_game(scores)
    turkey = had_turkey(scores)

    print("Total Score:", total_score)
    print("Average Score:", average_score)
    print("Lowest Score:", lowest_score, "in frame", lowest_frame)
    if free_game:
        print("Congratulations! You earned a free game!")
    else:
        print("You did not earn a free game this time.")
    if turkey:
        print("Congratulations! You had a Turkey!")
    else:
        print("You did not have a Turkey this time.")

if __name__ == "__main__":
    main()
