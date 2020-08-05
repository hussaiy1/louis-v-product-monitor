from discord_hooks import Webhook
#from datetime import *

WEBHOOK_URL = 'https://discordapp.com/api/webhooks/705399430903234590/Hv-EkDa0IYehBPED2zzf0U5DB6fC7H56jji-P3ONf6MiT-8m7SIHpQnnGV8P4dGfmRUW'

#dateTimeObj = datetime.now()

embed = Webhook(
    url=WEBHOOK_URL,
    username='Louis V',  # Username of the 'bot'
    color=222222,   # Colour of the side of the embed
)

def sendHook(prodtitle, url):
    embed.set_author(name='Louis V', url=url)
    embed.set_title(title=prodtitle, url= url)
    embed.set_desc("```\n I have found a new product ```")
    #embed.add_field(name="Field 1 \U0001f603", value="some of these properties have certain limits...", inline=False)
    #embed.add_field(name="Field 2 :scream:",
    #                value="try exceeding some of them!", inline=False)
    #embed.add_field(name="Field 3 :face_with_rolling_eyes:", value="Jokes, dont do that.", inline=False)
    #embed.add_field(name="Field 4 :face_with_rolling_eyes:", value="these last two")
    #embed.add_field(name="Field 5 :face_with_rolling_eyes:", value="are inline fields")
    ## Set the timestamp to either a ISO 8601 timestamp, or simply use `now=True`, which uses current time
    #embed.set_timestamp(time=str(dateTimeObj))
    #embed.set_thumbnail('tesco.png')
    #embed.set_image('https://cdn.shopify.com/s/files/1/0382/7695/6292/files/logo_360x.png?v=1587069640')
    #embed.set_footer(text='Time Stamp is here =>', ts=True,)
    embed.post()
