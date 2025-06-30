def get_melon_best_album(genres, plays):
    from collections import defaultdict

    genre_play_count = defaultdict(int)
    genre_song_list = defaultdict(list)

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        genre_play_count[genre] += play
        genre_song_list[genre].append((play, idx))  # 플레이 수 기준 정렬을 위해 (play, index)

    # 재생 수 총합 기준으로 장르 정렬
    sorted_genres = sorted(genre_play_count, key=lambda g: genre_play_count[g], reverse=True)

    result = []
    for genre in sorted_genres:
        # 해당 장르 안에서 play 수로 정렬 (동률이면 인덱스 낮은 순)
        songs = sorted(genre_song_list[genre], key=lambda x: (-x[0], x[1]))
        result.extend([idx for play, idx in songs[:2]])  # 최대 2곡까지 선택

    return result

print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(
    ["classic", "pop", "classic", "classic", "pop"],
    [500, 600, 150, 800, 2500]))

print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(
    ["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"],
    [2000, 500, 600, 150, 800, 2500, 2000]))
