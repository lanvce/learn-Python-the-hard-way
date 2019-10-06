from sys import exit
#突然想到这几天看的斗罗大陆动漫 唐三被独孤博抓走 今天遇到此题 突然想起 才有此程序


def Conversation():
    print("when you wake up,you find you're in a cave!")
    print("Then you see a man in front of you ,he says 'Are you tangsan?' ")
    print("Yes!")
    print("You beat my grandaught and release her poision,I'll kill you today")
    print("what do you do?")
    print("ps: one:escape two:taunt him ")
    words=input(">")
    if words=="one":
        print("Oh,fuck!you can't run away from my hand!")
        dead("You're so weak!go dead now!")
    elif words=="two：
        print("You have a lot courage!Congratulation!")
    #    live()
    else:
        dead("you'll die finally!")

def live():
    print("So you know how to cure her,so I can't send you to see god! ")
    print("If you can prove you're stronger than me in poision,you can live")
    print("Therefore ,accept my challenge")

def dead(why):
    print(why,"Let's meeting next life")
Conversation()
