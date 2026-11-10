data = input("Enter binary data: ")
block_size = int(input("Enter block size (8 or 16): "))

blocks = []

# Divide data into blocks
for i in range(0, len(data), block_size):
    block = data[i:i+block_size]

    if len(block) < block_size:
        block = block.ljust(block_size, '0')

    blocks.append(block)

# Calculate checksum
total = 0

for block in blocks:
    total += int(block, 2)
    total = (total & ((1 << block_size) - 1)) + (total >> block_size)

checksum = format(~total & ((1 << block_size) - 1),
                  f'0{block_size}b')

# Sender Side
print("\n--- Sender Side ---")
print("Original Data:", data)
print("Checksum:", checksum)

received_data = data + checksum

# Receiver Side
blocks_r = []

for i in range(0, len(received_data), block_size):
    blocks_r.append(received_data[i:i+block_size])

total_r = 0

for block in blocks_r:
    total_r += int(block, 2)
    total_r = (total_r & ((1 << block_size) - 1)) + (total_r >> block_size)

print("\n--- Receiver Side ---")

if total_r == (1 << block_size) - 1:
    print("No error detected")
else:
    print("Error detected")
