// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.
@i
M=0
@sum
M=0

(LOOP)
@i
D=M
@R1
D=D-A

// r1の数だけ繰り返したら終了
@END
D;JGE

// M[R0]の内容をDレジスタに格納
@R0
D=M
// M[sum]にこれまでのM[sum]の数値にM[R0]の数値を足す
@sum
M=D+M

// M[i]に1加算する
@i
M=M+1

@LOOP
0;JMP

(END)
@END
0;JMP