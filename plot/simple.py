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
import matplotlib.pyplot as plt
import random

class PerceptronPlot:
    def __init__(self):
        """initialize all properties"""
        self.xmin = -3.0
        self.xmax = 3.0

        self.x = np.linspace(self.xmin, self.xmax, 50)

        self.fig, self.ax = plt.subplots()
        self.ax.set_ylim([-4, 4])
        self.yFunc = np.vectorize(self.yValue)

        self.alpha = 0.25
        self.counter = 1

    def yValue(self, x, perceptron):
        """Calculates the y value of equation

        The equation is formed by weights of the neuron
        and represents the acceptation area in a
        cartesian plane

        formula:
                -( w0 + w1*x1 )/w2

        :x: integer value to calculate function
        :returns: float value

        """
        return (perceptron.weights[0]+perceptron.weights[1]*x)/perceptron.weights[2]*-1

    def xValue(self, y, perceptron):
        return (perceptron.weights[0]+perceptron.weights[2]*y)/perceptron.weights[1]*-1

    def add_perceptron(self, perceptron):
        """Add region of an perceptron represented in cartesian plane
        :returns: self
        """

        y=self.yFunc(self.x, perceptron)

        base_line, =self.ax.plot(self.x, y)
        ymin, ymax = self.ax.get_ylim()

        test_point_left = perceptron.get_output([1, self.xmin, ymax])
        test_point_rigth = perceptron.get_output([1, self.xmax, ymax])

        random.sample(range(1, 100), 3)
        y_random = random.uniform(ymin, ymax)
        x_calculated = self.xValue(y_random, perceptron)
        number_position = np.array([ x_calculated, y_random ])

        if x_calculated < self.xmin+0.5:
            number_position = np.array([ self.xmin+0.5, self.yValue(self.xmin+0.5, perceptron) ])


        text_position = number_position+np.array([0.5,0.5])
        print number_position, text_position
        if text_position[0] > self.xmax-1:
            text_position[0] = self.xmax-1
        if text_position[1] > ymax-1:
            text_position[1] = ymax-1

        self.ax.annotate(self.counter,
                         xy=(number_position[0], number_position[1]),
                         xytext=(text_position[0], text_position[1]),
                         arrowprops=dict(facecolor='black', width=1)
                         )
        self.counter += 1

        print "test point outputs: ", test_point_left, ' ', test_point_rigth
        if test_point_left > 0 or test_point_rigth > 0:
            self.ax.fill_between(self.x, y, ymax, facecolor=base_line.get_color(), alpha=self.alpha )
        else:
            self.ax.fill_between(self.x, ymin, y, facecolor=base_line.get_color(), alpha=self.alpha )
        return self

    def show(self):
        """ Show all regions added to plot

        :returns: None
        """
        self.ax.grid(b=True, which='both')
        self.ax.set_aspect('equal')
        self.ax.axhline(y=0, color='k')
        self.ax.axvline(x=0, color='k')
        plt.show();
