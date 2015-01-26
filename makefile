UNAME := $(shell uname)
cc = python3
cov = coverage3

ifeq ($(UNAME), Darwin)
	cov = coverage
endif

$(info $$cov is [${cov}])

all:

Collatz.html: Collatz.py
	pydoc3 -w Collatz

Collatz.log:
	git log > Collatz.log

RunCollatz.out: RunCollatz.py RunCollatz.in
	python3 RunCollatz.py < RunCollatz.in > RunCollatz.out

RunCollatz.tmp: RunCollatz.py RunCollatz.in
	python3 RunCollatz.py < RunCollatz.in > RunCollatz.tmp
	diff RunCollatz.tmp RunCollatz.out

TestCollatz.out: TestCollatz.py
	$(cov) run    --branch TestCollatz.py >  TestCollatz.out 2>&1
	$(cov) report -m                      >> TestCollatz.out

clean:
	rm -f .coverage
	rm -f *.pyc
	rm -f RunCollatz.tmp
	rm -f TestCollatz.out
	rm -rf __pycache__
