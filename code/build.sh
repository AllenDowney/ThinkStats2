cp ../solutions/chap*soln.ipynb .
python remove_soln.py
rm chap*soln.ipynb

# pip install pytest nbmake
pytest --nbmake chap*ex.ipynb

# push the changes
#git add chap*ex.ipynb
#git commit -m "Updating example notebooks"
#git push
