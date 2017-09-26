#Read and write files using the built-in Python files methods

def main():
    #open a file for writing and create it if it does not exist
    f = open("txtfile.txt","w+")
    
    #write some lines of data to the file
    for i in range(10):
        f.write("This is line %d\r\n" % (i+1))
        
    #close the file when done    
    f.close()

if __name__ == "__main__":
    main()