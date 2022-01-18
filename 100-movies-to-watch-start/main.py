import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
original_URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
contents = response.text
# print(contents)

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.prettify())
all_movies = soup.find_all(name="h3")
movies = [movie.text for movie in all_movies]
# print(movies)
movies_reverse = movies[::-1]

with open("top100-movies.csv", mode='w') as file:
    for movie in movies_reverse:
        file.write(f"{movie}\n")