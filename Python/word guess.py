import random
def fun(list,string):
    for cher in string:
        if cher not in list:
            string=string.replace(cher,"_")
    return(string)
##print(fun(["a","b","c","d"],"doggy"))
guess=[]
file=open("word_list.txt","r+")
words=[]
for var in file :
    words.append(var)
lives=5
anwser=(random.choice(words))
print(anwser)
user=(fun(guess,anwser))
while lives>0 and user != anwser:
    x=(input("leter nowwwwwwwww"))
    guess.append(x)
    user=(fun(guess,anwser))
    if x not in anwser:
        lives=lives-1
        print("wrong")
    if x not in anwser:
        print("you won")
    if lives==0:
        print("You lost")
        
    
    
