#!/usr/bin/env bash

set -e

if [ -f "venv/bin/activate" ]; then
  source venv/bin/activate
else
  echo "Error on venv activation"
  exit 1
fi

generate_pdfs() {
  for dir in $(ls -d Laborator*/ 2>/dev/null | sort -V); do
    echo "========================================"
    echo " Processing $dir"
    echo "========================================"

    cd "$dir"

    for py_file in $(ls *.py 2>/dev/null | sort -V); do
      echo "Running: python $py_file inside $dir"
      python "$py_file"
    done

    cd ..
    echo ""
  done
  echo "All scripts executed successfully!"
}

generate_pdfs
