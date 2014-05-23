%.html: %.py
	pygmentize -f html -O noclasses $< > $@
