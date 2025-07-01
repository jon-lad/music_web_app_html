import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route("/albums")
def all_albums():
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    albums = album_repository.all()
    album_strings = map(lambda x: str(x), albums)
    return ",\n".join(album_strings)

@app.route("/albums", methods=["POST"])
def create_album():
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)

    title = request.form["title"]
    release_year = int(request.form["release_year"])
    artist_id = int(request.form["artist_id"])

    album = Album(None, title, release_year, artist_id)

    album_repository.create(album)

    return "Album created."

@app.route("/artists")
def get_artists():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)

    artists = artist_repository.all()
    artist_names = [artist.name for artist in artists]
    return ", ".join(artist_names)

@app.route("/artists", methods=["POST"])
def create_artist():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)

    artist_repository.create(Artist(None, request.form["name"], request.form["genre"]))
    return "Artist added."


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

