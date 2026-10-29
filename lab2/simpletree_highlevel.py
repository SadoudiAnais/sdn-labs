import sys
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel


class SimpleTree(Topo):

    def build(self, n=2):
        self.dpid = 1
        core = self.newSwitch('C1')

        h = 1
        e = 1

        for a in range(1, n + 1):
            aggregation = self.newSwitch('A%d' % a)
            self.addLink(core, aggregation)

            for _ in range(n):
                edge = self.newSwitch('E%d' % e)
                e += 1
                self.addLink(aggregation, edge)

                for _ in range(n):
                    host = self.addHost('H%d' % h)
                    h += 1
                    self.addLink(edge, host)
    def newSwitch(self, name):
       sw = self.addSwitch(name, dpid='%016x' % self.dpid)
       self.dpid += 1
       return sw

if __name__ == '__main__':
    setLogLevel('info')
    n = int(sys.argv[1]) if len(sys.argv) > 1 else int(input('n = '))
    net = Mininet(topo=SimpleTree(n=n))
    net.start()
    CLI(net)
    net.stop()
