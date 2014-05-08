LATEX = latex

DVIPS = dvips

PDFFLAGS = -dCompatibilityLevel=1.4 -dPDFSETTINGS=/prepress \
           -dCompressPages=true -dUseFlateCompression=true  \
           -dEmbedAllFonts=true -dSubsetFonts=true -dMaxSubsetPct=100


%.dvi: %.tex
	$(LATEX) $<

%.ps: %.dvi
	$(DVIPS) -o $@ $<

%.pdf: %.ps
	ps2pdf $(PDFFLAGS) $<

all:	book.tex
	pdflatex book
	makeindex book.idx
	mv book.pdf thinkstats.pdf
	evince thinkstats.pdf

hevea:
	sed 's/\(figs\/[^.]*\).\(pdf\|png\)/\1.eps/' book.tex > thinkstats.tex
	rm -rf html
	mkdir html
	hevea -O -e latexonly htmlonly thinkstats
	imagen -png thinkstats
	hacha thinkstats.html
	cp up.png next.png back.png html
	mv index.html thinkstats.css thinkstats*.html thinkstats*.png *motif.gif html

DEST = /home/downey/public_html/greent/thinkstats

distrib:
	rm -rf dist
	mkdir dist dist/tex dist/tex/figs
	rsync -a thinkstats.pdf html cover_nolines.png dist
	rsync -a Makefile book.tex latexonly htmlonly dist/tex
	# rsync -a figs/*.fig figs/*.eps dist/tex/figs
	cd dist; zip -r thinkstats.tex.zip tex
	cd dist; zip -r thinkstats.html.zip html
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
	~/Downloads/xxe-perso-4_8_0/bin/xxe book/book.xml

vector:
	plastex --renderer=DocBook --theme=book --vector-imager=dvisvgm --filename=book.xml book.tex

small: small.tex
	plastex --renderer=DocBook --theme=book --image-resolution=300 --filename=small.xml small.tex

sample:
	plastex --renderer=DocBook --theme=book --image-resolution=300 --image-scale-factor=0.25 --filename=sample2e.xml sample2e.tex
	~/Downloads/xxe-perso-4_8_0/bin/xxe sample2e/sample2e.xml

oreilly:
	rsync -a book/ ~/oreilly
	rsync -a figs/* ~/oreilly/figs
	cp thinkstats.pdf ~/oreilly/pdf

clean:
	rm -f *~ *.aux *.log *.dvi *.idx *.ilg *.ind *.toc



