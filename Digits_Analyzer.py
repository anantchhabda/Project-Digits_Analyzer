#===========================================================================================================================
#This program is written to analyse the distribution of digits for numbers in a file.
#Creation Date: 20/05/2020
#Author: Anant Chhabda
#S/N: 21712878
#===========================================================================================================================


#This function will take a file, try to open it and validate it for the main function
def checkfileinput(filename):
    
    if type(filename) == int or type(filename) == float:
        return ("Please enter a valid input for file."), []
      
    try:
        datafile = open(filename, "r")
        
    except FileNotFoundError:
        return "Sorry, the program was unable to find the file.", []
        
    except OSError:
        return "Please check your input.", []
        
    except:
        return "Sorry, program was unable to open the file.", []
    
    return "", datafile #returns empty string(means valid input) and the opened file 


#This function will take no_places and validate it for the main function
def checkplacesinput(no_places):
    
    try:
        no_places/1  #check its not a string  
    except TypeError:
        return "Please enter a positive integer for no_places, do not enter a string."
    
    
    #reject negative values, allow floats like 2.0,4.0 etc.
    if no_places <=0 or (no_places%2 !=0 and no_places%2 != 1): 
        return "Please enter a positive integer for no_places."
   
   
    return "" #Empty string means its a valid input


#This function will take regularise and validate it for the main function
def checkregulariseinput(regularise):
         
    if regularise != 0 and regularise != 1:
        return "Please enter either True or False or correspondingly 1 or 0."
    else:
        return "" #Empty string - valid input


#This function will take a string input and check if it solely numerical
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False #return False if not numerical
    
    
#This function will take an opened file as input and extracts its numerical data    
def extract(datafile):
    
    fulldata = []
    
    for line in datafile:
        
        line = line.strip("\n")
        linelist = line.split(",")
        
        for value in linelist:
            if isfloat(value):
                value = float(value)
                value = int(value)
                if value <0:
                    fulldata.append(str(value*-1)) #negative signs unnecessary so removed
                else:
                    fulldata.append(str(value))
                
    datafile.close()                      
    return fulldata #returns list of all valid numerical data 


#This function will take a list, a positive integer and a boolean value or binary digit(0/1) and do the digit analysis as required 
def analysis(fulldata, no_places,regularise):

    finallist = []
    
    #creating a dictionary for each digit place
    for i in range(int(no_places)):
        
        dic ={}
        
        for number in fulldata:
            
            if len(number)>=i+1: 
                dic[number[i]] = dic.get(number[i], 0) + 1
        
        #add non-occuring numbers value as 0
        for j in range(0,10): 
            
            if ((str(j) in dic) == False):
                dic[str(j)] = 0
                
        list1 = list(dic.items())
        list1.sort()
        
        #creating a sorted list of values
        list2 = []
        for i in range(10):
            list2.append(list1[i][1])
                
        list2.append(list2[0]) #shift value of 0 to the end
        del list2[0]
        
        #check regularise value 
        if regularise == False:
            finallist.append(list2)
                
        else:
            if sum(list2) == 0:
                finallist.append(list2) 
            else:
                #create list of distribution values as fraction of total sum
                list3 = []
                for i in range(len(list2)):
                    list3.append(round(list2[i]/sum(list2),4))
                finallist.append(list3)
            
    return finallist #returns a list of lists containing the analysis 


#This function will take a list, a positive integer and a boolean value or binary digit(0/1), puts it all together and returns the analysis
def main(filename, no_places, regularise = False): 
    
    File_Error, datafile = checkfileinput(filename)
    
    #for error state, prints corresponding message and returns empty list
    if File_Error != "":
        print(File_Error) 
        return [] 
    
    Places_Error = checkplacesinput(no_places)
    
    if Places_Error != "":
        print(Places_Error)
        return []
    
    Regularise_Error = checkregulariseinput(regularise)
    
    if Regularise_Error != "":
        print(Regularise_Error)
        return []
    
    #final check for any other possible error
    try:
        fulldata = extract(datafile)
        
        if fulldata == []:
            print("Sorry, no analysis conducted as they was no numerical data in the file.")
            return []
  
        finallist = analysis(fulldata, no_places,regularise)
        return finallist
                
    except:
        
        print("Please check the program, there is an error in it.")
        return []

main("book1.csv",1,1)