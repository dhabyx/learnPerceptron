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
from abc import ABCMeta, abstractmethod


class Neuron:
    __metaclass__=ABCMeta
    @abstractmethod
    def get_output(self, data):
        """Obtains output of a Neuron
        :returns: np array

        """
        pass

    @abstractmethod
    def get_energy(self):
        """Calculate and return energy
        :returns: np array

        """
        pass

    @abstractmethod
    def set_inputs(self, inputs):
        """Store inputs of neuron

        :inputs: array or np input
        :returns: Neuron

        """
        pass

    @abstractmethod
    def set_weights(self, weights):
        """Store weights of neuron

        :weights: array or np input
        :returns: Neuron

        """
        pass



class Perceptron(Neuron):

    """ Basic structure for perceptron model

    Represents the basic structure for a perceptron,
    """

    def __init__(self, learning_constant = 1.0, use_bias = False):
        """Neuron documentation

        TODO: make better documentation
        """
        self.bias = use_bias
        self.weights = []
        self.inputs = []
        self.threshold = lambda x:x
        self.learning_constant = learning_constant
        self.train_counter = 1
        self.last_output = None

    def set_data(self, data):
        """Set inputs and weights in array format
        ([inputs],[weights])

        :data: array of data
        :returns: self

        """
        self.inputs = np.array(data[0])
        self.weights = np.array(data[1])
        return self

    def set_weights(self, weights):
        """set weights for inputs

        :weights: TODO
        :returns: TODO

        """
        self.weights = np.array(weights)

    def set_inputs(self, inputs):
        """TODO: Docstring for set_inputs.

        :inputs: TODO
        :returns: TODO

        """
        self.inputs= np.array(inputs)

    def use_bias(self, use_bias):
        """TODO: Docstring for use_bias.

        :use_bias: TODO
        :returns: TODO

        """
        self.bias = use_bias
        return self

    def set_threshold(self, threshold):
        """TODO: Docstring for set_threshold.

        :threshold: TODO
        :returns: TODO

        """
        self.threshold = threshold

    def get_output(self, data=None):
        """TODO: Docstring for process.
        :returns: TODO

        """

        if data == None:
            self.last_output = self.threshold(self.weights.dot(self.inputs))
        else:
            self.last_output = self.threshold(self.weights.dot(np.array(data)))
        return self.last_output

    def get_energy(self):
        """Return calculos of energy

        Energy = inputs * weights

        :returns: number

        """
        return self.weights.dot(self.inputs)

    def step_train(self, inputs, desired_output=0):
        self.set_inputs(inputs)
        output = self.get_output()
        if output != desired_output:
            self.weights = self.weights - self.learning_constant * (output - desired_output) * self.inputs
            print "T:", self.train_counter ," new weights: ", self.weights
        else:
            print "T:", self.train_counter ," no changes in weights: ", self.weights
        self.train_counter += 1
        return self


class Layer:

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

    def set_data(self, arrayData):
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

    def process_outputs(self):
        """Process inputs in each neuron into this layer

        :returns: self

        """
        self.output=[]
        for neuron in self.neuronData:
            self.__neuron.set_data(neuron)
            print self.__neuron.get_energy()
            self.output.append(
                    self.__neuron.get_output()
                    )

        return self
