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

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

class ErrorSurface:

    def __init__(self, trainer, perceptron):
        self._trainer = trainer
        self._perceptron = perceptron

        self.w1_min = -20
        self.w1_max = 20

        self.w2_min = -20
        self.w2_max = 20

        self.w0_default = -2.5
        self.steps = 50

    def sum_errors(self):
        error = 0
        for count in range(self._trainer.get_total_trains()):
            input_values, output_value = self._trainer.get_one_input()
            error += self._perceptron.get_output(input_values) - output_value
        return error

    def get_cost_values(self, w1, w2):
        result =  np.empty(w1.shape)
        for i in range(len(w1)):
            test_weights=[ self.w0_default, w1[i], w2[i]]
            self._perceptron.set_weights(test_weights)
            result[i]=(self.sum_errors()**2)*1/(2*self._trainer.get_total_trains())
        return result

    def get_mesh_value(self, x, y):
        result = np.empty(x.shape)
        for i in range(self.steps):
            result[i]= self.get_cost_values(x[i], y[i])

        return result

    def show(self):
        w1 = np.linspace(self.w1_min, self.w1_max, self.steps)
        w2 = np.linspace(self.w2_min, self.w2_max, self.steps)

        w1, w2 = np.meshgrid(w1, w2)
        J = self.get_mesh_value(w1, w2)

        print J

        fig = plt.figure()
        ax = fig.gca(projection='3d')

        surf = ax.plot_surface(w1, w2, J, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

        ax.set_xlabel('w1')
        ax.set_ylabel('w2')
        ax.set_zlabel('J')
        #ax.set_zlim(-0.2, 0.2)

        # ax.zaxis.set_major_locator(LinearLocator(10))
        # ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()
