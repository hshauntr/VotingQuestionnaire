import csv

def bordavoting():
    with open('Superheroes.csv', mode = 'r') as file:
        reader = csv.reader(file)
        
        #store reader as a list 
        data = list(reader)

        #function to define borda for each hero
        def bordavoting(i):
            herovotes = []
            for lines in data:

                #if int then true
                if lines[i].isdigit():

                    #add value to list in function
                    herovotes.append(int(lines[i]))

                    #loop for adding points
                    herototal = 0
                    for count in herovotes:
                        rank = 1
                        points = 12
                        for x in range(1,13):
                            if count == rank:
                                herototal += points
                            rank +=1
                            points -=1
                            
            #return total points
            return(herototal)

        #store values as a dictionary
        bordadict = {'BATMAN':bordavoting(1),'SUPERMAN':bordavoting(2),'CAPTAIN AMERICA':bordavoting(3),'WONDER WOMAN':bordavoting(4),'CAPTAIN MARVEL':bordavoting(5),
                   'CAT WOMAN':bordavoting(6),'STORM':bordavoting(7),'GREEN LANTERN':bordavoting(8),'BLACK PANTHER':bordavoting(9),'HAWK GIRL':bordavoting(10),
                     'SHE HULK':bordavoting(11),'IRON MAN':bordavoting(12)}

        #find max of values
        bordavalues = max(bordavoting(1), bordavoting(2), bordavoting(3),bordavoting(4),bordavoting(5),bordavoting(6),
                       bordavoting(7),bordavoting(8),bordavoting(9),bordavoting(10),bordavoting(11),bordavoting(12))

        #find owner of the most votes
        most = max(bordadict, key=bordadict.get)

        #print results        
        print('The Borda winner is',most,'with a total of',bordavalues,'victories')
