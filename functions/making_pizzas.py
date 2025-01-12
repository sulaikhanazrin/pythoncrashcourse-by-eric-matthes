import pizzza

pizzza.make_pizza(16,'peporoni')
pizzza.make_pizza(12,'mushroom','olives','cheese')


from pizzza import make_pizza as mp
mp(16,'cheese')
mp(16,'cheese')

import pizzza as p
p.make_pizza(16,'cheese')
p.make_pizza(16,'cheese')

from pizzza import *
make_pizza(16,'peporoni')
make_pizza(12,'mushroom','olives','cheese')