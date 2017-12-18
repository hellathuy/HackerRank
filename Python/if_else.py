if __name__ == '__main__':
    n = int(raw_input())
    check = n%2
       
    if check != 0:
        print "Weird"
    elif check == 0 and (2 <= n <= 5):
        print "Not Weird"
    elif check == 0 and (6 <= n <= 20):
        print "Weird"
    elif check == 0 and (n > 20):
        print "Not Weird"
