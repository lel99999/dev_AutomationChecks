nodes = [
  { :hostname => 'test-1', :ip => '192.168.77.10', :ram => 1024, :cpus => 1 },
  { :hostname => 'test-2', :ip => '192.168.77.11', :ram => 1024, :cpus => 1 },
  { :hostname => 'test-3', :ip => '192.168.77.12', :ram => 1024, :cpus => 1 },
  { :hostname => 'testhost-1', :ip => '192.168.77.13', :ram => 1024, :cpus => 1 }
]

Vagrant.configure("2") do |config|
  # Always use Vagrant's insecure key
  config.ssh.insert_key = false
  # Forward ssh agent to easily ssh into the different machines
  config.ssh.forward_agent = true
  # Provision nodes
  nodes.each do |node|
    config.vm.define node[:hostname] do |nodeconfig|
      nodeconfig.vm.box = "bento/ubuntu-20.04";
      nodeconfig.vm.hostname = node[:hostname] + ".box"
      nodeconfig.vm.network :private_network, ip: node[:ip]
      memory = node[:ram] ? node[:ram] : 1024;
      cpus = node[:cpus] ? node[:cpus] : 1;
      nodeconfig.vm.provider :virtualbox do |vb|
        vb.customize [
          "modifyvm", :id,
          "--memory", memory.to_s,
          "--cpus", cpus.to_s
        ]
      end
    end
  end
  # In addition, testhost-1 is the Ansible server
  config.vm.define "testhost-1" do |ansible|
    # Provision Ansible playbook
    ansible.vm.provision "file", source: "../Ansible", destination: "$HOME"
    # Install Ansible and configure nodes
    ansible.vm.provision "shell", path: "ansible.sh"
  end
end