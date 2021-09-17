import json 
import logging

from Loggers import logger

class Inventory:
    """
    Description:
        This class holds the methods for Inventory Management
        Methods created are open, add, display and remove
    """
  
    def __init__(self):
        self.json_f=[]  

    def open(self):
        '''
        Description:
            This function opens the json file
        '''
        try:
            with open('inventory.json', 'r') as file:
        
                self.json_f = json.load(file)
                
            
        except FileNotFoundError:
            logger.warning("File Not Found")

    def add_inventory(self):
        '''
        Description:
            This function adds the inventory details to json file
        '''
        try:
            dict = {}
            inv_id = input("Enter the Inventory ID : ")
            name = input("Enter the inventory Name : ")
            price = input("Enter the Inventory Price : ")
            weight = input("Enter the Inventory weight : ")
            self.open()
            dict = {"id": inv_id, "Name": name, "Price": price, "Weight": weight}
            self.json_f.append(dict)
            with open('inventory.json', 'w+') as file: 
               json.dump(self.json_f,file ,indent=2)
               logger.info("Record Inserted Successfully")
               
        except ValueError:
            logger.warning("Invalid Input")
        finally:
            file.close()   

    def display_inventory(self):
        '''
        Description: 
            This function displays the inventory details
        '''
        
        print(self.json_f)

    def remove(self):
        '''
        Description:
            This function removes the inventory details from json file
        '''
        try:
            if len(self.json_f) >= 1:
                id = (input("Enter the unique Id"))
                for i in range(len(self.json_f)):
                    if((self.json_f[i]['id']) == id):
                        del self.json_f[i]
                        with open('inventory.json', 'w+') as file: 
                         json.dump(self.json_f,file ,indent=2)
                         logger.info("Record Inserted Successfully")
               
                        
        except Exception as e:
            logger.error(e)

if __name__ == "__main__":
    try:
        data = Inventory()
        dict = data.open()
        while True:
            choice = int(input("\n 1. Add Inventory \n 2. Display Inventory \n 3. Remove Inventory \n 4. Exit \n "))
            if(choice == 1):
                data.add_inventory()
            if(choice == 2):
                data.display_inventory()
            if(choice == 3):
                data.remove()
            if(choice == 4):
                exit()
    except ValueError:
        logger.warning("Invalid Input")
    except TypeError:
        logger.warning("Invalid")