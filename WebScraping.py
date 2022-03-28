import requests
from bs4 import BeautifulSoup as bs


def get_profile_image():
    github_user = input('Input GitHub user: ')
    url = 'https://github.com/' + github_user
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    profile_image = soup.find('img', {'alt': 'Avatar'})['src']
    print(profile_image)


if __name__ == "__main__":
    print("Web scrapping program, get github user profile image!")

    get_profile_image()
