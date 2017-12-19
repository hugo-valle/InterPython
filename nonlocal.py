
message = 'global'

def enclosing():
    message = 'enclosing'
    def local():
        #global message
        nonlocal message
        message = 'local'
    print("Enclosing message:", message)
    local()
    print("Enclosing message:", message)


if __name__ == '__main__':
    print('Global message:', message)
    enclosing()
    print('Global message:', message)
