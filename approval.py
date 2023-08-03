import csv

def approvalvoting():
    with open('Superheroes.csv', mode = 'r') as file:
        reader = csv.reader(file)
        
        #defining each hero's name as a list
        batman = []
        superman = []
        captainamerica = []
        wonderwoman = []
        captainmarvel = []
        catwoman = []
        storm = []
        green = []
        blackpanther = []
        hawkgirl = []
        shehulk = []
        ironman = []

        #skip headers
        next(file)

        #place reader into a list
        data = list(reader)

        #for loop for each ballot
        for i in range(0,len(data)):

            #remove the id from the ballot list 
            removeid = data[i][1:]

            #making all the values in the list integer values
            formatdata = list(map(lambda x: int(x) if x else 0, removeid))
            removezero = list(map(lambda x: int(x) if x else 0, removeid)) 
            
            #Remove zeroes to calculate average using len()
            for value in list(removezero):
                if value == int(0):
                    removezero.remove(value)
                
            #If list is empty, average = 1, because program can't divide by zero
            if len(removezero) == 0:
                average = 1
                
            #If list is not empty, divide sum of values by how many votes are counted
            else: 
                average = sum(formatdata)/len(removezero)

            #determine that each hero vote is less than the average, not equal to the average, and isn't the value zero
            #if condition is passed, then add a value of 1 to their name's list
            if formatdata[0] < average and formatdata[0] != average and formatdata[0] != 0:
                batman.append(1) 
            
            if formatdata[1] < average and formatdata[1] != average and formatdata[1] != 0:
                superman.append(1)

            if formatdata[2] < average and formatdata[2] != average and formatdata[2] != 0:
                captainamerica.append(1)

            if formatdata[3] < average and formatdata[3] != average and formatdata[3] != 0:
                wonderwoman.append(1)

            if formatdata[4] < average and formatdata[4] != average and formatdata[4] != 0:
                captainmarvel.append(1)
                
            if formatdata[5] < average and formatdata[5] != average and formatdata[5] != 0:
                catwoman.append(1)
                
            if formatdata[6] < average and formatdata[6] != average and formatdata[6] != 0:
                storm.append(1)
                
            if formatdata[7] < average and formatdata[7] != average and formatdata[7] != 0:
                green.append(1)
                
            if formatdata[8] < average and formatdata[8] != average and formatdata[8] != 0:
                blackpanther.append(1)
                
            if formatdata[9] < average and formatdata[9] != average and formatdata[9] != 0:
                hawkgirl.append(1)
                
            if formatdata[10] < average and formatdata[10] != average and formatdata[10] != 0:
                shehulk.append(1)

            if formatdata[11] < average and formatdata[11] != average and formatdata[11] != 0:
                ironman.append(1)

        #find the highest value of approval wins
        winner = max(sum(batman),sum(superman),sum(captainamerica),sum(wonderwoman),sum(captainmarvel),sum(catwoman),sum(storm),sum(green),sum(blackpanther),sum(hawkgirl),sum(shehulk),sum(ironman))

        #placing final values in a dictionary
        approvalwinner = {sum(batman):'BATMAN',
                          sum(superman):'SUPERMAN',
                          sum(captainamerica):'CAPTAIN AMERICA',
                          sum(wonderwoman):'WONDER WOMAN',
                          sum(captainmarvel):'CAPTAIN MARVEL',
                          sum(catwoman):'CAT WOMAN',
                          sum(storm):'STORM',
                          sum(green):'GREEN LANTERN',
                          sum(blackpanther):'BLACK PANTHER',
                          sum(hawkgirl):'HAWK GIRL',
                          sum(shehulk):'SHE HULK',
                          sum(ironman):'IRON MAN'}

        #print results
        print('The Approval Winner is', approvalwinner[winner], 'with a score of',winner)
