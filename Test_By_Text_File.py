
import sys,os

def menu():
    print("1."," Take Test")
    print("2.", "Add Test Question")
    print("3.", "Remove Test Question")
    print("4."," Exit Program")
    
    
    menuChoices=input("Please Choose an option to begin with: ")
    value=int(menuChoices)
    done=False
    while not done:
        if value==1:
            takeTest()
            break
        elif value==2:
            addQuestion()
            break
        elif value==3:
            removeQuestion()
            break
        elif value==4:
            break
        else:
            print("Please enter a value between 1-5")
    
choiceList=["a","b","c","d"]        
def addQuestion():
    fileAdder=open("testQuestions.txt","a")
    question_taker=input("What is the question? ")
    choice1=input("What is the first choice? ")
    choice2=input("What is the second choice? ")
    choice3=input("What is the third choice? ")
    choice4=input("What is the fourth choice? ")
    answer=input("What is the answer to the question?(from a to d) ")
    points=input("How many points is your question? ")
    choice1=choice1.lower()
    choice2=choice2.lower()
    choice3=choice3.lower()
    choice4=choice4.lower()
    answer=answer.lower()
    fileAdder.write(question_taker+";"+choice1+";"+choice2+";"+choice3+";"+choice4+";"+answer+";"+points)
    fileAdder.close()
    
    
def removeQuestion():

    inputFile=open("testQuestions.txt","r")
    lines=inputFile.readlines()
    inputFile.close()
    lineRemover=int(input("Please chose the question(s) you want to remove: "))
    lineRemover-=1
    outputFile=open("testQuestions.txt","w")
    i=0
    if lineRemover<=len(lines) and lineRemover>=0:
        for i in range(len(lines)):
            if i==lineRemover:
                pass
            else:
                outputFile.write(lines[i])
    else:print("Please enter a value in between the question numbers")
        
                    
def takeTest():
    try: 
        inputFile=open("testQuestions.txt","r")
        line_numbers=inputFile.readline()
        totalPointPossible=0
        correctNumber=0
        counter=0
        while line_numbers !=' ':
            line=line_numbers.split(";")
            question=line[0]
            counter=counter+1
            firstChoice=line[1]
            secondChoice=line[2]
            thirdChoice=line[3]
            fourthChoice=line[4]
            answer=line[5]
            print("Question",counter,": ",question,end="")
            print("\n")
            print("a. ",firstChoice)
            print("b. ",secondChoice)
            print("c. ",thirdChoice)
            print("d. ",fourthChoice)
            totalPointPossible+=int(line[6])
            userInput=input("Enter your choice here: ")
            userInput=userInput.lower()
            if userInput in choiceList:
                if userInput==answer:
                    correctNumber+=int(line[6])
                    print("Correct Answer")
                else:
                    print("Incorrect answer, the correct option is ",line[5])
            else:
                print("Please enter a choice from a to d, you get no point from this question")
            line_numbers=inputFile.readline()
            
    
    except IOError as error_1:
        print("File location is not correct")
    except ValueError as error_2:
        print("Value error, with conversion")
    except TypeError as error_3:
        print("int/string type mismatch")
    except IndexError:
        print("Test is finished")
        print("Your total point is: ",correctNumber,"/", totalPointPossible)
    finally:
        inputFile.close()
             
menu()
    
    
        
        


