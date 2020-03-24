
all:	book.tex
	pdflatex book
	makeindex book.idx
	pdflatex book
	mv book.pdf thinkstats2.pdf
	evince thinkstats2.pdf

HEVEABUILDLOG=build.log
#HEVEABUILDLOG=build.log.old.log
#HEVEABUILDLOG=build.log.$(shell git rev-parse --short HEAD).log

hevea:
	sed 's/\(figs\/[^.]*\).\(pdf\|png\)/\1.eps/' book.tex > thinkstats2.tex
	rm -rf html
	mkdir html
	hevea macros.hva -O -e latexonly htmlonly thinkstats2 2>&1 | tee ${HEVEABUILDLOG}
# the following greps are a kludge to prevent imagen from seeing
# the definitions in latexonly, and to avoid headers on the images
	grep -v latexonly thinkstats2.image.tex > a; mv a thinkstats2.image.tex
	sed s/\\\\usepackage{fancyhdr}// < thinkstats2.image.tex > a; mv a thinkstats2.image.tex
	imagen -png thinkstats2
	hacha thinkstats2.html
	cp up.png next.png back.png html
	cat custom.css >> thinkstats2.css
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
	$(MAKE) clean-hevea

clean-hevea:
	rm -rf book.out html/ thinkstats2.*


docker-build:
	uid=$(id -u) docker build -t thinkbooks:latest .

docker-run-bash:
	docker run --rm -it -v "$(shell pwd)/..":/home/app/src thinkbooks:latest /bin/bash

docker-run-hevea:
	docker run --rm -it -v "$(shell pwd)/..":/home/app/src thinkbooks:latest make -C /home/app/src/book hevea


## Using heavea-compare-logs to determine when the hevea build output changed:
# pip install --user pyline
#
# make hevea; cp build.log ~/build.log.old.log
# git checkout abc123; mv ~/build.log.old.log .
# make hevea
# make hevea-compare-logs
#
# rev=$(git rev-parse --short HEAD)
# make hevea HEAVEABUILDLOG=build.log.${rev}.log
# make hevea-compare-logs LOG1=build.log.${rev}.log LOG2=build.log

PYLINE_CMD=pyline -F ':' --max 2 '(w[0], w[2]) if len(w) == 3 else l'
LOG1=build.log.old.log
LOG2=build.log
LOGSUFFIX=.stripped.log
LOG1STRIPPED=${LOG1}${LOGSUFFIX}
LOG2STRIPPED=${LOG2}${LOGSUFFIX}

hevea-compare-logs:
	@# pip install --user pyline
	test -f ${LOG1}
	test -f ${LOG2}
	cat ${LOG1} | ${PYLINE_CMD} > ${LOG1STRIPPED}
	cat ${LOG2} | ${PYLINE_CMD} > ${LOG2STRIPPED}
	diff -Naur ${LOG1STRIPPED} ${LOG2STRIPPED}

