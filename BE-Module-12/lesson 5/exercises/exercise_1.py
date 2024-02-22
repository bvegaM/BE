# Bubble sort to sort videos in playlists alphabetically by title
def bubble_sort_by_title(playlist):
    n = len(playlist)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if playlist[j]["title"] > playlist[j + 1]["title"]:
                playlist[j], playlist[j + 1] = playlist[j + 1], playlist[j]

# Test the sorting function
playlist = [
    {"title": "Video X", "duration": 180, "upload_date": "2022-01-01"},
    {"title": "Video A", "duration": 240, "upload_date": "2021-12-15"},
    {"title": "Video Z", "duration": 200, "upload_date": "2022-01-10"},
]

print("\nPlaylist Before Sorting:")
for video in playlist:
    print(video)

bubble_sort_by_title(playlist)
print("\nPlaylist Sorted by Title:")
for video in playlist:
    print(video["title"])