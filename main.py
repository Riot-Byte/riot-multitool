import requests, os, ipinfo, time, socket, random, discord, pyperclip
from discord.ext import commands
from discord import Webhook
from termcolor import colored

os.system('color 0a')
os.system('cls')
os.system('title RIOT Multi-tool')

ascii_art = """
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄       ▄▄  ▄         ▄  ▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄     ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄           
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░▌     ▐░░▌▐░▌       ▐░▌▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌   ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          
▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀      ▐░▌░▌   ▐░▐░▌▐░▌       ▐░▌▐░▌      ▀▀▀▀█░█▀▀▀▀  ▀▀▀▀█░█▀▀▀▀     ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌          
▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌     ▐░▌          ▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌             ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌       ▐░▌     ▐░▌          ▐░▌ ▐░▐░▌ ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌ ▄▄▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌     ▐░▌          ▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌▐░░░░░░░░░░░▌▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
▐░█▀▀▀▀█░█▀▀      ▐░▌     ▐░▌       ▐░▌     ▐░▌          ▐░▌   ▀   ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌ ▀▀▀▀▀▀▀▀▀▀▀ ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
▐░▌     ▐░▌       ▐░▌     ▐░▌       ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌             ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
▐░▌      ▐░▌  ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌          ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▄▄▄▄█░█▄▄▄▄         ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ 
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌     ▐░░░░░░░░░░░▌        ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀            ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀       ▀▀▀▀▀▀▀▀▀▀▀          ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ """

available_commands = """
[1] IP Geolocator            [4] Password generator             [7] Link hider              [10]

[2] Webhook spammer          [5] Paysafe code generator         [8] Server joiner           [11]

[3] Port scanner             [6] Server nuker                   [9] Self-bot                [12]
"""

selections = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

def geolocate():
    route = ""
    phone = ""
    timezone = ""
    hostname = ""
    access_token = '0a609209c5740c'
    address = input("IP Address : ")

    if address != "":
        handler = ipinfo.getHandler(access_token)
        details = handler.getDetails(address)
        city = details.city
        geolocation = details.loc
        country = details.country_name
        try:
            route = details.route
        except: pass
        try:
            phone = details.phone
        except: pass
        try:
            timezone = details.timezone
        except: pass
        try:
            hostname = details.hostname
        except: pass

        os.system("cls")
        print("Details for " +address)
        print("")
        print("City : " +city) #City
        print("Geolocation : " +geolocation) #Geolocation
        print("Country : " +country) #Country
        print("Hostname : " +hostname) #Hostname
        print("Route : " +route) #Route
        print("Phone : " +phone) #Phone
        print("Timezone : " +timezone) #Timezone
        print("")
        os.system('pause')
        os.system('python3 main.py')
    elif address == "":
        os.system('cls')
        os.system('python3 main.py')

def webhook_spammer():
    os.system('cls')
    msg = input("Message to spam : ")
    webhook = input("Webhook : ")
    amountToSend = input("Amount of messages to send before deleting hook : ")

    os.system("cls")
    print("Msg : "+msg)
    print("Webhook : "+webhook)
    print("")
    prompt = input("Is this correct? (y/n)")
    if prompt == "y":
        counter = 0
        while True:
            counter = counter + 1
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent {msg}")
            if data.status_code == 404:
                print(f"Sent {msg}")
                break
            if counter == int(amountToSend):
                    time.sleep(1)
                    requests.delete(webhook)
                    os.system('cls')
                    print("Webhook spammer exhausted")
                    time.sleep(2)
                    os.system('cls')
                    os.system("python3 main.py")
            else:
                try:
                    time.sleep(data.json()["retry_after"]/1000)
                except:
                    pass
    elif prompt == "n":
        print("User prompted N, going back.")
        webhook_spammer()

def portscan():
    os.system('cls')
    prompt = input("[1] Single scan\n[2] All ports scan\n\n>>> ")
    if prompt == "1":
        host = input("Host (IP) : ")
        port = input("Port to scan : ")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        try:
            if sock.connect_ex((host,port)):
                print(colored(f"Port {port} is closed.", 'red'))
            else:
                print(colored(f"Port {port} is open.", 'green'))
        except socket.gaierror as e:
            print("socket.gaierror on {host}")
            os.system("pause")
            os.system("python3 main.py")
    elif prompt == "2":
        host = input("Host (IP) : ")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        for port in range(1,65535):
            try:
                if sock.connect_ex((host,port)):
                    print(colored(f"Port {port} is closed.", 'red'))
                else:
                    print(colored(f"Port {port} is open.", 'green'))
            except socket.gaierror as e:
                print("socket.gaierror on {host}")
                os.system('pause')
                os.system('python3 main.py')

def passgen():
    os.system("cls")
    pswd = ""
    r_strings = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for i in range(1, 15):
        pswd += random.choice(r_strings)
    print(colored(f"Your password is {pswd}", 'green'))
    os.system('pause')
    os.system('python3 main.py')

def psfgen():
    num = "0123456789"
    final = ""
    prompt = input("Would you like to do a single generation or multiple generations?\n\n[1] Single\n[2] Multiple")
    if prompt == "1":
        os.system('cls')
        for _ in range(0,7):
            final += random.choice(num)
        final += "-"
        for _ in range(0, 7):
            final += random.choice(num)
        final += "-"
        for _ in range(0, 6):
            final += random.choice(num)
        print(colored(f"Your generated paysafe code is {final}", 'green'))
        os.system('pause')
        os.system('python3 main.py')
    elif prompt == "2":
        os.system('cls')
        prompt2 = input("How many? (0) for infinite: ")
        amount = 0
        if int(prompt2) == 0:
            while True:
                for _ in range(0,7):
                    final += random.choice(num)
                final += "-"
                for _ in range(0, 7):
                    final += random.choice(num)
                final += "-"
                for _ in range(0, 6):
                    final += random.choice(num)
                print(colored(f"({str(amount+1)}) Your generated paysafe code is {final}", 'green'))
                amount += 1
                final = ""
        elif int(prompt2) > 0:
            while amount < int(prompt2):
                for _ in range(0,7):
                    final += random.choice(num)
                final += "-"
                for _ in range(0, 7):
                    final += random.choice(num)
                final += "-"
                for _ in range(0, 6):
                    final += random.choice(num)
                print(colored(f"({str(amount+1)}) Your generated paysafe code is {final}", 'green'))
                amount += 1
                final = ""

def servernuke():
    os.system('cls')
    print(colored("WARNING: Ensure the bot has admin in the server you want to nuke. Gateway intents must all be enabled.", 'red'))
    bot_token = input("Bot token : ")
    
    client = commands.Bot(command_prefix='%',intents=discord.Intents.all())
    client.remove_command("help")

    @client.event
    async def on_ready():
        print(colored(f'{client.user} is ready to nuke. Run the command %startnuke in the server you want to nuke to start nuking.', 'green'))

    @client.command()
    async def startnuke(ctx):
        guild = ctx.guild
        print(colored(f"""Server nuker started on '{guild.name}'""", 'green'))
        for channel in guild.channels:
            try:
                await channel.delete()
                print(colored(f"""Nuked channel '{channel.name}'""", 'green'))
            except: print(colored(f"""Couldn't nuke '{channel.name}'""", 'red'))
        for member in guild.members:
            try:
                await member.ban()
                print(colored(f"""Banned member '{member.name}'""", 'green'))
            except: print(colored(f"""Couldn't ban '{member.name}'""", 'red'))
        for role in guild.roles:
            try:
                if role.name.lower() != "@everyone":
                    await role.delete()
                    print(colored(f"""Deleted role '{role.name}'""", 'green'))
            except: print(colored(f"""Couldn't delete role '{role.name}'""", 'red'))
                
        await ctx.guild.edit(name="NUKED NUKED NUKED NUKED", icon=None)
        print("")
        print(colored(f"""{guild.name} has been successfully nuked. Relaunch the multi-tool.""", 'green'))
        os.system('pause')
        os.system("python3 main.py")
    client.run(bot_token)
    
def linkhide():
    os.system('cls')
    text = input("Link to hide : ")
    final = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||||||||||"
    if text != "":
        try:
            final += text
            pyperclip.copy(final)
            print(colored("Text has been copied to your clipboard.", 'green'))
        except: print(colored("Error copying text to clipboard.", 'red'))
    os.system('cls')
    os.system('python3 main.py')

def svjoiner():
    os.system('cls')
    print(colored("WARNING: Ensure you have put your tokens in the ", 'red')+colored("joiner-tokens.txt ", 'green')+colored("file.", 'red'))
    print(colored("WARNING: You can be banned from Discord for this, do not use on your main.", 'red'))
    os.system('pause')
    invcode = input("Invite code : ")
    filename = open("joiner-tokens.txt")
    tokens = filename.readlines()
    for token in tokens:
        try:
            url = "https://discord.com/api/v9/invites/{}"
            
            headers = {
                "authorization":token,
                "authority":"discord.com",
                "method":"POST",
                "path":"/api/v9/invites/"+invcode,
                "scheme":"https",
                "accept":"*/*"
            }

            nigger = requests.post(url.format(invcode), headers=headers, json={})
            print(colored("Joined with ", 'green')+colored(token, 'red')+colored(f" (SUCCESS)", 'green'))
        except: print(colored("Couldn't join with ", 'green')+colored(f"{token} ", 'red')+colored(f" (FAIL)", 'green'))
    os.system('pause')
    os.system('python3 main.py')




def selfbot():
    os.system('cls')
    print(colored("WARNING: You can be banned from Discord for this, do not use on your main.", 'red'))
    os.system('pause')
    prefix = input("Bot prefix : ")
    token = input("Bot token : ")
    client = commands.Bot(command_prefix=prefix,intents=None,self_bot=True)
    client.remove_command('help')

    @client.event
    async def on_ready():
        print(colored('-', 'red')*20)
        print(colored(f"Logged in as {client.user.name}!", 'green'))
        print(colored(f"{prefix}help for a list of commands."))
        print(colored('-', 'red')*20)
    
    @client.command()
    async def iplookup(ctx, *, address):
        route = ""
        phone = ""
        timezone = ""
        hostname = ""
        access_token = '0a609209c5740c'

        if address != "":
            handler = ipinfo.getHandler(access_token)
            details = handler.getDetails(address)
            city = details.city
            geolocation = details.loc
            country = details.country_name
            try:
                route = details.route
            except: pass
            try:
                phone = details.phone
            except: pass
            try:
                timezone = details.timezone
            except: pass
            try:
                hostname = details.hostname
            except: pass

            os.system("cls")
            await ctx.send(f"""
Details for **{address}** :

City : **{city}**
Geolocation : **{geolocation}**
Country : **{country}**
Hostname : **{hostname}**
Route : **{route}**
Phone : **{route}**
Timezone : **{timezone}**
            """)

    client.run(token)


def main():
    print(colored(ascii_art, 'red'))
    print("")
    print(available_commands)
    next = (input(">>> "))
    if next in selections:
        if next == "1":
            geolocate()
        elif next == "2":
            webhook_spammer()
        elif next == "3":
            portscan()
        elif next == "4":
            passgen()
        elif next == "5":
            psfgen()
        elif next == "6":
            servernuke()
        elif next == "7":
            linkhide()
        elif next == "8":
            svjoiner()
        elif next == "9":
            selfbot()
    else:
        os.system('cls')
        print("Invalid selection!")
        time.sleep(2)
        main()


if __name__ == '__main__':
    main()