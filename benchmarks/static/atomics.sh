for i in $(seq 1 1 50); do
	echo "SIMULATION TEST ATOMICS WITH: $i ATOMICS"
	make clean
	make clean_files
	python generate_model.py -va $i -tp 1
	make all
done
