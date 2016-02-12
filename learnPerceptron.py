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

from perceptron.units import Perceptron
from perceptron.trainer import PerceptronTrainer
from plot.simple import PerceptronPlot
from plot.animated import AnimatedPlot
from plot.surface import ErrorSurface
import numpy as np
import math

def main():
    """TODO: Docstring for main.
    :returns: TODO

    """

    # testing XOR
    n1 = Perceptron()
    #plot = PerceptronPlot()
    #n1.set_threshold(lambda n: int(n >= 0))
    n1.set_threshold(lambda n: 1/(1+math.exp(n*-1)))

    initial_weights=[0.5, -0.7, 0.2]
    print "initial weights: ", initial_weights

    n1.set_weights(initial_weights)
    # plot.add_perceptron(n1)

    trainer = PerceptronTrainer()
    trainer.read_data('and.txt')


    # for i in range(0, 4):
    #     trainer.train(n1)

    #plot.show()

    #animated = AnimatedPlot()
    #animated.generate(trainer, n1)

    surface = ErrorSurface(trainer,n1)
    surface.show()


if __name__ == "__main__":
    main()
