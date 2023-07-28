from googletrans import Translator
from langdetect import detect
import os

def main():
  trans_file = input('翻訳したいファイルパスを入力して下さい>>')
  while True:
    if not os.path.isfile(trans_file):
      trans_file = input('ファイルが存在しません。再度入力して下さい>>')
    else:
      break
  translation(trans_file)

def translation(file_path):
  with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()
    f.close()
 
  tr = Translator()
  try:
    # 1行ずつ日本語に翻訳
    for line in lines:
      print("lang:", detect(line))
      if detect(line) == "en":
        result = tr.translate(line, src="en", dest="ja").text
      elif detect(line) == "ko":
        result = tr.translate(line, src="ko", dest="ja").text
      elif detect(line) == "ja":
        result = line
      else:
        result = tr.translate(line, src="en", dest="ja").text
      writing_translation(result)

    print('翻訳ファイルを作成しました。')
  except Exception as e:
    print(e)
 
# 書込み
def writing_translation(result):
  path = './ja.txt'
  f = open(path, 'a', encoding="utf-8")
  f.write(result + '\n')
  f.close()
 
if __name__ == "__main__":
  main()
