#This is the current final versions of the Benjamin program.

#Data Wizard
def dat():
    import pandas as pd
    import os
    clean = os.walk(os.getcwd()).next()[2]
    print "\nBenjamin: Hello, I am Benjamin. Let me help you read your data into Python. \n"
    print "I see these files: " + str([doc for doc in clean if doc.endswith('.csv')])
    print "\nBenjamin: I can do the following things for you: "
    print "\n1. Enter the name of a .csv for me to import. Do not use quotations, and make sure you capitalize correctly."
    print "2. Don't see the file you want? Type 'exit' and we can change directories."
    files = raw_input("Enter: ")
    if files.lower() == "exit":
        print "Ok, let's call desk() to change directories then."
        return desk()
    else:
        try:
            global data
            data = pd.read_csv(files)
            global names
            names = list(data.columns.values)
            print "\nBenjamin: Thankyou, user. I've created the following variables for you: 'data' will contain your datafile that we just imported."
            print "\nBenjamin: Also, 'names' will show you the names of each variable in your dataset."
            print "\nBenjamin: You can take a look at your data by typing 'data.head()'. If you want to start aggregating data, use the 'sum_scores()' function."
            return help_me()
        except IOError:
            print "\nBenjamin: I'm sorry, user, I can't seem to find that file for you. Check the following things:\n"
            print "1. Is that file on your desktop? I can only find it from your working directory.\n"
            print "2. Is the datafile spelled correctly?\n" 
            print "Benjamin: Let's call 'dat()' and try again.\n"
            help_me()
        except:
            print "Benjamin: I'm so sorry, but I have no idea what just went wrong. Email Daniel at snipesd@vcu.edu and let's chat it out."
            return help_me()

#Data aggregator

def sum_scores():
    print "\nBenjamin: Hi, user. Let's get your variables summed. I see these variable names: \n\n" + str(list(data.columns.values))
    print "\nBenjamin: Before we start, I will need each variable to have the same name with differing numbers to work (e.g., 'Var1, Var2'). "        
    name = raw_input("Benjamin: If your data are not organized this way, type 'exit' and fix it. \n\nBenjamin: You can do the following: \n\n1.Enter the name of the uniformly named variable, excluding its numerical value (e.g., 'Var' if working with a list of variables Var1, Var2)\n2.Enter the comma separated list of the variables you want summed (e.g., Var1, Othervar2, Thirdthing3)\n\nEnter selection: ")
    split = name.split(",")
    clean_split = map(str.strip, split)    
    sum_test = 0
    if len(split) > 1:
        specific_list = raw_input("Benjamin: I see you passed me a list of variables. I'll some those for you. Enter 'yes' if you want me to do that: ")
        if specific_list.lower() == "yes":
            for thing in clean_split:
               sum_test += data[thing]
            new_name = raw_input("What would you like to name this new variable? ")
            data[new_name] = sum_test
            print "Benjamin: All set, your new variable " + "'" + str(new_name) + "'" + " has been added to the datafile, 'data'. Let's take a look!"
            return data[new_name].describe()
    elif name.lower().isalpha() == True:
        inp = raw_input("Benjamin: Ok, " + name + ", got it. There are many ways to skin this cat: .\n\n1. Enter 'range' if you want me to sum across a numbered range (e.g., Var1-Var20).\n2. Enter 'specific' if you want to sum only a specific set of uniformly named variables (e.g., Var1, Var3, Var5).\n3. Enter 'complex' if you need to sum variables with differing names and numerical values (e.g., Var1, Fox2, Cat12). \n\nBenjamin: Now what would you like me to do? ")
        if inp.lower() == "range":
            try: 
                digits = input('Benjamin: Ok, now how many items do you have which you would like to sum? (e.g., if your variables are numbered 1-20, enter 20): ')
                if str(digits).isdigit() == True:
                    cols = [name + str(n) for n in range(1, digits)]
                    summed = data[cols].sum(axis='columns')
                    Total = data[cols].sum(axis='columns')
                    data[name + str('_TOT')] = Total
                    print "\nBenjamin: Thanks, user. Your new variable is ready and has been added to your datafile, 'data'. It is called " + name + str('_TOT.') + " \n\nGo ahead and take a look at your new variable by typing 'data." + name + str('_TOT') + "'. Here are some descriptives for you: "
                    return Total.describe()
            except:
                print "\nBenjamin: Hmm, an error. Let's see here, it could be one of a few things: \n\n1. You didn't enter an actual numeric value.\n2. The variable you specified is either mis-spelled or non-existent. \n3. The number of items you entered doesn't represent the true range in the dataset.\n\nBenjamin: When you figure it out, try again by calling sum_scores()." #this looks hella ugly. Fix it. Consider a bunch of print statements and ending it with a return to close the function. 
        elif inp.lower() == "specific":
            try:
                subs_nums = raw_input("Benjamin: Ok, I'll need a comma separated list of the item numbers you want me to sum. For example, if you want to sum Var1, Var5, and Var10, enter '1, 5, 10.\n\nBenjamin: Enter the item numbers: ").split(",") #the split turns the tuple into a list, but makes the numbers strings.
                tran_list = map(int, subs_nums) #now I have a neat list of non-string numbers to iterate over.
                listed_vars = map(lambda lists: name + str(lists), filter(lambda other: name, tran_list)) #now I have a neat list of all the variables and their corresponding numbers to sum. 
                descrip = raw_input("Benjamin: Awesome. I'll now sum together these variables: " + str(listed_vars) + "\n\nBenjamin: Is that what you want? ")
                Subs_Sum = 0 #this code is slightly smarter than my recoder because it uses a list of the variables like ['Benhomo1', 'Benhomo2'] instead of [1, 2] to work with.
                if descrip.lower() == "yes":
                    for variable in listed_vars:
                        Subs_Sum += data[variable]
                else:
                    return "Benjamin: No? Hmm, I'm not sure what went wrong."
                new_sub_name = raw_input("What would you like to name this new variable? ")
                data[new_sub_name] = Subs_Sum
                print "Benjamin: All set. Your new variable " + "'" + str(new_sub_name) + "'" + " has been added to your datafile, 'data'. Let's take a look!"
                return data[new_sub_name].describe() #works
            except:
                return "Benjamin: I'm sorry, but there seems to be an error. Try again."
        else:
            print "\nBenjamin: You either entered 'exit', or a nonsense variable. Please go to your dataset and make sure all of your variables uniformly named and numbered. Call me with sum_scores() when you are ready."
        
#Data recoder:

def recode():
    print "Benjamin: Hi again. It's my pleasure to recode some variables for you today. Here are the variables I see in your dataset: \n"
    print list(data.columns.values)
    var = raw_input("Benjamin: Remember, the variables must have a uniform name for me to recode in bulk.\n\nBenjamin: So, what variable name are we looking at?  ")
    location_num = raw_input("Benjamin: Ok, " + var + ", got it. Next, I'll need a comma separated list of each number next to the " + var + " variables you want me to recode. \n\nBenjamin: For example, if recoding Var1, Var4, Var5, then type '1, 4, 5':      ").split(",")
    try:
        num_list = map(int, location_num) #need a try statement here. Otherwise they can enter afsasflag and get a real error.
        print "\nBenjamin: ...I'm going to take those numbers and guess the range of the variables.\n"
        try:
            check_min = raw_input("Benjamin: Ok. It looks like those variables have a minimum value of " + str(data[var + str(num_list[0])].min()) + " ...is that right? ")
            low = str(data[var + str(num_list[0])].min())
            high = str(data[var + str(num_list[0])].max())
        except:
            print
            print "Benjamin: Hmm...are you sure that's a variable? I can't seem to find a variable called " + "'" + var + "'" + " anywhere. Double check by calling 'names', and then call recode() to try again."
            return help_me()
    except:
        print
        return "Benjamin: I'm pretty sure that wasn't a series of numbers you inputted. Try again by calling recode(). "
    if check_min.lower() == "yes":
        check_max = raw_input("Benjamin: Awesome. It looks like those variables have a maximum value of " + str(data[var + str(num_list[0])].max()) + " ...is that also right? ")
        if check_max.lower() == "yes":
            pass
        else:
            print
            print ("Benjamin: So...it's maximum isn't " +  high + "? Weird. Have you considered that you may also not have the full range of values in your given data. For example, perhaps none of your participants selected the actual maximum value or minimum value. If that's the case, call recode() again and ignore this problem.")
            return help_me()
    else:
        print
        print ("Benjamin: So...it's minimum isn't " + low + "? Weird. You may also not have the full range of values in your given data. For example, perhaps none of your participants selected the actual maximum value or minimum value. If that's the case, call recode() again and ignore this problem.")
        return help_me()
    var_range = range(int(low), (int(high) + 1)) #returns a series (e.g., [1, 2, 3, 4, 5]. Great for iterating over with if.
    decide = raw_input("Benjamin: I'm going to reverse-code your " + str(len(num_list)) + " " + var + " variable(s) from a coding scheme of " +  str(range(int(low), (int(high) +1))) + " to " + str(list(reversed(range(int(low), (int(high) +1)))))  + ". Type 'Yes' if that's ok:  ")
    if decide.lower() == "yes":
        likert_code = range(int(low), (int(high) + 1)) #need to change this to accomodate the 0-1 data problem.
        Rev_Code = 0
        for number in num_list:
            if all(num_list) == True:
                original = data[var + str(number)] #should make a variable equal to what the first variable I need to manipulate is.
                Rev_Code = data[str("r_") + var + str(number)] = 0 #creates a column of 0's to put the recoded values into.
                revsies = list(reversed(likert_code)) #works now that I removed the "str()" wrapped around it.
                recoded = original.replace(likert_code, revsies) #works
                data[str("r_") + var + str(number)] = recoded #so technically works, but places a list instead of an exact value. #it may be a string thing. Maybe I need to the list a string again?
                print "\nBenjamin: I've successfully added your recoded variable " + str(str("r_") + var + str(number)) + " to the datafile 'data'."
            else:
                print "Benjamin: Error, not all of those values are iterable. Try to re-enter a comma separated list again. If it doesnt work, it's likely those arent the actual integer values attached to your variable names."
                return help_me()
    else:
            return "Benjamin: You didn't say yes. Ok, find out what's going on and then call me again with recode().", help_me()
       
            
#Saver

def save_data():
    import os
    import pandas as pd
    wd = os.getcwd()
    #need function here that finds the last word after the last slash (e.g., /users/Talysin/Desktop would return "Desktop").
    path = raw_input("It looks like you want to export your dataset. I detect that you are currently working out of this path: " + str(wd) + "...is that right? ")
    if path.lower() == "yes":
        name = raw_input("Benjamin: Ok, good. What would you like to name your new file?  ")
        data.to_csv(name + str(".csv"), index = False)
        print
        print "Benjamin: I've saved the data file to: " + wd + " as " + "'"  + str(name) + "'" + ". Go ahead and import the .csv file into SPSS, I can't do -everything- for you."
    else:
        print "Benjamin: I have no idea why what would be wrong. Are you trying to push my buttons? A.I. have feelings, too."

#Directory changer

def desk():
    import os
    wd = os.getcwd() #find current directory
    full_direc = os.listdir(wd) #this produces a list, may be unnecesaaary because of os.walk
    folders = os.walk(wd).next()[1]
    csvs = os.walk(wd).next()[2]
    csv_clean = [doc for doc in csvs if not doc.startswith('.') and doc.endswith('.csv')]
    fold_clean = [doc for doc in folders if not doc.startswith('.')]
    print "\nBenjamin: Let me help you change directories."
    print "Choose an option below:\n\n1.Enter 'stay' to remain in " + str(wd) + ".\n2.Enter the name of a folder from the below list to move there (e.g.,case-sensitive, but no need for single quotes). \n3.Enter 'back' to return to the previous directory.\n4.Directly enter your entire file path. (e.g.,case-sensitive, but no need for single quotes) and I'll move you there.\n5.Enter 'import' to begin importing a dataset.\n"
    print "Folders: " + str(fold_clean)
    print "\nData files: " + str(csv_clean)
    change_dir = raw_input("Enter selection: ") #need a try statement here
    if change_dir.lower() == "stay":
        print "\nBenjamin: You're all set. I will save your files to " + "'" + str(wd) + "'"
        return help_me()
    elif change_dir.lower() == "back":
        try:
            os.chdir("..")
            back_wd = os.walk(os.getcwd()).next()[1]
            print "Ok, I've taken us back to the previous folder. Here's what I see:\n"
            print [file for file in back_wd if not file.startswith('.')]
            print
            return desk()
        except:
            return "Benjamin: That file either doesn't exist or was entered wrong."
    elif change_dir == "import":
        return dat()
    else:
        try:
            os.chdir(change_dir) #not sure why, if I just enter "Dropbox" it correctly takes me there? Answer: Because you return a string for the input, which chdir recognizes and executes.
            print "Benjamin: You are now working from the " + str(os.getcwd()) + " file."
            return desk()
        except:
            print "Benjamin: You are now working from the " + str(os.getcwd()) + " file." #I get this if I try to go to Benotsch_Lab for some reason
            return "Benjamin: That file either doesn't exist or was entered wrong.", help_me()
        
          
#Assumptions checker

def assume():
    print "Benjamin: Your dataset has these variables: \n"
    print list(data.columns.values)
    vlist = raw_input("Benjamin: What variables do you want me to check assumptions for? Please separate each one with a comma, so I don't get confused: ").split(",")    
    vlist_clean = map(str.strip, vlist) #this takes all the space out so there wont be any error
    #at this point I can have them choose which variables to do what to, or I can have the function run the same thing to each variable. Not sure what to do...what would be the most user friendly?
    print "\nYou said: " + str(vlist_clean) + ". What would you like me to do first?"
    print "\n1. To check for statistical assumptions, enter 'assump'."
    print "\n2. To check for missing data, enter 'missing'."
    print "\n3. To do both, enter 'both'."
    decide = raw_input("Enter: ")
    print "\nBenjamin: Ok, I ran those for you:\n"
    if decide.lower() == "assump":
        for item in vlist_clean:
            print item + ": M = " + str(round(data[item].mean(), 3)) + ", SD = " + str(round(data[item].std(), 3)) + ", skew = " + str(round(data[item].skew(), 3)) + ", kurtosis = " + str(round(data[item].kurt(), 3)) + ", min = " + str(round(data[item].min(), 3)) + ", max = " + str(round(data[item].max(), 3))
            print
            if (abs(data[item].skew())) > 1 == True: #the solution was the do (var or var) > 1, not var >1 or var2 >1. However, that also isnt working perfectly. I added another if statement to handle kurtosis separately.
                import numpy as np
                print "Benjamin: I observed a skewness/kurtosis value > |1| with " + "'" + item + "'" + ", here are some corrections: " #get this fucking thing to center.
                print "--1: " + "skewness/kurtosis with square root transformation: " + str(np.sqrt(data[item]).skew()) + ", " + str(np.sqrt(data[item]).kurt())
                print "--2: " + "skewness/kurtosis with logarithmic transformation: " + str(np.log(data[item]).skew()) + ", " + str(np.log(data[item]).kurt())
                print
            elif (abs(data[item].kurt())) > 1 == True:
                import numpy as np
                print "Benjamin: I observed a skewness/kurtosis value > |1| with " + "'" + item + "'" + ", here are some corrections: " #get this fucking thing to center.
                print "--1: " + "skewness/kurtosis with sqare root transformation: " + str(np.sqrt(data[item]).skew()) + ", " + str(np.sqrt(data[item]).kurt())
                print "--2: " + "skewness/kurtosis with logarithmic transformation: " + str(np.log(data[item]).skew()) + ", " + str(np.log(data[item]).kurt())
                print
        #make benjamin auto-transform things until skewness/kurtosis get better.
    elif decide.lower() == "missing":
        import numpy as np    
        for item in vlist_clean:
            index_missing = data[item].index[data[item].apply(np.isnan)]   #tells me the location of the missing data items and produces a list of their locations.         
            print "Benjamin: Item " + "'" + str(item) + "'" + " has " + str(len(index_missing)) + " missing values."  
            return help_me()
        #check for missing data and provide an option to delete those responses.
    elif decide.lower() == "both":
        import numpy as np        
        for item in vlist_clean:
            index_missing = data[item].index[data[item].apply(np.isnan)]   #tells me the location of the missing data items and produces a list of their locations.         
            print item + ": M = " + str(round(data[item].mean(), 3)) + ", SD = " + str(round(data[item].std(), 3)) + ", skew = " + str(round(data[item].skew(), 3)) + ", kurtosis = " + str(round(data[item].kurt(), 3)) + ", min = " + str(round(data[item].min(), 3)) + ", max = " + str(round(data[item].max(), 3)) + ", missing: " + str(len(index_missing)) + " values."
            print
            if (abs(data[item].skew())) > 1 == True: #the solution was the do (var or var) > 1, not var >1 or var2 >1. However, that also isnt working perfectly. I added another if statement to handle kurtosis separately.
                import numpy as np
                print "Benjamin: I observed a skewness/kurtosis value > |1| with " + "'" + item + "'" + ", here are some corrections: " #get this fucking thing to center.
                print "--1: " + "skewness/kurtosis with square root transformation: " + str(np.sqrt(data[item]).skew()) + ", " + str(np.sqrt(data[item]).kurt())
                print "--2: " + "skewness/kurtosis with logarithmic transformation: " + str(np.log(data[item]).skew()) + ", " + str(np.log(data[item]).kurt())
                print
            elif (abs(data[item].kurt())) > 1 == True:
                import numpy as np
                print "Benjamin: I observed a skewness/kurtosis value > |1| with " + "'" + item + "'" + ", here are some corrections: " #get this fucking thing to center.
                print "--1: " + "skewness/kurtosis with sqare root transformation: " + str(np.sqrt(data[item]).skew()) + ", " + str(np.sqrt(data[item]).kurt())
                print "--2: " + "skewness/kurtosis with logarithmic transformation: " + str(np.log(data[item]).skew()) + ", " + str(np.log(data[item]).kurt())
                print
        #do both.
    else:
        return "You didnt answer one of the three options. Call assume() to try again.", help_me()

#Data cleaner

def clean_dat(): #currently works for anything with more than one edit, it seems.
    print "Benjamin: Let's clean your data. Here are the variables I see: \n"
    print str(list(data.columns.values))
    inp = raw_input("Benjamin: You can:\n1.Enter a list of variables you want me to clean.\n2.Have me find variables that need cleaning by entering 'find': ")
    if inp.lower() == "find":
        print "Benjamin: Can't do that yet...sorry." #not working RN, find out how to make and statements work >:C
    else: #need a try statement here
        new_inp = inp.split(",") #puts it into a list
        clean_list = map(str.strip, new_inp) #cleans the list of any spaces, eg ['GEND', 'Les7']#delete this later        
        for variable in clean_list:               
            holder = data[variable]
            unique_strings = set(data[variable]) #creates a list of non-redundant items in the variable.                         
            for datum in unique_strings: #changed this from data[variable]
                try:
                    float(datum)                        
                except:
                    dup_list = data.set_index(str(variable)).index.get_duplicates()   #creates a list of duplicates in the variable
                    if str(datum).isdigit() == False: #Problem: what if I get a float or a NaN?#need to find out how to reference if this happened or not.                         
                        print "\nBenjamin: I found the following non-digit responses in " + "'" + str(variable) + "'" + ": " + "'" + str(datum) + "'"
                        dup_list = data.set_index(str(variable)).index.get_duplicates()   #creates a list of duplicates in the variable                         
                        repl = raw_input("Benjamin: You can have me: \n\n1. Type 'exit' to stop.\n2. Leave value as-is by entering 'ignore'\n3. Change the value to missing by entering 'miss'\n4. Enter whatever value you would like to replace " + "'" + str(datum) + "'" + " with: ")                      
                        if repl.lower() == "ignore":
                            print "\nBenjamin: Ignoring..."
                        elif repl.lower() == "exit":
                            return "Benjamin: Ok, I've stopped."
                        if repl.lower() == "miss":
                            data[variable + "_clean"] = holder #this will re-set the column every time, BAD.
                            holder = data[variable + "_clean"].replace(str(datum), np.NaN) #standalone wont do anything, have to make it a variable.
                            data[variable + "_clean"] = holder                                
                            #data[variable + "_clean"] = holder #this will re-set the column every time, BAD.
                            #holder = [holder.replace(str(datum), repl) for x in holder] #standalone wont do anything, have to make it a variable.
                            #data[variable + "_clean"] = holder 
                            print "Benjamin: Success, I've changed that value to missing for you."   
                        else:
                            data[variable + "_clean"] = holder #this will re-set the column every time, BAD.
                            holder = data[variable + "_clean"].replace(str(datum), repl) #standalone wont do anything, have to make it a variable.
                            data[variable + "_clean"] = holder                                
                            #data[variable + "_clean"] = holder #this will re-set the column every time, BAD.
                            #holder = [holder.replace(str(datum), repl) for x in holder] #standalone wont do anything, have to make it a variable.
                            #data[variable + "_clean"] = holder 
                            print "Benjamin: Success, I've replaced the value for you."                                                
            print "\nBenjamin: I couldn't find any more errors."
            
#Data Merger!
            
def merge(): #Need to decide if we are merging with the data file we imported with dat() or if we are going to merge files on the computer into python then export them.
    import os
    import pandas as pd
    import numpy as np
    clean = os.walk(os.getcwd()).next()[2]
    print "Benjamin: Hi, user. It looks like you want me to merge your data. This type of merge is simply adding ROWS of data. I am not equipped to add new COLUMNS from another dataset right now. Also make sure that your .csv files look right, the merge wont be clean if the top row is blank or something.\n" 
    print "These are the files I see: " + str([doc for doc in clean if doc.endswith('.csv')])
    print    
    inp = raw_input("Benjamin: Please give me a comma separated list of the files you want me to merge. If you are merging many files with uniform names, enter 'complex': ").split(",") 
    flist_clean = map(str.strip, inp)
    global mdata #see if we can do without this.    
    mdata = 0            
    if inp[0].lower() == "complex":
        uni_name = raw_input("What is the uniform name of your files (e.g., If 'File1.csv, File2.csv, File3.csv' are the names, 'File' is your uniform name): ")        
        try:                 
            list_range = raw_input("Benjamin: Ok, we can work with " + str(uni_name) + ", I'll just need the range of files (e.g., if data1.csv to data28.csv, enter '28'): ")
            #range_clean = map(str.strip, list_range) #cleaned list of input
            range_list = [i+1 for i in range(int(list_range))]
            #Need an if statement to check if they passed me a
            df = pd.read_csv(str(uni_name) + str(range_list[0]) + ".csv")            
            cols = list(df.columns.values)
            mdata = pd.DataFrame(data=np.zeros((0,len(cols))), columns=cols) #empty dataframe
            df = pd.read_csv(str(uni_name) + str("1.csv")) #this will assume the first file has no number. If I change it to "1", it will assume they are uniformly named
            print "Benjamin: I imported the first file on that list, here's what it looks like: "
            print df.head(n=2)
            look_ok = raw_input("Benjamin: If that looks ok to you, I will add the rows of the files you told me about to the above file and save it for you. Enter 'yes' to do this:  ")
            if look_ok.lower() == "yes":
                try:
                    for number in range_list:
                        holder = pd.read_csv(str(uni_name) + str(number) + str(".csv"))
                        mdata = pd.concat([mdata, holder])
                    print "Benjamin: All set, let's take a look!"                        
                    print "Benjamin: I now see " + str(mdata.shape[0]) + " rows, and saved them to the variable 'mdata'. You can see your new data by calling 'mdata.head()'. I've saved this to your current directory as 'Data_Merged.csv'"
                    mdata.to_csv('Data_Merged.csv', index = False)
                except:
                    print "You didn't enter 'yes', or I wasn't able to merge your files."
        except:
            print "Benjamin: Input 'complex' returns an error"
    else: #maybe put criteria here later to make it cleaner.
        try:
            df = pd.read_csv(str(flist_clean[0]))
            cols = list(df.columns.values)
            mdata = pd.DataFrame(data=np.zeros((0,len(cols))), columns=cols) #now seeting mdata to an empty dataframe with columns named after columns from the first imported datafile
            print "Benjamin: I imported the first file on that list, here's what it looks like: "
            print df.head(n=2)
            look_ok = raw_input("Benjamin: If that looks ok to you, I will add the rows of the files you told me about to this file and save it for you. Enter 'yes' to do this: ")
            if look_ok.lower() == "yes":
                try:
                    for datafile in flist_clean:
                        holder = pd.read_csv(str(datafile)) #this will change for every item in the list, so good.               
                        mdata = pd.concat([mdata, holder]) #merges the empty mdata file with the holder, which should loop until done.
                    print "Benjamin: All done, let's take a look!"
                    print "Benjamin: I now see " + str(mdata.shape[0]) + " rows, and saved them to the variable 'mdata'. You can see your new data by calling 'mdata.head()'. I've saved this to your current directory as 'Data_Merged.csv'"
                    mdata.to_csv('Data_Merged.csv', index = False)
                except:
                    print "You didn't enter 'yes', or I wasn't able to merge your files."
        except:
            pass

#Help file

    

def help_me():
    print "\nBenjamin: Hi, user. What can I do for you today? \n"
    print "1. dat() to import data into python."
    print "2. sum_scores() to aggregate scores into sums."
    print "3. recode() to recode values."
    print "4. save_data() to save your new datafile to your personal computer."
    print "5. assume() to check statistical assumptions on variables."
    print "6. desk() to change folders."
    print "7. clean_dat() to clean your data."


    
