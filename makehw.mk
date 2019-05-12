Resultados_hw2.pdf: Senal.png #TransformadasSenales.png amplitud1.png amplitud2.png amplitud3.png amplitud4.png
	pdflatex Resultados_hw2.tex

Senal.png: Fourier.py
	python Fourier.py

TransformadasSenales.png:Fourier.py
	python Fourier.py

EspectrogramaSenales.png:Fourier.py
	python Fourier.py

amplitud1.png:Plotws_hw2.py edificio.txt
	python Plotws_hw2.py

edificio.txt: edificio.cpp
	g++ edificio.cpp
	./a.out
