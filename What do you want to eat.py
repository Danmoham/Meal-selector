#create a variable asking where they want to eat
# if they specify a certain quizzine load a particular website which has this
import webbrowser
import random

def takeawayoption(type):
    x = True
    while x == True:
        type = input("your options for a takeaway are: pizza \n,chinese \n, Indian \n Chippy")
        type1 = type.lower()
        if type1 in ("pizza"):
            webbrowser.open("https://romerowilpshire.co.uk/")
        elif type1 in ("chinese"):
            webbrowser.open("https://sunnys-chinese-chippy.business.site/")
        elif type1 in ("indian"):
            webbrowser.open("https://roeleeindian.com/")
        elif type1 in ("chippy"):
            webbrowser.open("https://thefriarywhalley.com/order-now")
        else:
            print("Sorry, I do not recognise this.")
            continue

def mealoption(type):
    x = True
    while x == True:
        type = input("Your options for a meal are: \nChinese,\nJapanese,\nEnglish,\nIndian,\nBoujee\n,Italian, \nGreek \n")
        type1 = type.lower()
        if type1 in ("chinese"):
            chinese = input("Do you want this to be expensive or cheap?")
            chinese1 = chinese.lower()
            if chinese1 in ("expensive", "spenny"):
                webbrowser.open('https://www.yucopstergreen.co.uk/')
                x = False
            elif chinese1 in ("cheap"):
                webbrowser.open('https://www.kongsanclitheroe.com/')
                x = False
            else:
                print ("Sorry i do not recognise this")
                continue
        elif type1 in ("greek"):
            webbrowser.open("https://brizolabarandgrill.co.uk/")
            x = False
        elif type1 in ("japanese"):
            japanese = input ("Do you want this to be cheap or expensive?")
            japanese1= japanese.lower()
            if japanese1 in ("cheap"):
                webbrowser.open("https://yosushi.com/")
                x = False
            elif japanese1 in ("expensive", "spenny"):
                webbrowser.open("https://tattu.co.uk/locations/manchester/menus/")
                x = False
            else:
                print ("Sorry i do not recognise this")
                continue
        elif type1 in ("english"):
            webbrowser.open("https://theblackbulloldlangho.co.uk/menu/")
            x = False
        elif type1 in ("indian"):
            indian = input("Do you want cheap or expensive?")
            indian1 = indian.lower()
            if indian1 in ("cheap"):
                webbrowser.open("https://www.tripadvisor.co.uk/Restaurant_Review-g503948-d11512415-Reviews-The_Royal_Taj-Langho_Lancashire_England.html")
                x = False
            elif indian1 in ("expensive", "spenny"):
                webbrowser.open("http://shajan.pwdbuildarea2.co.uk/")
                x = False
            else:
                print("sorry I do not recognise this.")
                continue
        elif type1 in ("italian"):
            italian = input("Do you want cheap or expensive?")
            italian1 = italian.lower()
            if italian1 in ("cheap"):
                webbrowser.open("https://www.amicomio.co.uk/")
                x = False
            elif italian1 in ("expensive", "spenny"):
                webbrowser.open("https://www.tiggis-ribblevalley.co.uk/about-us/")
                x = False
            else:
                print("sorry I do not recognise this.")
                continue
        elif type1 in ("boujee", "bouje"):
            boujee = input("Lunch or tea?")
            boujee1 = boujee.lower()
            if boujee1 in ("lunch"):
                webbrowser.open("https://www.deuxamiswhalley.com/")
                x = False
            elif boujee1 in ("tea"):
                webbrowser.open("https://www.tapas47.co.uk/")
                x = False
                    
        else:
            print ("sorry, i do not recognise this")
            continue

def meal(type):
    #list of all restaurants
    restaurants = ['https://www.yucopstergreen.co.uk/', 'https://www.kongsanclitheroe.com/',"https://brizolabarandgrill.co.uk/","https://brizolabarandgrill.co.uk/",
               "https://tattu.co.uk/locations/manchester/menus/","https://theblackbulloldlangho.co.uk/menu/" ,"http://shajan.pwdbuildarea2.co.uk/",
               "https://www.tiggis-ribblevalley.co.uk/about-us/"]
    random_restaurant = random.choice(restaurants)
    type = input ("Do you want to choose a random meal or pick your meal? Press any key if you want to pick your restaurant, otherwise type random")
    type1 = type.lower()
    if type in ("random meal", "randommeal", "random"):
        webbrowser.open(random_restaurant)
    else:
        mealoption(user)

def takeaway(type):
    takeaway = ["https://romerowilpshire.co.uk/", "https://sunnys-chinese-chippy.business.site/", "https://roeleeindian.com/",]
    random_takeaway = random.choice(takeaway)
    type = input("Do you want to choose a random takeaway or pick your own takeaway? Press any key for your own takeaway if you want random, please type random")
    type1 = type.lower()
    if type1 in ("random takeaway", "randomtakeaway", "random"):
        webbrowser.open(random_takeaway)
    else:
        takeawayoption(user)

def fastfoodopt (type):
    x = True
    while x == True:
        type = input("Do you want a Burger, chicken, or sandwhiches or a pasty")
        type1 = type.lower()
        if type1 in ("burger"):
            burger = input ("Do you want cheap or expensive?")
            burger1 = burger.lower()
            if burger1 in ("cheap"):
                webbrowser.open("https://www.mcdonalds.com/gb/en-gb.html")
                x = False
            elif burger1 in ("spenny", "expensive"):
                webbrowser.open("https://fiveguys.co.uk/")
                x = False
            else:
                print("Sorry, I do not recognise this")
                continue
            
        elif type1 in ("chicken"):
            chicken = input ("Do you want cheap or expensive?")
            chicken1 = chicken.lower()
            if chicken1 in ("cheap"):
                webbrowser.open("https://www.kfc.co.uk/")
                x = False
            elif chicken1 in ("expensive", "spenny"):
                webbrowser.open("https://www.nandos.co.uk/")
                x = False
            else:
                print ("Sorry, I do not recognise this")
        elif type1 in("sandwhiches", "sandwhiches"):
            sandwhiches = type1.lower()
            if sandwhiches in ("sandwhich", "sandwhiches", "butty"):
                webbrowser.open("https://www.order-subway.co.uk/")
                x = False
            else:
                 print("Sorry I do not recognise this")
                 continue
        elif type1 in ("pasty"):
            webbrowser.open("https://www.greggs.co.uk/")
            x = False
        else:
            print("Sorry i do not recognise, please re-type what you need")
            continue
            
                
            
        
                


def fastfood (type):
    fastfood = ["https://fiveguys.co.uk/", "https://www.mcdonalds.com/gb/en-gb.html","https://www.kfc.co.uk/", "https://www.nandos.co.uk/","https://www.greggs.co.uk/", "https://www.order-subway.co.uk/" ]
    random_fast = random.choice(fastfood)
    type = input("Do you want to choose a fastfood place or do you want a random fast food place? if you want random, please type random, otherwise press any other key")
    type1 = type.lower()
    if type1 in ("random", "random fastfood", "randomfastfood"):
        webbrowser.open(random_fast)
    else:
        fastfoodopt(user)

    
T = True

while T == True:
    user = input("Please select the type of food you want to eat today, do you want a takeaway, fast food or to go for a meal?".lower())
    user1 = user.lower()
    if user1 in ("meal", "mea"): 
        meal(user1)
        newmeal = input ("Are you happy with your selection? If not please type no and i will reload the program for you")
        newmeal1 = newmeal.lower()
        if newmeal in ("no", "n"):
            continue
        else:
            T = False
            print ("Enjoy!")
            
    elif user1 in ("takeaway", "take away"):
        takeaway(user1)
        newtakeaway = input ("Are you happy with your selection? If not please type no and i will reload the program for you")
        newtakeaway1 = newtakeaway.lower()
        if newtakeaway1 in ("no", "n"):
            continue
        else:
            T = False
            print ("Enjoy!")
            
    elif user1 in ("fastfood","fast food"):
        fastfood(user1)
        newfastfood = input ("Are you happy with your selection? If not please type no and i will reload the program for you")
        newfastfood1 = newfastfood.lower()
        if newfastfood1 in ("no", "n"):
            continue
        else:
            T = False
            print ("Enjoy!")
            
    else:
        print ("Sorry i do not recognise this")
        continue 


