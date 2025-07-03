import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist
from lib.album_data_validator import AlbumDataValidator
from lib.artist_data_validator import ArtistDataValidator

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route("/albums")
def all_albums():
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    album_list = album_repository.all()
    return render_template('albums/index.html', albums=album_list)

@app.route("/albums/<id>")
def selected_album(id):
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    album = album_repository.find(id)
    return render_template('albums/show.html', album=album)

@app.route("/albums/new")
def get_new_album():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artists = artist_repository.all()
    return render_template("albums/new.html", artists=artists)

@app.route("/albums", methods=["POST"])
def create_album():
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    artist_repository = ArtistRepository(connection)
    album_data_validator = AlbumDataValidator(request.form["title"],
                                              request.form["release_year"],
                                              request.form["artist"])
    valid_data, errors = album_data_validator.is_valid()
    if valid_data:
        title, release_year, artist_id = album_data_validator.generate_values()
        album = Album(None, title, release_year, artist_id)
        album = album_repository.create(album)
    else:
        artists = artist_repository.all()
        return render_template("albums/new.html", artists=artists, errors=errors)

    return redirect(f"/albums/{album.id}")

@app.route("/artists")
def get_artists():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artists = artist_repository.all()
    return render_template("artists/index.html", artists=artists)

@app.route("/artists/<id>")
def selected_artist(id):
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artist = artist_repository.find(id)
    return render_template("artists/show.html", artist=artist)

@app.route("/artists/new")
def get_new_artist():
    return render_template("artists/new.html")

@app.route("/artists", methods=["POST"])
def create_artist():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artist_data_validator = ArtistDataValidator(request.form["title"],
                                                request.form["genre"])
    valid_data, errors = artist_data_validator.is_valid()
    if valid_data:
        title, genre = artist_data_validator.generate_values()
        artist = Artist(None, title, genre)
        artist = artist_repository.create(artist)
    else:
        return render_template("artists/new.html", errors=errors)

    return redirect(f"/artists/{artist.id}")

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

