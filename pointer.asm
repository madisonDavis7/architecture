@3030
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
M=M-1
A=M
D=M
@3
M=D

@3040
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
M=M-1
A=M
D=M
@4
M=D

@32
D=A
@SP
A=M
M=D
@SP
M=M+1

@2
D=A
@THIS
D=D+M
@R15
M=D
@SP
M=M-1
A=M
D=M
@R15
A=M
M=D

@46
D=A
@SP
A=M
M=D
@SP
M=M+1

@6
D=A
@THAT
D=D+M
@R15
M=D
@SP
M=M-1
A=M
D=M
@R15
A=M
M=D

@3
D=M
@SP
A=M
M=D
@SP
M=M+1


@4
D=M
@SP
A=M
M=D
@SP
M=M+1


@SP
M=M-1
A=M
D=M
@SP
A=M-1
M=D+M
@2
D=A
@THIS
A=M
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1


@SP
M=M-1
A=M
D=M
@SP
A=M-1
M=M-D
@6
D=A
@THAT
A=M
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1


@SP
M=M-1
A=M
D=M
@SP
A=M-1
M=D+M
(LABEL_1)
@LABEL_1
0;JMP
