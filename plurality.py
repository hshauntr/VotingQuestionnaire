import csv
def pluralityvoting():
    with open('Superheroes.csv', mode = 'r') as file:
        reader = csv.reader(file)
        #store the reader as a list
        data = list(reader)
        
        #plurality function to total votes of 1
        def plurvoting(i):
            name = []
            for lines in data:
                
                #if integer then add to a list based on which hero column
                if lines[i].isdigit():

                    #add all vote numbers to name list
                    name.append(int(lines[i]))

                    #adding votes of 1 based on how many 1's are counted in the list
                    result = name.count(1)

            #return counted votes of 1        
            return(result)

        #find the highest value of votes
        votewinner= max(plurvoting(1),plurvoting(2),plurvoting(3),plurvoting(4),
                        plurvoting(5),plurvoting(6),plurvoting(7),plurvoting(8),plurvoting(9),
                        plurvoting(10),plurvoting(11),plurvoting(12))

        #Define a dictionary with the total votes of 1 to the hero's name                                     
        plurwinner = {
            plurvoting(1): 'BATMAN',
            plurvoting(2): 'SUPERMAN',
            plurvoting(3): 'CAPTAIN AMERICA',
            plurvoting(4): 'WONDER WOMAN',
            plurvoting(5):'CAPTAIN MARVEL',
            plurvoting(6):'CAT WOMAN',
            plurvoting(7):'STORM',
            plurvoting(8):'GREEN LANTERN',
            plurvoting(9):'BLACK PANTHER',
            plurvoting(10):'HAWK GIRL',
            plurvoting(11):'SHE HULK',
            plurvoting(12):'IRON MAN'}

        #print results
        print('The plurality winner is', plurwinner[votewinner],'with a score of', votewinner)
