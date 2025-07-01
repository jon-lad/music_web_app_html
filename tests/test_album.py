from lib.album import Album

"""
Test Album constructs with atributes    
"""
def test_album_constructs_with_instance_properties():
    album = Album(1, "title", 2025, 1)

    assert album.id == 1
    assert album.title == "title"
    assert album.release_year == 2025
    assert album.artist_id == 1

"""
Test Albums with equal atributes are equal
"""
def test_albums_with_equal_attributes_are_equal():
    album_1 = Album(1, "title", 2025, 1)
    album_2 = Album(1, "title", 2025, 1)

    assert album_1 == album_2

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album(1, "title", 2025, 1)
    assert str(album) == "Album(1, title, 2025, 1)"