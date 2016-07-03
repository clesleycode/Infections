################################
# Lesley Cordero
# Khan Academy Project
################################

from user import User


class user_test(N):
    def test_user_id_unique(self, N):
        """Tests that all IDs are unique"""
        

    def test_add_coach_simple(self):
        """Using student.add_coach(coach) updates student *and* coach"""


    def test_add_coach_iterative(self):
        """Using student.add_coach() with a list of coaches updates everybody."""
        A = User()
        coaches = [User() for user in range(5)]
        A.add_coach(coaches)
        self.assertEqual(A._User__coached_by, set(coaches))
        for c in coaches:
            self.assertEqual(c.students(), set([A]))

    def test_add_coach_breaks_without_user(self):
        A = User()
        B = "coach"
        with self.assertRaises(TypeError):
            A.add_coach(B)

    def test_coaches_accessor(self):
        A = User()
        coaches = [User() for user in range(5)]
        A.add_coach(coaches)
        self.assertEqual(A.coaches(), set(coaches))


if __name__ == "__main__":
    unittest.main()
