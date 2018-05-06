for i in $(seq 1 10); do
	echo "SIMULATION TEST LINK TYPES: $i"
	make clean
	make clean_files
	python generate_model.py -va 11 -tp 10 -tl $i -vl 10 -t link_types
	make all
done
