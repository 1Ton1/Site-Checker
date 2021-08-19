# Imports
import click
import json
import requests
import os, sys, time

# Requests
response = requests.get("https://api.ipify.org/?format=json")


# Define
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


jprint(response.json())


# JSON
ip = json.loads(response.text)
with open('public_ip.json', 'w', encoding='utf-8') as f:
    json.dump(ip, f, ensure_ascii=False, indent=4)

data = json.load(open('public_ip.json'))
host = data['ip']


# Click
@click.command()
@click.option('-w', '--website', prompt='Enter the website you wish to check :', default=host)
def web(website):
    click.echo(f"Website/IP = {website}")
    ping(website)


# Define
def ping(website):
    response = os.system("ping -n 10 " + website)

    if response == 0:
        print(website, ' is online.')
        sys.exit(0)
    else:
        print(website + ' is offline')


if __name__ == '__main__':
    web()

