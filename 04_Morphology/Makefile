all: eus.gen.hfst

eus.lexc.hfst: eus.lexc
	hfst-lexc eus.lexc -o eus.lexc.hfst
eus.twol.hfst: eus.twol
	hfst-twolc eus.twol -o eus.twol.hfst
eus.gen.hfst: eus.lexc.hfst eus.twol.hfst
	hfst-compose-intersect -1 eus.lexc.hfst -2 eus.twol.hfst -o eus.gen.hfst
