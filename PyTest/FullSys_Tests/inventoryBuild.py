from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InvtoryManager

_inventory_file = '/tmp/inventory'
_dataloader = DataLoader()
_inventory = InventoryManager(loader = _dataloader,sources=[_inventory_file])

#variable_manager = VariableManager()
#loader = DataLoader()

#  Ansible: Load inventory
#inventory = Inventory(
#    loader = loader,
#    variable_manager = variable_manager,
#    host_list = '/tmp/inventory'
#)


def serialize(_inventory):
    if not isinstance(inventory, Inventory):
        return dict()

    data = list()
    for group in inventory.get_groups():
        if group != 'all':
            group_data = inventory.get_group(group).serialize()

            #  Seed host data for group
            host_data = list()
            for host in inventory.get_group(group).hosts:
                host_data.append(host.serialize())

            group_data['hosts'] = host_data
            data.append(group_data)

    return data

serialized_inventory = serialize(inventory)
print(serialized_inventory)
