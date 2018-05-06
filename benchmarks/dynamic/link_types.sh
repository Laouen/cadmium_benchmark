for i in $(seq 1 150); do
	echo "SIMULATION TEST PORTS: $i OUTPUT PORTS AND $i INPUT PORTS"
	make clean
	make clean_files
	python generate_model.py -va 300 -tp 150 -tl $i -vl 150 -t link_types
	make all
done
