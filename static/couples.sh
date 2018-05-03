for i in $(seq 0 500 10000); do
	echo "SIMULATION TEST COUPLED WITH: $i COUPLES"
	make clean
	make clean_files
	python generate_model.py -vc $i -tp 1
	make all
done
