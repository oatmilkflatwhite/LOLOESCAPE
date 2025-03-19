import random
outside = True
prompt_reply = "Input: "
text_invalid = "Text invalid. Please try again."
tab = "     "
text_title = "***LOLO ESCAPE***"
text_border = "*****************"
text_intro = "Lolo the boa has escaped from her enclosure!\nCan you help her choose what to eat while she's outside?\n"
lolo_startmass = 32 
feconv = 3.2808 # metres * feconv = ft
kgpm = 17.5 #kg/m
fooddict = {
    "Massive pizza":1.814,
    "Apple":0.200,
    "Bag of Crisps":0.090,
    "Adult Human":65,
    "Infant":3,
    "Small child": 20,
    "fat frog":1.2,
    "Wendy's Baconator":0.424,
    "Big rat":0.75, 
    "Really big rat":1.5,
    "Jumbo rotisserie chicken":4.0,
    "Roadkill (Virginia Opposum)":2.8,
    "Roadkill (Black Vulture)":2,
    "Roadkill (Brown Hare)":3.9,
    "Roadkill (Wild Turkey)":10,
    "Roadkill (Nine-banded armadillo)":3.4,
    "Roadkill (Mysterious)": 2.5,
    "Invasive burmese python (Adult)": 12,
    "Invasive burmese python (Baby)":3.2,
    "Two-toed amphiuma":0.8,
    "Tsuchinoko":2,
    "Jackalope":1,
    "Bigfoot":90,
    "Bigfoot (infant)":4.5,
    "100% Iberico acorn-fed ham shoulder":5,
    "Comically tall cartoon sandwich":1.7,
    "Extra-large strawberry milkshake":2,
    "Thanksgiving turkey (serves 10)":5.89,
    "Peking duck with pancakes":4.1,
    "Whole suckling pig":9.07,
    "Large serving of chicken biriyani":2.5,
    
    }

foodchoice = {}

food = {}

def inputreply(): #x must be +ve integer (number of poss options)
    doneflag = False
    while doneflag == False:
        rawinput = input(prompt_reply)
        inputted = rawinput.strip()
        if inputted.isdigit():
            try:
                inty = int(inputted)
            except TypeError:
                print(text_invalid)
            except:
                print(text_invalid)
            if inty > 0 and inty != 0 and inty <= 5:
                doneflag = True
                return inty
            else:
                print(text_invalid)
        else:
            print(text_invalid)

def textnoeat(x):
    vowels = {"a", "e", "i", "o", "u","1"}
    if x[0].lower() in vowels:
        print("Lolo can't eat an " + x.upper() +", she's not big enough.")
    else:
        print("Lolo can't eat a " + x.upper() +", she's not big enough.")

    
def textyeseat(x):
    vowels = {"a", "e", "i", "o", "u"}
    if x[0].lower() in vowels:
        print(" * Lolo ate an " + x.upper() +".")
    elif x[0:7].lower() == "roadkil":
        print(" * Lolo ate some " + x.upper() +".")
    else:
        print(" * Lolo ate a " + x.upper() +".")

def r2(x):
    y = round(x,2)
    string = str(y)
    return y

def lololength(x): #x = kg
    length = x/kgpm
    lengthyank = length*feconv #im not converting down to inches cos id rather kms :)
    #print("Lolo is now " + str(length2dec) + "m long! (" + str(feet2dec) + "ft)")
    return [length,lengthyank]

def lololimit(x): #x = kg
    limit = x*0.12
    limitlb = limit * 2.20462
    limst = round(limit,1)
    limlb = round(limitlb)
    return limit

def lololimitwprint(x): #x = kg
    limit = x*0.12
    limitlb = limit * 2.20462
    limst = round(limit,1)
    limlb = round(limitlb)
    print("You would guess that Lolo could eat something around " + str(limst) + " kg (" + str(limlb) + " lb) big.")
    return limit

def loloeat(x):
    totalm=0
    limit_r = r2(limit)
    #print(" ** up to " + str(limit_r) + "kg can be eaten")
    for i, k in food.items():
        if k > limit:
            textnoeat(i)
            eaten = 0
            totalm = totalm + eaten
        else:
            textyeseat(i)
            eaten = k
            totalm = totalm + eaten
    totalm_r = r2(totalm)
    #print(" ** lolo ate " + str(totalm_r) +"kg of food.")
    food.clear()
    return totalm
            
def compare(x,y):
    stringm = r2(x[0])
    stringft = r2(x[1])
    if x[0] > y:
        print("Lolo is now " + str(stringm) + "m long (" + str(stringft) + "ft)!")
    else:
        print("She is the same size as before.")
    return x[0]

def multichoice():
    z = 1
    y = random.sample(list(fooddict.items()),5)
    foodchoice.update(y)
    print(" * Lolo has found the following:")
    for i,k in foodchoice.items():
        print (tab + str(z) + ". " + i.upper())
        z= z+1
    ans = inputreply()
    b = list(foodchoice.items())
    indy = ans - 1
    yummy =b[indy]
    food[yummy[0]] = yummy [1]
    foodchoice.clear()


print(text_border)
print(text_title)
print(text_border)
print(text_intro)
m = lolo_startmass
turns = 1
p = lololength(m)
length = r2(p[0])
orig_length =  length
length_yr = r2(p[1])
print("Lolo is " + str(length) + "m (" + str(length_yr) + "ft).")


while outside == True:
    limit = lololimit(m)
    multichoice()
    foodeaten = loloeat(food)
    m = m + foodeaten
    newl = lololength(m)
    length = compare(newl,length)
    limit = lololimitwprint(m)
    if turns == 15:
        print(text_border)
        print(" * Lolo had enough and slithered home...")
        print("Her owner was delighted to see her!")
        lengthdiff = length - orig_length
        massdiff = m - lolo_startmass
        masslb = massdiff * 2.20462
        lengthft = lengthdiff * feconv
        engst = r2(lengthdiff)
        engst2 = r2(massdiff)
        lbst = round(masslb,1)
        ftst = r2(lengthft)
        print(tab + "\"I'm so happy to see you, Lolo!\"")
        print(tab + "\"You've grown " + str(engst) + " metres (" + str(ftst) + " ft)!\"")
        print(tab + "Lolo ate " + str(engst2) + " kilogrammes (" + str(lbst) + " lb) of food!")
        input("Press any key to play again! ")
        print(text_border)

    else:
        turns = turns + 1
        print(text_border)
