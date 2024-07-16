import operator
import sys
import json

#-----------------------loading the structure.json file----------------------
structure = open('structure.json')

sample = json.load(structure)

top_contents = sample["contents"]

display = "interpreter" + "\n"

names = []

arg_len = len(sys.argv)

top_contents = sample["contents"]

for each_item in top_contents:
    names.append(each_item["name"])
    

rev_top_contents = top_contents[::-1]

top_contents_data = ""

top_contents_data_rev = ""

top_file_data = ""

top_dir_data = ""

top_file_data = []

top_dir_data = []

top_file_data_rev = []

top_dir_data_rev = []

top_file_data_str = ""

top_dir_data_str = ""

top_file_data_rev_str = ""

top_dir_data_rev_str = ""

sorted_top_file_data_by_time = []

sorted_top_dir_data_by_time = []

sorted_top_file_data_by_time_str = ""

sorted_top_dir_data_by_time_str = ""


top_file_names = [name for name in names if name.isupper() or "." in name]

top_dir_names = [name for name in names if name not in top_file_names]



sorted_list_by_time = sorted(top_contents, key=operator.itemgetter('time_modified'))


#------------------------Get the list data of top content--------------------------------

for each_item in top_contents:
        top_contents_data = top_contents_data+each_item["permissions"]+" "+str(each_item["size"])+" "+str(each_item["time_modified"])+" "+each_item["name"]+"\n"
   


#------------------------Get the list data of top content in reverse--------------------------------

for each_item in rev_top_contents:
        top_contents_data_rev = top_contents_data_rev+each_item["permissions"]+" "+str(each_item["size"])+" "+str(each_item["time_modified"])+" "+each_item["name"]+"\n"
   

#------------------------Get the list data of top files and dir--------------------------------


for each_item in top_contents:
    
    if each_item["name"] in top_file_names:
        
        top_file_data.append(each_item)
    
        top_file_data_str = top_file_data_str+each_item["permissions"]+" "+str(each_item["size"])+" "+str(each_item["time_modified"])+" "+each_item["name"]+"\n"


    elif each_item["name"] in top_dir_names:
        
        top_dir_data.append(each_item)
       
        top_dir_data_str = top_dir_data_str+each_item["permissions"]+" "+str(each_item["size"])+" "+str(each_item["time_modified"])+" "+each_item["name"]+"\n"


top_file_data_rev = top_file_data[::-1]

top_dir_data_rev = top_dir_data[::-1]



for each_item in top_file_data_rev:
    top_file_data_rev_str = top_file_data_rev_str+each_item["permissions"]+" "+str(each_item["size"])+" "+str(each_item["time_modified"])+" "+each_item["name"]+"\n"



for each_item in top_dir_data_rev:
    top_dir_data_rev_str = top_dir_data_rev_str+each_item["permissions"]+" "+str(each_item["size"])+" "+str(each_item["time_modified"])+" "+each_item["name"]+"\n"


sorted_top_dir_data_by_time = sorted(top_dir_data, key=operator.itemgetter('time_modified'))

sorted_top_file_data_by_time = sorted(top_file_data, key=operator.itemgetter('time_modified'))

for each_item in sorted_top_dir_data_by_time:
    sorted_top_dir_data_by_time_str = sorted_top_dir_data_by_time_str+each_item["permissions"]+" "+str(each_item["size"])+" "+str(each_item["time_modified"])+" "+each_item["name"]+"\n"



for each_item in sorted_top_file_data_by_time:
    sorted_top_file_data_by_time_str = sorted_top_file_data_by_time_str+each_item["permissions"]+" "+str(each_item["size"])+" "+str(each_item["time_modified"])+" "+each_item["name"]+"\n"



#----------------------preparing display variable containing the files names in tree structure--------------

for each_item in top_contents:
   
    display = display + "|-" + each_item["name"] + "\n"
    
    
    if "contents" in each_item.keys() and type(each_item["contents"])==list:
       
        for each_item1 in each_item["contents"]:
           
            display = display + "| |-" + each_item1["name"] + "\n"
           

#---------------------implimenting pyls command------------------------

if arg_len == 1:

    pyls_names = [name for name in names if not name.startswith(".")]

   
    for x in range(len(pyls_names)):
        print(pyls_names[x], end=" ")


#---------------------implimenting pyls -A command------------------------
        
if arg_len == 2 and '-A' in sys.argv[1]:
    
    for x in range(len(names)):
        print(names[x], end=" ")
   
  
#---------------------implimenting pyls -l command------------------------

if arg_len == 2 and '-l' in sys.argv[1]:
    
    print(top_contents_data)
   


 
#---------------------implimenting pyls -l command in reverse------------------------

if arg_len == 3 and '-l' in sys.argv[1] and '-r' in sys.argv[2]:

    print(top_contents_data_rev)

    


#---------------------implimenting pyls with sort by time command in reverse------------------------

if arg_len == 4 and '-l' in sys.argv and '-r' in sys.argv and '-t' in sys.argv:


    for each_item in sorted_list_by_time:
        print(each_item["permissions"]+" "+str(each_item["size"])+" "+str(each_item["time_modified"])+" "+each_item["name"]+"\n")
   


#---------------------implimenting pyls with dir/file listing------------------------

if arg_len == 3 and '-l' in sys.argv and '--filter=dir' in sys.argv:
    print(top_dir_data_str)
    
elif arg_len == 4 and '-l' in sys.argv and '--filter=dir' in sys.argv and '-r' in sys.argv:
    print(top_dir_data_rev_str)


elif arg_len == 3 and '-l' in sys.argv and '--filter=file' in sys.argv:
    print(top_file_data_str)
    
elif arg_len == 4 and '-l' in sys.argv and '--filter=file' in sys.argv and '-r' in sys.argv:
    print(top_file_data_rev_str)
    
    
elif arg_len == 5 and '-l' in sys.argv and '--filter=file' in sys.argv and '-r' in sys.argv and '-t' in sys.argv:
    print(top_file_data_rev_str)
    
elif arg_len == 5 and '-l' in sys.argv and '--filter=dir' in sys.argv and '-r' in sys.argv and '-t' in sys.argv:
    print(top_dir_data_rev_str)

elif arg_len == 4 and '-l' in sys.argv and '--filter=dir' in sys.argv and '-t' in sys.argv:
    print(sorted_top_dir_data_by_time_str)
    

elif arg_len == 4 and '-l' in sys.argv and '--filter=file' in sys.argv and '-t' in sys.argv:
    print(sorted_top_file_data_by_time_str)


elif "--filter" in sys.argv:
    if "--filter=dir" not in sys.argv or "--filter=file" not in sys.argv:
        print("Invalid")

 
elif "--filter=folder" in sys.argv:
    print("error: folder is not a valid criteria. Available filters are dir and file.")
 


#---------------------implimenting pyls implimenting parser--------------------------

list_data_str = ""

for name in top_dir_names:
    
    if name in sys.argv:
        
        for each_item in top_contents:
            
            if name == each_item["name"]:
                
                if "contents" in each_item.keys():
                    
                    list_data = each_item["contents"]
                    
                    for each_data in list_data:
                        
                        if '-h' in sys.argv:
                            size = each_data["size"]/1000
                            
                            list_data_str = list_data_str+each_data["permissions"]+" "+str(size)+" "+str(each_data["time_modified"])+" "+each_data["name"]+"\n"

                        else:    
                            list_data_str = list_data_str+each_data["permissions"]+" "+str(each_data["size"])+" "+str(each_data["time_modified"])+" "+each_data["name"]+"\n"
                        

        print(list_data_str)
        

for each_argv in sys.argv:
    
    if '/' in each_argv:
        
        file_name = each_argv.split('/')[-1]
        
        for each_item in top_contents:
            
            if "contents" in each_item.keys():
                
                for each_data in each_item["contents"]:
                    
                    if file_name == each_data["name"]:
                        
                        if '-h' in sys.argv:
                            size = each_data["size"]/1000
                            list_data_str = list_data_str+each_data["permissions"]+" "+str(size)+" "+str(each_data["time_modified"])+" "+each_argv+"\n"

                        else:    
                            list_data_str = list_data_str+each_data["permissions"]+" "+str(each_data["size"])+" "+str(each_data["time_modified"])+" "+each_argv+"\n"
                        
        
        if not list_data_str:
            print("error:can not access,"+each_argv+"no such file or directory")
            
        print(list_data_str)

#---------------------displaying the directories and files in tree structure-------------------------------
        
if len(sys.argv)<3 and '-d' in sys.argv:
    print(display)


#---------------------implimenting pyls implimenting help-------------------------------
        
if len(sys.argv)<4 and '--help' in sys.argv:
    print("**pyls program is printing the directories and files in tree structure.below are the utilities and their usage\n")
    print("pyls -d: Display the directories and files in tree structure\n")
    print("pyls: Display the directories and files in a line\n")
    print("pyls -A: Display the directories and files in a line including files starting with .\n")
    print("pyls -l: Display the directories and files vertically with additional information\n")
    print("pyls -l -r: Display the directories and files vertically in reverse\n")
    print("pyls -l -r -t: Display the directories and files vertically in reverse sorted by time_modified\n")
    print("pyls -l -r --filter<option>: Display the directories and files vertically in reverse if option=dir then directories else files if option=file\n")
    print("pyls -l -r -h --filter<option>: Display the directories and files vertically in reverse directories if option=dir else files if option=file\n and human readable size")

    

