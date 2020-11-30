import threading

print('Before threading')
print('Cats', 'Dogs', 'Frogs', sep=' $ ')
print()

# Create a thread object with 'Cats', 'Dogs', 'Frogs'
# as args and sep=' $ ' as kwargs

print('Threading is now applied.')
threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
threadObj.start()

