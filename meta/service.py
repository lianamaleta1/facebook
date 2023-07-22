import requests

token = 'EABnyao4k9EoBAGSBilGsMy6SZAqtC7mLQdoCq94OLLYLZA4PkG87szaArZBmTbIUbaUTPNerUF2r812rSRQwTLvYJ2GqQNhuFLrHkNLPO0Hg9WZA71KVrNrKdI3GS0wZCoshUMfT867gzmBDU0zV65soZCpYJd0MBsyPqo3RAxudBAPep1Hnd2NQiNue8Y1f1wv8fC6ZAhKxWKont50UYb8RGZC0OX9B9rKYTS65EqHQyivq9CA1AWxPR0Eu7qCDgmIZD'
url = 'https://graph.facebook.com/v12.0/me?metadata=1'

response = requests.get(url, headers={'Authorization': f'Bearer {token}'})

print(response.json())