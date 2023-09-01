import time

class Tape(object):

    blank_symbol = " "

    def __init__(self,
                 tape_string = ""):
        self.__tape = dict((enumerate(tape_string)))
    
    def __str__(self):
        s = ""
        min_used_index = min(self.__tape.keys()) 
        max_used_index = max(self.__tape.keys())
        for i in range(min_used_index, max_used_index):
            s += self.__tape[i]
        return s    

    def __getitem__(self,index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return Tape.blank_symbol

    def __setitem__(self, pos, char):
        self.__tape[pos] = char 

class TuringMachine(object):
    
    def __init__(self, 
                 tape = "", 
                 blank_symbol = " ",
                 initial_state = "",
                 final_states = None,
                 transition_function = None):
        self.__tape = Tape(tape)
        self.__head_position = 0
        self.__blank_symbol = blank_symbol
        self.__current_state = initial_state
        if transition_function == None:
            self.__transition_function = {}
        else:
            self.__transition_function = transition_function
        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)
        
    def get_tape(self): 
        return str(self.__tape)
    
    def step(self):
        time.sleep(0.05)
        print(hesaplama.get_tape())
        char_under_head = self.__tape[self.__head_position]
        x = (self.__current_state, char_under_head)
        print(x[0])
        if x in self.__transition_function:
            y = self.__transition_function[x]
            self.__tape[self.__head_position] = y[1]
            if y[2] == "R":
                self.__head_position += 1
            elif y[2] == "L":
                self.__head_position -= 1
            self.__current_state = y[0]

    def final(self):
        if self.__current_state in self.__final_states:
            return True
        else:
            return False
        
initial_state = "s1",
accepting_states = ["s1","s2","s3","s4","s5","s6","s7","s8","s9","s10","s11","s12"
                    ,"s13","s14","s15","s16","s17","s18","s19","s20","s21"],
transition_function = {
    ("s1", "0"): ("s2", "0", "L"),
    ("s1", "1"): ("s2", "1", "L"),
    ("s2", " "): ("s3", "+", "R"),
    ("s3", "0"): ("s3", "0", "R"),
    ("s3", "1"): ("s3", "1", "R"),
    ("s3", "*"): ("s3", "*", "R"),
    ("s3", " "): ("s4", " ", "L"),
    ("s4", "0"): ("s6", " ", "L"),
    ("s4", "1"): ("s5", " ", "L"),
    ("s5", "0"): ("s5", "0", "L"),
    ("s5", "1"): ("s5", "1", "L"),
    ("s5", "*"): ("s12", "*", "L"),
    ("s6", "0"): ("s6", "0", "L"),
    ("s6", "1"): ("s6", "1", "L"),
    ("s6", "*"): ("s8", "0", "R"),
    ("s7", "0"): ("s7", "0", "R"),
    ("s7", "1"): ("s7", "1", "R"),
    ("s7", "+"): ("s7", "+", "R"),
    ("s7", "*"): ("s8", "0", "R"),
    ("s8", "0"): ("s9", "*", "R"),
    ("s8", "1"): ("s10", "*", "R"),
    ("s8", " "): ("s11", " ", "L"),
    ("s9", "0"): ("s9", "0", "R"),
    ("s9", "1"): ("s10", "0", "R"),
    ("s9", " "): ("s3", "0", "R"),
    ("s10", "0"): ("s9", "1", "R"),
    ("s10", "1"): ("s10", "1", "R"),
    ("s10", " "): ("s3", "1", "R"),
    ("s11", "0"): ("s11", " ", "L"),
    ("s11", "1"): ("s11", " ", "L"),
    ("s11", "+"): ("s21", " ", "L"),
    ("s12", "0"): ("s13", "c", "L"),
    ("s12", "1"): ("s14", "c", "L"),
    ("s12", "+"): ("s20", "+", "L"),
    ("s13", "0"): ("s13", "0", "L"),
    ("s13", "1"): ("s13", "1", "L"),
    ("s13", "+"): ("s15", "+", "L"),
    ("s14", "0"): ("s14", "0", "L"),
    ("s14", "1"): ("s14", "1", "L"),
    ("s14", "+"): ("s16", "+", "L"),
    ("s15", "0"): ("s18", "O", "R"),
    ("s15", " "): ("s18", "O", "R"),
    ("s15", "1"): ("s18", "I", "R"),
    ("s15", "O"): ("s15", "O", "L"),
    ("s15", "I"): ("s15", "I", "L"),
    ("s16", "0"): ("s19", "I", "R"),
    ("s16", " "): ("s19", "I", "R"),
    ("s16", "1"): ("s17", "O", "L"),
    ("s16", "O"): ("s16", "O", "L"),
    ("s16", "I"): ("s16", "I", "L"),
    ("s17", "0"): ("s19", "1", "R"),
    ("s17", " "): ("s19", "1", "R"),
    ("s17", "1"): ("s17", "0", "L"),
    ("s18", "0"): ("s18", "0", "R"),
    ("s18", "I"): ("s18", "I", "R"),
    ("s18", "1"): ("s18", "1", "R"),
    ("s18", "O"): ("s18", "O", "R"),
    ("s18", "+"): ("s18", "+", "R"),
    ("s18", "c"): ("s12", "0", "L"),
    ("s19", "0"): ("s19", "0", "R"),
    ("s19", "I"): ("s19", "I", "R"),
    ("s19", "1"): ("s19", "1", "R"),
    ("s19", "O"): ("s19", "O", "R"),
    ("s19", "+"): ("s19", "+", "R"),
    ("s19", "c"): ("s12", "1", "L"),
    ("s20", "O"): ("s20", "0", "L"),
    ("s20", "I"): ("s20", "1", "L"),
    ("s20", "0"): ("s20", "0", "L"),
    ("s20", "1"): ("s20", "1", "L"),
    ("s20", " "): ("s7", " ", "R")
}
final_states = {"s21"}

int_sayi = input("Karesini almak istediginiz sayiyi binary olarak yaziniz: ")

hesaplama = TuringMachine(str(int_sayi) + "*" + str(int_sayi) + " ", 
                  initial_state = "s1",
                  final_states = final_states,
                  transition_function=transition_function)

while not hesaplama.final():
    hesaplama.step()

print("Girilen sayinin karesi:")
print(hesaplama.get_tape())