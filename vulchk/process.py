
def parse(data):
    for key,value in data.items():
        print (str(key)+'->'+str(value))
        if type(value) == type(dict()):
            parse(value)
        elif type(value) == type(list()):
            for val in value:
                if type(val) == type(str()):
                    pass
                elif type(val) == type(list()):
                    pass
                else:
                    parse(val)
