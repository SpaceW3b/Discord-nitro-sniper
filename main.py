import re, requests

from colorama import Fore, init
from discord.ext import commands

#By Space#2000
init()
SpaceSniper = commands.Bot(command_prefix="!", help_command=None, self_bot=False)

alt_token = "Ici faut que tu mettes le token de ton dc parce que y'a des petits chance pour que tu chope un ban"
nitro_redeem_token = "bon la tu met ton vrai token, t'aurais pas envie que ton dc recup le nitro pas vrai :)"


@SpaceSniper.event
async def on_connect():
    print("Tout est bon, les nitros seront automathiquement recup")


@SpaceSniper.event
async def on_message(message):
    try:
        if 'discord.gift/' in message.content:
            code = re.search("discord.gift/(.*)", message.content).group(1)
            headers = {
                'Authorization': nitro_redeem_token,
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36 "
            }
            nitro = f"{Fore.MAGENTA}Nitro-Sniper {Fore.RESET}| Code: {Fore.BLUE}{code} {Fore.RESET}| "
            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers)
            if '{"message": "Faux cadeau nitro", "code": 10038}' in r.text:
                print(nitro + Fore.RED + "Le code est invalide!")
            elif '{"message": "Le cadeau à déjà été récup.", "code": 50050}' in r.text:
                print(nitro + Fore.YELLOW + "Déjà récup...!")
            elif 'Aie, tes rate limite...' in r.text:
                print(nitro + Fore.RED + "FAIT GAFFE TES RATE LIMITE!")
            elif 'Accès refusé...' in r.text:
                print(nitro + Fore.RED + "Accès réfusé!")
            elif 'subscription_plan' in r.text:
                print(nitro + Fore.GREEN + "GG T'A EU UN NITRO")
    except AttributeError:
        pass


SpaceSniper.run(alt_token, bot=False)
