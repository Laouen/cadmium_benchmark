for i in $(seq 0 500 10000); do
	echo "SIMULATION TEST LINKS WITH: $i LINKS"
	make clean
	make clean_files
	python generate_model.py -va 10001 -tp 1 -vl $i -t 'link_amount'
	make all
done
