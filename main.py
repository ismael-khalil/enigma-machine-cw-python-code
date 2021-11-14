count = 0           # global variable for counting the number of rotations the first rotor perform and it start with zero.


#create a class to work on the rotors
class Rotors:
    #these are the lists for each rotor and the reflector containig upper and lower case letters + numbers
    #they are inside the constructor so they can be shared with the other functions/methods inside the class
    def __init__(self):
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4',
                         '5', '6', '7', '8', '9']
        self.rotor1list = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U',
                           'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J', 'e', 'k', 'm', 'f', 'l', 'g', 'd', 'q', 'v', 'z',
                           'n', 't', 'o', 'w', 'y', 'h', 'x', 'u', 's', 'p', 'a', 'i', 'b', 'r', 'c', 'j', '5', '3',
                           '8', '2', '9', '1', '0', '4', '7', '6']
        self.rotor2list = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G',
                           'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E', 'a', 'j', 'd', 'k', 's', 'i', 'r', 'u', 'x', 'b',
                           'l', 'h', 'w', 't', 'm', 'c', 'q', 'g', 'z', 'n', 'p', 'y', 'f', 'v', 'o', 'e', '4', '6',
                           '9', '5', '7', '0', '8', '1', '3', '2']
        self.rotor3list = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W',
                           'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O', 'b', 'd', 'f', 'h', 'j', 'l', 'c', 'p', 'r', 't',
                           'x', 'v', 'z', 'n', 'y', 'e', 'i', 'w', 'g', 'a', 'k', 'm', 'u', 's', 'q', 'o',  '2', '5',
                           '0', '8', '6', '7', '1', '3', '4', '9']
        self.a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
                  'h', 'i', 'j', 'k', 'l', 'm', '0', '1', '2', '3', '4']

        self.b = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z', '5', '6', '7', '8', '9']

    #this function is for setting each rotor starting
    #it uses the slicing techniques which is slicing the list in parts then joining them later according to the number of rotations
    def rotor_num(self, rotate_list_one, rotate_list_two, rotate_list_three):
        self.rotor1list = self.rotor1list[rotate_list_one:] + self.rotor1list[:rotate_list_one]
        self.rotor2list = self.rotor2list[rotate_list_two:] + self.rotor2list[:rotate_list_two]
        self.rotor3list = self.rotor3list[rotate_list_three:] + self.rotor3list[:rotate_list_three]

    def reflectortest(self, r_n):            #function for getting the firts value of rotor 3(rotor3_1)
        for i in range(len(self.a)):         #then looping around the 2 lists of reflector to match each letter
            if r_n == self.a[i]:             #with its corresponding one and return the value taken by rotor3 again(rotor3_2)
                return self.b[i]
            elif r_n == self.b[i]:
                return self.a[i]

    def rotor1_1(self, letter): # getting rotor 1 first value by looping the alphabet and matching it with the same letter index from rotor 1 list and return the letter in the index
        global count
        self.rotor1list = self.rotor1list[1:] + self.rotor1list[:1]  # auto rotate 1 try each time a letter is shifted using the same slicing techniques
        count += 1                     #adding one to count every time the rotor rotate
        for i in range(len(self.alphabet)):
            if self.alphabet[i] == letter:
                return self.rotor1list[i]


    # function for getting rotor 2 first value by looping the alphabet and matching it with the same letter index from rotor 2 list and return the letter in the index
    def rotor2_1(self, letter):
        global count                #calling the global variable
        if count % 62 == 0:     # the modulus will return reminder of count divided by 62 so the reminder will be 0 for 62 and its multiples
            self.rotor2list = self.rotor2list[1:] + self.rotor2list[:1]   #so the (if) function will check if value is ==0 and every time the answer is zero it will shift one time
            for i in range(len(self.alphabet)):
                if self.alphabet[i] == letter:
                    return self.rotor2list[i]
        else:                                                   #in the other cases the function will not affect the rotor rotation
            for i in range(len(self.alphabet)):
                if self.alphabet[i] == letter:
                    return self.rotor2list[i]

    def rotor3_1(self, letter):    # getting rotor 3 first value by looping the alphabet and matching it with the same letter index from rotor 3 list and return the one in the index
        global count
        if count % 3844 == 0:  # the modulus will return reminder of count divided by 62 so the reminder will be 0 for 3844 and its multiple then it will performe as the previous function
            self.rotor3list = self.rotor3list[1:] + self.rotor3list[:1]
            for i in range(len(self.alphabet)):
                if self.alphabet[i] == letter:
                    return self.rotor3list[i]
        else:
            for i in range(len(self.alphabet)):
                if self.alphabet[i] == letter:
                    return self.rotor3list[i]

    def rotor3_2(self, letter): # getting the value returned by reflector and loop around rotor 3 list to match the letter index and return the letter in this index which is the second letter for rotor 3 (rotor3_2)
        for i in range(len(self.rotor3list)):
            if self.rotor3list[i] == letter:
                return self.alphabet[i]

    def rotor2_2(self, letter):  # getting rotor 2 second(rotor2_2) value by looping rotor 2 list and matching it with the same letter index from alphabet list and return the one in the index
        for i in range(len(self.rotor2list)):
            if self.rotor2list[i] == letter:
                return self.alphabet[i]

    def rotor1_2(self, letter): # getting rotor 1 second(rotor1_2) value by looping rotor 1 list and matching it with the same letter index from alphabet list and return the one in the index
        for i in range(len(self.rotor1list)):
            if self.rotor1list[i] == letter:
                return self.alphabet[i]


while True:
    try:
        input_rotate_rotor_one = int(input("Set rotor one to : "))          #integrs input fot first rotor starting setting assigned to a variable
        assert 0 <= input_rotate_rotor_one <= 62
    except ValueError:
        print('Invalid entry !, please entre numbers only')
    except AssertionError:
        print('Invalid entry!, choose from 0 to 62')
    else:
        break
while True:
    try:
        input_rotate_rotor_two = int(input("Set rotor two to : "))           #integrs input second rotor starting setting assigned to a variable
        assert 0 <= input_rotate_rotor_two <= 62
    except ValueError:
        print('Invalid entry !, please entre numbers only')
    except AssertionError:
        print('Invalid entry!, choose from 0 to 62')
    else:
        break
while True:
    try:
        input_rotate_rotor_three = int(input("Set rotor three to : "))  # integrs input third rotor starting setting assigned to a variable
        assert 0 <= input_rotate_rotor_three <= 62
    except ValueError:
        print('Invalid entry !, please entre numbers only')
    except AssertionError:
        print('Invalid entry!, choose from 0 to 62')
    else:
        break

encripted = ""        #variable
x = Rotors()
x.rotor_num(input_rotate_rotor_one, input_rotate_rotor_two, input_rotate_rotor_three)      # calling function rotor_num inside class Rotors which is now called x and to this function passed the inputs for setting the start of the rotor. The inputs are passed using their variable names.


input_from_user_Message = input("what is the MESSAGE  ")            #input the message for encryption or decryption assigned to a variable with the




for q in input_from_user_Message: # FOR LOOP that loop around the message and takes evey letter
    if q == " ":
        encripted = encripted + " "                # If the program finds a space breaks out the loop and appends a space
    elif q not in x.alphabet:
        print("sorry I did not understand" + " " + q + " " + "I will Pass a space)")
        encripted = encripted + " "
    else:
        rotor1_1_output = x.rotor1_1(q)                              #calling the functions inside the class and in the same time assigning them to variables
        rotor2_1_output = x.rotor2_1(rotor1_1_output)
        rotor3_1_output = x.rotor3_1(rotor2_1_output)
        reflector_output = x.reflectortest(rotor3_1_output)
        rotor3_2_output = x.rotor3_2(reflector_output)
        rotor2_2_output = x.rotor2_2(rotor3_2_output)
        rotor1_2_output = x.rotor1_2(rotor2_2_output)
        encripted = str(encripted) + str(rotor1_2_output)


print('the encrypted message: ' + encripted)
