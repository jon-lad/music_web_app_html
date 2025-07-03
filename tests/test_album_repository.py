from lib.album_repository import AlbumRepository
from lib.album import Album

"""
Test calling all on album repository returns a list of 'Album insances
"""
def test_calling_all_returns_a_list_of_album_instances(db_connection):
    db_connection.seed("seeds/music_library.sql")
    album_repository = AlbumRepository(db_connection)
    

    actual = album_repository.all()

    expected = [
            Album(1, 'Doolittle', 1989, 1),
            Album(2, 'Surfer Rosa', 1988, 1),
            Album(3, 'Waterloo', 1974, 2),
            Album(4, 'Super Trouper', 1980, 2),
            Album(5, 'Bossanova', 1990, 1),
            Album(6, 'Lover', 2019, 3),
            Album(7, 'Folklore', 2020, 3),
            Album(8, 'I Put a Spell on You', 1965, 4),
            Album(9, 'Baltimore', 1978, 4),
            Album(10, 'Here Comes the Sun', 1971, 4),
            Album(11, 'Fodder on My Wings', 1982, 4),
            Album(12, 'Ring Ring', 1973, 2)
        ]
    
    assert actual == expected

"""
Test calling find with an id returns album with that id
"""
def test_calling_find_returns_album_with_id(db_connection):
    db_connection.seed("seeds/music_library.sql")
    album_repository = AlbumRepository(db_connection)

    actual = album_repository.find(7)

    expected = Album(7, 'Folklore', 2020, 3)

    assert actual == expected

"""
Test creating an album gets it returned by all
"""
def test_create_adds_album_to_list_returned_by_all(db_connection):
    db_connection.seed("seeds/music_library.sql")
    album_repository = AlbumRepository(db_connection)
    
    album = Album(None, 'Trompe le Monde', 1991, 1)
    album_repository.create(album)

    actual = album_repository.all()

    expected = [
            Album(1, 'Doolittle', 1989, 1),
            Album(2, 'Surfer Rosa', 1988, 1),
            Album(3, 'Waterloo', 1974, 2),
            Album(4, 'Super Trouper', 1980, 2),
            Album(5, 'Bossanova', 1990, 1),
            Album(6, 'Lover', 2019, 3),
            Album(7, 'Folklore', 2020, 3),
            Album(8, 'I Put a Spell on You', 1965, 4),
            Album(9, 'Baltimore', 1978, 4),
            Album(10, 'Here Comes the Sun', 1971, 4),
            Album(11, 'Fodder on My Wings', 1982, 4),
            Album(12, 'Ring Ring', 1973, 2),
            Album(13, 'Trompe le Monde', 1991, 1)
        ]
    
    assert actual == expected

"""
Test delete removes album from list returned by all
"""
def test_delete_removes_item_from_list_returned_by_all(db_connection):
    db_connection.seed("seeds/music_library.sql")
    album_repository = AlbumRepository(db_connection)
    
    album_repository.delete(8)

    actual = album_repository.all()

    expected = [
            Album(1, 'Doolittle', 1989, 1),
            Album(2, 'Surfer Rosa', 1988, 1),
            Album(3, 'Waterloo', 1974, 2),
            Album(4, 'Super Trouper', 1980, 2),
            Album(5, 'Bossanova', 1990, 1),
            Album(6, 'Lover', 2019, 3),
            Album(7, 'Folklore', 2020, 3),
            Album(9, 'Baltimore', 1978, 4),
            Album(10, 'Here Comes the Sun', 1971, 4),
            Album(11, 'Fodder on My Wings', 1982, 4),
            Album(12, 'Ring Ring', 1973, 2),
        ]
    
    assert actual == expected