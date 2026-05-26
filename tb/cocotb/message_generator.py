# generates input messages to be used by the testbench

import random

# generates random int within 32-bit length limit
def generate_true_random_message():
    message = random.randint(0,4294967295)
    return message

# generates 32-bit length message, allowing limits for each field (default is the bit-width limitss)
def generate_paramaterised_random_message(type_limit=15, id_limit=15, val_a_limit=255, val_b_limit=255, flags_limit=255):
    # set all fields to random numbers within their limit
    message_type = random.randint(0,type_limit)
    channel_id = random.randint(0,id_limit)
    value_a = random.randint(0,val_a_limit)
    value_b = random.randint(0, val_b_limit)
    flags = random.randint(0,flags_limit)


    message_type = f'{message_type:0{4}b}'
    channel_id = f'{channel_id:0{4}b}'
    value_a = f'{value_a:0{8}b}'
    value_b = f'{value_b:0{8}b}'
    flags = f'{flags:0{8}b}'

    # convert to int base 2
    message = int((str(message_type) + str(channel_id) + str(value_a) + str(value_b) + str(flags)), 2)

    return message


if __name__ == "__main__":
    # demo message gen

    message = generate_paramaterised_random_message()
    print("Param Message (dec):", message, "Param Message (bin):", bin(message))
    message = generate_true_random_message()
    print("Random Message (dec):", message, "Random Message (bin):", bin(message))
