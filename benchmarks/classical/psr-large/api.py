domains = [
{'description': 'Developed by Sylvie Thiebaux and Jorg Hoffmann. Planners must resupply a number of lines in a faulty electricity network. The flow of electricity through the network, at any point in time, is given by a transitive closure over the network connections, subject to the states of the switches and electricity supply devices. The domain is therefore a good example of the usefulness of derived predicates in real-world applications.',
 'ipc': '2004',
 'name': 'psr-large',
 'problems': [('psr-large/domain.pddl', 'psr-large/p01-s29-n2-l5-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p02-s46-n3-l5-f50.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p03-s53-n4-l3-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p04-s66-n5-l2-f50.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p05-s71-n5-l3-f70.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p06-s74-n5-l4-f50.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p07-s81-n6-l2-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p08-s87-n6-l3-f70.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p09-s90-n6-l4-f50.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p10-s93-n6-l5-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p11-s100-n7-l3-f10.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p12-s103-n7-l3-f70.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p13-s106-n7-l4-f50.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p14-s112-n8-l2-f10.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p15-s114-n8-l2-f50.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p16-s119-n8-l3-f70.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p17-s129-n9-l2-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p18-s133-n9-l3-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p19-s144-n10-l2-f10.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p20-s149-n10-l3-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p21-s160-n12-l2-f10.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p22-s162-n12-l3-f10.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p23-s164-n15-l2-f10.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p24-s166-n15-l3-f10.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p25-s168-n20-l2-f10.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p26-s170-n20-l3-f10.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p27-s172-n25-l2-f10.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p28-s174-n25-l3-f10.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p29-s177-n30-l2-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p30-s179-n30-l3-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p31-s181-n35-l2-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p32-s183-n35-l3-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p33-s185-n40-l2-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p34-s187-n40-l3-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p35-s189-n45-l2-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p36-s191-n45-l3-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p37-s193-n50-l2-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p38-s195-n50-l3-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p39-s197-n55-l2-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p40-s199-n55-l3-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p41-s201-n60-l2-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p42-s203-n60-l3-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p43-s205-n70-l2-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p44-s207-n70-l3-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p45-s209-n80-l2-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p46-s211-n80-l3-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p47-s213-n90-l2-f30.pddl'),
              ('psr-large/domain.pddl', 'psr-large/p48-s215-n90-l3-f30.pddl'),
              ('psr-large/domain.pddl',
               'psr-large/p49-s217-n100-l2-f30.pddl'),
              ('psr-large/domain.pddl',
               'psr-large/p50-s219-n100-l3-f30.pddl')]}
]