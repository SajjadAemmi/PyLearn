from instabot import Bot


bot = Bot()

u = input('Please enter username: ')
p = input('Please enter password: ')

bot.login(username=u, password=p)
print("you have successfully logged in")
bot.upload_photo("apple.jpg", caption="this is an apple")
