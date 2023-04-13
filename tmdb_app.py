import requests as req
import os
import json
# import random
import random

def tmdb_api_call(requestURL,parameters):
    response = req.get(url=requestURL,params=parameters)
    print(response.status_code)
    if response.status_code != 200:
        print(response.json())
        exit()
    data = response.json()
    return json.dumps(data)

def get_popular_movies_by_page(api_key, page_number=10):
    #requestURL = "https://api.themoviedb.org/3/movie/upcoming"
    requestURL = "https://api.themoviedb.org/3/movie/popular"
    parameters = {"api_key" : api_key, "page" : page_number, "language": "en-US" }
    return tmdb_api_call(requestURL, parameters)
    
def main():
    # prints a random value from the list
    ran = random.randint(5, 15)
    api_key = "e569c1e35adc9e9d76303e288fa33024"
    upcoming_movie_list = get_popular_movies_by_page(api_key,ran)
    data = json.loads(upcoming_movie_list)
    print(json.dumps(data["results"]))
	

if __name__=="__main__":
    main()
