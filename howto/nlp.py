import nltk


def extract_entities(text, all=True, verbose=False):
    ne_list = []
    tokens = nltk.word_tokenize(text)
    for chunk in nltk.ne_chunk(nltk.pos_tag(tokens)):
        if all:
            if verbose: print(chunk)
        if type(chunk) is nltk.tree.Tree:
            first_word = ' '.join(c[0] for c in chunk.leaves()).split()[0]
            ne_tag = chunk.label()
            ne_list.append([ne_tag, first_word, tokens.index(first_word)])
            if verbose: print(ne_list[-1])
        elif chunk[1] == 'CD':
            first_word = chunk[0]
            ne_list.append(['CD', first_word, tokens.index(first_word)])
            if verbose: print(ne_list[-1])

    return ne_list
