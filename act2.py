class Employee:
    def __init__(self):
        print('Employee ceated')

        def __del__(self):
            print("Destructor called")

def create_obj():
            print('Making Object...')
            obj = Employee()
            print('function end ...')
            return obj
        
print('Calling create_job() function...')
obj = create_obj()
print ("program end")