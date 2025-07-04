from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
Test GET /albums
  expected:
  Status code 200 OK:
  h1 to contain Albums
"""
def test_get_albums_has_title_albums(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Albums")

"""
Test GET /albums
  expected:
  Status code 200 OK:
  there to be 12 li tags
"""
def test_get_albums_has_all_albums(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    li_tag = page.locator("li")
    expect(li_tag).to_have_count(12)

"""
Test GET /albums
  expected:
  Status code 200 OK:
  there to be a li with id = "2"
  which contains correct album title
"""
def test_get_albums_has_albums_with_text(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    li_tag_2 = page.locator('li[id="2"]')
    expect(li_tag_2).to_have_text("Surfer Rosa")
    
"""
Test GET /albums/1
  expected:
  Status code 200 OK:
  h1 to contain Doolittle
"""
def test_get_albums_1_has_album_title(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Doolittle")

"""
Test GET /albums/7
  expected:
  Status code 200 OK:
  there to be a paragraph with class t_release_year
  which contains correct album information
"""
def test_get_albums_7_has_album_with_text(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/7")
    release_year_tag = page.locator(".t_release_year")
    expect(release_year_tag).to_have_text("Released: 2020")

"""
Test click on album link 'Waterloo'
  expected:
  Status code 200 OK:
  there to be an paragraph with class t_release_year
  which contains correct album information
"""
def test_link_takes_to_correct_page(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click('text="Waterloo"')
    release_year_tag = page.locator(".t_release_year")
    expect(release_year_tag).to_have_text("Released: 1974")

"""
Test clicking on back returns to albums page
"""
def test_click_back_takes_you_back_to_albums(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click('text="Waterloo"')
    page.click('text="Go back to list of albums"')
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Albums")

"""
Test GET /artists
  expected:
  Status code 200 OK:
  h1 to contain Artist
"""
def test_get_artists_has_title_artists(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Artists")

"""
Test GET /artists
  expected:
  Status code 200 OK:
  there to be 4 li tags
"""
def test_get_artists_has_all_artists(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    li_tag = page.locator("li")
    expect(li_tag).to_have_count(4)

"""
Test GET /artists
  expected:
  Status code 200 OK:
  there to be a li with id = "2"
  which contains correct album information
"""
def test_get_artists_has_li_with_name(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    li_tag_2 = page.locator('li[id="2"]')
    expect(li_tag_2).to_have_text("ABBA")
    

"""
Test GET /artists/1
  expected:
  Status code 200 OK:
  h1 to contain Pixies
"""
def test_get_artist_1_has_name(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/1")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Pixies")

"""
Test GET /artists/4
  expected:
  Status code 200 OK:
  there to be a paragraph with class t_genre
  which contains correct artist information
"""
def test_get_artist_4_has_genre_with_text(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/4")
    genre_tag = page.locator(".t_genre")
    expect(genre_tag).to_have_text("Genre: Jazz")

"""
Test click on artist link 'Taylor Swift'
  expected:
  Status code 200 OK:
  there to be an paragraph with class t_genre
  which contains correct artist information
"""
def test_artist_link_takes_to_correct_page(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click('text="Taylor Swift"')
    genre_tag = page.locator(".t_genre")
    expect(genre_tag).to_have_text("Genre: Pop")


"""
Test clicking on back returns to artist page
"""
def test_click_back_takes_you_back_to_artists(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click('text="Nina Simone"')
    page.click('text="Go back to list of artists"')
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Artists")

"""
Test adding a new album
"""
def test_adding_album_takes_you_to_album_page(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")

    page.click("text='Add new album'")

    page.fill("input[name=title]", "Test Title")
    page.fill("input[name=release_year]", "2025")
    page.select_option("select[name=artist]", "ABBA")

    page.click("text='Add album'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Test Title")

"""
Try to add an album without filling in the forms
Then the form shows some errors
"""
def test_attempt_to_make_an_album_with_errors(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")

    page.click("text='Add new album'")
    page.click("text='Add album'")

    errors_tag = page.locator(".t_errors")
    expect(errors_tag).to_have_text(
        "Your form contained errors: Title can't be blank, "\
        "Release Year can't be blank")
    
"""
Try to add an album with inalild year
Then the form shows some errors
"""
def test_attempt_to_make_an_a_with_invalid_year(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")

    page.click("text='Add new album'")
    page.fill("input[name='release_year']", "hello")
    page.click("text='Add album'")
    

    errors_tag = page.locator(".t_errors")
    expect(errors_tag).to_have_text(
        "Your form contained errors: Title can't be blank, "\
        "Invalid input for Release Year")
    
"""
Test adding a new artist
"""
def test_adding_artist_takes_you_to_artist_page(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")

    page.click("text='Add new artist'")

    page.fill("input[name='name']", "Test name")
    page.fill("input[name='genre']", "Test genre")

    page.click("text='Add artist'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Test name")

"""
Try to add an artist without filling in the forms
Then the form shows some errors
"""
def test_attempt_to_make_an_artist_with_errors(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")

    page.click("text='Add new artist'")
    page.click("text='Add artist'")

    errors_tag = page.locator(".t_errors")
    expect(errors_tag).to_have_text(
        "Your form contained errors: Title can't be blank, "\
        "Genre can't be blank")
    
"""
Test deleting an album removes it from the list
"""
def test_delete_an_album(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")

    page.click("text='Delete album'")
    page.select_option("select[name='album']", "Folklore")
    page.click("text='Delete album'")
    li_tag = page.locator("li")
    expect(li_tag).to_have_count(11)
