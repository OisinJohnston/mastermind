import random as r
C = ["red", "green", "blue", "orange", "purple"]
def main():
    x = r.choices(C, k=4)
    attempts = 1
    print(x)
    while True:
        print("Choose from: " + ", ".join(C))
        users_colours = input("Your four colours (space seperated): ").split(" ")
        if [i for i in users_colours if i.lower() not in C] or len(users_colours) != 4:
            print("Please double check your entry and try again")
            continue
        if users_colours == x:
            print(f"You Win! it took you {attempts} attempts")
            break
        in_correct_space = len([v for i,v in enumerate(users_colours) if x[i] == v ])
        correct_colour_wrong_place = len([i for i in users_colours if i in chosen_colours]) - in_correct_space
        print(f"Correct colour in the correct space: {in_correct_space}")
        print(f"Correct colour but in the wrong space: {correct_colour_wrong_place}")
        attempts += 1
if __name__ == "__main__":
    main()
