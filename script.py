import requests

script_url = 'https://raw.githubusercontent.com/azvno/newtab/main/script.py'

def update_script():
    response = requests.get(script_url)
    if response.status_code == 200:
        with open('script.py', 'wb') as f:
            f.write(response.content)

update_script()
