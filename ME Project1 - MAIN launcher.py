#ME PROJECT 1 By: Shaun Tran

#importing each voting method external files
import csv
from plurality import pluralityvoting
from borda import bordavoting
from condorcet import condorcetvoting
from approval import approvalvoting

#ask for user input 
method = input('Please enter your voting method.\nEnter 1 for Plurality\nEnter 2 for Borda\nEnter 3 for Condorcet\nEnter 4 for Approval\n')

with open('Superheroes.csv', mode = 'r') as file:
    
    #read the csv file
    reader = csv.reader(file)
    
    #If Plurality Voting Method Chosen
    if method == '1':
        
        pluralityvoting()

    #If Borda Voting Method Chosen
    if method == '2':
        
        bordavoting()

    #If Condorcet Voting Method Chosen
    if method == '3':
        
        condorcetvoting()
            
    #If Approval Voting Method Chosen
    if method == '4':

        approvalvoting()
            
