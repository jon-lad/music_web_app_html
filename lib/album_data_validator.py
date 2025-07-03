class AlbumDataValidator:
    def __init__(self, title, release_year, artist_id):
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

    def is_valid(self):
        errors = []
        if self.title == "" or self.title == None:
                errors.append("Title can't be blank")
        try:
            self.release_year = int(self.release_year)
        except ValueError:
            if self.release_year:
                errors.append("Invalid input for Release Year")
            else:
                errors.append("Release Year can't be blank")
        if len(errors) == 0:
                return True, None
        else:
                return False, ", ".join(errors)
        
    def generate_values(self):
        return (self.title, int(self.release_year), int(self.artist_id))
        