import requests
from bs4 import BeautifulSoup

def get_songs():
  res = requests.get("https://music.bugs.co.kr/chart")
  soup = BeautifulSoup(res.text, "html.parser")
  tr_list = soup.select("table.byChart > tbody > tr")

  songs = []

  for rank, tr in enumerate(tr_list,1):
    song_no = tr.select_one("input")["value"]
    title_tag = tr.select_one("th > p > a")
    artist_tag = tr.select_one("td > p > a")
    album_tag = tr.select_one("td > .album")

    song = {
      "song_no": song_no,
      "title": title_tag.text,
      "artist": artist_tag.text,
      "album": album_tag.text
    }

    songs.append(song)

  return songs

if __name__ == "__main__":
  songs = get_songs()
  for song in songs:
    print(song)