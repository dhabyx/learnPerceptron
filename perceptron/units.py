# -*- coding: utf-8; -*-
# 
# Copyright (C) 2015  Dhaby Xiloj <dhabyx@gmail.com>
# Author: Dhaby Xiloj <dhabyx@gmail.com>
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np

class neuron:

    """ Basic structure for perceptron model
    
    Represents the basic structure for a perceptron,
    """

    def __init__(self, useBias = False):
        """Neuron documentation
        
        TODO: make better documentation
        """
        self.bias = useBias
        self.weights = []
        self.inputs = []
        self.threshold = lambda x:x

    def setData(self, data):
        """Set inputs and weights in array format
        ([inputs],[weights])

        :data: array of data
        :returns: self

        """
        self.inputs = np.array(data[0])
        self.weights = np.array(data[1])
        return self

    def setWeights(self, weights):
        """set weights for inputs

        :weights: TODO
        :returns: TODO

        """
        self.weights = np.array(weights)

    def setInputs(self, inputs):
        """TODO: Docstring for setInputs.

        :inputs: TODO
        :returns: TODO

        """
        self.inputs= np.array(inputs)

    def useBias(self, useBias):
        """TODO: Docstring for useBias.

        :useBias: TODO
        :returns: TODO

        """
        self.bias = useBias

    def setThreshold(self, threshold):
        """TODO: Docstring for setThreshold.

        :threshold: TODO
        :returns: TODO

        """
        self.threshold = threshold 

    def getOutput(self):
        """TODO: Docstring for process.
        :returns: TODO

        """
        return self.threshold(self.weights.dot(self.inputs))

    def getEnergy(self):
        """Return calculos of energy

        Energy = inputs * weights
        
        :returns: number

        """
        return self.weights.dot(self.inputs)

class layer:

    """Layer structure for RNA
    
    Basic layer structure, this class is not for use
    in training, only for store data and test it.
    """
    def __init__(self, neuron):
        """TODO: Docstring for __init__.

        :neuron: class to use for calculate outputs for each neuron
        :returns: None

        """
        self.neuronData = []
        self.output = []
        self.__neuron = neuron

    def setData(self, arrayData):
        """Set complete data for neurons

        This data need an matrix of information, with data for
        weights and inputs for each neuron:

        [
        ([1,2,3],[4,5,6]), # neuron0 ([inputs],[weights])
        ([4,5,6],[7,8,9]), # neuron1 ([inputs],[weights])
        ]

        :arrayData: inputs and weights for each neuron into layer
        :returns: self

        """
        self.neuronData=arrayData
        return self

    def processOutputs(self):
        """Process inputs in each neuron into this layer

        :returns: self

        """
        self.output=[]
        for neuron in self.neuronData:
            self.__neuron.setData(neuron)
            print self.__neuron.getEnergy()
            self.output.append(
                    self.__neuron.getOutput()
                    )

        return self
