class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username.lower() == username.lower():
                return user
        return None

    def update(self, user):
        target = self.find(user.username)
        if target:
            target.name, target.email = user.name, user.email
            
    def delete(self, username):
        for i, user in enumerate(self.users):
            if user.username.lower() == username.lower():
                del self.users[i]
                break

    def list_all(self):
        return self.users

# Créez des instances d'utilisateurs avec la classe User
users = [User('aakash', 'Aakash Rai', 'aakash@example.com'),
 User('biraj', 'Biraj Das', 'biraj@example.com'),
 User('hemanth', 'Hemanth Jain', 'hemanth@example.com'),
 User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com'),
 User('siddhant', 'Siddhant Sinha', 'siddhant@example.com'),
 User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com'),
 User('vishal', 'Vishal Goel', 'vishal@example.com')]

database = UserDatabase()

# Insérez les utilisateurs dans la base de données
for user in users:
    database.insert(user)

# Effectuez la recherche pour 'aakash'
user = database.find('siddhant')
if user:
    print(user.username, user.name, user.email)
else:
    print("Utilisateur introuvable")
    
# Delete the user 'aakash'
# database.delete('aakash')