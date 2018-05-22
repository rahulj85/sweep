import pandas as pd
import sklearn
import random

class Bunch:
    def __init__(self, mycards=None):
        if mycards==None:
            mycards=[0]*52
        self.mycards=mycards #spades, hearts, clubs, diamonds. Ace to King
        
    def remove(self, cards):
        if sum([a and b for a,b in zip(self.mycards, cards.mycards)])==1:
            self.mycards = [int(a != b) for a,b in zip(self.mycards, cards.mycards)]
        else:
            print("Error: Card not found "+str(cards.mycards.index(1)))
            
    def add(self, cards):
        if sum([a and b for a,b in zip(self.mycards, cards.mycards)])==1:
            print("Error: Card already exists "+str(cards.mycards.index(1)))
        else:
            self.mycards = [int(a != b) for a,b in zip(self.mycards, cards.mycards)]
    
    def pick_random(self):
        pos=random.choice([i for i, x in enumerate(self.mycards) if x==1])
        self.mycards[pos]=0
        picked=Card(pos=pos)
        return(picked)
    

class Card(Bunch):
    def __init__(self, pos=-1, mycards=None):
        if mycards==None:
            mycards=[0]*52
        if pos>=0 and pos<52:
            self.mycards=mycards
            self.mycards[pos]=1
            self.suit=int(pos/13)
            self.val=pos%13+1
        elif sum(card_arr)==1:
            self.mycards=mycards
            pos=mycards.index(1)
            self.suit=int(pos/13)
            self.val=pos%13+1
        else:
            print("Error")
            exit(1) #self.mycards=mycards #spades, hearts, clubs, diamonds. Ace to King

class Stack(Bunch):
    def __init__(self, card):
        self.val=card.val
        #self.points=
        self.mycards=card.mycards
        self.pukka=False
    
    def modify(self, card):
        newval=self.val+card.val
        if self.pukka or newval>13 or newval<9:
            print("Error")
            exit(1)
        else:
            self.val=newval
            self.add(card)
    
    def combine(self, card, stack1=None):
        if stack1 is None and card.val==self.val:
            self.add(card)
            self.pukka=True
        elif stack1 is not None:
            if stack1.pukka==False and card.val+stack1.val==self.val:
                self.add(card)
                self.add(stack1)
                self.pukka=True
            else:
                print("Error")
                exit(1)
        else:
            print("Error")
            exit(1)
        
    def pick(self, card, pl):
        if card.val==self.val:
            pass
        pass
    
class Player:
    def __init__(self, num, turn):
        self.turn=turn
        self.num=num
        self.hand=Bunch()
        self.pocket=Bunch()
        
    def play(self, card, middle, action=-1, addon=None, target=None): #-1=throw; 0=combine; 1=pick
        if action==-1:
            middle.throw(card)
        elif action==0:
            middle.combine(card, addon, target)
        elif action==1:
            middle.pick(card)
        else:
            print("Error")
            exit(1)

class Middle():
    def __init__(self, card_arr=None):
        self.stacks=[]
        if card_arr is not None:
            for k in card_arr:
                self.stacks.append(Stack(k))
    
    def throw(self, card):
        self.stacks.append(Stack(k))
    
    def combine(self, card, addon=None, target=None):
        if target is None:
            if card.val==addon.val:
                pass
            else:
                #self.stacks.append({card.val+})
                pass    
    def pick(self, card, pl):
        for k in self.stacks:
            if card.val in k:
                pass

class Game:
    def __init__(self, num_pl=2):
        #create deck
        self.create_deck() 
        deck=Bunch([1]*52)
        
        #all players
        pl=[]
        for i in range(num_pl):
            pl.append(Player(i,i))
        
        #game board
        middle=[]
        for i in range(4):
            middle.append(Stack(deck.pick_random()))
        
        for i in range(12):
            temp=stack.pick_random()
        if i<4:
            p1_start.append(temp)
        p1.hand.add(temp)
        p2.hand.add(stack.pick_random())
        
    def create_deck(self):
        self.suit={}
        self.val={}
        for i in range(52):
            self.suit[i]=int(i/13) #0-spades,1-hearts,2-clubs,3-diamonds
            self.val[i]=i%13+1 #1,2,...,13
            
    
#def main():
p1=Player(1)
p2=Player(2)

b=Board()
p1_start=[]
