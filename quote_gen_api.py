import requests

#importe une citation aléatoire d'une API
""" def get_random_quote():
    # category = enter_category()
    category = 'happiness'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text) """

# import requests
def get_random_quotes():
    # category = 'happiness'
    # api_url = 'https://api.api-ninjas.com/v1/quotes?category=art'
    api_url= 'https://zenquotes.io/api/today'
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
    if response.status_code == 200:
        data = response.json()
        return f'{data["content"]} – {data["author"]}'
    else:
        return "Could not retrieve a quote at this time."


#Affiche la citation
print("Ta citation du jour:")
print(get_random_quotes())
