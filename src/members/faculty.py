from members.members import Member

class Faculty(Member):
    def __init__(self, member_id, name):
        super().__init__(member_id, name, 10)