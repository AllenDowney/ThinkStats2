
all:	book.tex
	pdflatex book
	makeindex book.idx
	pdflatex book
	mv book.pdf thinkstats2.pdf
	evince thinkstats2.pdf

hevea:
	sed 's/\(figs\/[^.]*\).\(pdf\|png\)/\1.eps/' book.tex > thinkstats2.tex
	rm -rf html
	mkdir html
	hevea -O -e latexonly htmlonly thinkstats2
# the following greps are a kludge to prevent imagen from seeing
# the definitions in latexonly, and to avoid headers on the images
	grep -v latexonly thinkstats2.image.tex > a; mv a thinkstats2.image.tex
	sed s/\\\\usepackage{fancyhdr}// < thinkstats2.image.tex > a; mv a thinkstats2.image.tex
	imagen -png thinkstats2
	hacha thinkstats2.html
	cp up.png next.png back.png html
	mv index.html thinkstats2.css thinkstats2*.html thinkstats2*.png *motif.gif html

DEST = /home/downey/public_html/greent/thinkstats2

distrib:
	rm -rf dist
	mkdir dist
	rsync -a thinkstats2.pdf html dist
	# rsync -a figs/*.fig figs/*.eps dist/tex/figs
	rsync -a dist/* $(DEST)
	chmod -R o+r $(DEST)/*
	cd $(DEST)/..; sh back

plastex:
	# Before running plastex, we need the current directory in PYTHONPATH
	# export PYTHONPATH=$PYTHONPATH:.
	rm -rf /home/downey/thinkstats/trunk/book/.svn
	plastex --renderer=DocBook --theme=book --image-resolution=300 --filename=book.xml book.tex
	rm -rf /home/downey/thinkstats/trunk/book/.svn

xxe:
	xmlcopyeditor ~/thinkstats/trunk/ThinkStats2/book/book/book.xml &

lint:
	xmllint -noout book/book.xml

vector:
	plastex --renderer=DocBook --theme=book --vector-imager=dvisvgm --filename=book.xml book.tex

small: small.tex
	plastex --renderer=DocBook --theme=book --image-resolution=300 --filename=small.xml small.tex

sample:
	plastex --renderer=DocBook --theme=book --image-resolution=300 --image-scale-factor=0.25 --filename=sample2e.xml sample2e.tex
	~/Downloads/xxe-perso-4_8_0/bin/xxe sample2e/sample2e.xml

FIGURES = figs/Correlation_examples.png

oreilly:
	rsync -a book/book.xml ~/oreilly/1234000002166
	rsync -a figs/*.pdf $(FIGURES) ~/oreilly/1234000002166/figs

clean:
	rm -f *~ *.aux *.log *.dvi *.idx *.ilg *.ind *.toc



