rm -rf dist
pipreqs --no-pin --force && echo sphinxcontrib_napoleon >> requirements.txt && echo sphinx_rtd_theme >> requirements.txt && echo m2r2 >> requirements.txt
./docs/generate_docs.sh
python3 -m build
twine upload dist/*
