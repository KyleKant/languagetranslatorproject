# Language Translator with module googletrans
from googletrans import Translator

trans = Translator()

try:
    with open("original_language.txt", 'w') as orig_file:
        paragraph = '''Google Translate is a multilingual neural machine translation service developed by Google to translate text, documents and websites from one language into another. It offers a website interface, a mobile app for Android and iOS, and an API that helps developers build browser extensions and software applications.[3] As of November 2022, Google Translate supports 133 languages at various levels,[4] and as of April 2016, claimed over 500 million total users, with more than 100 billion words translated daily,[5] after the company stated in May 2013 that it served over 200 million people daily.[6]

        Launched in April 2006 as a statistical machine translation service, it used United Nations and European Parliament documents and transcripts to gather linguistic data. Rather than translating languages directly, it first translates text to English and then pivots to the target language in most of the language combinations it posits in its grid,[7] with a few exceptions including Catalan-Spanish.[8] During a translation, it looks for patterns in millions of documents to help decide which words to choose and how to arrange them in the target language. Its accuracy, which has been criticized on several occasions,[9] has been measured to vary greatly across languages.[10] In November 2016, Google announced that Google Translate would switch to a neural machine translation engine – Google Neural Machine Translation (GNMT) – which translates "whole sentences at a time, rather than just piece by piece. It uses this broader context to help it figure out the most relevant translation, which it then rearranges and adjusts to be more like a human speaking with proper grammar".[2]'''
        orig_file.write(paragraph)
    # End write file
except Exception as err:
    print(err)

try:
    with open('original_language.txt', 'r') as f:
        # print(f.read())
        orig_lang = f.read()
        trans_lang = trans.translate(orig_lang, dest='vi')
        # print(trans_lang.text)
        try:
            with open("trans_language.txt", 'w', encoding='utf-8') as translated_file:
                translated_file.write(trans_lang.text)
            # End write file
        except Exception as err:
            print(err)
    # end open file
except Exception as err:
    print(err)

try:
    with open("trans_language.txt", 'r', encoding='utf-8') as read_translated_file:
        print(read_translated_file.read())
    # End read file
except Exception as err:
    print(err)
