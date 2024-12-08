import requests
class Fetcher:
    def __init__(self):
        self.__student = requests.get(
            'https://cdn.ituring.ir/ex/users.json').json()

    def nerds(self):
        result = set()
        for i in self.__student:
            if i["score"] > 18.5:
                result.add(i["name"] + i["last_name"])
        return result

    def sultans(self):
        result = list()
        max_score = self.__student[0]["score"]
        for i in self.__student:
            if i["score"] > max_score:
                max_score = i["score"]
        for i in self.__student:
            if i["score"] == max_score:
                result.append(i["name"] + i["last_name"])
        return tuple(result)

    def mean(self):
        result = list()
        for i in self.__student:
            result.append(i["score"])
        return sum(result) / len(result)

    def get_students(self):
        result = list()
        for i in self.__student:
            result.append({
                "name": i["name"],
                "last_name": i["last_name"],
                "height": i["height"],
                "weight": i["weight"],
                "score": i["score"],
                "savings": i["savings"],
                "salary": i["salary"]
            })
        return result
