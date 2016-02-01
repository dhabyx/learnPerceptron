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

class PerceptronTrainer:
    inputs = 0
    outputs = 0
    _input_values = 0
    _output_values = 0
    _total_values = 0
    _train_counter = 0

    def read_data(self, filename):
        """ Loads data from file and initializes the arrays that will be
        passed to neuron
        """
        f = open(filename)

        for line in f:
            if line.startswith('['):
                line = line[1:-2].split()
                self.inputs = int(line[0])
                self._input_values  = np.empty(shape=(1, self.inputs))
                self.outputs = int(line[1])
                self._output_values = np.empty(shape=(1,self.outputs))
                print "Inputs:{} Outputs:{}".format(self.inputs, self.outputs)
            else:
                line=np.array(line.split()).astype(int)
                self._input_values = np.vstack([self._input_values,line[: -self.outputs ]])
                self._output_values = np.append(self._output_values, line[ -self.outputs: ])
                self._total_values += 1

        self._input_values = np.delete(self._input_values, (0), axis=0)
        self._output_values = np.delete(self._output_values, (0))
        print "Input Values:"
        print self._input_values
        print "Outpu Values: ",self._output_values

    def train(self, perceptron):
        perceptron.step_train(self._input_values[self._train_counter],
        self._output_values[self._train_counter])
        if self._train_counter == self._total_values-1:
            self._train_counter = 0
        else:
            self._train_counter += 1
        return self
