import datetime

def logging(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('logs/logs.log', 'a', encoding='utf-8') as log_file:
            log_file.write(f'{datetime.datetime.now()} - {old_function.__name__} - {args} & {kwargs} - {result} \n')
            return result

    return new_function

def param_logging(path):
    def _logging(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as log_file:
                log_file.write(f'{datetime.datetime.now()} - {old_function.__name__} - {args} & {kwargs} - {result} \n')
                return result

        return new_function

    return _logging