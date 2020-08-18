from string import ascii_lowercase

# key = []
# for i in range(len(ascii_lowercase)):
#     key[ascii_lowercase[i]] = i+1

# letters = ascii_lowercase
#
# num = list(range(1, 27))
#
# key = dict(zip(letters, num))

# ****************************************

# file = '''
#     Sometime her trots, as if he told the steps,
# With gentle majesty and modest pride;
# Anon he rears upright, curvets and leaps,
# As who should say, 'Lo! thus my strength is tried;
#      And this I do to captivate the eye
#      Of the fair breeder that is standing by.'
#
# What recketh he his rider's angry stir,
# His flattering 'Holla,' or his 'Stand, I say?'
# What cares he now for curb of pricking spur?
# For rich caparisons or trapping gay?
#      He sees his love, and nothing else he sees,
#      Nor nothing else with his proud sight agrees.
#
# Look, when a painter would surpass the life,
# In limning out a well-proportion'd steed,
# His art with nature's workmanship at strife,
# As if the dead the living should exceed;
#      So did this horse excel a common one,
#      In shape, in courage, colour, pace and bone
#
# Round-hoof'd, short-jointed, fetlocks shag and long,
# Broad breast, full eye, small head, and nostril wide,
# High crest, short ears, straight legs and passing strong,
# Thin mane, thick tail, broad buttock, tender hide:
#      Look, what a horse should have he did not lack,
#      Save a proud rider on so proud a back.
# '''

# file = file.split()
#
# book = {}
#
# for word in file:
#     if word not in book:
#         book[word] = 1
#     else:
#         book[word] += 1

# ****************************************


# def phone_number():
#     x = input("Enter your phone number: ")
#     print(f'({x[:3]}){x[3:6]}-{x[6:]}')
#
# def ssn():
#     x = input("Entter your ssn: ")
#     print(f'{x[:3]}-{x[3:5]}-{x[5:]}')


# ****************************************


students = ['steve', 'john', 'mark']
s_dict = {student[0].upper(): student for student in students}
print(s_dict)
