from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams
from pathlib import Path
from re import findall,search,compile,search,split

pdf_path = Path(__file__).with_name('SampleSet.pdf')

laparams = LAParams(boxes_flow=None)
text = extract_text(pdf_path, laparams=laparams)
print(text)

# def parse_text(text):
    # for i in range(1,21):
    #     print(i)
    #     r = search(f'{i}[:.]',text)
    #     print(r)

    # r = findall(r'\n[0-9][:.]',text)
    # r = split("[0-9][0-9][:.]|B[12][:.]|\n[1-9][:.]",text)
    # return r

print(parse_text(text))