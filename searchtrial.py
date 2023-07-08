import urllib.request
import re
import webbrowser
websites = [
    ["Google", "https://www.google.com/search?q="],
    ["YouTube", "https://www.youtube.com/results?search_query="],
    ["Facebook", "https://www.facebook.com/search/top/?q="],
    ["Amazon", "https://www.amazon.com/s?k="],
    ["Twitter", "https://twitter.com/search?q="],
    ["Instagram", "https://www.instagram.com/explore/tags/"],
    ["LinkedIn", "https://www.linkedin.com/search/results/all/?keywords="],
    ["Netflix", "https://www.netflix.com/search?q="],
    ["Reddit", "https://www.reddit.com/search?q="],
    ["Pinterest", "https://www.pinterest.com/search/pins/?q="]
]


def get_index2D(element,list):
    for i in range(len(list)):
        if element == list[i][0]:
            return i


i = get_index2D("IG",websites)
print(i)
print(websites[i])
# html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + sk)


