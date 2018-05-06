for i in $(seq 1 150); do
	echo "SIMULATION TEST PORTS: $i OUTPUT PORTS AND $i INPUT PORTS"
	make clean
	make clean_files
	python generate_model.py -va 1 -tp $i
	make all
done
