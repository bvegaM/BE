def video_search(video_list, query):
    results = []
    for video in video_list:
        if query.lower() in video["title"].lower() or query.lower() in video["channel"].lower():
            results.append(video)
    return results

# Test the video_search function
video_list = [
    {"title": "Tutorial: Python Basics", "channel": "Programming with John"},
    {"title": "Data Science Masterclass", "channel": "Tech Explorers"},
    {"title": "Web Development Crash Course", "channel": "Code Ninja"},
]

search_query = "python"
search_results = video_search(video_list, search_query)
print("Search Results:")
for video in search_results:
    print(video)