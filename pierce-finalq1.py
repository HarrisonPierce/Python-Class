#Harrison Pierce
#Final exam q1

#This program lets the user enter a string and figures out which
#character is displayed the most and shows the user this character

def main():
	#accept input from user for a string
	userstring = input("Enter a string: ")
	a=0	#set variable for each character to 0
	b=0
	c=0
	d=0
	e=0
	f=0
	g=0
	h=0
	i=0
	j=0
	k=0
	l=0
	m=0
	n=0
	o=0
	p=0
	q=0
	r=0
	s=0
	t=0
	u=0
	v=0
	w=0
	x=0
	y=0
	z=0

#add 1 to each variable for each character in the userstring according to its characterization
	for ch in userstring:
		if ch == "a":
			a += 1
		if ch == "b":
			b += 1
		if ch == "c":
			c += 1
		if ch == "d":
			d += 1
		if ch == "e":
			e += 1
		if ch == "f":
			f += 1
		if ch == "g":
			g += 1
		if ch == "h":
			h += 1
		if ch == "i":
			i += 1
		if ch == "j":
			j += 1
		if ch == "k":
			k += 1
		if ch == "l":
			l += 1
		if ch == "m":
			m += 1
		if ch == "n":
			n += 1
		if ch == "o":
			o += 1
		if ch == "p":
			p += 1
		if ch == "q":
			q += 1
		if ch == "r":
			r += 1
		if ch == "s":
			s += 1
		if ch == "t":
			t += 1
		if ch == "u":
			u += 1
		if ch == "v":
			v += 1
		if ch == "w":
			w += 1
		if ch == "x":
			x += 1
		if ch == "y":
			y += 1
		if ch == "z":
			z += 1

	print(max(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z))
 	#prints the number of characters appearing the most in the user input
main()