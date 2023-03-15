import quiz3

while True:
    try:
        # stdin
        message = input()
        if not message:
            break
        message = message.rstrip()
        # Get key length
        k = quiz3.try_key_length(message)
        print("Key length for this message should be:", k) 
        # Get key
        key = quiz3.get_key(message, k)
        print("The key may be:", key)
        # Obtain the plain text
        plain = quiz3.get_plain(message, key)
        print("The plain text is:")
        # stdout
        count = 0
        for a in plain:
            print(end=a)
            count += 1
            if count == 5:
                print(end=" ")
                count = 0
        # Save to "message_out.txt"
        f = open("message_out.txt", "a")
        f.write(plain)
        f.close()
    except EOFError:
        print(end="")
        break