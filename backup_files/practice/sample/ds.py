'''d={'Af':11,'bh':15,'Ne':16}
for name,value in enumerate(d):
    print name,value'''
from enum import Enum
class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
for data in Country:
    print('{:5} = {}'.format(data.name, data.value))
	
