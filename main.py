from fileWalker import fileUtility
import sys, getopt, os

# Prints the help message
def printHelp():
    print("Usage: main.py [options]")
    print("Options:")
    print("-h, --help: Show this help message and exit")
    print("-d, --directory: Directory to search (default: current directory)")
    print("-f, --file: File to search For")
    print("-s, --search: Search for file in directory")
    print("-w, --walk: Walk through directory (Will print all files and directories. Set -q and -o to output to file)")
    print("-a, --all: Search for file in directory and subdirectories")
    print("-r, --recursive: Search for file in directory and subdirectories recursively (default: true)")
    print("-v, --verbose: Prints out all files found (default: true) when printing directories")
    print("-t, --time: Prints out the time it takes to search for files")
    print("-c, --count: Prints out the number of files found (Only works when searching -s)")
    print("-e, --extension: File extension to search for")
    print("-m, --maxdepth: Maximum depth to search (default: None)")
    print("-o, --output: Output file")


def main(argv):
    # Set default values
    dir = os.getcwd()
    maxDepth = None
    extension = None
    file = None
    search = False
    walk = False
    verbose = True
    count = False
    outputFile = None
    recursive = True
    time = False

    
    # If no arguments are given, print help message
    if(len(argv) == 0):
        printHelp()

    # Get arguments
    try:
        opts, args = getopt.getopt(argv, "hd:f:swarvtc:e:m:o:", ["help", "directory=", "file=", "search", "walk", "all", "recursive", "verbose", "time", "count", "extension=", "maxdepth=", "output="])
    
    except Exception as e:
        print(e)
        printHelp()
        sys.exit(2)
    
    # Set arguments
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            printHelp()
            sys.exit()

        elif opt in ("-d", "--directory"):
            dir = arg
        
        elif opt in ("-e", "--extension"):
            extension = arg
        
        elif opt in ("-s", "--search"):
            search = True
        
        elif opt in ("-w", "--walk"):
            walk = True
        
        elif opt in ("-t", "--time"):
            time = True
        
        elif opt in ("-c", "--count"):
            count = True
        
        elif opt in ("-r", "--recursive"):
            recursive = True

        elif opt in ("-v", "--verbose"):
            verbose = True
            
        elif opt in ("-o", "--output"):
            outputFile = arg
            verbose = False

        elif opt in ("-m", "--maxdepth"):
            maxDepth = int(arg)
        
        elif opt in ("-f", "--file"):
            file = arg
        
        else:
            print("Unknown option: " + opt)
            printHelp()

        
    # Launch file utility function that controls file walker and searcher.    
    try:
        fileUtility(path=dir, depthLimit=maxDepth, extension=extension, recursive=recursive, search=search, walk=walk, time=time, count=count, outputFile=outputFile, verbose=verbose, file=file)
    
    except Exception as e:
        print(e)
        sys.exit(2)




    

if __name__ == "__main__":
    main(sys.argv[1:])