class user:
    def __init__(self,username,user_id,followers):
        self.username=username
        self.user_id=user_id
        self.followers=followers

user1=user("pavan","pavanbabu860",524)
print(user1.username)
print(user1.user_id)
print(user1.followers)