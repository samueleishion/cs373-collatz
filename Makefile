run: RunCollatz.py RunCollatz.in
	python3 RunCollatz.py < RunCollatz.in > RunCollatz.out 
	diff RunCollatz.sample.out RunCollatz.out 

test: TestCollatz.py 
	python3 TestCollatz.py 

sphere: SphereCollatz.py 
	python3 SphereCollatz.py < RunCollatz.in 

check: RunCollatz.py ../collatz-tests/kevinwhe-RunCollatz.in ../collatz-tests/kevinwhe-RunCollatz.out 
	python3 RunCollatz.py < ../collatz-tests/kevinwhe-RunCollatz.in > test.out 
	diff ../collatz-tests/kevinwhe-RunCollatz.out test.out 
	rm test.out 

create: TestMaker.py 
	python3 TestMaker.py > samuelei-RunCollatz.in 
	python3 RunCollatz.py < samuelei-RunCollatz.in > samuelei-RunCollatz.out 

clean: 
	rm *.pyc *~
	rm -rf __pycache__ 