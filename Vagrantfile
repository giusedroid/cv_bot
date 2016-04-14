# -*- mode: ruby -*-
# vi: set ft=ruby :
require 'net/http'

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "trusty"

  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"


  config.vm.hostname = "cv-bot"

  # SERVING CV REST API ON PORT 8080
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.network "public_network"

  # PROXY PROXY PROXY PROXY PROXY PROXY PROXY PROXY PROXY PROXY PROXY PROXY PROXY PROXY PROXY PROXY 
  #
  # Uncomment the following lines if you're using
  # a dynamic service to fetch your proxy
  # otherwise ENV variable will be used
  #
  #http_URI = URI("http://localhost:8088/proxy/http")     # insert http  proxy
  #https_URI = URI("http://localhost:8088/proxy/https")   # insert https proxy
  #ENV['HTTP_PROXY'] = Net::HTTP.get(http_URI)
  #ENV['HTTPS_PROXY'] = Net::HTTP.get(https_URI)
  #
  if Vagrant.has_plugin?("vagrant-proxyconf") and ENV['HTTP_PROXY'] != "" and ENV['HTTPS_PROXY'] != ""
    puts "Configuring proxy with \nhttp=\t#{ENV['HTTP_PROXY']}\nhttps=\t#{ENV['HTTPS_PROXY']}"
    config.proxy.http = ENV['HTTP_PROXY']
    config.proxy.https = ENV['HTTPS_PROXY']
    config.proxy.no_proxy = "localhost,127.0.0.1"
  end
  #
  # PROXY PROXY PROXY PROXY PROXY PROXY PROXY PROXY PROXY PROXY PROXY PROXY PROXY PROXY PROXY PROXY 

  config.ssh.forward_agent = true

  config.vm.synced_folder "data", "/vagrant_data"

  config.vm.provider "virtualbox" do |vb|
     vb.gui = false
     vb.memory = "512"
  end

  config.vm.provision "shell", path: "bootstrap.sh"
end
