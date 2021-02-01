from bs4 import BeautifulSoup
import requests
import json

def get_ids():

    r = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('table', attrs={'class':'chart'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    movie_ids = []

    for row in rows:
        cols = row.find_all('td')
        id = cols[0].a["href"][7:-1]
        movie_ids.append(id)

    return movie_ids

def get_movie_data_from_id(id):
    movie_data = {}
    r = requests.get(f"http://www.omdbapi.com/?i=+{id}&apikey=5cd1e9b2")
    movie_json = json.loads(r.text)

    movie_data["title"] = movie_json["Title"]
    movie_data["year"] = movie_json["Year"]
    movie_data["runtime"] = movie_json["Runtime"]
    movie_data["rated"] = movie_json["Rated"]
    movie_data["genre"] = movie_json["Genre"]
    movie_data["director"] = movie_json["Director"]
    movie_data["actors"] = movie_json["Actors"]
    movie_data["plot"] = movie_json["Plot"]
    movie_data["language"] = movie_json["Language"]
    movie_data["awards"] = movie_json["Awards"]
    movie_data["poster"] = movie_json["Poster"]
    # movie_data["rotten_tomato"] = movie_json["Ratings"][1]["Value"]
    # movie_data["imdb"] = movie_json["Ratings"][0]["Value"]
    # movie_data["metacritic"] = movie_json["Ratings"][2]["Value"]

    return movie_data
