# A python model to compare the output of the verilog design to

# splits inputted message into components and returns
def parse_message(message:int):
    message_type = int((message >> 28) & 0b1111) # masks bits 31:28
    channel_id = int((message >> 24) & 0b1111)   # masks bits 27:24
    value_a = int((message >> 16) & 0b1111_1111) # masks bits 23:16
    value_b = int((message >> 8) & 0b1111_1111)  # masks bits 15:8
    flags = int((message) & 0b1111_1111)         # masks bits 7:0

    fields = {
        "type": message_type,
        "id": channel_id,
        "a": value_a,
        "b": value_b,
        "flags": flags
    }
    # print("Type:", message_type, "ID:", channel_id, "A:", value_a, "B:", value_b, "Flag:", flags)
    return fields

def message_filter(fields:dict):
    if (fields["type"] != 0):
        reject_reason = 1 # invalid type
    elif (fields["a"] > 200):
        reject_reason = 2 # a too high
    elif (fields["b"] > 200):
        reject_reason = 3 # b too high
    else:
        reject_reason = 0 # pass filter

    if (reject_reason == 0):
        value_a = fields["a"]
        value_b = fields["b"] # pass values if pass filter
    else:
        value_a = value_b = 0 # zero values if reject

    result = {
        "a" : value_a,
        "b" : value_b,
        "reject_reason" : reject_reason
    }
    return result

def reference_model(message:int): # coordinator func
    fields = parse_message(message)
    result = message_filter(fields)

    return result
