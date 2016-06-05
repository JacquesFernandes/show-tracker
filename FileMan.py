import os;
import json;

'''
File-man
 - File manager
 - Handles file-related functions

Files (All in ./assets/):
 - shows.txt (names and dirs)
 - positions.txt (names and position in series) //TO WORK ON
'''

'''
FUNCTIONS
'''
def error(msg):
    print("ERROR :: "+msg);

'''
Func: getShowDict
Input: nothing
output: dictionary of format {"show name":"show path/dir"}
'''
def getShowDict():
    showfile = None;
    try:
        showfile = open("./assets/shows.txt","r");
    except FileNotFoundError:
        error("shows.txt not found! Creating...")
        if "assets" in os.listdir():
            showfile = open("./assets/shows.txt","w");
            showfile.write("{}");
            showfile.close();
            showfile = open("./assets/shows.txt","r");
        else:
            os.mkdir("assets");
            showfile = open("./assets/shows.txt","w");
            showfile.write("{}");
            showfile.close();
            showfile = open("./assets/shows.txt","r");
    show_json_string = showfile.readline();
    showfile.close();
    if len(show_json_string) is 0:
        error("Empty shows.txt! Creating base....");
        showfile = open("./assets/shows.txt","w");
        showfile.write("{}");
        showfile.close();
    showfile = open("./assets/shows.txt","r");
    show_dict = json.loads(showfile.readline());
    showfile.close();
    return(show_dict);

def addShow(show_name, show_dir):
    shows = getShowDict();
    if show_name in shows.keys():
        print("The show "+show_name+" already has an entry with dir: "+shows[show_name]);
        choice = input("Replace?[y/n]: ");
        if choice == "y" or choice == "Y":
            shows[show_name] = show_dir;
        elif choice == "n" or choice == "N":
            print("Directory will remain unchanged...");
    shows[show_name] = show_dir;
    show_file = open("./assets/shows.txt","w");
    show_file.write(json.dumps(shows)+"\n");
    show_file.close();
    print("Show successfully added!");
