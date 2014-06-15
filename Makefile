run: RunCollatz.py RunCollatz.in
	python3 RunCollatz.py < RunCollatz.in > RunCollatz.out 
	diff RunCollatz.sample.out RunCollatz.out 

test: TestCollatz.py 
	python3 TestCollatz.py

clean: 
	rm *.pyc *~