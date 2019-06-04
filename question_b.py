def compareVersions(line1, line2):  
    try:
        val1 = float(line1)
        val2 = float(line2)

        if val1 > val2:
            return("%s is greater than %s" % (line1, line2)) 
        elif val1 < val2:
            return("%s is lesser than %s" % (line1, line2))
        elif val1 == val2:
            return("%s is equal than %s" % (line1, line2))
        else: 
            return "error"

    except (ValueError, TypeError):
        if(line1 == line2):
            return("%s is equal than %s" % (line1, line2))
        elif(line1>line2):
            return("%s is greater than %s" % (line1, line2)) 
        else:
            return("%s is lesser than %s" % (line1, line2))
