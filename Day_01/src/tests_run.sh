echo "_________EX00: input data"
cat tests/data.txt
echo ""
echo "_________EX00: output of blockchain.py"
cat tests/data.txt | python3 blockchain.py 10
echo ""
echo "_________EX01: input"
echo "Have you delivered eggplant pizza at restored keep?"
echo "_________EX01: output of decypher.py"
python3 decypher.py "Have you delivered eggplant pizza at restored keep?"
echo ""
echo "_________EX02: input data"
cat tests/m.txt
echo ""
echo "_________EX02: output of mfinder.py"
cat tests/m.txt | python3 mfinder.py