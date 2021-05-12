'''The Task
Implement the strstr() function from string.h in the C standard library.
Thisfunction is also known as index() in Perl, find() in Python, and indexOf() inJava and JavaScript.
The function should take two string parameters, short_str and long_str 
(note that these are just the variable names, not types), 
and return the first occurrence of short_str in long_str as a 0-based index into long_str.
If short_str does not exist in long_str, the function should return -1.
You should provide a suite of test data along with your implementation.

Constraints

You may implement the function in Perl, Python, or C, but you MUST NOT use highlevel language 
facilities such as regular expressions or multi-character stringcomparisons.
If you choose to implement in C, you may return a char * that points to the
character from long_str where the match begins, or NULL if short_str is not
found.This should be written as "production quality" code, meaning that it should
be code you'd be willing to check in to a production tree. No extraneous
debug statements, exit() calls, or anything else that would disturb
production code.
The solution should be expressed in a single file with no outside
dependencies. It should contain at least one function named strstr() that
performs the task, and one function named test() that returns a true value if
the strstr() function passes all testcases. You may factor strstr() into
multiple functions if you like.
'''


def strstr(long_str, sub_str):
    '''
    Check if a substring exists inside a string. If exists, returns the substring, if not returns -1.  
    
    Keyword arguments:

    long_str -> string -- String to search in. \n
    sub_str -> string -- String to be searched.
    \n
    repo: https://github.com/fredbrowne/py_strstr
    '''
    string_size = len(long_str)
    sub_size = len(sub_str)
    if sub_size == 0 or string_size == 0:
        return -1
    i = 0
    while i < string_size:
        if long_str[i:i+sub_size] == sub_str:
            return long_str[i:i+sub_size]
        else:
            i += 1
    return -1
    
def test():
    '''
    Test case consists of 10 random Shakespeare quotes and random words to search for.
    '''
    testcase = {
        'Bear me to prison, where I am committed.':'prison',
        'All the world‘s a stage, and all the men and women merely players. They have their exits and their entrances; And one man in his time plays many parts.':'entrances',
        'Some are born great, some achieve greatness, and some have greatness thrust upon them.': 'thrust',
        'Full fathom five thy father lies, of his bones are coral made. Those are pearls that were his eyes. Nothing of him that doth fade, but doth suffer a sea-change into something rich and strange.':'sea-change',
        'If you prick us, do we not bleed? If you tickle us, do we not laugh? If you poison us, do we not die? And if you wrong us, shall we not revenge?':'revenge',
        'Love looks not with the eyes, but with the mind; and therefore is winged Cupid painted blind.':'pearls',
        'The fault, dear Brutus, lies not within the stars, but in ourselves, that we are underlings.':'within',
        'Lifes but a walking shadow, a poor player, that struts and frets his hour upon the stage, and then is heard no more; it is a tale told by an idiot, full of sound and fury, signifying nothing.':'eyes',
        'There are more things in heaven and earth, Horatio, than are dreamt of in your philosophy.':'philosophy',
        'There is nothing either good or bad, but thinking makes it so.':'things'
    }
    for k, v in testcase.items():
        print(strstr(k,v))


if __name__ == '__main__':
    test()