def crc_remainder(data_bin, gen_bin):
    data = int(data_bin + '0' * (len(gen_bin) - 1), 2)
    gen = int(gen_bin, 2)

    shift = len(data_bin)

    for i in range(shift):
        if data & (1 << (shift + len(gen_bin) - 2 - i)):
            data ^= gen << (shift - i)

    rem = bin(data)[2:].zfill(len(gen_bin) - 1)

    return rem


def sender(data_bin, gen_bin):
    rem = crc_remainder(data_bin, gen_bin)

    codeword = data_bin + rem

    print("Remainder on sender side is:", rem)
    print("Data sent:", codeword)

    return codeword


def receiver(codeword_bin, gen_bin):
    # Take the entire codeword without slicing
    data = int(codeword_bin, 2)
    gen = int(gen_bin, 2)

    shift = len(codeword_bin) - len(gen_bin) + 1

    for i in range(shift):
        if data & (1 << (shift + len(gen_bin) - 2 - i)):
            data ^= gen << (shift - i)

    rem_check = bin(data)[2:].zfill(len(gen_bin) - 1)

    print("Remainder on receiver side is:", rem_check)

    if int(rem_check, 2) == 0:
        print("Data received without noise")
    else:
        print("Data consists of some noise")


data = input("Enter the data to be sent (in binary): ")
generator = input("Enter the binary Generator string: ")

codeword = sender(data, generator)
receiver(codeword, generator)
