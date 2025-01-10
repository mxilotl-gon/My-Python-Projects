#Michelle Xilotl
#Pd-3
#What Bikini Bottom Character R U?

print("Welcome to What is Your Bikini Bottom Character Quiz?") #intro prints
print("Answer the questions to find out which character you are!")
ans=input("Indoors(i) or Outdoors(o)? ")

if ans=="i": #starts a sequence of choices for choosing indoors
    ans=input("Spicy(y) or Sour(u)? ")
    if ans=="y":
        ans=input("Watching tv(w) or Coding(c)? ")
        if ans=="w":
            print("You are Gary the Snail!")
        else:
            print("You are Karen!")
    else:
        ans=input("Building(b) or Hearing Music(m)? ")
        if ans=="b":
            print("You are Sandy Cheeks!")
        else:
            print("You are Squidward Tentacles!")

if ans=="o": #starts a sequence of prompts after choosing outdoors
    ans=input("Sweet(e) or Salty(t)? ")
    if ans=="e":
        ans=input("Shopping(g) or Teaching(a)? ")
        if ans=="g":
            print("You are Pearl!")
        else:
            print("You are Mrs. Puff!")
    else:
        ans=input("Learning(l) or Eating(n)? ")
        if ans=="l":
            print("You are Spongebob Squarepants!")
        else:
            print("You are Patrick Star!")

