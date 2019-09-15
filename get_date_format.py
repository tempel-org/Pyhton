from datetime import datetime

def get_date_format(date_str):
    '''Devuelve el formato de una fecha tipo ``str`` si cumple con algun formato sino devuelve ``False``.\\
    Return: ``str`` o ``False``\\
    Params:\\
    fecha_str ``str`` fecha en formato string'''

    if type(date_str) is str:
        date1 = date_str.split()[0]
        date1 = date1[0:10]
        try:
            date1 = (datetime.strptime(date1, '%Y/%m/%d'))
            date_format = '%Y/%m/%d'
        except ValueError:
            try:
                date1 = (datetime.strptime(date1, '%d/%m/%Y'))
                date_format = '%d/%m/%Y'
            except ValueError:
                try:
                    date1 = (datetime.strptime(date1, '%m/%d/%Y'))
                    date_format = '%m/%d/%Y'
                except ValueError:
                    try:
                        date1 = (datetime.strptime(date1, '%Y-%m-%d'))
                        date_format = '%Y-%m-%d'
                    except ValueError:
                        try:
                            date1 = (datetime.strptime(date1, '%d-%m-%Y'))
                            date_format = '%d-%m-%Y'
                        except ValueError:
                            try:
                                date1 = (datetime.strptime(date1, '%m-%d-%Y'))
                                date_format = '%m-%d-%Y'
                            except ValueError:
                                try:
                                    date1 = (datetime.strptime(date1, '%Y%m%d'))
                                    date_format = '%Y%m%d'
                                except ValueError:
                                    try:
                                        date1 = (datetime.strptime(date1, '%d%m%Y'))
                                        date_format = '%d%m%Y'
                                    except ValueError:
                                        try:
                                            date1 = (datetime.strptime(date1, '%m%d%Y'))
                                            date_format = '%m%d%Y'
                                        except ValueError:
                                            return False
        return date_format
    else:
        return False
