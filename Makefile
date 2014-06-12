run: RunCollatz.py RunCollatz.in
	python RunCollatz.py < RunCollatz.in > RunCollatz.out 

test: TestCollatz.py 
	python TestCollatz.py

clean: 
	rm *.pyc *~