from persistence import *

import sys

def main(args : list):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            product = repo.products.find(id=splittedline[0])
            

            if((int(splittedline[1])) > 0) :  # we need to add quantity>0
                # we update the quantity and creat an activity.
                repo.products.update({'quantity':int(product[0].quantity) + int(splittedline[1])}, {'id':splittedline[0]})
                activity = Activitie(splittedline[0], splittedline[1], splittedline[2], splittedline[3])
                repo.activities.insert(activity)
                product = repo.products.find(id=splittedline[0])

                # quantity<0 and product.quantity >= quantity.
            elif((int(splittedline[1])) < 0 and int(product[0].quantity) >= -1 * int(splittedline[1])):
                # we update the quantity and creat an activity.
                repo.products.update({'quantity':int(product[0].quantity) + int(splittedline[1])}, {'id':splittedline[0]})
                activity = Activitie(splittedline[0], splittedline[1], splittedline[2], splittedline[3])
                repo.activities.insert(activity)
                
if __name__ == '__main__':
    main(sys.argv)