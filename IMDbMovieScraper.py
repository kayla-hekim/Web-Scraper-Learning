from bs4 import BeautifulSoup
import requests
import csv

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

page_to_scrape = requests.get("https://imdb.com/chart/top/", headers=headers)
print(f"Status Code: {page_to_scrape.status_code}")

soup = BeautifulSoup(page_to_scrape.text, "html.parser")
movie_names = soup.findAll("h3", attrs={"class": "ipc-title__text"})
ratings = soup.findAll("span", attrs={"class":"ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"})

file = open("top_24_movies_IMDb.csv", "w", newline='', encoding='utf-8')
writer = csv.writer(file)

writer.writerow(["Movie Names", "Ratings"])

if len(movie_names) == 0:
    print("No movies found. The class name might have changed.")
else:
    for movie_name,rating in zip(movie_names,ratings):
        print(movie_name.text + " - " + rating.text)
        writer.writerow([movie_name.text, rating.text])

file.close()
