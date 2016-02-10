
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "landregistry/centos"
  config.vm.provision "shell", inline: <<-SCRIPT
    yum install -y http://rpm.landregistryconcept.co.uk/landregistry/x86_64/lr-python3-3.4.3-1.x86_64.rpm
    cp /usr/local/bin/pip3 /usr/bin
    pip3 install virtualenv
  SCRIPT

  config.vm.network "private_network", :ip => "192.168.42.11"

  config.vm.provider :virtualbox do |vb|
    vb.customize ['modifyvm', :id, '--memory', ENV['VM_MEMORY'] || 2048]
    vb.customize ["modifyvm", :id, "--cpus", ENV['VM_CPUS'] || 4]
  end
end
