#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This is a port of the Donut 3D ASCII animation to Python.
# Written by ChatGPT from https://www.a1k0n.net/js/donut.js , modified by me.
import math
import time


class Donut:
    def __init__(self):
        '''
        This is the constructor for the Donut class.
        '''
        self.A = 1
        self.B = 1

    def asciiframe(self):
        '''
        This is the main function that generates the ASCII frame.
        Each call to this function generates next frame.
        '''
        b = []
        z = []
        self.A += 0.07
        self.B += 0.03
        cA = math.cos(self.A)
        sA = math.sin(self.A)
        cB = math.cos(self.B)
        sB = math.sin(self.B)
        for k in range(1760):
            if k % 80 == 79:
                b.append("\n")
            else:
                b.append(" ")
            z.append(0)
        for j in [x*0.07 for x in range(int(6.28/0.07))]:
            ct = math.cos(j)
            st = math.sin(j)
            for i in [x*0.02 for x in range(int(6.28/0.02))]:
                sp = math.sin(i)
                cp = math.cos(i)
                h = ct + 2
                D = 1 / (sp*h*sA + st*cA + 5)
                t = sp*h*cA - st*sA
                x = int(40 + 30*D*(cp*h*cB - t*sB))
                y = int(12 + 15*D*(cp*h*sB + t*cB))
                o = x + 80*y
                N = int(8*((st*sA - sp*ct*cA)*cB - sp*ct*sA - st*cA - cp*ct*sB))
                if y < 22 and y >= 0 and x >= 0 and x < 79 and D > z[o]:
                    z[o] = D
                    b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]
        return "".join(b)

    def run(self):
        '''
        This is the main loop that runs the program.
        '''
        while True:
            print("\x1b[H")  # move cursor to top left
            print(self.asciiframe())
            time.sleep(0.05)


if __name__ == "__main__":
    donut = Donut()
    donut.run()
