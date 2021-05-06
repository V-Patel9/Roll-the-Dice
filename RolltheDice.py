import random #imported random package to generate random number
def main(): #main function
   print("enter no.of sides(4-20)")
   sides=int(input()) #taking no.of sides
   while((sides!=4) and (sides!=6) and (sides!=12) and (sides!=20)): #checking whether the side is 4   or 6 or 12 or 20
   	print("enter valid no.of sides 4,6,12,20")
   	sides=int(input())
   print("\nThanks! Here we go....\n")
   rolled=0 #taking required variables
   l_1=[]
   l_2=[]
   doubles=0
   play(rolled,doubles,l_1,l_2,sides) #calling play function to roll die
  def play(rolled,doubles,l_1,l_2,sides):
   dice_1=random.randint(1,sides) #generating random number
   dice_2=random.randint(1,sides)
   l_1.append(dice_1) #storing number into list to calculate average die roll
   l_2.append(dice_2)
   print("dice number 1 is ",dice_1," dice number 2 ",dice_2)
   if(dice_1==1 and dice_2==1): #condition for snake eyes.
   	doubles=doubles+1
   	rolled=rolled+1
   	print("You got Snake eyes! Finally! on try ",rolled)
   	print("Along the way you rolled doubles ",doubles," times (",round((doubles/rolled)*100,2),"% of all roll were doubles)") #calculating doubles percentage
   	print("The Average roll for die 1 was",round(sum(l_1)/len(l_1),2))
   	print("The Average roll for die 2 was",round(sum(l_2)/len(l_2),2))
   elif(dice_1==dice_2): #condition for doubles
   	doubles=doubles+1
   	rolled=rolled+1
   	play(rolled,doubles,l_1,l_2,sides)
   else: #condition if it is not snake eyes.
   	rolled=rolled+1
   	play(rolled,doubles,l_1,l_2,sides)
main()
