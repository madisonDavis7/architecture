
import os
import sys
# run with: python project7.py <fileName.vm> > <fileName.asm>

# The following dictionaries are used to translate VM language commands to machine
# This contains the binary operations add, sub, and, or as values. The keys are the

# Assume a getPopD() has been called prior to this lookup.
ARITH_BINARY = {
    'sub': '@SP, A=M-1, M=M-D',
    'add': '@SP, A=M-1, M=D+M',
    'and': '@SP, A=M-1, M=D&M',
    'or': '@SP, A=M-1, M=D|M',

}
# As above, but now the keys are unary operations neg, not
# Values are sequences of Hack ML code, seperated by commas.
# In this case do not assume a getPopD() has been called prior to the lookup
ARITH_UNARY = {
    'neg': '@SP, A=M-1, M=-M',
    'not': '@SP, A=M-1, M=!M',

}
# Now, the code for operations gt, lt, eq as values.
# These are assumed to be preceded by getPopD()
# The ML code corresponds very nicely to the jump conditions in
# Hack assembly
ARITH_TEST = {
    'lt': 'D;JLT',
    'gt': 'D;JGT',
    'eq': 'D;JEQ',
}
# Boring, but needed - translate the long VM names argument, local, this, that
# to the shorthand forms of these found in symbol table used for Hack assembly
SEGLABEL = {
    'argument': 'ARG',
    'local': 'LCL',
    'this': 'THIS',
    'that': 'THAT',
}

# This will be used to generate unique labels when they are needed.
LABEL_NUMBER = 0

def pointerSeg(pushpop,seg,index):
    '''
    This function returns Hack ML code to push a memory location to
    to the stack, or pop the stack to a memory location.
    INPUTS:
    pushpop = a text string 'pop' means pop to memory location, 'push'
    is push memory location onto stack
    seg = the name of the segment that will be be the base address
    in the form of a text string
    index = an integer that specifies the offset from the base
    address specified by seg
    RETURN:
    The memory address is speficied by segment's pointer (SEGLABEL[seg]) +
    index (index))
    if pushpop is 'push', push the address contents to the stack
    if pushpop is 'pop' then pop the stack to the memory address.
    The string returned accomplishes this. ML commands are seperated by commas
    (,).
    This function will only be called if the seg is one of:
    "local", "argument", "this", "that"
    '''
        #define base pointers
    segments = {
        'local': 'LCL',
        'argument': 'ARG',
        'this': 'THIS',
        'that': 'THAT',
    }

    if seg not in segments:
        raise ValueError("invaid try again :( ")
    
    base_addr = segments[seg]

    if pushpop == 'push':
        #load base address, add index, push value
        return (
            f"@{index}, D=A, @{base_addr}, A=M, A=D+A, D=M," + getPushD() + "\n"
        )
    elif pushpop == 'pop':
        #load base address, add index, pop value
        #need to store in a temp so var R15 so redo
        return (
            f"@{index}, D=A, @{base_addr}, D=D+M, @R15, M=D, " + getPopD() + "@R15, A=M, M=D\n"
        )
    else:
        raise ValueError("invalid push or pop try again")
    

def fixedSeg(pushpop,seg,index):
    #For pointer and temp segments
    #temp is 5-12
    #pointer 0 --> this(3)
    #pointer 1 --> that(4)
    if (seg != "temp" and seg != "pointer"):
        raise ValueError("invalid try again :(")
    
    elif seg == "temp":
        addr = 5 + int(index) #base addr is 5 
    elif seg == "pointer":
        addr = 3 + int(index)

    #pushpop nonsense
    if (pushpop != "push" and pushpop != "pop"):
        raise ValueError("Not push or pop sadly")
    elif pushpop == "push":
        return f"@{addr}, D=M, " + getPushD() + "\n"
    elif pushpop == "pop":
        return getPopD() + f"@{addr}, M=D\n"


def constantSeg(pushpop,seg,index):
    #This will do constant and static segments
    #for constant load to D then push
    #for static...
    if seg == "constant":
        if pushpop == "push":
            #explainn
            return f"@{index}, D=A, " + getPushD()
        elif pushpop == "pop":
            raise ValueError("popping not allowed try again")
        else:
            raise ValueError("Not valid :(")
        
    #static stuff
    elif seg == "static":
        #i dont know 
        variable = f"Static.{index}"
        if pushpop == 'push':
            return f"@{variable}, D=M, " + getPushD()
        elif pushpop == 'pop':
            return getPopD() + f", @{variable}, M=D"
    else:
        raise ValueError("Not constant or seg so try again")
        
#project 8 methods
def getIf_goto(label):
    """
    Returns Hack ML to goto the label specified as
    an input arguement if the top entry of the stack is
    true.
    """
    #pop and check if true
    

def getGoto(label):
    """
    Return Hack ML string that will unconditionally 
    jumpt to the input label.
    """
    return f"{label}, 0;JMP" + "\n"

def getLabel(label):
    """
    Returns Hack ML for a label, eg (label)
    """
    #using uniqueLabel()
    label = uniqueLabel()
    return f"{label}" + "\n"

def getCall(function,nargs):
    """
    This function returns the Hack ML code to 
    invoke the `call function nargs` type command in 
    the Hack virtual machine (VM) language.

    In order for this to work, review slides
    46-58 in the Project 8 presentation available 
    on the nand2tetris.org website.
    """

def getFunction(function,nlocal):
    """
    Return the Hack ML code to represent a function which sets a label
    and initializes local variables to zero.
    See slides 59-63 in the nand2tetris book.
    """

def getReturn():
    """
    Returns Hack ML code to perform a return, one
    of the more complex operations in this unit.
    The code restores all the memory segments to the
    calling function. It also has to restore the 
    instruction pointer (IP) and reset the stack 
    pointer. See slides 64-76 of nand2tetris.org
    project 8.

    """

# More jank, this time to define the function pointers for flow control.
PROG_FLOW  = {'if-goto':getIf_goto,'goto':getGoto,'label':getLabel,'call':getCall,'function':getFunction,'return':getReturn}

def _getPushMem(src):
    """
    Helper function to push memory to location src to stack
    """
    #load address, push value to stack
    #D=M because you dont need the RAM you want what is in the memory location
    #src could be local, argument...
    return f"@{src}, D=M, " + getPushD() + "\n"
    

def _getPushLabel(src):
    """
    Helper function to push the ROM address of a label to the
    stack.
    """
    #load address, push value to stack, use A because label in ROM
    #label so use ROM
    return f"@{src}, D=A, " + getPushD() + "\n"

   

def _getPopMem(dest):
    """
    Helper function to pop the stack to the memory address dest.
    """
    #pop value to D, store in dest
    return getPopD() + f"@{dest}, M=D\n"
  

def _getMoveMem(src,dest):
    """
    Helper function to move the contents of src to memory location dest.
    """
    #load src, store in dest
    #acccess src, move to D, access dest, store in M
    #after the dest is overwritten 
    return f"@{src}, D=M, @{dest}, M=D\n"


  
def line2Command(line):
    """ This just returns a cleaned up line, removing unneeded spaces and comments"""
    line = line.strip()
    if "//" in line:
        line = line[:line.index("//")] #takes from beginning up to comment sign
    return line.strip()

def uniqueLabel():
    #Uses LABEL_NUMBER to generate and return a unique label
    #for conditional stuff
    global LABEL_NUMBER #increment every time to go through file right
    LABEL_NUMBER += 1
    return f"LABEL_{LABEL_NUMBER}"

def getPushD():
# This method takes no arguments and returns a string with assembly language
# that will push the contents of the D register to the stack.
    return "@SP, A=M, M=D, @SP, M=M+1\n"

def getPopD():
# This method takes no arguments and returns a string with assembly language
# that will pop the stack to the D register.
# SIDE EFFECT: The A register contains the SP.
    return "@SP, M=M-1, A=M, D=M\n"

# Here are the segments, put in functions to make life easier maybe (put below stuffs)
#value is function 
SEGMENTS = {
    'local': pointerSeg,
    'argument': pointerSeg,
    'this': pointerSeg,
    'that': pointerSeg, 
    'pointer': fixedSeg,
    'temp': fixedSeg,
    'constant': constantSeg, #work in progresss
    'static': constantSeg

}
def ParseFile(file):
    outString = "" #initialize to store hack code
    for line in file:
        command = line2Command(line) #clean file
        if not command:
            continue
        args = [x.strip() for x in command.split()] # Break command into list of arguments, no return characters

        if args[0] in ARITH_BINARY.keys():
            """
            Code that will deal with any of the binary operations (add, sub,
            and, or)
            do so by doing the things all have in common, then do what is
            specific
            to each by pulling a key from the appropriate dictionary.
            Remember, it's always about putting together strings of Hack ML
            code.
            """
            #pop from stack then do operation
            #pop into D, move to second, do M = M+D, store, dec SP
            #@SP AM=M-1 D=M A=A-1 M=M+D
            outString += getPopD()
            outString += ARITH_BINARY[args[0]] + '\n'

        elif args[0] in ARITH_UNARY.keys():
            """
            As above, but now for the unary operators (neg, not)
            """
            #top of stack
            outString += ARITH_UNARY[args[0]] + '\n'

        elif args[0] in ARITH_TEST.keys():
            """
            Deals with the three simple operators (lt,gt,eq), but likely the
            hardest
            section because you'll have to write assembly to jump to a
            different part
            of the code, depending on the result.
            To define where to jump to, use the uniqueLabel() function to get
            labels.
            The result should be true (-1) (0xFFFF) or false (0) (0x0000) depending on
            the test.
            That goes back onto 5?
            """
            #pop top two from stack (y-x)
            outString += getPopD() #puts top in D so now y is on top
            outString += "@SP, M=M-1, A=M, D=M-D\n" #dec SP to point to y, load y into M, D=y-x

            #create labels 
            labelTrue = uniqueLabel() #for comparison true
            labelEnd = uniqueLabel()

            #jump if true/ 
            outString += f"@{labelTrue}, {ARITH_TEST[args[0]]}\n"

            #if no jump then store false and increment SP
            outString += "@SP, A=M, M=0, @SP, M=M+1\n"

            #jump to end unconditionally
            outString += f"@{labelEnd}, 0;JMP\n"

            #if true push value (-1) onto stack
            outString += f"({labelTrue})\n"
            outString += "@SP, A=M, M=-1, @SP, M=M+1\n"

            #end
            outString += f"({labelEnd})\n"

            
            #add a check for first arg
        elif args[0] in ('push', 'pop') and args[1] in SEGMENTS.keys():
            """
            Here we deal with code that's like push/pop segment index.
            You've written the functions, the code in here selects the right
            function by picking a function handle from a dictionary.
            """
            #memory access commands push/pop segment index so 1 is segment 
            segment = args[1]
            index = args[2]
            function = SEGMENTS[segment] #gets correct function 
            outString += function(args[0], segment, index) + '\n'
            #outString += function(args[0], args[1], args[2]) + '\n'

        else:
            print("Unknown command!")
            print(args)
            sys.exit(-1)

    l = uniqueLabel()
    outString += '(%s)'%(l)+',@%s,0;JMP'%l # Final endless loop
    return outString.replace(" ","").replace(',','\n')



filename = sys.argv[1].strip()

#see if it exists
if not os.path.isfile(filename):
    print(f"Error: File '{filename}' does not exist. :(")
    sys.exit(1)

try:
    with open(filename, 'r') as file:
        print(ParseFile(file))
except Exception as e:
    print(f"Failed to open or process the file how tragic: {e}")
    sys.exit(1)