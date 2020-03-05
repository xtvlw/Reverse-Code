#_[N_F]_
message = input('message : ')
final_message, n = '', len(message)
x = 0
while x < n:
    final_message += message[n-x-1]
    x += 1
print(final_message)
