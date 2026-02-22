from typing import Any
import list_adt_student as listadt

def create_alien() -> dict[str, Any]:
    """
    Creates an 'alien' dictionary with a list to store messages.
    """
    return {
        'messages':listadt.create_list(100),  
        'R':None,                           
        'minimum_sequence':None,                       
        'maximum_sequence':None,                       
        'lastmessage':0                      
    }

def add(seq: int, msg: str, length: int, alienList: dict):
    """
    Adds a message to the alien's message list based on the given rules.
    """
    if len(msg)!=length:
        return  
    if alienList['minimum_sequence'] is None or seq<alienList['minimum_sequence']:
        alienList['minimum_sequence']=seq 
    if alienList['maximum_sequence'] is None or seq>alienList['maximum_sequence']:
        alienList['maximum_sequence']=seq
    if alienList['minimum_sequence']<seq<alienList['maximum_sequence']:
        return 
    
    if alienList['R'] is not None: 
        if seq<alienList['lastmessage']:
            newassign=alienList['R']+1
        elif seq>alienList['lastmessage']:
            newassign=alienList['R']-1
        else:
            newassign=alienList['R']

    else: #assign a random number R
        alienList['R']=seq 
        newassign=alienList['R']

    alienList['lastmessage']+=1
    listadt.insert_last((newassign,msg), alienList['messages'])

def delete(seq: int, msg: str, length: int, alienList: dict):
    """
    Deletes the last received message if the sequence number is 0.
    """
    if seq==0:
        if listadt.is_empty(alienList['messages'])==False:
            listadt.remove_last(alienList['messages'])
            alienList['lastmessage'] -= 1  
            if alienList['lastmessage']==0: #used for test 03
                alienList['minimum_sequence']=None
                alienList['maximum_sequence']=None

def get_messages(alienList: dict) -> str:
    """
    Returns all messages in the conversation in decreasing order of their assigned numbers.
    """
    answer=""
    for x in range(100):
        messages=[None]*x
    number_of_msg=0

    while listadt.is_empty(alienList['messages'])==False:
        removed=listadt.remove_last(alienList['messages'])
        messages[number_of_msg]=removed
        number_of_msg+=1

    for val1 in range(number_of_msg-1):
        for val2 in range(number_of_msg-val1-1):
            if messages[val2][0]<messages[val2+1][0]:
                messages[val2], messages[val2+1]=messages[val2+1],messages[val2]

    final_messages=[None]*number_of_msg   
    for value in range(number_of_msg):
        final_messages[value]=messages[value][1]
    for value in range(number_of_msg):
        answer+=final_messages[value]
        if value<number_of_msg-1:
            answer+=" "
    return answer

def main(filename) -> list[str]:
    """
    Reads data from a file, processes it, and returns the conversation as a list.
    """
    alienList = create_alien()
    with open(filename) as f:
        for line in f:
            line=line.strip()
            tokens=line.split()
            str=tokens[0]
            if str.isdigit():
                seq=int(str)
            else:
                continue  
            if len(tokens)>1:
                msg=tokens[1] 
            else:
                msg=""  
            if len(tokens)>2 and tokens[2].isdigit():
                length=int(tokens[2])
            else:
                length=0
            if seq<0:
                break  
            elif seq==0:
                delete(seq, msg, length, alienList)  
            else:
                add(seq, msg, length, alienList)

    return get_messages(alienList)
if __name__ == "__main__":
    print(main("alien\\inputs\\alien02.txt"))