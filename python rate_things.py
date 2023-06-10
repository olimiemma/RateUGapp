import requests
import json

def get_ratings(country):
  """Gets the ratings for all the things in a country.

  Args:
    country: The name of the country.

  Returns:
    A list of ratings.
  """

  url = "https://api.yelp.com/v3/businesses/search?term=restaurants&location={}".format(country)
  response = requests.get(url, headers={"Authorization": "Bearer YOUR_API_KEY"})
  if response.status_code == 200:
    data = json.loads(response.content)
    ratings = []
    for business in data["businesses"]:
      rating = business["rating"]
      ratings.append(rating)
    return ratings
  else:
    raise Exception("Error getting ratings: {}".format(response.status_code))

def main():
  """The main function"""

  country = input("Enter the name of the country: ")
  ratings = get_ratings(country)
  print("The average rating for restaurants in {} is {}".format(country, sum(ratings) / len(ratings)))

if __name__ == "__main__":
  main()
python rate_things.py
