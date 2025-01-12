def send_msg(not_sent, sent):
    while not_sent:
        current_sent = not_sent.pop()
        print(f'Sending message: {current_sent}')
        sent.append(current_sent)

def show_msg(sent):
    """Show all massage"""
    print('\nPrinted massage:')
    for s in sent:
        print(s)

not_sent = ['Hallo', 'How are you', 'I like Python', 'See you later!']
sent = []

send_msg(not_sent, sent)
show_msg(sent)

def send_msg(not_sent, sent):
    while not_sent:
        current_sent = not_sent.pop()
        print(f'Sending message: {current_sent}')
        sent.append(current_sent)

def show_msg(sent):
    """Show all massage"""
    print('\nPrinted massage:')
    for s in sent:
        print(s)

not_sent = ['Hallo', 'How are you', 'I like Python', 'See you later!']
sent = []

send_msg(not_sent[:], sent)
show_msg(sent)
print(not_sent)
print(sent)
print(not_sent[:])