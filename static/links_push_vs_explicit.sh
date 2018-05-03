for i in $(seq 10000 -500 0); do
	echo "SIMULATION TEST LINKS PUSH: $i LINKS"
	make clean
	make clean_files
	python generate_test_vlinks.py -vl $i
	make all
done

for i in $(seq 10000 -500 0); do
	echo "SIMULATION TEST LINKS EXPLICIT: $i LINKS"
	make clean
	make clean_files
	python generate_test_vlinks.py -vl $i -t explicit_definition
	make all
done