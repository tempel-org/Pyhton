def obt_formato_fecha(fecha_str):
    '''Devuelve el formato de una fecha tipo ``str`` si cumple con algun formato sino devuelve ``False``.\\
    Return: ``str`` o ``False``\\
    Params:\\
    fecha_str ``str`` fecha en formato string'''

    if type(fecha_str) is str:
        fecha = fecha_str.split()[0]
        fecha = fecha[0:10]
        try:
            fecha = (datetime.strptime(fecha, '%Y/%m/%d'))
            date_format = '%Y/%m/%d'
        except ValueError:
            try:
                fecha = (datetime.strptime(fecha, '%d/%m/%Y'))
                date_format = '%d/%m/%Y'
            except ValueError:
                try:
                    fecha = (datetime.strptime(fecha, '%m/%d/%Y'))
                    date_format = '%m/%d/%Y'
                except ValueError:
                    try:
                        fecha = (datetime.strptime(fecha, '%Y-%m-%d'))
                        date_format = '%Y-%m-%d'
                    except ValueError:
                        try:
                            fecha = (datetime.strptime(fecha, '%d-%m-%Y'))
                            date_format = '%d-%m-%Y'
                        except ValueError:
                            try:
                                fecha = (datetime.strptime(fecha, '%m-%d-%Y'))
                                date_format = '%m-%d-%Y'
                            except ValueError:
                                try:
                                    fecha = (datetime.strptime(fecha, '%Y%m%d'))
                                    date_format = '%Y%m%d'
                                except ValueError:
                                    try:
                                        fecha = (datetime.strptime(fecha, '%d%m%Y'))
                                        date_format = '%d%m%Y'
                                    except ValueError:
                                        try:
                                            fecha = (datetime.strptime(fecha, '%m%d%Y'))
                                            date_format = '%m%d%Y'
                                        except ValueError:
                                            return False
        return date_format
    else:
        return False
