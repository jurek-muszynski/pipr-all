# Zadanie 1


def count_symbols(symbols_list):
    distinct_symbols = {}
    for symbols_inner_list in symbols_list:
        for symbol in symbols_inner_list:
            distinct_symbols[symbol] = distinct_symbols.get(
                symbol, 0) + 1
    return distinct_symbols

# Zadanie 2


def time_description(hrs, mins):

    if (hrs > 12 or hrs < 0 or mins > 59 or mins < 0):
        return 'Incorrect input data!'

    num_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                15: 'quarter', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
                19: 'nineteen', 20: 'twenty', 30: 'half'}

    def format_hours(hrs, mins):
        return f"{'past' if mins <= 30 else 'to'} {num_dict[hrs]}"

    def format_minutes(mins):
        if (mins <= 30):
            if (mins % 15 == 0):
                return f"{num_dict[mins]}{' minutes' if mins % 15 else ''}"
            if (mins <= 20):
                return f"{num_dict[mins]} {'minute' if mins == 1 else 'minutes'}"
        return f"{num_dict[mins-(mins%10)]} {num_dict.get(mins%10)} minutes"

    if (mins == 0):
        return f"{num_dict[hrs]} o' clock"
    if (mins <= 30):
        return f"{format_minutes(mins)} {format_hours(hrs,mins)}"
    return f"{format_minutes(60 - mins)} {format_hours((hrs+1)%12,mins)}"
