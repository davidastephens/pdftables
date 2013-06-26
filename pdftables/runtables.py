#!/usr/bin/env python
# ScraperWiki Limited
# Ian Hopkinson, 2013-06-21
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
#import sys
#import codecs
# sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
"""
Tell us what this does
"""

import os
from pdftables import get_pdf_page, page_to_tables
from os.path import join, dirname
import pdftablesAnalysis as ptA

PDF_TEST_FILES = join(dirname(__file__), '..', 'fixture')
hints = []
# SelectedPDF = "cit0613.pdf"
# pagenumber = 1 # Wierd - each word is a figure?. First page can be broken
# down to boxes containing no text SelectedPDF = "COPAWEEKLYJUNE52013.pdf" #1
# page -
# pagenumber = 1 # parses if we just accept the whole page as a table, extend_y = True
#SelectedPDF = "COPAMONTHLYMay2013.pdf"
#pagenumber = 1 # Fails because it's two column and there are two tables. May be fixed by local / adaptive minima
SelectedPDF = "13_06_12_10_36_58_boletim_ingles_junho_2013.pdf" # 32 pages, Long document with many tables
pagenumber = 5
# pagenumber = 6
# SelectedPDF = "1359397366Final_Coceral grain estimate_2012_December.pdf" #3 pages Slow to interpret
#pagenumber = 1 # couple of places where columns are welded, fixed with going to single characters
#pagenumber = 2 # works without going to single characters
#pagenumber = 3 # As for page 1 - some columns are welded, fixed with going to single characters
#SelectedPDF = "ClinicalResearchDisclosureReport2012Q2.pdf"
# pagenumber = 1 # PDFEncryptionError('Unknown algorithm: param=%r' % param)
# SelectedPDF = "argentina_diputados_voting_record.pdf" # 1page
# pagenumber = 1
# hints = ['Apellido', '']
#SelectedPDF = "bo_page24.pdf" # 1 page Multi-column text and tables mixed on the page
#pagenumber = 1 # Fails - need a multicolumn detector
# SelectedPDF = "tabla_subsidios.pdf" # 1 page, fairly simple table
# pagenumber = 1 # works fine
# SelectedPDF = "m27-dexpeg2-polymer.pdf" # No tables, two column text
# SelectedPDF = "m29-JDent36s2-7.pdf" # One table, two column text, equations may cause problems?
# pagenumber = 4 # Works OK but some - signs are missed and we need to use extend_y
#SelectedPDF = "m30-JDent36s15-20.pdf" # several tables
#pagenumber = 4 # fails two different tables on one page, two column layout but tables span page -
#pagenumber = 5 # fails, very small table in two column layout, yComb is not ordered
# Open a PDF file.

#SelectedPDF = "2012.01.PosRpt.pdf" # 7 pages works fine in pdfminer, 4 for first test 2012.01.PosRpt.pdf
#pagenumber = 1 # Table too small to find - needs hints
# hints = [u"% Change", u"Uncommited"]
#pagenumber = 2 # Looks really nice
#pagenumber = 3 # Looks really nice
#pagenumber = 4 # the original!
#pagenumber = 5 # easier
#pagenumber = 6 # Columns welded: 21.94% 157, 201, 476 and where there is a spanning footer, cells overwriting
#pagenumber = 7 # welding caused by isolated spanning text (fixed by dynamic threshold)

# This needs "Get table from hints", really heavy hints!
#fh = pdftables.filehandleFromURL("http://www.candyusa.com/files/1st%20qtr%202013%20report.pdf")
#pagenumber = 1

filepath = os.path.join(PDF_TEST_FILES, SelectedPDF)
fh = open(filepath, 'rb')
pdf_page = get_pdf_page(fh, pagenumber)

table, diagnosticData = page_to_tables(pdf_page, extend_y=True, hints=hints)

fig, ax1 = ptA.plotpage(diagnosticData)

#for row in table:
#    print row

for rows in table:
    #print u'| '.join(map(unicode.strip, map(unicode, rows))).encode('utf-8')
    cells = map(unicode.strip, rows)
    #print cells
    #for cell in cells:
    #    print cell.__class__
    row = '| '.join(cells)
    print row
    # print(repr(row))


# BoxList = plotAllPages(open(filepath, 'rb'))