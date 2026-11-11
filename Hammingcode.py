def hamming74_encode(data_bits):
    # data_bits: string of 4 bits
    d = [int(x) for x in data_bits]

    # positions 1-7: P1 P2 D1 P3 D2 D3 D4
    h = [0]*7

    h[2] = d[0]  # D1
    h[4] = d[1]  # D2
    h[5] = d[2]  # D3
    h[6] = d[3]  # D4

    # Parity bits
    h[0] = h[2] ^ h[4] ^ h[6]  # P1
    h[1] = h[2] ^ h[5] ^ h[6]  # P2
    h[3] = h[4] ^ h[5] ^ h[6]  # P3

    return h


def hamming74_decode(received):
    h = [int(x) for x in received]

    # Check parity bits
    s1 = h[0] ^ h[2] ^ h[4] ^ h[6]
    s2 = h[1] ^ h[2] ^ h[5] ^ h[6]
    s3 = h[3] ^ h[4] ^ h[5] ^ h[6]

    # Find error position
    error_position = s1 + (s2 * 2) + (s3 * 4)

    if error_position == 0:
        print("No error detected. Hamming code is correct.")
    else:
        print("Error detected at position:", error_position)

        # Correct the error
        h[error_position - 1] = h[error_position - 1] ^ 1

        print("Corrected Hamming code:", "".join(str(x) for x in h))

    return h


# User input
inp = input("Enter 4-bit data: ")

if len(inp) != 4 or any(x not in "01" for x in inp):
    print("Please enter exactly 4 binary bits.")
else:
    code = hamming74_encode(inp)

    output = "".join(str(x) for x in code)
    print("7-bit Hamming code:", output)

    # Receive code for error checking
    received = input("Enter received 7-bit Hamming code: ")

    if len(received) != 7 or any(x not in "01" for x in received):
        print("Please enter exactly 7 binary bits.")
    else:
        corrected = hamming74_decode(received)

        print("Final Hamming code:", "".join(str(x) for x in corrected))
        print("Original data:", corrected[2], corrected[4],
              corrected[5], corrected[6])
