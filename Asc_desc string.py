# Problem : We have a string - A,B,D,E,E, F,G,H,IK,M, N, OO, PP, QQ, ZZ , X,Y,Z,9,4,3,1,5,6,7,8, 1.1.0.2

# Write logic to 
# 1. Sort in Ascending Order and Print
# 2. Sort in Descending Order and Print  
# 3. Extract Numbers only and Sort in Ascending Order and Print (Descending also)
# 4. Extract string only and Sort in Ascending Order and Print (Descending also)
# 5. Remove all duplicates and Sort ASC and Desc
# Remember these are 5 Separate Tasks and not 1. If you stuck in one start other But i need this let me know when you can complete same 

def main():
    List=["E","E","F","G","H","IK","M","N","OO","PP","QQ","ZZ","X","Y","Z","A","B","D","9","4","3","1","5","6","7","8","1.1","0.2"]
    
    #Sorting the list in ascending order
    List.sort()
    print(f"Ascending order of list : {List}")
    
    #Sorting the list in descending order
    List.sort(reverse=True)
    print(f"Desending order of list :{List}")

    #Extract only numbers  from list 
    List1=[i for i in List if i.isdigit()]
    print(f"Extracting only numbers from list : {List1}")
    

    #List1=[float(i) if '.' in i else int(i) for i in List if i.replace('.','',1).isdigit()]
    #Sorting ascending order only for numbers 
    List1.sort()
    print(f"Extract only numbers from List in Ascending order :{List1}")
    
    #Sorting descending order from list only  numbers
    List1.sort(reverse=True)
    print(f"Extrct only numbers from List in Descending order :{List1}")

     #Extract only Letters from List
    List=[i for i in List if i.isalpha()]

    #Sorting Ascending order from List only letters
    List.sort()
    print(f"Extract only Letters from List in Ascending order :{List}")

    #Sorting Descending order from List only letters 
    List.sort(reverse=True)
    print(f"Extract only Letters from List in Descending order :{List}")

    #Removing duplicates
    remove_duplicates=list(set(List))

    #Ascending order from list after removing duplicates
    remove_duplicates.sort()
    print(f"After removing duplicates List is printing in Ascending order :{remove_duplicates}")

    #Descending order from List after removing duplicates 
    remove_duplicates.sort(reverse=True)
    print(f"After removing duplicates List is printing in Descending order :{remove_duplicates}")

    


if __name__ =="__main__":
    main()