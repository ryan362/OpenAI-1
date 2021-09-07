import os
import openai
#import time
from discord.ext import commands
bot = commands.Bot(command_prefix=">")

openai.organization = "org-OGfdwElgq9qaRldixSiBWMoJ"
openai.api_key = os.getenv("API_Key")

@bot.command()
async def summarize(ctx, args):
	text = str(args)
	print(args)
	#Count Words - if above quota then return and send error message also if above 100 return and send error
	#Check Content - use the OpenAI content filter and filter out content returned with a 2 that the AI is confident about. Also maybe add some of your own
	
	'''
	response = openai.Completion.create(
		engine="curie",
		prompt=text + "\n\ntl;dr:",
		temperature=0.3,
		max_tokens=100,
		frequency_penalty=0,
		presence_penalty=0,
		stop=["\n"],
		user=ctx.author.id
	)
	print(response.choices[0].text)
	'''

def checkContent(cont):
	response = openai.Completion.create(
		engine="content-filter-alpha-c4",
		prompt="<|endoftext|>" + cont + "\n--\nLabel:",
		temperature=0,
		max_tokens=1,
		top_p=0,
		frequency_penalty=0,
		presence_penalty=0,
		logprobs=10
	)

	return response

bot.run(os.getenv("token"))