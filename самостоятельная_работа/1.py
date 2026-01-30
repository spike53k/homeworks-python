class Team:
    def __init__(self):
        self.team_members = []
    def add_member(self, name, position):
        self.team_members.append({"имя": name, "должность": position})
    def show_team(self):
        for member in self.team_members:
            print(member)

t1 = Team()
t1.add_member("john", "программист")
t1.add_member("bob", "программист")
t1.show_team()