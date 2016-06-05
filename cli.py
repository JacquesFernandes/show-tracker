import FileMan as fman;
'''
CLI file
 - All the "menus" in the software
'''

'''
FUNCTIONS
'''
def error(msg):
	print("ERROR :: "+msg);

'''
Func: mainMenu
Input: nothing
output:
 - number based on below o/p's
'''
def mainMenu():
	print(":: Main Menu ::");
	print("1 - Shows");
	print("2 - Add Show");
	choice = int(input("-> "));
	while choice != 1 and choice != 2:
		error("Invalid Choice!");
		choice = int(input("-> "));
	return(choice);

'''
Func: showsMenu
Input: nothing
Output:
 - prints out list of shows
'''
def showsMenu():
    print(":: Shows ::");
    shows = fman.getShowDict();
    if len(shows) is 0:
        print("Shows list is empty....");
        return;
    i = 1;
    for show in shows.keys():
        print(str(i)+" - "+show);
        i+=1;

'''
Func: addShowMenu
Input: nothing
Output:
 - Show is added to shows.txt
'''
def addShowMenu():
    print(":: Add a Show ::");
    show_name = input("Show name: ");
    print("Show path/directory (drag and drop the folder onto the terminal, the path should come by itself)");
    show_dir = input("-> ").lstrip("'").rstrip("' ");
    fman.addShow(show_name,show_dir);
    #print("Name: "+show_name+"\tDir: "+show_dir+"|");

'''
MAIN
'''
if __name__ == "__main__":
    print("cli.py test successful");
