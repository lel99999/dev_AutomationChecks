
variable_manager = VariableManager()
loader = DataLoader()

#  Ansible: Load inventory
inventory = Inventory(
    loader = loader,
    variable_manager = variable_manager,
    host_list = 'hosts', '/tmp/inventory'
)


def serialize(inventory):
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
