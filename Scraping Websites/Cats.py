import requests
# call = requests.get("https://catfact.ninja/fact")
call = requests.get("http://www.chartlyrics.com/api.aspx")

# print("Here's a cat fact!")
# print(call.json()['fact'])

print(call)
print(call.json()["Beetles"])