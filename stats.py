def get_num_words(text):
    words = text.split()
    return len(words)

def get_symbol_count(text):
    symbols = {}
    for symbol in text.lower():
        if symbol in symbols:
            symbols[symbol] += 1
        else:
            symbols[symbol] = 1
    return symbols

def sort_on(items):
    return items["num"]

def analyze_text(symbols):
    result = []
    for symbol in symbols:
        if symbol.isalpha():
            result.append({"char": symbol, "num": symbols[symbol]})
    result.sort(reverse=True, key=sort_on)
    return result
