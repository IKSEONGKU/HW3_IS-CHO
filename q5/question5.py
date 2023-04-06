def reverse_words(str):
    list = str.split()
    list.reverse()   

    reversed_words = ""
    for i in range(len(list)):
        if i != len(list)-1:
            reversed_words += list[i] +" "
        else:
            reversed_words += list[i]
        
    return reversed_words


if __name__ == "__main__":
    str = input("Word Reversing Program, input the string : ")
    print("\nInput string : ",str)
    print("\nreversed string : ",reverse_words(str))
