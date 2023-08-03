import csv
from itertools import combinations

def condorcetvoting():
    with open('Superheroes.csv', mode = 'r') as file:
        reader = csv.reader(file)
#skipping 1st line to avoid headers
        headers = next(reader)

        #storing the data as a list 
        data = list(reader)
    
        #function to assign each hero their total votes 
        def herovotes(i):
            votes = []
            for lines in data:
                
                #if int then true
                if lines[i].isdigit():
                    
                    #add value to list in function
                    votes.append(int(lines[i]))
                    
            return(sum(votes))

        #dictionary for assigning the name with how many votes they have
        condorcetnumbers = {'BATMAN':herovotes(1),
                            'SUPERMAN':herovotes(2),
                            'CAPTAIN AMERICA':herovotes(3),
                            'WONDER WOMAN':herovotes(4),
                            'CAPTAIN MARVEL':herovotes(5),
                            'CATWOMAN':herovotes(6),
                            'STORM':herovotes(7),
                            'GREEN LANTERN':herovotes(8),
                            'BLACK PANTHER':herovotes(9),
                            'HAWK GIRL':herovotes(10),
                            'SHE-HULK':herovotes(11),
                            'IRON MAN':herovotes(12),
                            }
        
        #use combinations to find each possible pair
        a = combinations(headers[1:],2)
        
        #defining their victories as 0
        batmanwins = 0
        supermanwins = 0
        captainamericawins = 0
        wonderwomanwins = 0
        captainmarvelwins = 0
        catwomanwins = 0
        stormwins = 0
        greenlanterwins = 0
        blackpantherwins = 0
        hawkgirlwins = 0
        shehulkwins = 0
        ironmanwins = 0

        #head to head battle, using the combinations function to find each unique pair
        for compare in list(a):
                
                #if left is winner, they get a point (lower points is a winner)
                if condorcetnumbers[compare[0]] < condorcetnumbers[compare[1]]:
                    if 'BATMAN' in compare[0]:
                        batmanwins += 1
                    if 'SUPERMAN' in compare[0]:
                        supermanwins += 1
                    if 'CAPTAIN AMERICA' in compare[0]:
                        captainamericawins += 1
                    if 'WONDER WOMAN' in compare[0]:
                        wonderwomanwins += 1
                    if 'CAPTAIN MARVEL' in compare[0]:
                        captainmarvelwins += 1
                    if 'CATWOMAN' in compare[0]:
                        catwomanwins += 1
                    if 'STORM' in compare[0]:
                        stormwins += 1
                    if 'GREEN LANTERN' in compare[0]:
                        greenlanterwins += 1
                    if 'BLACK PANTHER' in compare[0]:
                        blackpantherwins += 1
                    if 'HAWK GIRL' in compare[0]:
                        hawkgirlwins += 1
                    if 'SHE-HULK' in compare[0]:
                        shehulkwins += 1
                    if 'IRON MAN' in compare[0]:
                        ironmanwins += 1

                #if right is winner, they get a point (lower points is a winner)
                if condorcetnumbers[compare[0]] > condorcetnumbers[compare[1]]:
                    if 'BATMAN' in compare[1]:
                        batmanwins += 1
                    if 'SUPERMAN' in compare[1]:
                        supermanwins += 1
                    if 'CAPTAIN AMERICA' in compare[1]:
                        captainamericawins += 1
                    if 'WONDER WOMAN' in compare[1]:
                        wonderwomanwins += 1
                    if 'CAPTAIN MARVEL' in compare[1]:
                        captainmarvelwins += 1
                    if 'CATWOMAN' in compare[1]:
                        catwomanwins += 1
                    if 'STORM' in compare[1]:
                        stormwins += 1
                    if 'GREEN LANTERN' in compare[1]:
                        greenlanterwins += 1
                    if 'BLACK PANTHER' in compare[1]:
                        blackpantherwins += 1
                    if 'HAWK GIRL' in compare[1]:
                        hawkgirlwins += 1
                    if 'SHE-HULK' in compare[1]:
                        shehulkwins += 1
                    if 'IRON MAN' in compare[1]:
                        ironmanwins += 1
                        
        #finding the biggest number of total wins
        winner = max(batmanwins,supermanwins,captainamericawins,wonderwomanwins,captainmarvelwins,catwomanwins,stormwins,greenlanterwins,blackpantherwins,hawkgirlwins,shehulkwins,ironmanwins)

        #placing final values in a dictionary
        condorcetwinner = {batmanwins:'BATMAN',
                           supermanwins:'SUPERMAN',
                           captainamericawins:'CAPTAIN AMERICA',
                           wonderwomanwins:'WONDER WOMAN',
                           captainmarvelwins:'CAPTAIN MARVEL',
                           catwomanwins:'CAT WOMAN',
                           stormwins:'STORM',
                           greenlanterwins:'GREEN LANTERN',
                           blackpantherwins:'BLACK PANTHER',
                           hawkgirlwins:'HAWK GIRL',
                           shehulkwins:'SHE HULK',
                           ironmanwins:'IRON MAN'
            }

        #print results
        print('The Condorcet winner is', condorcetwinner[winner],'with a total of',winner,'victories')
