class ArtistDataValidator:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def is_valid(self):
        errors = []
        if self.title == "" or self.title == None:
            errors.append("Title can't be blank")
        if self.genre == "" or self.genre == None:
            errors.append("Genre can't be blank")
        if len(errors) == 0:
                return True, None
        else:
                return False, ", ".join(errors)
        
    def generate_values(self):
        return (self.title, self.genre)