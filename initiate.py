from persistence import *

import sys
import os

def add_branche(splittedline : list):
    
    #create a DTO
    branch = Branche(splittedline[0], splittedline[1], splittedline[2])
    #send to DAO
    repo.branches.insert(branch)


def add_supplier(splittedline : list):
    #create a DTO
    supplier = Supplier(splittedline[0], splittedline[1], splittedline[2])
    #send to DAO
    repo.suppliers.insert(supplier)

def add_product(splittedline : list):
    #create a DTO
    product = Product(splittedline[0], splittedline[1], splittedline[2], splittedline[3])
    #send to DAO
    repo.products.insert(product)

def add_employee(splittedline : list):
    #create a DTO
    employee = Employee(splittedline[0], splittedline[1], splittedline[2], splittedline[3])
    #send to DAO
    repo.employees.insert(employee)   

adders = {  "B": add_branche,
            "S": add_supplier,
            "P": add_product,
            "E": add_employee}

def main(args : list):  #was list[str])
    inputfilename = args[1]
    # delete the database file if it exists
    repo._close()
    
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")
    repo.__init__()
    repo.create_tables()
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(",")
            adders.get(splittedline[0])(splittedline[1:]) 

if __name__ == '__main__':
    main(sys.argv) 