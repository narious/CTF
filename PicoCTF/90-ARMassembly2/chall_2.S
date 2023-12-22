	.arch armv8-a
	.file	"chall_2.c"
	.text
	.align	2
	.global	func1
	.type	func1, %function
func1:
	sub	sp, sp, #32 
	str	w0, [sp, 12]
	str	wzr, [sp, 24] ; wzr = write zero register
	str	wzr, [sp, 28]
	b	.L2
.L3: ; This part forms a loop 
	ldr	w0, [sp, 24]
	add	w0, w0, 3
	str	w0, [sp, 24]
	ldr	w0, [sp, 28]
	add	w0, w0, 1
	str	w0, [sp, 28]
.L2:
	ldr	w1, [sp, 28]
	ldr	w0, [sp, 12]
	cmp	w1, w0
	bcc	.L3 ; branch conditional code BEQ (zero flag set)
	ldr	w0, [sp, 24]
	add	sp, sp, 32
	ret
	.size	func1, .-func1
	.section	.rodata
	.align	3
.LC0:
	.string	"Result: %ld\n"
	.text
	.align	2
	.global	main
	.type	main, %function
main: 
	; arg = 3297082261
	stp	x29, x30, [sp, -48]! ; Store pair x29 (frame pointer) x30 link pointer and !
 			 	     ; means to update the sp after. 48-41 is x29 40-33 is x30  
	add	x29, sp, 0 ; zeroes x29 is now stack pointer
	str	w0, [x29, 28] ; stores 4 bytes in 32-28 is w0 (w0 is an arg)
	str	x1, [x29, 16] ; stores 8 bytes at 29-16
	ldr	x0, [x29, 16] ; loads x1  into x0
	add	x0, x0, 8 ; adds 8
	ldr	x0, [x0] ; dereference x0
	bl	atoi ; convert x0 to integer (if it was a string)
	bl	func1
	str	w0, [x29, 44]
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	ldr	w1, [x29, 44]
	bl	printf
	nop
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits