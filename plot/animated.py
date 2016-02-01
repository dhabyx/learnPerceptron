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
import matplotlib.animation as ani

class AnimatedPlot:
    def __init__(self):
        """initialize all properties"""
        self.xmin = -3.0
        self.xmax = 3.0

        self.x = np.linspace(self.xmin, self.xmax, 50)

        self.fig, self.ax = plt.subplots()
        #self.ax.set_ylim([-4, 4])
        plt.xlim(self.xmin, self.xmax)
        plt.ylim(self.xmin-1, self.xmax+1)
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

    def generate_label(self, perceptron):
        text = "T"+str(perceptron.train_counter)+" W:"+str(perceptron.weights)+"\n"
        text += "I:"+str(perceptron.inputs) + " O:"+str(perceptron.last_output)
        return text

    def update_iteration(self, i, trainer, perceptron):
        trainer.train(perceptron)
        
        self.annotation.set_text(self.generate_label(perceptron))

        y = self.yValue(self.x, perceptron)
        self.line.set_ydata(y)

        for coll in (self.ax.collections):
            self.ax.collections.remove(coll)

        test_point_left = perceptron.get_output([1, self.xmin, self.xmax+1])
        test_point_rigth = perceptron.get_output([1, self.xmax, self.xmax+1])

        if test_point_left > 0 or test_point_rigth > 0:
            self.ax.fill_between(self.x, y, self.xmax+1, alpha=self.alpha )
        else:
            self.ax.fill_between(self.x, self.xmin-1, y, alpha=self.alpha )
        #self.ax.fill_between(self.x, self.xmin-1, y, alpha=self.alpha )

        return self.line, self.annotation

    def generate(self, trainer, perceptron):
        self.line, = self.ax.plot(self.x, self.yValue(self.x, perceptron))

        self.annotation = plt.annotate(self.generate_label(perceptron),
                                       xy=(self.xmin+1,self.xmax))

        self.ax.grid(b=True, which='both')
        self.ax.set_aspect('equal')
        self.ax.axhline(y=0, color='k')
        self.ax.axvline(x=0, color='k')

        # configuring save to gif
        # animation_format = ani.writers['imagemagick']
        # writer = animation_format(fps=2)

        animation = ani.FuncAnimation(self.fig, self.update_iteration, frames=25,
                                      fargs=(trainer,perceptron), interval=1000
                                      )
        #animation.save('train.gif', writer)
        plt.show()
