import sanalyzer as sa

# Event nodes
E1 = sa.createNode('global governance failure','event')
E2 = sa.createNode('critical systems failure','event')
E3 = sa.createNode('failure of diplomatic conflict resolution','event')
E4 = sa.createNode('massive incident of data fraud or theft','event')
# Action nodes
A1 = sa.createNode('massive digital misinformation','action')
A2 = sa.createNode('leakism','action')
A3 = sa.createNode('hacktivism','action')
A4 = sa.createNode('cyber-attacks','action')
A5 = sa.createNode('terrorism','action')
A6 = sa.createNode('Zero-day vulnerability discovery','action')
# Create Agent
NewAgent = sa.initAgent()

#==============================================================================
# Action To Event Links
#==============================================================================

sa.connect(NewAgent,A1,E1) # 'massive digital misinformation' -> 'global governance failure'
sa.connect(NewAgent,A2,E1) # 'leakism' -> 'global governance failure'
sa.connect(NewAgent,A3,E1) # 'hacktivism' -> 'global governance failure'
sa.connect(NewAgent,A4,E1) # 'cyber-attacks' -> 'global governance failure'
sa.connect(NewAgent,A5,E1) # 'terrorism' -> 'global governance failure'

sa.connect(NewAgent,A3,E2) # 'hacktivism' -> 'critical systems failure'
sa.connect(NewAgent,A4,E2) # 'cyber-attacks' -> 'critical systems failure'
sa.connect(NewAgent,A5,E2) # 'terrorism' -> 'critical systems failure'

sa.connect(NewAgent,A1,E3) # 'massive digital misinformation' -> 'failure of diplomatic conflict resolution'
sa.connect(NewAgent,A2,E3) # 'leakism' -> 'failure of diplomatic conflict resolution'
sa.connect(NewAgent,A3,E3) # 'hacktivism' -> 'failure of diplomatic conflict resolution'
sa.connect(NewAgent,A4,E3) # 'cyber-attacks' -> 'failure of diplomatic conflict resolution'
sa.connect(NewAgent,A5,E3) # 'terrorism' -> 'failure of diplomatic conflict resolution'

sa.connect(NewAgent,A3,E4) # 'hacktivism' -> 'massive incident of data fraud or theft'
sa.connect(NewAgent,A4,E4) # 'cyber-attacks' -> 'massive incident of data fraud or theft'
         
          
#==============================================================================
# Action to Action Links
#==============================================================================

sa.connect(NewAgent,A6,A3) # 'Zero-day vulnerability discovery' -> 'hacktivism'
sa.connect(NewAgent,A6,A4) # 'Zero-day vulnerability discovery' -> 'cyber-attacks'
sa.connect(NewAgent,A3,A4) # 'hacktivism' -> 'cyber-attacks'
sa.connect(NewAgent,A4,A3) # 'cyber-attacks' -> 'hacktivism'
sa.connect(NewAgent,A5,A3) # 'terrorism' -> 'hacktivism'
sa.connect(NewAgent,A3,A5) # 'hacktivism' -> 'terrorism'
sa.connect(NewAgent,A4,A5) # 'cyber-attacks' -> 'terrorism'
sa.connect(NewAgent,A5,A4) # 'terrorism' -> 'cyber-attacks'
sa.connect(NewAgent,A2,A3) # 'leakism' -> 'hacktivism'
sa.connect(NewAgent,A2,A4) # 'leakism' -> 'cyber-attacks'
sa.connect(NewAgent,A2,A5) # 'leakism' -> 'terrorism'
sa.connect(NewAgent,A3,A1) # 'hacktivism' -> 'massive digital misinformation'
sa.connect(NewAgent,A5,A1) # 'terrorism' -> 'massive digital misinformation'
sa.connect(NewAgent,A1,A3) # 'massive digital misinformation' -> 'hacktivism'
sa.connect(NewAgent,A1,A5) # 'massive digital misinformation' -> 'terrorism'


#==============================================================================
# Event to Action Links
#==============================================================================

sa.connect(NewAgent,E1,A1) # 'global governance failure' -> 'massive digital misinformation'
sa.connect(NewAgent,E1,A2) # 'global governance failure' -> 'leakism'
sa.connect(NewAgent,E1,A3) # 'global governance failure' -> 'hacktivism'
sa.connect(NewAgent,E1,A4) # 'global governance failure' -> 'cyber-attacks'
sa.connect(NewAgent,E1,A5) # 'global governance failure' -> 'terrorism'

sa.connect(NewAgent,E2,A3) # 'critical systems failure' -> 'hacktivism'
sa.connect(NewAgent,E2,A4) # 'critical systems failure' -> 'cyber-attacks'
sa.connect(NewAgent,E2,A5) # 'critical systems failure' -> 'terrorism'

sa.connect(NewAgent,E3,A1) # 'failure of diplomatic conflict resolution' -> 'massive digital misinformation'
sa.connect(NewAgent,E3,A2) # 'failure of diplomatic conflict resolution' -> 'leakism'
sa.connect(NewAgent,E3,A3) # 'failure of diplomatic conflict resolution' -> 'hacktivism'
sa.connect(NewAgent,E3,A4) # 'failure of diplomatic conflict resolution' -> 'cyber-attacks'
sa.connect(NewAgent,E3,A5) # 'failure of diplomatic conflict resolution' -> 'terrorism'

sa.connect(NewAgent,E4,A3) # 'massive incident of data fraud or theft' -> 'hacktivism'
sa.connect(NewAgent,E4,A4) # 'massive incident of data fraud or theft' -> 'cyber-attacks'
sa.connect(NewAgent,E4,A1) # 'massive incident of data fraud or theft' -> 'massive digital misinformation'
sa.connect(NewAgent,E4,A2) # 'massive incident of data fraud or theft' -> 'leakism'
sa.connect(NewAgent,E4,A5) # 'massive incident of data fraud or theft' -> 'terrorism'


#==============================================================================
# Event to Event Links
#==============================================================================

sa.connect(NewAgent,E2,E1) # 'critical systems failure' -> 'global governance failure'
sa.connect(NewAgent,E3,E1) # 'failure of diplomatic conflict resolution' -> 'global governance failure'
sa.connect(NewAgent,E1,E3) # 'global governance failure' -> 'failure of diplomatic conflict resolution'

# Plan for objective
sa.plan(NewAgent,[E1])

#==============================================================================
# Carlos Pedro Goncalves, 2017
# University of Lisbon
# Instituto Superior de Ciencias Sociais e Politicas (ISCSP)
# Copyright (c) 2017 Carlos Pedro Gonçalves
#==============================================================================