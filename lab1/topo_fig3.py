#!/usr/bin/env python3
# Part B.5 - Topology of Figure 3
# Run with: sudo python3 topo_fig3.py

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel


class Fig3Topo(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        h1 = self.addHost('h1', ip='10.0.0.1/8', cpu=0.2)
        h2 = self.addHost('h2', ip='10.0.0.2/8')

        self.addLink(h1, s1)
        self.addLink(h2, s1, bw=10, delay='50ms')

topos = {'fig3': Fig3Topo}


if __name__ == '__main__':
    setLogLevel('info')
    net = Mininet(topo=Fig3Topo(), host=CPULimitedHost, link=TCLink)
    net.start()

    net.pingAll()
    CLI(net)
    net.stop()
