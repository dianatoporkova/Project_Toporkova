n = {'пшеница', 'рожь', 'рис', 'картофель', 'свекла', 'подсолнечник'}
kolhoz1 = {'рис', 'свекла', 'подсолнечник'}
kolhoz2 = {'пшеница', 'рожь', 'рис', 'свекла'}
kolhoz3 = {'рис', 'картофель', 'подсолнечник'}
v = (kolhoz1 - kolhoz2) | (kolhoz1 - kolhoz3) | (kolhoz2 - kolhoz1) | (kolhoz2 - kolhoz3) | (kolhoz3 - kolhoz1) | (kolhoz3 - kolhoz2)
print ('Во всех колхозах выращивают:', kolhoz1 & kolhoz2 & kolhoz3)
print ('В некоторых колхозах выращивают: ', v)