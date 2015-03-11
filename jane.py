# |------------|
# |  +   A  B  |
# |------------|
#   U D L R A B 

# Register: Takes in a sequence of keys, and a name for that sequcence
# Keypress: Takes a key that was pressed, and returns the name(s) of the sequences that matched.

# register(['A','B','A'], "fireball")
# keypress('A') -> [] # potential fireball
# keypress('B') -> [] # potential fireball
# keypress('A') -> ["fireball"] # fireball
# register(['B','A'], "dive")
# keypress('B')
# keypress('A') -> ["dive", "fireball"] 



sequence_master = list()
sequence_max_length = 0
keystrokes = ""

def register(sequence, name):
    # returns nothing, but adds the sequence to a list of sequences
    # O(len(sequence)); appending to a list is O(1) in Python if DLL
    
    if len(sequence) > sequence_max_length:
        sequence_max_length = len(sequence)
    
    str_sequence = ''.join(sequence)
    
    sequence_master.append((str_sequence, name))
    
def keypress(character):
    # returning a name if we recognize a sequence, else nothing
    # O(num(sequences)* [ len(sequence) + len(sequence) + O(1) ])
    # O(num(sequences)*len(sequences))
    # O( num(sequences) * max_len(sequences) )
    # O(total length of all registers)
    
    if len(keystrokes) >= (2 * sequence_max_length):
        keystrokes = keystrokes[-sequence_max_length:]
    
    matches = list()
    keystrokes.append(character)
    
    for (sequence, name) in sequence_master:
        len_sequence = len(sequence)
        if keystrokes[-len_sequence:] == sequence:
            matches.append(name)
        
    return matches
    

    
    
# O( num(sequences) * max_len(sequences))   # time complexity
# O( num(sequences) * max_len(name))        # space complexify
# keystrokes -> O( num(keypresses))
        
        