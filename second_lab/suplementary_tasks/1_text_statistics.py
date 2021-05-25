import re


def generate_ngrams(s, n):
    s = s.lower()
    s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
    
    tokens = [token for token in s.split(" ") if token != ""]
    sequence = [tokens[i:] for i in range(n)]
    ngrams = zip(*sequence)
    return list(ngrams)

def word_st(text):
    text = text.replace('...','.')
    split_sentences = text.split('.')
    split_sentences.pop(-1)
    sentences_count = len(split_sentences)
    words = format_text(text)
    word_count = len(words)
    amount_w = []
    median = 0
    word_met = {}

    for sentence in split_sentences:
        amount_w.append(len(format_text(sentence)))

    for word in words:
        word_met[word] = words.count(word)

    print("\nThe word: ")
    for key in word_met:
        print('-{}- --> {} '.format(key,word_met[key]))
        
    middle = round(word_count/sentences_count) 
    print("\nThe middle amountof words: {}".format(middle))

    sort = sorted(amount_w)
    if len(sort)%2 == 0:
        median = sort[int((len(sort)/2-1))]
    else:
        median = (sort[int((len(sort)/2-1))] + sort[int((len(sort)/2-1)) + 1])/2
    print("\nThe median amount: {}".format(median))


def format_text(text):
    symb = [',','!','?','.',':',';','  ','...']
    for sym in symb:
        text = text.replace(sym,"")
    return text.split(' ')


def main():
    stroka = input()

    word_st(stroka)
    print('Do you want to input K and N? 1.Yes/2.No')
    answer = int(input())
    if answer == 1:
        print("\nPlease input K: ")
        K = int(input())
        print("\nPlease input N: ")
        N = int(input())
        ngrams = generate_ngrams(stroka, N)
        d.clear()
        for gramm in ngrams:
            d[gramm] = ngrams.count(gramm)
        list_d = list(d.items())
        list_d.sort(key=lambda i: i[1])
        print("\nTop-{} {}-gram".format(K,N))
        i = 0
        for grams in list_d:
            if i < K:
                print ("-> {} \t".format(grams[0]))
                i+=1
            else:
                break
    
                

if __name__ == '__main__':
    main()
