## Summary:

FileWalker is a command-line utility tool that is made to not only show
directory contents, but to also allow for users to look for specific files, find all files with a specific extension, as well as count the number of files on a system with the specified extension. This tool is mostly useful for people who may forget where they saved a recently downloaded a powerpoint or report, but may have forgotten where it is or if one wants to know how many say .docx files are on a system to see if they have a full set.


<br>

## Dependencies:

FileWalker keeps things simple and only requires that one should already have on their system if they have python. Though I will try my best to keep the dependencies section updated, and if a dependecy is required I will list it.

<br>

## Install and Start-up:

Once the the project folder has been insalled and is ready to use you should be able to use one of these two commands to activate the virtual env this project uses. Please remember the commands below are for if you are currently in the project folder, so if you are not please update the path.

<br>

For Unix/macOS:

    source env/bin/activate

For Windows:

    .\env\Scripts\activate

<br>

## Arguments:

    Usage: main.py [options]
    Options:
    -h, --help: Show this help message and exit
    -d, --directory: Directory to search (default: current directory)
    -f, --file: File to search For
    -s, --search: Search for file in directory
    -w, --walk: Walk through directory (Will print all files and directories. Set -q and -o to output to file)
    -a, --all: Search for file in directory and subdirectories
    -r, --recursive: Search for file in directory and subdirectories recursively (default: true)
    -v, --verbose: Prints out all files found (default: true) when printing directories
    -t, --time: Prints out the time it takes to search for files
    -c, --count: Prints out the number of files found (Only works when searching -s)
    -e, --extension: File extension to search for
    -m, --maxdepth: Maximum depth to search (default: None)
    -o, --output: Output file


## Future:

I hope to be able to continue this project in the future by adding more and more utility features to it
(or just creating another standalone application), so please stay tuned and feel free to mention if you 
have any ideas on what would be a good idea to add.