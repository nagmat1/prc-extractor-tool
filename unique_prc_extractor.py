# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    count = 0;
    my_list=[]
    print('PyCharm')
    file1 = open("vc707.log",'r')
    Lines = file1.readlines()
    for line in Lines :
        if "prc " in line:
            count +=1;
            taze = line.index("prc ");
            prc = line[taze+4:taze+20];
            #print(prc)
            if prc not in my_list :
                my_list.append(prc)
    print(my_list)
    print("Prc_sany",len(my_list))
    print("count=",count);


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
