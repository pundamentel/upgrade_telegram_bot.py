import os
import random
import telebot
bot = telebot.TeleBot('7538906280:AAFPwuPUs-xfOND3WOS_hqy-IwsoWXejyuA')
facts = ['Honey Never Spoils: Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.',
         'Octopuses Have Three Hearts: Two pump blood to the gills, while the third pumps it to the rest of the body.',
         'Bananas Are Berries: Botanically speaking, bananas qualify as berries, while strawberries do not!',
         'Wombat Poop is Cube-Shaped: Wombats produce cube-shaped droppings to mark their territory, preventing them from rolling away.',
         'The Eiffel Tower Can Be 15 cm Taller: During hot days, thermal expansion can make the iron in the Eiffel Tower expand, increasing its height.',
         'A Day on Venus is Longer than a Year: Venus takes about 243 Earth days to rotate on its axis but only about 225 Earth days to orbit the Sun.',
         'The Shortest War in History Lasted 38 Minutes: The Anglo-Zanzibar War in 1896 was fought between the British Empire and the Sultanate of Zanzibar, ending quickly in favor of the British.',
         'Cows Have Best Friends: Research has shown that cows form strong bonds with other cows and can become stressed when separated from their friends.',
         'Sharks Are Older than Trees: Sharks have existed for around 400 million years, while trees appeared about 350 million years ago.',
         'Humans Share 60% of Their DNA with Bananas: While we are very different from bananas, a significant portion of our genetic material is shared.'

]


#@bot.message_handler(commands=['meme'])
#def send_mem(message):
#    with open('dog.jpeg', 'rb') as f:  
#        bot.send_photo(message.chat.id, f) 
 
@bot.message_handler(commands=['mem'])
def send_mem(message):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        bot.send_photo(message.chat.id, f)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id,  'use the command /mem to recieve a random meme and /fact for a random fact. ')

@bot.message_handler(commands=['fact'])
def fact_giver(message):
    fact = random.choice(facts) 
    bot.send_message(message.chat.id, fact)

@bot.message_handler(commands=['coinflip'])
def coinflip(message):
    flip = random.randint(0, 2)
    if flip == 0:
        bot.send_message(message.chat.id, 'tails')
    else:   
    
        bot.send_message(message.chat.id, 'heads')

@bot.message_handler(commands=['roll'])
def roll_dice(message):
    roll = random.randint(1,6)
    bot.send_message(message.chat.id, roll)

@bot.message_handler(commands=['dog'])
def dog(message):
    bot.send_audio(message.chat.id, audio=open('dog.wav', 'rb'))




bot.polling()
