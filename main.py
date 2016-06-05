import cli;
import FileMan;

'''
Main file
 - Main execution file
'''

'''
FUNCTIONS
'''

'''
MAIN
'''

if __name__ == "__main__":
    choice = cli.mainMenu();
    if choice is 1:
        choice = cli.showsMenu();
    elif choice is 2:
        cli.addShowMenu();
