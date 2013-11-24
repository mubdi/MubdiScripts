import csv
import xlrd

def xlstocsv(infile, outfile, ws=0):
    book = xlrd.open_workbook(infile)
    outcsv = csv.writer(open(outfile, 'w'), delimiter='\t')
    sheet = book.sheet_by_index(ws)
    numrows = sheet.nrows
    numcols = sheet.ncols
    for ry in range(numrows):
        temprow = list()
        for rx in range(numcols):
            temprow.append(sheet.cell_value(rowx=ry, colx=rx))
        outcsv.writerow(temprow)
        