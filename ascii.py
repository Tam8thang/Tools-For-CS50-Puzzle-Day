"""
The ASCII code tables on the following URL are loaded as dictionaries
"https://www.ascii-code.com/"

Please use following dictionaries according to your needs

dec_oct, oct_dec
dec_hex, hex_dec
dec_bin, bin_dec
dec_symbol, symbol_dec
dec_html_number, html_number_dec
dec_html_name, html_name_dec

You can edit the "main" function to decode the problems.
"""

from bs4 import BeautifulSoup
import requests

def main():
    example = "Apple"

    print()
    print(f"Example word: {example}")
    print("Decoded as DEC: ", end=" ")
    for i in range(len(example)):
        if i != len(example) -1:
            print(symbol_dec[example[i]], end=", ")
        else:
            print(symbol_dec[example[i]])

    print()
    example = "77 79 79 78"
    print(f"Example numbers: {example}")
    example = example.split(" ")
    print("Decoded as Symbol: ", end=" ")
    for i in range(len(example)):
        print(dec_symbol[int(example[i])], end="")
    print()
    print()

URL = "https://www.ascii-code.com/"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')

tables = soup.findAll('table')


thead = tables[0].thead
tr = thead.tr
ths = tr.findAll('th')
titles=[]
for th in ths:
    if len(th.contents) != 0:
        titles.append(th.contents[0])

data_table = []
for table in tables:
    tbody = table.tbody
    trs = tbody.findAll('tr')
    for tr in trs:
        tds = tr.findAll('td')
        td_tables = []
        for td in tds:
            if td.a != None:
                if len(td.a.contents) != 0:
                    if (len(td.a.contents[0]) == 0) or (td.a.contents[0] == '\xa0'):
                        td_tables.append('\xa0')
                    else:
                        td_tables.append(td.a.contents[0])
            else:
                if len(td.contents) != 0:
                    if (len(td.contents[0]) == 0) or (td.contents[0] == '\xa0'):
                        td_tables.append('\xa0')
                    else:
                        td_tables.append(td.contents[0])
        td_tables.pop(0)
        data_table.append(td_tables)

oct = []
hex = []
bin = []
symbol = []
html_number = []
html_name = []



for data_ in data_table:
    oct.append(data_[1])
    hex.append(data_[2])
    bin.append(data_[3])
    if int(data_[0]) not in [129,141,143,144,157]:
        symbol.append(data_[4])
        html_number.append(data_[5])
        html_name.append(data_[6])
    else:
        symbol.append(" ")
        html_number.append(" ")
        html_name.append(data_[4])

symbol[173] = "SHY"

dec_oct = dict()
oct_dec = dict()

dec_hex = dict()
hex_dec = dict()

dec_bin = dict()
bin_dec = dict()

dec_symbol = dict()
symbol_dec = dict()

dec_html_number = dict()
html_number_dec = dict()

dec_html_name = dict()
html_name_dec = dict()

for i in range(256):
    dec_oct[i] = oct[i]
    oct_dec[oct[i]] = i
    dec_hex[i] = hex[i]
    hex_dec[hex[i]] = i
    dec_bin[i] = bin[i]
    bin_dec[bin[i]] = i

    if i not in [129,141,143,144,157]:
        if symbol[i] != "\xa0":
            dec_symbol[i] = symbol[i]
            symbol_dec[symbol[i]] = i
        if html_number[i] != "\xa0":
            dec_html_number[i] = html_number[i]
            html_number_dec[html_number[i]] = i
    if html_name[i] != "\xa0":
        dec_html_name[i] = html_name[i]
        html_name_dec[html_name[i]] = i

main()