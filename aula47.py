import os

secret_word = 'Jesus'
new_word = ''
secret_letter = ''
count = 0


while True:
    letter = input('Type a letter: ')
    if len(letter)> 1:
        print('Type one letter.')

    if letter in secret_word:
        new_word += letter

    form_word = ''    
    for secret_letter in secret_word:
        if secret_letter in new_word:
            form_word += secret_letter
        else:
            form_word += '*'
    count +=1
    print(f'formed word: `{form_word}')
    if form_word == secret_word:
        os.system('cls')
        print(f'Congratulations the word formed is: {secret_word}')
        print(f'You make {count} intents.')
        new_word = ''
        secret_letter = ''
    
    
    
    
    
   