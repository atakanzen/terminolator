import sys
import nltk
import xlsxwriter

from google_trans_new import google_translator
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

if len(sys.argv) < 2:
    print('Please provide a .txt file.')
    sys.exit()
elif sys.argv[1].find('.txt') == -1:
    print('Please provide a .txt file.')
    sys.exit()

nltk.download('stopwords')
nltk.download('punkt')

print('Process started, this may take some time depending on the file size.')

translator = google_translator()
text = open(sys.argv[1], 'r').read()

stop_words = set(stopwords.words('english'))
tokenized_text = word_tokenize(text)
words = [word.lower() for word in tokenized_text if word.isalpha()]

ordered_words = set()
result = {}
for src_word in words:
    if src_word not in stop_words and src_word not in ordered_words:
        ordered_words.add(src_word)
        tgt_word = translator.translate(src_word, lang_src='en', lang_tgt='tr')
        result[src_word] = tgt_word

workbook = xlsxwriter.Workbook(f'{sys.argv[1].lower()}_Terminology.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, 'source_language')
worksheet.write(0, 1, 'target_language')

row = 1
col = 0
for src, trg in result.items():
    worksheet.write(row, col, src)
    worksheet.write(row, col + 1, trg)
    row += 1

workbook.close()
