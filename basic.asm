@10
D=A
@SP
A=M
M=D
@SP
M=M+1

@0
D=A
@LCL
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

@21
D=A
@SP
A=M
M=D
@SP
M=M+1

@22
D=A
@SP
A=M
M=D
@SP
M=M+1

@2
D=A
@ARG
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

@1
D=A
@ARG
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

@36
D=A
@SP
A=M
M=D
@SP
M=M+1

@6
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

@42
D=A
@SP
A=M
M=D
@SP
M=M+1

@45
D=A
@SP
A=M
M=D
@SP
M=M+1

@5
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

@2
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

@510
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
@11
M=D

@0
D=A
@LCL
A=M
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1


@5
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
@1
D=A
@ARG
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
@THIS
A=M
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1


@6
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
M=D+M
@SP
M=M-1
A=M
D=M
@SP
A=M-1
M=M-D
@11
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
