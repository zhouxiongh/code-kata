import unittest

from kata18 import Dependencies


class TestCase(unittest.TestCase):
    def test_basic(self):
        dep = Dependencies()
        dep.add_direct("A", ["B", "C"])
        dep.add_direct("B", ["C", "E"])
        dep.add_direct("C", ["G"])
        dep.add_direct("D", ["A", "F"])
        dep.add_direct("E", ["F"])
        dep.add_direct("F", ["H"])

        self.assertEqual(["B", "C", "E", "F", "G", "H"], dep.dependencies_for("A"))
        self.assertEqual(["C", "E", "F", "G", "H"], dep.dependencies_for("B"))
        self.assertEqual(["G"], dep.dependencies_for("C"))
        self.assertEqual(["A", "B", "C", "E", "F", "G", "H"], dep.dependencies_for("D"))
        self.assertEqual(["F", "H"], dep.dependencies_for("E"))
        self.assertEqual(["H"], dep.dependencies_for("F"))


if __name__ == "__main__":
    unittest.main()
