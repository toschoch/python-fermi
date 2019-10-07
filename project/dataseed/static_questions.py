from datetime import datetime

from project.server.models import Question, Unit, DataSource

number_unit = Unit(name="number")
density_per_squarecentimeter_unit = Unit(name="1/(centimeter)^2")
liter_unit = Unit(name="liter")
hour_unit = Unit(name="hour")

user_created = DataSource(name="UserCreated")

questions = [
    Question(text="How many cells does a human body contain?", answer=37200000000000,
             unit=number_unit, source=user_created,
             uncertainty=8100000000000, creation=datetime(2019, 5, 30, 16, 38, 55),
             reference='"An estimation of the number of cells in the human body". Annals of Human Biology. 40 (6): 463–471'),
    Question(text="How many human beings have ever lived on earth up to now?",
             answer=107000000000, unit=number_unit, source=user_created,
             uncertainty=5000000000, creation=datetime(2019, 5, 31, 12, 34, 55),
             reference='BBC, Federal Bureau of Population Reference'),
    Question(text="How many passengers travel with Swiss railways SBB in a day?",
             answer=1250000, unit=number_unit, source=user_created,
             uncertainty=100000, creation=datetime(2019, 6, 3, 5, 8, 55),
             reference='www.sbb.ch'),
    Question(text="How many passengers travel with Swiss railways SBB in a day?",
             answer=1250000, unit=number_unit, source=user_created,
             uncertainty=100000, creation=datetime(2019, 6, 3, 5, 8, 55),
             reference='www.sbb.ch'),
    Question(text="How many trees stand within the borders of Switzerland?",
             answer=535000000, unit=number_unit, source=user_created,
             uncertainty=1000000, creation=datetime(2019, 6, 3, 5, 11, 55),
             reference='www.wikipedia.com'),
    Question(text="What is the average density of hair on a human head?",
             answer=200, unit=density_per_squarecentimeter_unit, source=user_created,
             uncertainty=20, creation=datetime(2019, 6, 3, 5, 13, 55),
             reference='www.wikipedia.com'),
    Question(text="How many satellites have human beings brought to the universe?",
             answer=1495, unit=number_unit, source=user_created,
             uncertainty=20, creation=datetime(2019, 10, 1, 18, 13, 55),
             reference='https://www.campusjaeger.de'),
    Question(text="How many articles were available on wikipedia.com in 2014?",
             answer=30e+6, unit=number_unit, source=user_created,
             uncertainty=1e+6, creation=datetime(2019, 10, 1, 18, 14, 55),
             reference='https://www.campusjaeger.de'),
    Question(text="How many liters of beer are consumed in Germany per capita and year?",
             answer=100, unit=liter_unit, source=user_created,
             uncertainty=10, creation=datetime(2019, 10, 1, 18, 14, 55),
             reference='https://www.campusjaeger.de'),
    Question(text="How many hours of video are totally being uploaded to youtube.com per minute?",
             answer=300, unit=hour_unit, source=user_created,
             uncertainty=50, creation=datetime(2019, 10, 1, 18, 14, 55),
             reference='https://www.campusjaeger.de')
]