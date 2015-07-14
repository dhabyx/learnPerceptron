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

from perceptron.units import neuron, layer
import numpy as np

def main():
    """TODO: Docstring for main.
    :returns: TODO

    """

    # testing XOR
    n1 = neuron()
    n1.setThreshold(lambda n: int(n >= 0))

    # first layer
    l1 = layer(n1)
    inputs = [1,1,0] # [bias, input1, input2]
    l1.setData([
        (inputs,[-0.5,1,1]),
        (inputs,[1.5,-1,-1]),
        ])
    print l1.processOutputs().output

    #second layer
    l2 = layer(n1)
    inputs2 = np.insert(l1.output,0,1)
    l2.setData([
        (inputs2 , [-1.5,1,1])
        ])
    print l2.processOutputs().output


if __name__ == "__main__":
    main()
