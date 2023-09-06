import os
import telebot
import requests
import json
import csv

# Get your environment variables
OMDB_APIKEY = '1b18cfd5'
TELE_BOT_TOKEN = '6292297866:AAF4IMdaiJZ0cCALRWUETBEc9keXxB0e95o'

bot = telebot.TeleBot(TELE_BOT_TOKEN)
movie_watchlist=[]
botRunning = False  # Initialize botRunning variable

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    
@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For example: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')

@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
    
    # Extract the movie name from the message
    movie_name = message.text.split(' ', 1)[1]
    
    # Make a request to the OMDB API to get movie information
    api_url = "http://www.omdbapi.com/"
    params = {"t": movie_name, "apikey": OMDB_APIKEY}
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        movie_data = response.json()
        # TODO: 1.3 Show the movie information in the chat window
        bot.reply_to(message, f"Movie Title: {movie_data.get('Title', 'N/A')}\nYear: {movie_data.get('Year', 'N/A')}\nDirector: {movie_data.get('Director', 'N/A')}\nGenre: {movie_data.get('Genre', 'N/A')}")
        
        # TODO: 2.1 Create a CSV file and dump the movie information in it
        with open('movie_data.csv', mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([movie_data.get('Title', 'N/A'), movie_data.get('Year', 'N/A'), movie_data.get('Director', 'N/A'), movie_data.get('Genre', 'N/A')])
        
    else:
        bot.reply_to(message, 'Error: Unable to fetch movie information from the API')

@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    
    # TODO: 2.2 Send downloadable CSV file to the Telegram chat
    with open('movie_data.csv', 'rb') as file:
        bot.send_document(message.chat.id, file)

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')

bot.infinity_polling()
