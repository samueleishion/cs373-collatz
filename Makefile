run: RunCollatz.py RunCollatz.in
	python3 RunCollatz.py < RunCollatz.in > RunCollatz.out 
	diff RunCollatz.sample.out RunCollatz.out 

test: TestCollatz.py 
	python3 TestCollatz.py 

sphere: SphereCollatz.py 
	python3 SphereCollatz.py < RunCollatz.in 

clean: 
	rm *.pyc *~