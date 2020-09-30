import json
import collections

def main():

    # Creates an empty list of contacts
    contactlist = collections.OrderedDict()
    loops = True

    # While loop used for options, it loops for user input until sequence is over
    while loops == True:

        # Prints option list for the user
        print ('Greetings user! Lets make an addressbook!', '\n', '\n', 'Would you like to: ', '\n', '1.) Add a New Contact', '\n', '2.) List All Contacts', '\n', '3.)  Search Contacts', '\n', '4) Delete A Contact', '\n', '5.) Quit Program')

        # Asks for users input from 1-5
        userInput = input("Select an option: ")

        # 1 : Add a new contact to list, also start of program if no file is made
        if userInput == "1":
            contactname = input("Enter name: ")

            contactlist[contactname] = {'name': contactname, 'phone': input("Enter phone number: "), 'email': input("Enter email: ").lower()}

            json.dump(contactlist, open('contacts.txt', 'w'))

            print ("Contact Added!")


        #  2 : list of contacts in addressbook
        elif userInput == "2":
            print ('\n', "Listing Contacts...")
            try:
                contactlist = json.load(open('contacts.txt','r'))
                name_keys = list(contactlist.keys())
            except:
                contacts = {}

            print ("%-30s %-30s %-30s" % ('NAME','PHONE','EMAIL'))
            #better formatting than using tab spaces and keeps items in a predetermined space apart from eachother

            for k in name_keys:
                print ("%-30s %-30s %-30s" % (contactlist[k]['name'],  contactlist[k]['phone'], contactlist[k]['email']))
                #same idea as fotmatting above for each of the dict values

        #  3 : search through contacts!
        elif userInput == "3":
            print ('\n', "Searching Contacts...")
            search = input("Please enter name (case sensitive): ")

            try:
                contactlist = json.load(open('contacts.txt','r'))
            except:
                contactlist = []

            try:
                print ("%-30s %-30s %-30s" % (contactlist[search]['name'], contactlist[search]['phone'], contactlist[search]['email']))
            except KeyError: #error reporting- whenever a dict() object is requested & key is not in the dict.
                print ("Not Found")


##########################################################################

        #  5 : Delete contact
        elif userInput == "4":
            print ("Deleting Contact...")
            contactname = input("Enter Contact Name: ")
            contacts = json.loads(open('contacts.txt').read())

            try:
                contacts.pop(contactname)
                json.dump(contacts, open('contacts.txt','w'))
            except KeyError: #error reporting- whenever a dict() object is requested & key is not in the dict.
                print ('\n', "Contact Not Found")



        # 6 : end program
        elif userInput == "5":
            print ('\n', "Ending Contact Book.")
            print('Have a nice day!')
            loop = False
        else:
            print ("Invalid Input! Try again.")


main()

