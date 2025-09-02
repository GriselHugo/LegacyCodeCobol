cobc -x src/main.cob src/operations.cob src/data.cob -o CobolAccountingSystem
mkdir -p build
mv CobolAccountingSystem build/
echo "Build done"
