class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement

    def __repr__ (self):
        return f'<User {self.name}>'
    
user0 = User("Maya", 32)

print(user0)