from project import (
    load_planets,
    load_quiz,
    random_planet_name,
    valid_planets,
    quiz_result
)

planets = load_planets()
questions = load_quiz()


def test_load_planets():
    assert isinstance(planets, dict)
    assert len(planets) == 8
    assert "Earth" in planets
    assert "Mars" in planets


def test_load_quiz():
    assert isinstance(questions, list)
    assert len(questions) >= 10


def test_random_planet_name():
    planet = random_planet_name(planets)
    assert planet in planets


def test_valid_planets():
    assert valid_planets(planets, "Earth", "Mars")
    assert not valid_planets(planets, "Earth", "Earth")
    assert not valid_planets(planets, "Earth", "Pluto")
    assert not valid_planets(planets, "Pluto", "Earth")


def test_quiz_result():
    assert quiz_result(5) == "🌟 Outstanding! You're a Solar System expert!"
    assert quiz_result(4) == "🚀 Excellent! You know your planets very well."
    assert quiz_result(3) == "🌍 Good job! You have a solid understanding of the Solar System."
    assert quiz_result(2) == "🪐 Not bad! Keep exploring the universe and you'll improve."
    assert quiz_result(1) == "☄️ You got one right. Time to brush up on your astronomy!"
    assert quiz_result(0) == "🌌 Don't worry! Every astronomer starts somewhere. Keep learning!"
