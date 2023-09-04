# Bugs Top100 크롤링

> 이 저장소는 벅스 실시간 Top100을 크롤링하는 코드를 담고 있습니다.

## 환경 설정 및 실행

```bash
(venv) $ pip install -r requirements.txt
(venv) $ python bugs_top100/main.py
```

## 예제

```python
$ pip install git+https://github.com/sigmadream/bugs_top100
$ python

>>> from bugs_top100 import get_songs
>>> get_songs()
[{'song_no': '6213264', 'title': 'Love Lee', 'artist': 'AKMU(악뮤)', 'album': 'Love Lee'}, {'song_no': '6208880', 'title': 'ETA', 'artist': 'NewJeans', 'album': "NewJeans 2nd EP 'Get Up'"}, {'song_no': '6213265', 'title': '후라이의 꿈', 'artist': 'AKMU(악뮤)', 'album': 'Love Lee'}, {'song_no': '6211874', 'title': 'Fast Forward', 'artist': '전소미', 'album': 'GAME PLAN'}, {'song_no': '6206291', 'title': 'Super Shy', 'artist': 'NewJeans', 'album': "NewJeans 2nd EP 'Get Up'"}, {'song_no': '6207490', 'title': 'Seven (feat. Latto) - Clean Ver.', 'artist': '정국', 'album': 'Seven (feat. Latto) - Clean Ver.'}, {'song_no': '6196923', 'title': '헤어지자 말해요', 'artist': '박재정', 'album': '1집 Alone'}, {'song_no': '6206268', 'title': 'New Jeans', 'artist': 'NewJeans', 'album': "NewJea ...
```

## 참고

해당 Top100은 [벅스](https://music.bugs.co.kr/)에서 제공하고 있습니다. 패키지의 과도한 사용으로 인해서 서비스 제공자에게 불이익이 가지 않도록 주의해서 사용해주세요. 감사합니다.

## License

MIT
