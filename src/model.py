

class RiskModel:

    def __init__(self, model_path="models/model_data.txt"):
        self._payload = {"grade": {}, "sub_grade": {},
                      "int_rate": [], "out_prncp": []}

        with open(model_path) as file:
            lines = file.readlines()
            for line in lines:
                line = line.replace('"', "")
                feature, instance, points = line.split(",")
                points = float(points)
                if feature in ["grade", "sub_grade"]:
                    self._payload[feature][instance.lstrip(feature + "_")] = points
                elif feature in ["int_rate", "out_prncp"]:
                    maximum = instance.split()[1].split('|')[1]
                    self._payload[feature].append((float(maximum), points))
                else:
                    raise ValueError
        self._payload["int_rate"].sort(key=self.__sorter)
        self._len_int_rate = len(self._payload["int_rate"])
        self._payload["out_prncp"].sort(key=self.__sorter)
        self._len_out_prncp = len(self._payload["out_prncp"])

    def predict(self, data):
        """Returns a scoreboard of the credit risk of lending money to an
        individual"""

        sub_grade = data.get("sub_grade")
        int_rate = data.get("int_rate")
        out_prncp = data.get("out_prncp")
        if sub_grade is None or int_rate is None or out_prncp is None:
            raise ValueError("One or more data is required")
        grade = sub_grade[0]
        buffer = 0
        if grade not in self._payload["grade"] or \
                sub_grade not in self._payload["sub_grade"]:
            raise ValueError("Error with input data")
        buffer += self._payload["grade"][grade]
        buffer += self._payload["sub_grade"][sub_grade]

        for i in range(self._len_int_rate):
            maximum, points = self._payload["int_rate"][i]
            if int_rate <= maximum or self._len_int_rate-1 == i:
                buffer += points
                break

        for i in range(self._len_out_prncp):
            maximum, points = self._payload["out_prncp"][i]
            if out_prncp <= maximum or self._len_out_prncp-1 == i:
                buffer += points
                break
        return buffer

    @staticmethod
    def __sorter(e):
        return e[0]