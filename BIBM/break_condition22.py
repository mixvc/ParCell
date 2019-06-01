import  os

def breakCondition(current_time, Total_time, Total_number_of_cells, breakCheck1):

    try:
        if current_time >= Total_time:

           breakCheck1 = 1

    except:
        curr = os.getcwd()
        os.chdir('Output')
        fw = open("logfile.txt", "a+")
        os.chdir(curr)
        fw.write("Error in defining the simulation end rules block, Please use proper notation and equation.\n")
        fw.close()
        if current_time >= Total_time:

           breakCheck1 = 1
    #print breakCheck

    return breakCheck1