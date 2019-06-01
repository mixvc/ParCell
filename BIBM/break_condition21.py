import  os

def breakCondition(t, T, N, breakCheck1):

    try:
        if input1:
           breakCheck1 = 1

    except:
        curr = os.getcwd()
        os.chdir('Output')
        fw = open("logfile.pcl", "a+")
        os.chdir(curr)
        fw.write("Error in defining the simulation end rules block, Please use proper notation and equation.\n")
        fw.close()
        if input1:
           breakCheck1 = 1
    #print breakCheck

    return breakCheck1
