from datetime import date, datetime

"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.
"""


def date_time_parser(s: str)-> str:
    parsed_string = datetime.strptime(s, "%I:%M:%S%p")
    
    str_time = datetime.strftime(parsed_string, "%H:%M:%S")
    return str_time



def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    test(date_time_parser, "07:05:45PM", "19:05:45")
    test(date_time_parser, "01:01:00AM", "01:01:00")
