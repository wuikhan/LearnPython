def main():
    f = open("txtfile.txt","w+")
    
    for i in range(10):
        f.write("This is line %d\r\n" % (i+1))
        
    f.close()

if __name__ == "__main__":
    main()