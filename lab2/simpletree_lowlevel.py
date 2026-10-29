import sys
from mininet.node import Host, OVSSwitch, DefaultController
from mininet.link import Link
from mininet.log import setLogLevel, info

def build(n):
    switches = []
    hosts = []
    dpid = [1]

    C0 = DefaultController('C0', inNamespace=False)

    def newSwitch(name):
        sw = OVSSwitch(name, dpid='%016x' % dpid[0], inNamespace=False)
        dpid[0] += 1
        switches.append(sw)
        return sw
    core = newSwitch('C1')
    h = 1
    e = 1

    for a in range(1, n + 1):
        agg = newSwitch('A%d' % a)
        Link(core, agg)

        for _ in range(n):
            edge = newSwitch('E%d' % e)
            e += 1
            Link(agg, edge)

            for _ in range(n):
                host = Host('H%d' % h)
                Link(edge, host)
                host.setIP('10.0.0.%d/8' % h)
                hosts.append(host)
                h += 1

    return C0, switches, hosts

def pingAll(hosts):
    sent = 0
    ok = 0
    for src in hosts:
        result = src.name + '->'
        for dst in hosts:
            if src == dst:
                continue
            out = src.cmd('ping -c1 -W2 %s' % dst.IP())
            sent += 1
            if '1 received' in out:
                ok += 1
                result += dst.name + ' '
            else:
                result += 'X '
        info(result + '\n')
    info('*** Results: %d/%d received\n' % (ok, sent))


if __name__ == '__main__':
    setLogLevel('info')
    n = int(sys.argv[1]) if len(sys.argv) > 1 else int(input('n = '))

    info('*** Creating nodes and links\n')
    C0, switches, hosts = build(n)

    info('*** Starting controller and switches\n')
    C0.start()
    for sw in switches:
        sw.start([C0])

    info('*** Testing connectivity\n')
    pingAll(hosts)

    input('*** Press Enter to stop...')

    info('*** Stopping\n')
    for sw in switches:
        sw.stop()
    for host in hosts:
        host.terminate()
    C0.stop()
