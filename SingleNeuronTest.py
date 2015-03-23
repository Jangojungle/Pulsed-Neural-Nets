'''
# Neural Network Model
# This program is an event driven model of a neural network, closly related to pulse neural networks.
'''

__author__ = 'JangoJungle'

import numpy as num
import scipy as sci

fault = 999999
synaptic_weights = num.matrix([[1, 1, 1]])
state_of_synapses = num.matrix([[0, 0, 0]])    # 1 for up, -1 for down, 0 for inactive
synaptic_delays = num.matrix([[1, 1, 1]])
previous_synapse_level = num.matrix([[0, 0, 0]])
current_synapse_level = num.matrix([[0, 0, 0]])
synaptic_event_times = num.matrix([[fault, fault, fault]])
pulse_times = num.matrix([[0]])
threshold = 3./2
current_time = 0

# main loop

'''
Scan for next event: neuron firing time or synapse change of state
'''

next_event = num.matrix([[num.min(synaptic_event_times), num.min(pulse_times)]])

'''
If it's a synaptic event, update the neuron fiting time and the next synaptic event
'''

'''
If it's a neuron firing, reset the synapses, find all the synapses this neuron is connected to, and update those synapses
'''

'''
Update the neuron firing time / create pulse train
'''


# end loop
