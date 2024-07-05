from game_data import data
from game_data import logo
from game_data import vs
from random import choice


def play_game():
    print("Welcome to the Higher Lower Game!")
    print(logo)
    acc = choice(data)
    lst = [acc]

    def get_next_account():
        second = choice(data)
        while second == acc or second in lst:
            second = choice(data)
        lst.append(second)
        return second

    score = 0
    while True:
        if len(lst) > len(data):
            print("You've completed the game!")
            break
        print(f"Compare A: {acc['name']}, a {acc['description']}, from {acc['country']}.")
        print(vs)
        sec = get_next_account()
        print(f"Against B: {sec['name']}, a {sec['description']}, from {sec['country']}.")
        ans = input("Who has more followers? Type 'A' or 'B': ").lower()
        if (ans == 'a' and acc['follower_count'] > sec['follower_count']) or (
                ans == 'b' and acc['follower_count'] < sec['follower_count']):
            score += 1
            acc = sec
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            break


if __name__ == '__main__':
    play_game()
