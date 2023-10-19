import discord, os, sqlite3

from discord.ext import commands
from colorama import Fore
from datetime import datetime
from getpass import getpass

# ---------------------------------------------------------------- Config ----------------------------------------------------------------
def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

with create_connection(os.path.join(os.getcwd(), "./database/auto.db")) as conn:
    cur = conn.cursor()
    if conn is not None:
        cur.execute("""CREATE TABLE IF NOT EXISTS auth(id INTEGER PRIMARY KEY,token VARCHAR(255), channel_id VARCHAR(255));""")
        cur.execute("""CREATE TABLE IF NOT EXISTS whitelist(id INTEGER PRIMARY KEY,member_id VARCHAR(255));""")
        conn.commit()

        cur.execute("SELECT token FROM auth;")
        row = cur.fetchone()
        if row is None:
            cur.execute("INSERT INTO auth (token, channel_id) VALUES ('UrFingPoor', '00000000000000');")
        conn.commit()
    else:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [{Fore.LIGHTRED_EX}Local Database Error{Fore.WHITE}].')  

def GetChannelID():
    cur.execute(f"SELECT channel_id FROM auth;")
    channel_id = cur.fetchone()
    return channel_id[0]  
     
def GetToken():
    cur.execute(f"SELECT token FROM auth;")
    Token = cur.fetchone()
    return Token[0]
# ---------------------------------------------------------------- Bot ----------------------------------------------------------------
FriendlyStaff = commands.Bot(command_prefix="!!",help_command=None, status=discord.Status.do_not_disturb)
# ---------------------------------------------------------------- Handling/Events ----------------------------------------------------------------
@FriendlyStaff.event
async def on_command_error(error):
    if isinstance(error, commands.MissingRequiredArgument):
        print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [{Fore.LIGHTRED_EX}Error{Fore.WHITE}]{Fore.WHITE} [+] You are missing input requirements.')
    elif isinstance(error, discord.HTTPException):
       print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [{Fore.LIGHTRED_EX}Error{Fore.WHITE}]{Fore.WHITE} [+] You are ratelimited | Request could not be sent.')
    elif isinstance(error, commands.CommandNotFound):
        print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [{Fore.LIGHTRED_EX}Error{Fore.WHITE}]{Fore.WHITE} [+] That is not a command. Do {FriendlyStaff.command_prefix}help for commands')   
    elif isinstance(error, discord.ClientException):
        pass 
    else:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [{Fore.LIGHTRED_EX}Error{Fore.WHITE}]{Fore.WHITE} [+] {error}')
# ---------------------------------------------------------------- Commands ----------------------------------------------------------------    

@FriendlyStaff.command()
async def add(ctx, Member_ID):
    cur.execute(f"SELECT member_id FROM whitelist;") 
    WhitedListedFriends = list(cur.fetchall())
    for i in WhitedListedFriends:
        if ctx.author.id == int(i[0]):
            WhiteListUser(Member_ID)
            Logo() 
            await ctx.send(f"User Was Added To Whitedlist", delete_after=2)
        else:
            pass

@FriendlyStaff.command()
async def remove(ctx, Member_ID):
    cur.execute(f"SELECT member_id FROM whitelist;") 
    WhitedListedFriends = list(cur.fetchall())
    for i in WhitedListedFriends:
        if ctx.author.id == int(i[0]):
            RemoveWhiteListUser(Member_ID)
            Logo() 
            await ctx.send(f"User Was Removed From Whitedlist", delete_after=2)
        else:
            pass        

@FriendlyStaff.command()
async def help(ctx):
    cur.execute(f"SELECT member_id FROM whitelist;") 
    WhitedListedFriends = list(cur.fetchall())
    for i in WhitedListedFriends:
        if ctx.author.id == int(i[0]):
            hidemsg = '||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||'         
            await ctx.send(f"{hidemsg} https://tinyurl.com/UrFingPoor")
        else:
            pass

@FriendlyStaff.command()
async def kick(ctx, user: discord.Member):
    cur.execute(f"SELECT member_id FROM whitelist;") 
    WhitedListedFriends = list(cur.fetchall())
    for i in WhitedListedFriends:
        if ctx.author.id == int(i[0]):
            channel = FriendlyStaff.get_channel(int(GetChannelID()))
            await ctx.send(f"{user.mention} Was kicked From Voice Call", delete_after=2)
            await channel.send(f"!voice-kick {user.mention}")
        else:
            pass           
        
@FriendlyStaff.command()
async def ban(ctx, user: discord.Member):
    cur.execute(f"SELECT member_id FROM whitelist;") 
    WhitedListedFriends = list(cur.fetchall())
    for i in WhitedListedFriends:
        if ctx.author.id == int(i[0]):
            channel = FriendlyStaff.get_channel(int(GetChannelID()))
            await ctx.send(f"{user.mention} Was Banned From Voice Call", delete_after=2)
            await channel.send(f"!voice-ban {user.mention}")
        else:
            pass           

@FriendlyStaff.command()
async def unban(ctx, user: discord.Member):
    cur.execute(f"SELECT member_id FROM whitelist;") 
    WhitedListedFriends = list(cur.fetchall())
    for i in WhitedListedFriends:
        if ctx.author.id == int(i[0]):
            channel = FriendlyStaff.get_channel(int(GetChannelID()))
            await ctx.send(f"{user.mention} Was Unbanned From Voice Call", delete_after=2)
            await channel.send(f"!voice-unban {user.mention}")
        else:
            pass          

@FriendlyStaff.command()
async def hide(ctx):
    cur.execute(f"SELECT member_id FROM whitelist;") 
    WhitedListedFriends = list(cur.fetchall())
    for i in WhitedListedFriends:
        if ctx.author.id == int(i[0]):
            channel = FriendlyStaff.get_channel(int(GetChannelID()))
            await ctx.send(f"Voice Call Hidden!", delete_after=2)
            await channel.send(f"!voice-hide")
        else:
            pass

@FriendlyStaff.command()
async def show(ctx):
    cur.execute(f"SELECT member_id FROM whitelist;") 
    WhitedListedFriends = list(cur.fetchall())
    for i in WhitedListedFriends:
        if ctx.author.id == int(i):
            channel = FriendlyStaff.get_channel(int(GetChannelID()))
            await ctx.send(f"Voice Call Unhidden!", delete_after=2)
            await channel.send(f"!voice-reveal")
        else:
            pass

@FriendlyStaff.command()
async def limit(ctx, value):
    cur.execute(f"SELECT member_id FROM whitelist;") 
    WhitedListedFriends = list(cur.fetchall())
    for i in WhitedListedFriends:
        if ctx.author.id == int(i[0]):
            channel = FriendlyStaff.get_channel(int(GetChannelID()))
            await ctx.send(f"Changed Voice Call Limit Changed To: {value}", delete_after=2)
            await channel.send(f"!voice-limit {value}") 
        else:
            pass           

@FriendlyStaff.command()
async def lock(ctx):
    cur.execute(f"SELECT member_id FROM whitelist;") 
    WhitedListedFriends = list(cur.fetchall())
    for i in WhitedListedFriends:
        if ctx.author.id == int(i[0]):
            channel = FriendlyStaff.get_channel(int(GetChannelID()))
            await ctx.send(f"Voice Call Locked!", delete_after=2)
            await channel.send(f"!voice-lock")
        else:
            pass

@FriendlyStaff.command()
async def unlock(ctx):
    cur.execute(f"SELECT member_id FROM whitelist;") 
    WhitedListedFriends = list(cur.fetchall())
    for i in WhitedListedFriends:
        if ctx.author.id == int(i[0]):
            channel = FriendlyStaff.get_channel(int(GetChannelID()))
            await ctx.send(f"Voice Call Unlocked!", delete_after=2)
            await channel.send(f"!voice-unlock") 
        else:
            pass
# ---------------------------------------------------------------- Entry Point / Main ----------------------------------------------------------------
"""
You can add custom logos here.
FriendlyStaff used patorjk.

Link: https://patorjk.com/software/taag/
"""

def InitGradientLoad(text):
    faded = ""
    red = 40
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
        if not red == 255:
            red += 15
            if red > 255:
                red = 255
    return faded

def Logo():
    os.system("cls")
    os.system('title FriendlyStaff v1.0')
    logo = """
            ███████╗██████╗ ██╗███████╗███╗   ██╗██████╗ ██╗  ██╗   ██╗███████╗████████╗ █████╗ ███████╗███████╗
            ██╔════╝██╔══██╗██║██╔════╝████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔════╝
            █████╗  ██████╔╝██║█████╗  ██╔██╗ ██║██║  ██║██║   ╚████╔╝ ███████╗   ██║   ███████║█████╗  █████╗  
            ██╔══╝  ██╔══██╗██║██╔══╝  ██║╚██╗██║██║  ██║██║    ╚██╔╝  ╚════██║   ██║   ██╔══██║██╔══╝  ██╔══╝  
            ██║     ██║  ██║██║███████╗██║ ╚████║██████╔╝███████╗██║   ███████║   ██║   ██║  ██║██║     ██║     
            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝   ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝     
                                      ╔══════════════════════════════════════════╗
                                      ║         Freind's Have Power Too          ║    
                                      ║        FriendlyStaff Version 1.0         ║
                                      ║  Developed By: (Josh)UrFingPoor & Maxie  ║
                                      ╚══════════════════════════════════════════╝
    """
    print(InitGradientLoad(logo))

def ChangeToken(discord_token):
    try:
        cur.execute(f"UPDATE auth SET token='{discord_token}';")
        conn.commit()
        os.system("cls")
        print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [{Fore.LIGHTRED_EX}Alert{Fore.WHITE}] [+] {Fore.LIGHTGREEN_EX}Successfully {Fore.WHITE}Changed discord token.')
        main() 
    except:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [{Fore.LIGHTRED_EX}Alert{Fore.WHITE}] [+] Local DB Error.')            

def WhiteListUser(whitelistedid):
    try:
        cur.execute(f"INSERT INTO whitelist (member_id) VALUES ({whitelistedid});")
        conn.commit()
        os.system("cls")
        print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [{Fore.LIGHTRED_EX}Alert{Fore.WHITE}] [+] {Fore.LIGHTGREEN_EX}Successfully {Fore.WHITE}Added Friend To Whitelist.')              
    except:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [{Fore.LIGHTRED_EX}Alert{Fore.WHITE}] [+] Local DB Error.')           

def RemoveWhiteListUser(whitelistedid):
    try:
        cur.execute(f"DELETE FROM whitelist WHERE member_id = '{whitelistedid}';")
        conn.commit()
        os.system("cls")
        print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [{Fore.LIGHTRED_EX}Alert{Fore.WHITE}] [+] {Fore.LIGHTGREEN_EX}Successfully {Fore.WHITE}Removed Friend From Whitelist.')              
    except:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [{Fore.LIGHTRED_EX}Alert{Fore.WHITE}] [+] Local DB Error.')           

def UpdateChannelID(channel_id):
    try:
        cur.execute(f"UPDATE auth SET channel_id='{channel_id}';")
        conn.commit()
        os.system("cls")
        print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [{Fore.LIGHTRED_EX}Alert{Fore.WHITE}] [+] {Fore.LIGHTGREEN_EX}Successfully {Fore.WHITE}Changed Channel ID.')
        main() 
    except:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [{Fore.LIGHTRED_EX}Alert{Fore.WHITE}] [+] Local DB Error.')            

def main():
    Logo()
    print(f'{Fore.LIGHTYELLOW_EX}\n\nOptions:\n1. Run Bot\n2. Add User\n3. Remove User\n4. Change Token\n5. Change Channelid\n6. Exit Application{Fore.WHITE}\n')
    match input(f"{Fore.WHITE}What's Your Choice: "):
        case "1":
            Logo()
            print(f"\nYou have {Fore.LIGHTGREEN_EX}Successfully{Fore.WHITE} Logged in! Please Enjoy Using {Fore.LIGHTYELLOW_EX}Friendly Staff{Fore.WHITE} v1.0.")
            FriendlyStaff.run(f"{GetToken()}")          
        case "2":
            user_id = input(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.LIGHTGREEN_EX}Info{Fore.WHITE}] [+] Enter The Person You Wish To Whitelist: ')
            WhiteListUser(user_id)   
            main()  
        case "3":
            user_id = input(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.LIGHTGREEN_EX}Info{Fore.WHITE}] [+] Enter The Person You Wish To Remove From Whitelist: ')
            RemoveWhiteListUser(user_id)   
            main()
        case "4":
            token = getpass(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.LIGHTGREEN_EX}Info{Fore.WHITE}] [+] Enter Your {Fore.LIGHTMAGENTA_EX}Discord{Fore.WHITE} Key ({Fore.LIGHTGREEN_EX}Right-Click To Paste {Fore.WHITE}|{Fore.LIGHTGREEN_EX} Token Will Not Show{Fore.WHITE}): ')
            ChangeToken(token)     
        case "5":
            ChannelID = input(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.LIGHTGREEN_EX}Info{Fore.WHITE}] [+] Enter The Channel ID: ')
            UpdateChannelID(ChannelID)               
        case "6":
            exit()
    
if __name__ == "__main__":
	main()
