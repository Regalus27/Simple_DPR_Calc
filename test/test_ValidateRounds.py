from Attack import Attack
from Combat import validate_rounds
from DamageEvent import DamageEvent
from Round import Round
import unittest

class ValidateRoundsTest(unittest.TestCase):
    def setUp(self):
        self.attacks = [Attack('Greatsword', [DamageEvent(2, 6, 1, '+1 Greatsword')])]
        self.rounds = []
        self.rounds.append(Round(2, self.attacks, 'Round 2'))
        self.rounds.append(Round(1, self.attacks, 'Round 1'))
        self.rounds.append(Round(1, self.attacks, 'Round 1 duplicate'))
        self.rounds.append(Round(4, self.attacks, 'Round 4'))
        self.rounds.append(Round(0, self.attacks, 'Invalid Round'))
        self.rounds.append(Round(-25, self.attacks, 'Invalid Round'))
        self.rounds.append(Round(999, self.attacks, 'Invalid Round'))

    def test_validate_rounds(self):
        test_rounds = []
        test_rounds.append(Round(1, self.attacks, 'Round 1'))
        test_rounds.append(Round(2, self.attacks, 'Round 2'))
        test_rounds.append(Round(3, self.attacks)) # Duplicate of round 2 attacks
        test_rounds.append(Round(4, self.attacks, 'Round 4'))

        validated_rounds = validate_rounds(self.rounds, 4)

        self.assertEqual(len(test_rounds), len(validated_rounds))

        for i in range(len(test_rounds)):
            self.assertEqual(test_rounds[i].get_round_number(), 
                             validated_rounds[i].get_round_number())
