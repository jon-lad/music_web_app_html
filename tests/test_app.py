from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
Test GET /albums
  expected:
  Status code 200 OK:
  h1 to contain Albums
"""
def test_get_albums_has_title_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Albums")

"""
Test GET /albums
  expected:
  Status code 200 OK:
  there to be 12 article tags
"""
def test_get_albums_has_all_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    article_tag = page.locator("article")
    expect(article_tag).to_have_count(12)

"""
Test GET /albums
  expected:
  Status code 200 OK:
  there to be an article with id = "2"
  which contains correct album information
"""
def test_get_albums_has_albums_with_text(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    article_tag_2 = page.locator('article[id="2"]')
    p_tag = article_tag_2.locator("p")
    expect(p_tag).to_have_text("Title: Surfer Rosa\nReleased: 1988")
    

"""
Test GET /albums/1
  expected:
  Status code 200 OK:
  h1 to contain Doolittle
"""
def test_get_albums_1_has_album_title(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Doolittle")

"""
Test GET /albums/7
  expected:
  Status code 200 OK:
  there to be a article with id = "7"
  which contains correct album information
"""
def test_get_albums_7_has_album_with_text(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/7")
    article_tag_2 = page.locator('article[id="7"]')
    p_tag = article_tag_2.locator("p")
    expect(p_tag).to_have_text("Released: 2020")

"""
Test GET /albums/8
  expected:
  Status code 200 OK:
  there to be 1 article tags
"""
def test_get_albums_8_has_one_article(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/8")
    article_tag = page.locator("article")
    expect(article_tag).to_have_count(1)