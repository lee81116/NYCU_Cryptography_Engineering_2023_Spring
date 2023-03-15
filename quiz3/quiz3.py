def get_ic(message, key_length):
    # Initialization
    groups = {}
    for i in range(key_length):
        groups[i] = [0] * 26
    totals = [0] * key_length
    # Count the letters and the total length for each group
    for i in range(len(message)):
        groups[i % key_length][ord(message[i]) - ord('A')] += 1
        totals[i % key_length] += 1
    # Calculate the IC values for each group
    ics = 0
    for i in range(key_length):
        ic = 0
        for j in range(26):
            ic += (groups[i][j]*(groups[i][j]-1)) / (totals[i]*(totals[i]-1))
        # Sum the IC values
        ics += ic
    # return the average IC value
    ics /= key_length
    return ics


def try_key_length(message):
    # suppose key length doesn't exceed 7
    min_ic_diff = 10
    for n in range(2, 9):
        ic = get_ic(message, n)
        ic_diff = abs(ic - 0.0667)
        # get the one with minimal difference from its IC value and plaintext's
        if ic_diff < min_ic_diff:
            min_ic_diff = ic_diff
            key_length = n
    return key_length

def get_key(message, k):
    # Frequencies for each alphabets
    freqs = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406,
             6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]
    # Initialization
    groups = {}
    for i in range(k):
        groups[i] = [0] * 26
    totals = [0] * k
    # Count the letters and the total length for each group
    for i in range(len(message)):
        groups[i % k][ord(message[i]) - ord('A')] += 1
        totals[i % k] += 1
    # Find the key letter for each group and concatenate 
    thekey = ""
    for i in range(k):
        # Find the letter with lowest Chi-Square Test score
        minCST = float("inf")
        for alpha in range(26):
            cst = 0
            for a in range(26):
                # sum (Observed - Expected)^2 / Expected
                cst += (groups[i][(a+alpha) % 26] - freqs[a])**2 / freqs[a]
            if cst < minCST:
                minCST = cst
                key = alpha
        thekey += chr(ord("A") + key)
    return thekey

def get_plain(message, key):
    plain_text = ""
    for i in range(len(message)):
        k = ord(key[i % len(key)])
        l = ord(message[i])
        plain_text += chr(((l-k+26)%26) + ord("A"))
    return plain_text
