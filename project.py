import json
import random


# -------------------------
# Data Loading Functions
# -------------------------


def load_planets():
    with open("planets.json") as file:
        return json.load(file)


def load_quiz():
    with open("quiz.json") as file:
        return json.load(file)


# -------------------------
# Helper Functions
# -------------------------


def random_planet_name(planets):
    return random.choice(list(planets.keys()))


def valid_planets(planets, first, second):
    if first not in planets:
        return False
    if second not in planets:
        return False
    if first == second:
        return False
    return True


def quiz_result(score):
    if score == 5:
        return "🌟 Outstanding! You're a Solar System expert!"
    elif score == 4:
        return "🚀 Excellent! You know your planets very well."
    elif score == 3:
        return "🌍 Good job! You have a solid understanding of the Solar System."
    elif score == 2:
        return "🪐 Not bad! Keep exploring the universe and you'll improve."
    elif score == 1:
        return "☄️ You got one right. Time to brush up on your astronomy!"
    else:
        return "🌌 Don't worry! Every astronomer starts somewhere. Keep learning!"


# -------------------------
# Planet Functions
# -------------------------


def show_planet(planets, name):
    planet = planets[name]

    print(f"\n====== {name} ======")
    for key, value in planet.items():
        print(f"{key.replace('_', ' ').title():<20} : {value}")


def display_planets(planets):
    print("\nAvailable Planets:")
    for planet in planets:
        print(f"- {planet}")


def view_planets(planets):
    display_planets(planets)

    name = input("\nEnter planet name: ").title()

    if name in planets:
        show_planet(planets, name)
    else:
        print("Planet not found. Please check the given name and try again.")


def compare_planets(planets):
    display_planets(planets)
    first = input("\nFirst planet: ").title()
    second = input("Second planet: ").title()

    # Ensure both planet names are valid before comparison
    if not valid_planets(planets, first, second):
        if first not in planets:
            print(f"{first} not found.")
        elif second not in planets:
            print(f"{second} not found.")
        else:
            print("Please choose two different planets.")
        return

    planet1 = planets[first]
    planet2 = planets[second]

    print(f"\n====== {first} vs {second} ======\n")

    for key in planet1:
        print(f"{key.replace('_', ' ').title()}")
        print(f"{first:<10}: {planet1[key]}")
        print(f"{second:<10}: {planet2[key]}")
        print()


def random_planet(planets):
    chosen_one = random_planet_name(planets)
    print("\n====== Random Planet of the Day ======\n")
    show_planet(planets, chosen_one)


# -------------------------
# Quiz Functions
# -------------------------


def quiz(questions):
    # Randomly choose 5 questions for each quiz attempt
    selected_questions = random.sample(questions, 5)

    score = 0

    print("\n" + "=" * 50)
    print("🌌         ASTRONOMY QUIZ         🌌")
    print("=" * 50)
    print("Answer the following 5 questions!\n")

    for number, question in enumerate(selected_questions, start=1):
        print(f"\nQuestion {number}/5")
        print("-" * 40)
        print("\n" + question['question'])

        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")

        print()

        while True:
            try:
                guess = int(input("Your answer: "))

                if 1 <= guess <= 4:
                    break

                print("Please enter a number between 1 and 4")

            except ValueError:
                print("Please enter a valid number.")

        if guess == question["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(
                f"❌ Incorrect! The correct answer was "
                f"{question['options'][question['answer'] - 1]}"
            )

    print("\n" + "=" * 50)
    print(f"FINAL SCORE: {score}/5")
    print("=" * 50)

    print(quiz_result(score))

    print("\nThanks for playing Astronomy Explorer!")


def play_quiz(questions):
    # Keep offering the quiz until the user chooses to stop
    while True:
        quiz(questions)

        again = input("\nWould you like to play the quiz again? (y/n): ").strip().lower()

        if again == "y":
            continue
        elif again == "n":
            break
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")


# -------------------------
# Main Program
# -------------------------


def main():
    planets = load_planets()
    questions = load_quiz()
    while True:
        print("\n" + "=" * 45)
        print("🌌      ASTRONOMY EXPLORER      🌌")
        print("=" * 45)
        print("1. View Planets")
        print("2. Compare Planets")
        print("3. Random Planet")
        print("4. Astronomy Quiz")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                view_planets(planets)
            elif choice == 2:
                compare_planets(planets)
            elif choice == 3:
                random_planet(planets)
            elif choice == 4:
                play_quiz(questions)
            elif choice == 5:
                print("\nThank you for using Astronomy Explorer!")
                print("Keep looking up! 🚀🌌")
                break
            else:
                print("Invalid choice. Please enter a number between 1 to 5.")
        except ValueError:
            print("Invalid choice. Please enter a number.")


if __name__ == "__main__":
    main()
