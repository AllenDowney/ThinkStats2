# the versions in code are canonical
cp ../code/thinkstats2.py .
cp ../code/thinkplot.py .

# pip install pytest nbmake
pytest --nbmake chap*.ipynb

# push the changes
#git add chap*.ipynb
#git commit -m "Updating solutions"
#git push
