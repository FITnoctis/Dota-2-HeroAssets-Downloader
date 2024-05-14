import requests
import os
from tqdm import tqdm

url = "https://api.opendota.com/api/heroes"

path = input("Enter Folder name: ")
response = requests.get(url)
data = response.json()

for hero in data:
    hero_name = hero['localized_name'].replace(' ', '-')
    if hero_name == "Centaur-Warrunner":
        hero_name = "centaur-warchief"
        hero_image_url = f"https://www.dotafire.com/images/hero/icon/{hero_name}.png"
    elif hero_name == "Nature's-Prophet":
        hero_name = "Natures-Prophet"
        hero_image_url = f"https://www.dotafire.com/images/hero/icon/{hero_name}.png"
    hero_image_url = f"https://www.dotafire.com/images/hero/icon/{hero_name}.png"
    

    # Download the hero image
    response = requests.get(hero_image_url, stream=True)
    if response.status_code == 200:
        # Create the directory if it doesn't exist
        os.makedirs(path, exist_ok=True)

        # Save the image to a file
        with open(f"{path}/{hero_name}.png", "wb") as file:
            total_size = int(response.headers.get('content-length', 0))
            progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True, desc=f"Downloading {hero_name}.png")
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
                progress_bar.update(len(chunk))
            progress_bar.close()

    else:
        print(f"No image found for {hero_name}")

print("Image download completed!")
