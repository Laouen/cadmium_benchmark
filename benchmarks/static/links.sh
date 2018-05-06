for i in $(seq 1 1 10); do
	echo "SIMULATION TEST LINKS WITH: $i LINKS"
	make clean
	make clean_files
	python generate_model.py -va 11 -tp 1 -vl $i -t 'link_amount'
	make all
done
