for i in $(seq 1 1 15); do
	echo "SIMULATION TEST COUPLED WITH: $i COUPLES"
	make clean
	make clean_files
	python generate_model.py -vc $i -tp 1
	make all
done
