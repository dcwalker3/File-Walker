import os
from timer import Timer

"""
<summary>
    Function to recursively print out all files in a directory and subdirectories.
</summary>
<param name="path"> The path to the directory to search. </param>
<param name="depth"> The depth of the current directory. </param>
<param name="depthLimit"> The maximum depth to search. </param>
<param name="outputFileFile"> The file to output the results to. </param>
<param name="verbose"> Whether or not to print the results to the console. </param>
<param name="recursive"> Whether or not to search subdirectories. </param>
<returns> Nothing. </returns>
"""
def fileWalker(path, depth=0, depthLimit=None, outputFile=None, verbose=True, recursive=True):
    # Get list of contents in the current directory
    dirContents = os.listdir(path)

    # Print the current directory 
    if(outputFile):
        outputFile.write(" "*depth + path + "\n") 
    elif(verbose):
        print(path)

    # Loop through the contents
    for item in dirContents:
        
        # If the item is a directory
        if(os.path.isdir(os.path.join(path, item))):
            
            # If the depth is less than the depth limit or the depth limit is not set
            if(recursive==True and depthLimit is None or depth < depthLimit):
                fileWalker(path=os.path.join(path, item), depth=depth+1, depthLimit=depthLimit, outputFile=outputFile, verbose=verbose )
            
            # If we are not searching recursively
            else:
                # Output the directory
                print("File: " + os.path.join(path, item))
                if(outputFile):
                    outputFile.write(" "*depth + os.path.join(path, item) + "\n")
                elif(verbose):
                    print(" "*depth + os.path.join(path, item))
        
        # If the item is a file then output it by console or file.
        elif(os.path.isfile(os.path.join(path, item))):
            if(verbose):
                print(" "*(depth+1) + "~ " + item)

            elif(outputFile is not None):
                outputFile.write(" "*(depth+1) + "~ " + item + "\n")
            


"""
<summary> 
    Function to look for files with a specific extension in a directory and subdirectories. 
</summary>
<param name="path"> The path to the directory to search. </param>
<param name="depth"> The depth of the current directory. </param>
<param name="depthLimit"> The maximum depth to search. </param>
<param name="outputFileFile"> The file to output the results to. </param>
<param name="verbose"> Whether or not to print the results to the console. </param>
<param name="recursive"> Whether or not to search subdirectories. </param>
<param name="results"> The list to append the results to. (Made a param due to functions recursive nature) </param>
<returns> 
    If count=False: The list of files with the specified extension.
    If count=True: The number of files with the specified extension. 
</returns>
"""
def fileSearcher(path, depth=0, depthLimit=None, file=None, extension=None, recursive=True, count=False, results=[]):
    
    dir_list = os.listdir(path)
    for item in dir_list:
        
        if(os.path.isfile(os.path.join(path, item))):
            # If the current file is the file we are looking for
            # then return it.
            if(item == file):
                return os.path.join(path, item)
            
            # If we have set an extension to search for and the file has the extension
            # then append to results
            elif(extension is not None and item.endswith(extension)):
                    results.append(os.path.join(path, item))

        elif(os.path.isdir(os.path.join(path, item))):
            # Check if we have met our limits for depth or even if we are searching recursively
            if(recursive==True and depthLimit is None or depth < depthLimit ):
                    
                    # If we are searching recursively, recurse into the directory
                    results = fileSearcher(path=os.path.join(path, item), depth=depth+1, depthLimit=depthLimit, extension=extension, recursive=recursive, results=results)
    
    # Return the results
    if(count):
        print(count)
        return len(results)
    else:
        return results

"""
<summary> 
    Controller function to detirmine to walk, search, or both. 
</summary>
<param name="path"> The path to the directory to search. </param>
<param name="depthLimit"> The maximum depth to search. </param>
<param name="file"> The file to search for. </param>
<param name="extension"> The extension to search for. </param>
<param name="recursive"> Whether or not to search subdirectories. </param>
<param name="verbose"> Whether or not to print the results to the console. </param>
<param name="outputFile"> The file to output the results to. </param>
<param name="count"> Whether or not to count the results. </param>
<param name="time"> Whether or not to time the search. </param>
<returns> Nothing. </returns>
"""
def fileUtility(path, depthLimit=None, extension=None, recursive=True, search=False, walk=False, time=False, count=False, outputFile=None, verbose=True, file=None):
    # Create a file if we are using it.
    if(outputFile is not None):
        outputFile = open(outputFile, "w+")
    
    # Start the timer if we are timing.
    if(time):
        timer = Timer()
        timer.start()
    
    # If we are searching for a file or files with a specific extension
    if(search):

        results = fileSearcher(path=path, depthLimit=depthLimit, extension=extension, recursive=recursive, count=count, file=file)

        # If we are counting the number of files with the specified extension
        if(count):

            # Output the number of files with the specified extension
            if(verbose):
                if(extension is not None):
                    print(str(results) + " files found in " + path + " with extension " + extension)
                
            elif(outputFile):
                outputFile.write(str(results) + " files found in " + path + " with extension " + extension + "\n")
        
        # If we are not counting the number of files with the specified extension
        # then just output the files with the specified extension or the file we are looking for.
        else:
            if(verbose):
                if(file is None):
                    for file in results:
                        print(file)
            
                # Output the file we were looking for if we found it.
                elif(file is not None and results is not None):
                    print(results)
            
            elif(outputFile):
                if(file is None):
                    for file in results:
                        outputFile.write(file + "\n")
            
                else:
                    outputFile.write(file + "\n")

    # Walk through directory
    # fileWalker will internally output the result I did this
    # for ease of use. The fileSearcher function is different
    # in case I need to do something different with the results
    # besides outputting them.
    elif(walk):
        results = fileWalker(path=path, depthLimit=depthLimit, outputFile=outputFile, verbose=verbose, recursive=recursive)
    
    # Output the time taken
    if(time):
        timer.stop()
        if(verbose):
            print(str(timer))
        elif(outputFile):
            outputFile.write(str(timer) + "\n")
    
    # Close the file if we are using it.
    if(outputFile is not None):
        outputFile.close()

    