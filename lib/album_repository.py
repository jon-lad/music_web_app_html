from lib.album import Album

class AlbumRepository:
    def __init__(self, connection) -> None:
        self.connection = connection
    
    def all(self):
        self.connection.connect()
        rows = self.connection.execute("SELECT * FROM albums")
        albums = []
        for row in rows:
            albums.append(Album(row["id"], row["title"], row["release_year"], row["artist_id"]))

        return albums
    
    def find(self, album_id):
        self.connection.connect()
        rows = self.connection.execute('SELECT * FROM albums WHERE id = %s', [album_id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])
    
    def create(self, album):
        self.connection.connect()
        rows = self.connection.execute("""INSERT INTO albums (title, release_year, artist_id) 
                                VALUES (%s, %s, %s)
                                RETURNING id""",
                                [
                                    album.title,
                                    album.release_year,
                                    album.artist_id
                                ])
        row = rows[0]
        album.id = row["id"]
        return album
        
    def delete(self, id):
        self.connection.connect()
        self.connection.execute("DELETE FROM albums WHERE id = %s", [id])