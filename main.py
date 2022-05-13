#Logic gates test in python 
#PLEASE RUN IN PYTHON v3.10.X AS CASE STATEMENTS DO NOT WORK PRIOR TO THIS
#(will break)

#defined the input variables for later use in functions
input1 = 0
input2 = 0

#ascii art
print("==================================================================")
print("   __          _                 __        __          __         ")
print("  / /__  ___ _(_)___  ___ ____ _/ /____   / /____ ___ / /____ ____")
print(" / / _ \/ _ `/ / __/ / _ `/ _ `/ __/ -_) / __/ -_|_-</ __/ -_) __/")
print("/_/\___/\_, /_/\__/  \_, /\_,_/\__/\__/  \__/\__/___/\__/\__/_/   ")
print("       /___/        /___/                                         ")
print("==================================================================\n")

#function for gate selection and logic
def gates(gatetype):
  print("selected gatetype:")

  #defines the beginning of the case statement
  match gatetype:

    #case - we're working with case statements, and the parameter is taken and
    #what happens next is defined next
    case 1:
      #AND
      print("AND\n=>",input1 and input2)
    
    case 2:
      #NAND
      print("NAND\n=>",not(input1 and input2))
   
    case 3:
      #OR
      print("OR\n=>",input1 or input2)
    
    case 4:
      #XOR
      print("XOR")
      if input1 == input2:
        print("=>",not input1)
      else:
        print("=>",input1 or input2)
    
    case 5:
      #NOR
      print("NOR\n=>",not(input1 or input2))
  
    case 6:
      #NOT
      print("NOT\ninput 1 =>",not input1,"\ninput 2 =>",not input2)

    #default case statement
    case _:
      print("something went wrong here... oops. try a number from 1 to 6.")

#the "main" function
def rolling():
  
  #i is used for the while function to loop unless broken by the user
  i = 1  
  while i == 1:
    print("select your gate type:\n1) AND\n2) NAND\n3) OR\n4) XOR\n5) NOR\n6) NOT")
    gatetype = int(input("=> "))
    print("\n==================================================================\n")
    print("select numbers for the desired gate\n(NOT can have two inputs and operate with each individually)")
    checkvar = 0
    while checkvar == 0:
      global input1
      global input2
      input1 = int(input("Input 1: (1/0)\n=> "))
      input2 = int(input("input 2: (1/0)\n=> "))
      if input1 > 1:
        print("Your input:",input1,"was incorrect")
      else:
        if input2 > 1:
          print("Your input:",input2,"was incorrect")
        else:
              checkvar = 1
    else:
      print("Your inputs are:",input1,"and",input2)

    gates(gatetype)
    cont = input("\n==================================================================\n\nUse the tester again?\n=> ")

    #"intelligent" input where things that could be interpreted as yes or no including
    #nerds who write 1/0 or true or false
    match cont:
      case "yes":
        print("continuing.\n")
                
      case "y":
        print("continuing.\n")

      case "1":
        print("nerd. continuing.\n")
      
      case "true":
        print("nerd. continuing.\n")
      
      case "no":
        i = 0
        print("ok! thanks for using this!")

      case "n":
        i = 0
        print("ok! thanks for using this!")
            
      case "0":
        i = 0
        print("ok! thanks for using this (supernerdy)")
    
      case "false":
        i = 0
        print("ok! thanks for using this (supernerdy)")

      case _:
        i = 0
        print("not sure what you did there but I'm going to end it here ¯\_(ツ)_/¯")
    
  else:
    print("\n==================================================================")
        
rolling()
