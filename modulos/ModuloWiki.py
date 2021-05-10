import wikipedia



def wikiSearch(text):
    wikipedia.set_lang('es')
    texto_wiki = wikipedia.summary(text,sentences=2)
    return texto_wiki







