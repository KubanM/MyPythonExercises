class User:
    """ A member of friend face. For now we are storing only their fitst name, last name and birthday. """

    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday

        # Extract first and last names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]


user = User("David Bowman", "12344321")

print user.first_name
print user.last_name
print user.birthday
