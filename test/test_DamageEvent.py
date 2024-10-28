from DamageEvent import *
import unittest

class DamageEventTest(unittest.TestCase):
    def setUp(self):
        self.damageEvent = DamageEvent(2, 6, 1)
        self.noCritEvent = DamageEvent(1, 8, 0, can_crit=False)
        self.noCritConditional = DamageEvent(2, 8, 0, can_crit=False, conditional_chance=0.5)
        self.alwaysHits = DamageEvent(2, 6, 1, always_hit=True)
        self.dmgOnMiss = DamageEvent(2, 6, 1, damage_on_miss=3)

    def test_calc_critical_damage(self):
        self.assertEqual(15, self.damageEvent.calc_critical_damage())
        self.assertEqual(4.5, self.noCritEvent.calc_critical_damage())
        self.assertEqual(4.5, self.noCritConditional.calc_critical_damage())
        self.assertEqual(15, self.alwaysHits.calc_critical_damage())
        self.assertEqual(15, self.dmgOnMiss.calc_critical_damage())

    def test_calc_hit_damage(self):
        self.assertEqual(8, self.damageEvent.calc_hit_damage())
        self.assertEqual(4.5, self.noCritEvent.calc_hit_damage())
        self.assertEqual(4.5, self.noCritConditional.calc_hit_damage())
        self.assertEqual(8, self.alwaysHits.calc_hit_damage())
        self.assertEqual(8, self.dmgOnMiss.calc_hit_damage())

    def test_calc_miss_damage(self):
        self.assertEqual(0, self.damageEvent.calc_miss_damage())
        self.assertEqual(0, self.noCritEvent.calc_miss_damage())
        self.assertEqual(0, self.noCritConditional.calc_miss_damage())
        self.assertEqual(8, self.alwaysHits.calc_miss_damage())
        self.assertEqual(3, self.dmgOnMiss.calc_miss_damage())

    """def test_display(self):
        self.assertEqual("2d6 + 1, 5.15 Average Damage, 100% Conditional Chance",
                         self.damageEvent.display())"""

if __name__ == 'main':
    unittest.main()