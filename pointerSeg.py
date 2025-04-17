
def getPushD():
    # Placeholder implementation for getPushD
    return "@SP, A=M, M=D, @SP, M=M+1,"

def getPopD():
    return "@SP, M=M-1, A=M, D=M,"

def pointerSeg(pushpop, seg, index):
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
            f"@{index}, D=A, @{base_addr}, A=M, A=A+D, D+M" + getPushD()
        )
    elif pushpop == 'pop':
        #load base address, add index, pop value
        #need to store in a temp so var R15 so redo
        return (
            f"@{index}, D=A, @R15, M=D, @(base_addr), D=M, @R15, M=M+D" + getPopD() + "@R15, A=M, M=D"
        )
    else:
        raise ValueError("invalid push or pop try again")
    