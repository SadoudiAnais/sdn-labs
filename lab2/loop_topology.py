from mininet.net import Mininet
from mininet.node import OVSBridge
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def run():
    net = Mininet(controller=None)
    info('*** Adding switches (STP)\n')
    s1 = net.addSwitch('s1', cls=OVSBridge, stp=True)
    s2 = net.addSwitch('s2', cls=OVSBridge, stp=True)
    s3 = net.addSwitch('s3', cls=OVSBridge, stp=True)

    info('*** Adding hosts\n')
    h1 = net.addHost('h1', ip='10.0.0.1/8')
    h2 = net.addHost('h2', ip='10.0.0.2/8')
    h3 = net.addHost('h3', ip='10.0.0.3/8')


    info('*** Creating links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s2)
    net.addLink(h3, s3)

    net.addLink(s1, s2)
    net.addLink(s2, s3)
    net.addLink(s3, s1)   
    net.start()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()
