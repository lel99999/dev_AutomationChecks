from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager

_inventory_file = '/tmp/inventory'
_dataloader = DataLoader()
_inventory = InventoryManager(loader = _dataloader,sources=[_inventory_file])

print(_inventory.get_groups_dict())
