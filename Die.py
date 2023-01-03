class Die:
    def __init__(self, left_sides, right_sides, center_sides, blank_sides):
        self.left_sides = left_sides
        self.right_sides = right_sides
        self.center_sides = center_sides
        self.blank_sides = blank_sides
        self.total_sides = left_sides+right_sides+center_sides+blank_sides

    def get_probability(self, probability_type):
        """ returns a probability for the given type"""
        if probability_type == "L":
            return self.left_sides/self.total_sides
        elif probability_type == "R":
            return self.right_sides/self.total_sides
        elif probability_type == "C":
            return self.center_sides/self.total_sides
        elif probability_type == "B":
            return self.blank_sides/self.total_sides
        else:
            raise ValueError

    def get_all_probabilities(self):
        """returns a map of all probabilities on the die"""
        types = ["L", "R", "C", "B"]
        probabilities = {}
        for type in types:
            probabilities[type] = self.get_probability(type)
        return probabilities


