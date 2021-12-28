# any imported module works as object
# Or we can import particular function from a module
import converter
from converter import kg_to_lbs
from utils import find_max
# importing a package
from first_pkg.shipping import cal_shipping
from first_pkg import shipping


print(converter.lbs_to_kg(192))
print(kg_to_lbs(86.5))

# list1 = [2, 49, 6, 7]
list1 = input(f'Enter a list of numbers to find maximum: ')
print(find_max(list1))

cal_shipping()
shipping.cal_shipping()