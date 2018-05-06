for i in $(seq 1 50 1001); do
	echo "SIMULATION TEST ATOMIC TYPES WITH: $i DIFFERENT ATOMIC TYPES"
	make clean
	make clean_files
	python generate_model.py -va 1002 -ta $i -tp 1 -t atomic_types
	make all
done
