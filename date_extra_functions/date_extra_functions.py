from datetime import datetime

def today_():
    '''Returns today's date'''
    return datetime.today().date()

def today_str():
    '''Returns today's date in string format dd/mm/aaaa'''
    today = datetime.today()
    return str(today.day) + '/' + str(today.month) + '/' + str(today.year)

def get_date_format(date_str):
    '''Returns the format from a ``str`` type date if it matches with any valid format, else returns ``False``.\\
    Return: ``str`` or ``False``\\
    Params:\\
    date_str ``str`` string format date'''

    if type(date_str) is str:
        date_ = date_str.split()[0]
        date_ = date_[0:10]
        try:
            date_ = (datetime.strptime(date_, '%Y/%m/%d'))
            date_format = '%Y/%m/%d'
        except ValueError:
            try:
                date_ = (datetime.strptime(date_, '%d/%m/%Y'))
                date_format = '%d/%m/%Y'
            except ValueError:
                try:
                    date_ = (datetime.strptime(date_, '%m/%d/%Y'))
                    date_format = '%m/%d/%Y'
                except ValueError:
                    try:
                        date_ = (datetime.strptime(date_, '%Y-%m-%d'))
                        date_format = '%Y-%m-%d'
                    except ValueError:
                        try:
                            date_ = (datetime.strptime(date_, '%d-%m-%Y'))
                            date_format = '%d-%m-%Y'
                        except ValueError:
                            try:
                                date_ = (datetime.strptime(date_, '%m-%d-%Y'))
                                date_format = '%m-%d-%Y'
                            except ValueError:
                                try:
                                    date_ = (datetime.strptime(date_, '%Y%m%d'))
                                    date_format = '%Y%m%d'
                                except ValueError:
                                    try:
                                        date_ = (datetime.strptime(date_, '%d%m%Y'))
                                        date_format = '%d%m%Y'
                                    except ValueError:
                                        try:
                                            date_ = (datetime.strptime(date_, '%m%d%Y'))
                                            date_format = '%m%d%Y'
                                        except ValueError:
                                            return False
        return date_format
    else:
        return False

def calc_age(birth_date):
    return 1

def parse_date(date_str, format="%d/%m/%Y"):
    '''Returns a date with a new ``str`` format if it matches with any valid date format, else returns ``False``.\\
    Return: ``str`` o ``False``\\
    Params:\\
    date_str ``str`` string format date.\\
    format ``str`` new date format. Default: %d/%m/%Y'''

    if get_date_format(date_str):
        return datetime.strptime(date_str, get_date_format(date_str)).strftime(format)
    else:
        return False

def eval_date(value_, list_=[]):
    if value_ is not None and list_ is not None:
        return True if value_ in list_ else False
        
