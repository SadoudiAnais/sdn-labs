#!/usr/bin/env python3
# Part B.3 - Custom topology of Figure 2
# Run with: sudo python3 topo_fig2.py

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel


class Fig2Topo(Topo):
    def build(self)
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        h3 = self.addHost('h3', ip='10.0.1.2/24')
        h4 = self.addHost('h4', ip='10.0.1.3/24')
        h5 = self.addHost('h5', ip='10.0.2.2/24')
        self.addLink(h3, s1)
        self.addLink(h4, s1)
        self.addLink(s1, s2)
        self.addLink(s2, h5)

topos = {'fig2': Fig2Topo}


if __name__ == '__main__':
    setLogLevel('info')
    net = Mininet(topo=Fig2Topo(), controller=None)
    net.addController('c0', controller=Controller, ip='127.0.0.1', port=6633)
    net.start()

    for host in net.hosts:
        host.cmd(f'ip route add default dev {host.name}-eth0')

    net.pingAll()
    CLI(net)
    net.stop()
